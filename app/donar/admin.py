from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Donation)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['food_name', 'food_type',
                    'quantity', 'user', 'is_booked', 'is_collected']
    list_editable = ['is_booked', 'is_collected']
