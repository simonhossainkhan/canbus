from rest_framework import serializers

from models import Trips, TripInformation


class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = (
            'id',
            'name',
            'start_point',
            'end_point',
            'start_time',
            'end_time',
            'start_miles',
            'end_miles',
            'start_gas_level',
            'end_gas_level',
        )


class TripsInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripInformation
        fields = (
            'id',
            'location',
            'time',
            'rpm',
            'trip',
        )
