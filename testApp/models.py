from django.db import models
from django.contrib.auth.models import User


class Advisor(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='advisor/')

    def __str__(self):
        return self.name


class AdvisorBook(models.Model):
    booking_time = models.DateTimeField(auto_now_add=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    advisor = models.OneToOneField(Advisor, on_delete=models.CASCADE)
