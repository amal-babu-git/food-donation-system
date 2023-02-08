from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookedDonationSerializer
from .models import BookedDonation
# Create your views here.


class BookedDonationViewSet(ModelViewSet):
    serializer_class = BookedDonationSerializer
    queryset = BookedDonation.objects.all()

    def get_serializer_context(self):
        return {
            'user_id': self.request.user.id
        }
