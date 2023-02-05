from django.contrib import admin

# Register your models here.
# from django.db.models.query import QuerySet
from . import models
from typing import Sequence


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email','full_name','user_type']

    search_fields = ['full_name', 'email']
    list_editable: Sequence[str] = ['full_name','user_type']
