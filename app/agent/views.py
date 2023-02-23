from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import BookedDonationSerializer, OrderSerializer
from .models import BookedDonation, Order
# Create your views here.


class BookedDonationViewSet(ModelViewSet):
    serializer_class = BookedDonationSerializer

    def get_queryset(self):
        user = self.request.user
        return BookedDonation.objects.filter(user_id=user.id)

    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            'user_id': self.request.user.id
        }


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user_id=user.id).order_by('-booked_at')

    def get_permissions(self):
        # only agent
        if self.request.user and self.request.user.user_type == 'A':
            return [IsAuthenticated()]
        return [IsAdminUser()]

    def get_serializer_context(self):
        return {
            'user_id': self.request.user.id
        }
