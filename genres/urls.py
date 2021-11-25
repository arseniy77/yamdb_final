from django.urls import path
from django.urls.conf import include

from rest_framework import routers

from .views import CategoriesViewSet, GenresViewSet, TitilesViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'categories', CategoriesViewSet, basename=r'^categories')
router_v1.register(r'genres', GenresViewSet, basename=r'^genres')
router_v1.register(r'titles', TitilesViewSet, basename=r'^titles')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
