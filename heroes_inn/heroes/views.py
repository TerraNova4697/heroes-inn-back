from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.authentication import TokenAuthentication
import time
from django.core.files.storage import default_storage

from .models import (
    Character,
    Weapon,
)
from heroes import serializers


class CharacterViewSet(viewsets.ModelViewSet):
    """View for manage character APIs."""
    serializer_class = serializers.CharacterDetailsSerializer
    queryset = Character.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.CharacterSerializer
        elif self.action == 'upload_image':
            return serializers.CharacterImageSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new Character."""
        serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='upload_img')
    def upload_image(self, request, pk=None):
        """Upload an image to recipe."""
        character = self.get_object()
        serializer = self.get_serializer(character, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# GET-запрос списка персонажей конкретного пользователя
# class HeroesAPIView(generics.ListAPIView):
#     serializer_class = HeroesSerializer
#     permission_classes = (IsAuthenticated, )

#     def get_queryset(self):
#         user = self.request.user
#         return Hero.objects.filter(owner=user.id)


# # GET-запрос списка всего оружия
# class WeaponsAPIView(generics.ListAPIView):
#     serializer_class = WeaponSerializer
#     queryset = Weapon.objects.all()


# # POST-запрос создания персонажа
# class HeroCreateAPIView(generics.CreateAPIView):
#     queryset = Hero.objects.all()
#     serializer_class = HeroSerializer
#     permission_classes = (IsAuthenticated, )


# # POST-запрос персонажа
# class HeroRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Hero.objects.prefetch_related('weapons').all()
#     serializer_class = HeroWeaponSerializer
#     permission_classes = (IsAuthenticated,)

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)

#         # Здесь выполняется проверка соответствия владельца персонажа. В случае провала проверки отправляется ошибка 403
#         if instance.owner.id != request.user.id:
#             raise PermissionDenied(detail="Упс! Похоже это персонаж другого игрока.", code=HTTP_403_FORBIDDEN)

#         return Response(serializer.data)


# # PATCH-запрос на частичное обновление персонажа.
# class HeroUpdateAPIView(generics.UpdateAPIView):
#     queryset = Hero.objects.prefetch_related('weapons').all()
#     serializer_class = HeroSerializer
#     permission_classes = (IsAuthenticated, )

#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()

#         # Также выполняется проверка соответствия владельца персонажа
#         if instance.owner.id != request.user.id:
#             raise PermissionDenied(detail="Упс! Похоже это персонаж другого игрока.", code=HTTP_403_FORBIDDEN)

#         # Если есть старое изображение и если оно не дефолтное, то удаляем его
#         hero = Hero.objects.filter(pk=instance.id).get()
#         if hero.hero_img is not '':
#             old_image_name = hero.hero_img.split('/')[-1]
#             if default_storage.exists(old_image_name) and old_image_name != 'default-hero-image.jpg':
#                 default_storage.delete(old_image_name)

#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         if getattr(instance, '_prefetched_objects_cache', None):
#             # If 'prefetch_related' has been applied to a queryset, we need to
#             # forcibly invalidate the prefetch cache on the instance.
#             instance._prefetched_objects_cache = {}

#         return Response(serializer.data)


# # DELETE-запрос на удаление персонажа
# class HeroDeleteAPIView(generics.DestroyAPIView):
#     queryset = Hero.objects.all()
#     serializer_class = HeroSerializer
#     permission_classes = (IsAuthenticated, )

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()

#         # Также выполняется проверка соответствия владельца персонажа
#         if instance.owner.id != request.user.id:
#             raise PermissionDenied(detail="Упс! Похоже это персонаж другого игрока.", code=HTTP_403_FORBIDDEN)

#         # Перед удалением записи в БД, удалить изображение персонажа если это не дефолтное изображение
#         if instance.hero_img != '':
#             image_name = instance.hero_img.split('/')[-1]
#             if default_storage.exists(image_name) and image_name != 'default-hero-image.jpg':
#                 default_storage.delete(image_name)

#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # В случае обновления изображения персонажа удаляется старое изображение
# @api_view(['POST'])
# def image_view(request):
#     if request.method == 'POST':

#         # Получаем данные из формы
#         # 1. Файл изображения
#         # 2. Путь к старому изображению
#         image = request.FILES['image']
#         old_image = request.data.get('old_image')

#         # Проверяем есть ли старое изображение. Если есть, то удаляем его
#         if old_image is not None:
#             old_image_name = old_image.split('/')[-1]
#             if default_storage.exists(old_image_name) and old_image_name != 'default-hero-image.jpg':
#                 default_storage.delete(old_image_name)

#         # Сохраняем новое изображение и отправляем ответ
#         time_now = round(time.time_ns())
#         image_name = default_storage.save(f'{time_now}.jpg', image)

#         return Response(status=status.HTTP_201_CREATED, data={'imageURL': f'/{image_name}'})
#     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
