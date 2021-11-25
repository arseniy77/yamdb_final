from django.db.models import Avg
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, serializers, viewsets
from rest_framework.pagination import (LimitOffsetPagination,
                                       PageNumberPagination)

from .filters import TitleFilter
from .mixins import CreateRetrieveViewSet
from .models import Categories, Genres, Review, Title
from .permissions import AuthorOrAdminOrModeratorOnly, ModeratorOrReadOnly
from .serializers import (CategoriesSerializer, CommentSerializer,
                          GenresSerializer, ReviewSerializer,
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


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(Avg('reviews__score'))
    pagination_class = PageNumberPagination
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ModeratorOrReadOnly)
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleListSerializer
        return TitlePostSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (AuthorOrAdminOrModeratorOnly,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return Review.objects.filter(title=title)

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        if Review.objects.all().filter(author=self.request.user, title=title):
            raise serializers.ValidationError(
                'Вы уже оставили отзыв.'
            )
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AuthorOrAdminOrModeratorOnly,)

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'),
            title_id=self.kwargs.get('title_id')
        )
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'),
            title_id=self.kwargs.get('title_id')
        )
        serializer.save(author=self.request.user, review=review)
