from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers
# Create your views here.


class DonationViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'PUT':
            return serializers.UpdateDonationSerializer
        return serializers.DonationSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'A':
            return models.Donation.objects.all().order_by('-id')
        elif user.user_type == 'D':
            return models.Donation.objects.filter(user_id=user.id).order_by('-id')

    def get_serializer_context(self):
        user_id = self.request.user.id
        return {
            'user_id': user_id
        }
