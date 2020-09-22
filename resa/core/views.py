from rest_framework.viewsets import ModelViewSet
from core.serializers import UserSerializer, ReservationSerializer
from core.models import Reservation, User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer