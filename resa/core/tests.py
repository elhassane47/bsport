from django.test import TestCase
from core.models import User, Reservation
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from core.models import Reservation, User
from core.serializers import UserSerializer, ReservationSerializer
from django.utils import timezone
import json

class RestApiTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        self.user = User.objects.create(
            first_name='el', last_name="gr", email="gr@gmail.com", phone_number="0644225578")

        self.user1= User.objects.create(
            first_name='hass', last_name="gem", email="gem@gmail.com", phone_number="0644225576")

        self.resa = Reservation.objects.create(
            name="event1", reservation_date=timezone.now(), address="rue rivoli",
            created_at= timezone.now(),user= self.user)

        self.client = APIClient()


    def test_get_all_users(self):
        response = self.client.get(reverse('api:users-list'))
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_reservations(self):
        # get API response
        response = self.client.get(reverse('api:reservations-list'))
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_user(self):

        body = {
            'first_name': "EL",
            'last_name': "Gargem",
            'email': "elhassanegargem@gmail.com",
            'phone_number': "0678830537"
        }
        invalid_body = {
            'first_name': "",
            'last_name': "Gargem",
            'email': "elhassanegargem@gmail.com",
            'phone_number': "xx0678x830537"
        }
        response = self.client.post(reverse('api:users-list'),json.dumps(body), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse('api:users-list'), json.dumps(invalid_body), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_reservation(self):

        body = {
            'name': "ev",
            'reservation_date': str(timezone.now()),
            'address': "haussemann",
            'user': self.user.pk
        }

        response = self.client.post(reverse('api:reservations-list'),json.dumps(body), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_valid_single_user(self):
        response = self.client.get(reverse('api:users-detail', kwargs={'pk': self.user.pk}))
        user = User.objects.get(pk=self.user.pk)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_reservation(self):
        response = self.client.get(reverse('api:reservations-detail', kwargs={'pk': self.resa.pk}))
        resa = Reservation.objects.get(pk=self.user.pk)
        serializer = ReservationSerializer(resa)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_user(self):
        body = {
            'last_name': "Gargem",
        }

        response = self.client.patch(reverse('api:users-detail', kwargs={'pk': self.user.pk}), json.dumps(body), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.last_name, "Gargem")

    def test_delete_user(self):
        response = self.client.delete(reverse('api:users-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_inexistant_user(self):
        response = self.client.delete(reverse('api:users-detail', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)





