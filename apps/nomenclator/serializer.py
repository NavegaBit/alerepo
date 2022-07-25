from rest_framework import serializers
from .models import Location, Country, Municipality, ConstructState, TuristDestination, \
    Category, Coin, Place, ImageFieldShow



class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['name', 'share', 'ico', 'image', 'active', 'created_at', 'updated_at']