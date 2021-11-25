from rest_framework import serializers

from .models import Categories, Genres, Titles


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
        model = Titles
        fields = '__all__'


class TitleListSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True)
    category = CategoriesSerializer()
    rating = serializers.FloatField()

    class Meta:
        model = Titles
        fields = '__all__'
