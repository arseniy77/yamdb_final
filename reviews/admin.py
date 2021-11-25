from django.conf import settings
from django.contrib import admin

from .models import Categories, Comment, Genres, Review, Title


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = settings.BLANK_VALUE_CONST


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = settings.BLANK_VALUE_CONST


@admin.register(Title)
class TitlesAdmin(admin.ModelAdmin):
    # 'genre'
    list_display = (
        'pk', 'name', 'year', 'rating', 'description', 'category'
    )
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = settings.BLANK_VALUE_CONST


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'title', 'score')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = settings.BLANK_VALUE_CONST


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'pub_date', 'review')
    search_fields = ('text',)
    list_filter = ('author',)
    empty_value_display = settings.BLANK_VALUE_CONST
