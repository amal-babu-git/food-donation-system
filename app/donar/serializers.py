from rest_framework import serializers
from . import models


class DonationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    def create(self, validated_data):
        user_id = self.context['user_id']
        print("user_id",user_id)
        return models.Donation.objects.create(user_id=user_id, **validated_data)

    class Meta:
        model = models.Donation
        fields = ['food_name', 'food_type', 'quantity', 'contact',
                  'address', 'is_ordered', 'user']
