from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers
# Create your views here.


class DonationViewSet(ModelViewSet):
    serializer_class = serializers.DonationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'A':
            return models.Donation.objects.all()
        elif user.user_type == 'D':
            return models.Donation.objects.filter(user_id=user.id)

    def get_serializer_context(self):
        user_id = self.request.user.id
        return {
            'user_id': user_id
        }
