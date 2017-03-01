from rest_framework import serializers

from models import Trips, TripInformation


class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = (
            'id',
            'name',
            'start_time',
            'end_time',
            'start_fuel',
            'end_fuel',
        )


class TripsInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripInformation
        fields = (
            'id',
            'trip',
            'time',
            'rpm',
            'mph',
            'throttle',
            'load',
            'fuel_status',
        )
