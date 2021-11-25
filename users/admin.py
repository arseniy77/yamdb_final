from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'bio', 'email')
    search_fields = ('first_name',)
    empty_value_display = '(None)'
