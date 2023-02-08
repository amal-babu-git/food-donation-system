from rest_framework import serializers
from . import models
from donar.serializers import DonationSerializer, UpdateDonationSerializer,SimpleDonationSerializer


class BookedDonationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    donation = SimpleDonationSerializer()

    def create(self, validated_data):
        user_id = self.context['user_id']
        print("user_id", user_id)
        return models.BookedDonation.objects.create(user_id=user_id, **validated_data)

    class Meta:
        model = models.BookedDonation
        fields = ['id', 'booked_at', 'donation','user']
