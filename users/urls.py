from django.urls import include, path  # isort:skip
from rest_framework.routers import DefaultRouter  # isort:skip

from users.views import get_jwt_token, signup, UserViewSet  # isort:skip

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
