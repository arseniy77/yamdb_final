from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Categories, Comment, Genres, Review, Title


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ('name', 'slug')


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genres
        fields = ('name', 'slug')


class TitlePostSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        many=True,
        queryset=Genres.objects.all())
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all())

    class Meta:
        model = Title
        fields = '__all__'


class TitleListSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True)
    category = CategoriesSerializer()
    rating = serializers.FloatField(
        read_only=True, source='reviews__score__avg')

    class Meta:
        model = Title
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(
        required=False,
        read_only=True)
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True)
    title = serializers.HiddenField(
        default=serializers.PrimaryKeyRelatedField(read_only=True))

    class Meta:
        model = Review
        fields = ('id', 'text', 'title', 'author', 'score', 'pub_date')
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('author', 'title')
            )
        ]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
