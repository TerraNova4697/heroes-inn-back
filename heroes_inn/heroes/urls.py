from django.urls import path, include
from rest_framework.routers import DefaultRouter

from heroes import views


router = DefaultRouter()
router.register('characters', views.CharacterViewSet)
router.register('weapon', views.WeaponViewSet)
router.register('spells', views.SpellsViewSet)
router.register('items', views.ItemsViewSet)
router.register('features', views.FeaturesViewSet)


app_name = 'inn'

urlpatterns = [
    path('', include(router.urls)),
]
