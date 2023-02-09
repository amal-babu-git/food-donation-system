from django.contrib import admin
from . import models
# Register your models here.




# @admin.register(models.BookedDonation)
# class AgentAdmin(admin.ModelAdmin):
#     list_display=['id','booked_at','user']
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','booked_at','food_details','donar_details','donar_contact','is_collected','user',]
    list_editable=['is_collected']