from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Donate(models.Model):
    name_of_card_holder = models.CharField(max_length=255, null=False, blank=False)
    card_number = models.IntegerField(null=False, blank=False)
    cvv = models.IntegerField(null=False, blank=False)
    donate = models.IntegerField(null=False, blank=False)
