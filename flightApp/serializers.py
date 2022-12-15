from rest_framework import serializers
from flightApp.models import Flight, Passenger, Reservation

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fileds='__all___'

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fileds='__all___'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fileds='__all___'