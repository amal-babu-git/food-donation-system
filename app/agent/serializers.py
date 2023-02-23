from rest_framework import serializers
from . import models
from donar.serializers import DonationSerializer, UpdateDonationSerializer, SimpleDonationSerializer


class BookedItemSerializer(serializers.ModelSerializer):
    donation = SimpleDonationSerializer()

    class Meta:
        model = models.BookedItem
        fields = ['id', 'donation']


class BookedDonationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    items = BookedItemSerializer(many=True)

    def create(self, validated_data):
        user_id = self.context['user_id']
        print("user_id", user_id)
        return models.BookedDonation.objects.create(user_id=user_id, **validated_data)

    class Meta:
        model = models.BookedDonation
        fields = ['id', 'booked_at', 'user', 'items']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    def create(self, validated_data):
        user_id = self.context['user_id']
        print("user_id", user_id)
        return models.Order.objects.create(user_id=user_id, **validated_data)

    class Meta:
        model = models.Order
        fields = ['id', 'user', 'food_details', 'donar_details',
                  'is_collected', 'donar_contact', 'booked_at',]
