from django_filters import rest_framework as filters

from .models import Titles


class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name='genre__slug')
    category = filters.CharFilter(field_name='category__slug')
    name = filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Titles
        fields = ('genre', 'category', 'name', 'year')
