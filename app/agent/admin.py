from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.BookedDonation)
class AgentAdmin(admin.ModelAdmin):
    list_display=['booked_at','user','donation']