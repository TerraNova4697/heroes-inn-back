from rest_framework import generics, status
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN
import time
from django.core.files.storage import default_storage

from .models import Hero, Weapon
from .serializers import HeroesSerializer, HeroSerializer, WeaponSerializer, HeroWeaponSerializer


# Create your views here.


class HeroesAPIView(generics.ListAPIView):
    serializer_class = HeroesSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Hero.objects.filter(owner=user.id)


class WeaponsAPIView(generics.ListAPIView):
    serializer_class = WeaponSerializer
    queryset = Weapon.objects.all()


class HeroCreateAPIView(generics.CreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class HeroRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Hero.objects.prefetch_related('weapons').all()
    serializer_class = HeroWeaponSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance.owner.id != request.user.id:
            raise PermissionDenied(detail="Упс! Похоже это персонаж другого игрока.", code=HTTP_403_FORBIDDEN)
        return Response(serializer.data)


class HeroUpdateAPIView(generics.UpdateAPIView):
    queryset = Hero.objects.prefetch_related('weapons').all()
    serializer_class = HeroSerializer
    permission_classes = (IsAuthenticated, )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if instance.owner.id != request.user.id:
            raise PermissionDenied(detail="Упс! Похоже это персонаж другого игрока.", code=HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class HeroDeleteAPIView(generics.DestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.owner.id != request.user.id:
            raise PermissionDenied(detail="Упс! Похоже это персонаж другого игрока.", code=HTTP_403_FORBIDDEN)

        # Перед удалением записи в БД, удалить изображение персонажа если это не дефолтное изображение
        image_name = instance.hero_img.split('/')[-1]
        if default_storage.exists(image_name) and image_name != 'default-hero-image.jpg':
            default_storage.delete(image_name)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def image_view(request):
    if request.method == 'POST':

        # Получаем данные из формы
        # 1. Файл изображения
        # 2. Путь к старому изображению
        image = request.FILES['image']
        old_image = request.data['old_image']

        # Проверяем есть ли старое изображение. Если есть, то удаляем его
        if old_image:
            old_image_name = old_image.split('/')[-1]
            if default_storage.exists(old_image_name) and old_image_name != 'default-hero-image.jpg':
                default_storage.delete(old_image_name)

        # Сохраняем новое изображение и отправляем ответ
        time_now = round(time.time_ns())
        image_name = default_storage.save(f'{time_now}.jpg', image)

        return Response(status=status.HTTP_201_CREATED, data={'imageURL': f'/{image_name}'})
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
