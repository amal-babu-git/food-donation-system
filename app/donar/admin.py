from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Donation)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['food_name', 'food_type',
                    'quantity', 'user', 'is_booked',]
    list_editable = ['is_booked',]
