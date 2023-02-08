from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Donation(models.Model):
    FOOD_TYPE_VEG = 'V'
    FOOD_TYPE_NON_VEG = 'N'

    FOOD_TYPE_CHOICES = [
        (FOOD_TYPE_NON_VEG, 'Non-Veg'),
        (FOOD_TYPE_VEG, 'Veg'),
    ]

    food_name = models.CharField(max_length=255)
    food_type = models.CharField(
        max_length=1, choices=FOOD_TYPE_CHOICES, default=FOOD_TYPE_NON_VEG)
    quantity = models.PositiveSmallIntegerField()
    contact = models.CharField(max_length=14)
    address = models.TextField()
    is_booked = models.BooleanField(default=False)
    is_collected = models.BooleanField(default=False)
    remark = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.food_name +" donated by "+ str(self.user) +"(DONAR)"
