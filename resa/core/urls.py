from django.urls import path, include
from core.views import UserViewSet, ReservationViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('reservations', ReservationViewSet, basename='reservations')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
