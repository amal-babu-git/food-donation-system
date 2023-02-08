from django.db import models
from django.contrib.auth import get_user_model
from donar.models import Donation
# Create your models here.

User = get_user_model()


class BookedDonation(models.Model):
    booked_at = models.DateTimeField(auto_now_add=True)
    is_collected = models.BooleanField(default=False)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.donation + "assigned to " + str(self.user) + "(AGENT)"
