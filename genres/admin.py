from django.conf import settings
from django.contrib import admin

from .models import Categories, Genres, Titles


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


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    # 'genre'
    list_display = (
        'pk', 'name', 'year', 'rating', 'description', 'category'
    )
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = settings.BLANK_VALUE_CONST
