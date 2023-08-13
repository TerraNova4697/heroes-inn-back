from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from .models import (
    Character,
    Weapon,
    Spell,
    Item,
    Feature
)
from heroes import serializers
from .services.cache import Cache, RedisCache


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


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'name',
                OpenApiTypes.STR,
                description='Get items by name',
            )
        ]
    )
)
class PredefinedItemsViewSet(viewsets.ReadOnlyModelViewSet):
    """View for predefined items."""
    cache = Cache(RedisCache())

    def get_queryset(self):
        """Get filtered queryset."""
        name = self.request.query_params.get('name')
        queryset = self.queryset
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset.order_by('name')

    def retrieve(self, request, *args, **kwargs):
        """Retrieve item from Redis Cache if exists. Otherwise get it from the DB and cache it."""
        name, item_pk = request.path.split('/')[3:5]
        obj = self.cache.get_item(name, item_pk)
        if obj:
            return Response(obj)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data
            self.cache.set_item(name, data)
            return Response(data)


class SpellsViewSet(PredefinedItemsViewSet):
    """View for retrieve spells."""
    serializer_class = serializers.SpellSerializer
    queryset = Spell.objects.all()


class WeaponViewSet(PredefinedItemsViewSet):
    """View for retrieve weapon."""
    serializer_class = serializers.WeaponSerializer
    queryset = Weapon.objects.all()


class ItemsViewSet(PredefinedItemsViewSet):
    """View for retrieve all type of items."""
    serializer_class = serializers.ItemSerializer
    queryset = Item.objects.all()


class FeaturesViewSet(PredefinedItemsViewSet):
    """View for retrieve features."""
    serializer_class = serializers.FeatureSerializer
    queryset = Feature.objects.all()
