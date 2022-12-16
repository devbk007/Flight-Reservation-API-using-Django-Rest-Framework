from rest_framework import serializers
from flightApp.models import Flight, Passenger, Reservation
import re

def isFlightNumberValid(data):
    if(re.match("^[a-zA-Z0-9]*$", data['flightNumber'])==None):
            raise serializers.ValidationError("Invalid Flight Number. Make sure, its alpha numeric")
    return data


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [isFlightNumberValid]
    
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'