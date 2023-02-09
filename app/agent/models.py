from django.db import models
from django.contrib.auth import get_user_model
from donar.models import Donation
# Create your models here.

User = get_user_model()

# FIXME: TODO agent not working expected, so plan to do it later
class BookedDonation(models.Model):
    booked_at = models.DateTimeField(auto_now_add=True)
    is_collected = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.donation + "assigned to " + str(self.user) + "(AGENT)"

class BookedItem(models.Model):
     donation = models.ForeignKey(Donation, on_delete=models.CASCADE,related_name='donations')
     booked_donation=models.ForeignKey(BookedDonation,on_delete=models.CASCADE,related_name='items')
     
     
# FIXME TODO temporary solution for Agent
class Order(models.Model):
    booked_at = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    food_details=models.TextField(null=True,blank=True)
    is_collected = models.BooleanField(default=False)
    donar_contact=models.CharField(max_length=14,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
