from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):

    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid phone number")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return "{} - {}".format(self.first_name, self.last_name)


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    reservation_date = models.DateTimeField()
    created_at = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=256, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='reservations')

    def __str__(self):
        return "{} reserved by {}  at {}".format(self.name, self.user, self.reservation_date)



