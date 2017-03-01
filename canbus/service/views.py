from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from models import TripInformation, Trips
from serializers import TripsSerializer, TripsInformationSerializer

from datetime import datetime
import StringIO
import csv
import string
import random
import pytz


class TripsList(generics.ListCreateAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer
    permission_classes = (AllowAny,)


class TripsInformationList(generics.ListCreateAPIView):
    queryset = TripInformation.objects.all()
    serializer_class = TripsInformationSerializer
    permission_classes = (AllowAny,)


class SaveLogFile(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TripsSerializer
    queryset = Trips.objects.all()

    def update_date(self, data):
        for car_log in data:
            if car_log["Time"]:
                date_today = datetime.now().strftime('%Y-%m-%d')
                car_log["Time"] += "-" + date_today
        return data

    def log_date_format(self):
        return "%H:%M:%S.%f-%Y-%m-%d"

    def read_data(self, log_data):
        f = StringIO.StringIO(log_data)
        reader = csv.reader(f, delimiter=',')
        row_cntr = 0
        data_list = list()
        for row in reader:
            data_dict = dict()
            if row_cntr == 0:
                header_list = row
                row_cntr += 1
                continue
            if row_cntr == 1:
                row_cntr += 1
                continue
            for x in range(0, len(header_list)):
                data_dict[header_list[x].strip()] = row[x]
                if data_dict not in data_list:
                    data_list.append(data_dict)
        data_list = self.update_date(data_list)
        return data_list

    def save_trip(self, data):

        random_name = str()
        for x in range(0, 3):
            random_name += (random.choice(string.letters))

        start_time_unaware = datetime.strptime(data[0].get("Time"), self.log_date_format())
        start_time_aware = start_time_unaware.replace(tzinfo=pytz.UTC)

        end_time_unaware = datetime.strptime(data[-1].get("Time"), self.log_date_format())
        end_time_aware = end_time_unaware.replace(tzinfo=pytz.UTC)

        start_fuel = data[0].get("Fuel Status")
        end_fuel = data[-1].get("Fuel Status")

        new_trip = Trips.objects.create(
            name=random_name.upper(),
            start_time=start_time_aware,
            end_time=end_time_aware,
            start_fuel=start_fuel,
            end_fuel=end_fuel
        )

        return new_trip

    def save_trip_informaion(self, new_trip, data):

        objs_to_create = list()
        for x in range(0, len(data)):
            time_unaware = datetime.strptime(data[x].get("Time"), self.log_date_format())
            time_aware_date = time_unaware.replace(tzinfo=pytz.UTC)
            objs_to_create.append(
                TripInformation(
                    trip=new_trip,
                    time=time_aware_date,
                    rpm=data[x]["RPM"],
                    mph=data[x]["MPH"],
                    throttle=data[x]["Throttle"],
                    load=data[x]["Load"],
                    fuel_status=data[x]["Fuel Status"],
                )
            )
        trip_info = TripInformation.objects.bulk_create(objs_to_create)
        return trip_info

    def post(self, request, *args, **kwargs):
        formatted_data = self.read_data(request.body)
        new_trip = self.save_trip(formatted_data)
        new_trip_info = self.save_trip_informaion(new_trip, formatted_data)

        if new_trip_info:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
