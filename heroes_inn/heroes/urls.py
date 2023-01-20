from django.urls import path, include
from .views import (HeroesAPIView, HeroCreateAPIView, HeroUpdateAPIView, WeaponsAPIView, image_view,
                    HeroDeleteAPIView, HeroRetrieveAPIView)

app_name = 'heroes'

urlpatterns = [
    path('api/v1/heroeslist/', HeroesAPIView.as_view(), name='heroes_list'),
    path('api/v1/createhero/', HeroCreateAPIView.as_view(), name='create_hero'),
    path('api/v1/deletehero/<int:pk>', HeroDeleteAPIView.as_view(), name='delete_hero'),
    path('api/v1/herosheet/<int:pk>', HeroRetrieveAPIView.as_view(), name='get_hero'),
    path('api/v1/heroupdate/<int:pk>', HeroUpdateAPIView.as_view(), name='update_hero'),
    path('api/v1/weapons/', WeaponsAPIView.as_view(), name='weapons'),
    path('api/v1/image', image_view, name='image_upload'),
]