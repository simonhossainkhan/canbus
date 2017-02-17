from rest_framework import generics
from rest_framework.permissions import AllowAny

from models import TripInformation, Trips
from serializers import TripsSerializer, TripsInformationSerializer


class TripsList(generics.ListCreateAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer
    permission_classes = (AllowAny,)


class TripsInformationList(generics.ListCreateAPIView):
    queryset = TripInformation.objects.all()
    serializer_class = TripsInformationSerializer
    permission_classes = (AllowAny,)
