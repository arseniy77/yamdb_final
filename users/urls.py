from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, get_jwt_token, signup

VERSION = 'v1'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')

URLS = [
    path('auth/signup/', signup, name='signup'),
    path('auth/token/', get_jwt_token, name='token'),
]

URLS += router_v1.urls

urlpatterns = [
    path(f'{VERSION}/', include(URLS)),
]
