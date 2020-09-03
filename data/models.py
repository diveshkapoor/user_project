from django.db import models
import random
#from timezone_field import TimeZoneField

# Create your models here.
class User_data(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    real_name = models.CharField(max_length=60)
    tz = models.CharField(default= 'Europe/London',max_length=60)

    def __str__(self):
        return self.name

class Period(models.Model):
    member = models.ForeignKey(User_data, on_delete = models.CASCADE)
    start = models.DateTimeField()