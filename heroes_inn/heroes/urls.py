from django.urls import path, include
from .views import (HeroesListView, HeroesAPIView, HeroCreateAPIView, HeroUpdateAPIView, WeaponsAPIView, image_view,
                    HeroDeleteAPIView, HeroRetrieveAPIView)

app_name = 'heroes'

urlpatterns = [
    path('', HeroesListView.as_view(), name='heroes_list'),
    path('api/v1/heroeslist/', HeroesAPIView.as_view()),
    path('api/v1/createhero/', HeroCreateAPIView.as_view()),
    path('api/v1/deletehero/<int:pk>', HeroDeleteAPIView.as_view()),
    path('api/v1/herosheet/<int:pk>', HeroRetrieveAPIView.as_view()),
    path('api/v1/heroupdate/<int:pk>', HeroUpdateAPIView.as_view()),
    path('api/v1/weapons/', WeaponsAPIView.as_view()),
    path('api/v1/image', image_view),
]