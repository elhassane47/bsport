from rest_framework import serializers
from core.models import Reservation, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk','first_name','last_name','email','created_at','phone_number',)


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('pk', 'name', 'reservation_date', 'address', 'created_at','user',)

