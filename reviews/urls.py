from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (CategoriesViewSet, CommentViewSet, GenresViewSet,
                    ReviewViewSet, TitlesViewSet)

app_name = 'reviews'


router_v1 = DefaultRouter()

router_v1.register(r'categories', CategoriesViewSet, basename=r'^categories')
router_v1.register(r'genres', GenresViewSet, basename=r'^genres')
router_v1.register(r'titles', TitlesViewSet, basename=r'^titles')

router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews',
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
