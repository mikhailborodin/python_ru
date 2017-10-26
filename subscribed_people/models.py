from datetime import datetime
from django.db import models
from model_utils.models import TimeStampedModel


class SubscribedPerson(TimeStampedModel):
    email = models.EmailField(blank=False)
    date = models.DateField(default=datetime.today)
