from django.db.models import Avg

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import PageNumberPagination

from .filters import TitleFilter
from .mixins import CreateRetrieveViewSet
from .models import Categories, Genres, Title
from .permissions import ModeratorOrReadOnly
from .serializers import (CategoriesSerializer, GenresSerializer,
                          TitleListSerializer, TitlePostSerializer)


class CategoriesViewSet(CreateRetrieveViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = PageNumberPagination
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ModeratorOrReadOnly)
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )


class GenresViewSet(CreateRetrieveViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    pagination_class = PageNumberPagination
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ModeratorOrReadOnly)
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )


class TitilesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(Avg('reviews__score'))
    pagination_class = PageNumberPagination
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ModeratorOrReadOnly
    )
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleListSerializer
        return TitlePostSerializer
