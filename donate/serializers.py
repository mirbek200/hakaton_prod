from rest_framework import serializers
from .models import Donate


class DonateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donate
        fields = ['name_of_card_holder', 'card_number', 'cvv', 'donate']