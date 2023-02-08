from django.contrib import admin
from . import models
# Register your models here.




@admin.register(models.BookedDonation)
class AgentAdmin(admin.ModelAdmin):
    list_display=['id','booked_at','donation','user']