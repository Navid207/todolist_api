from django.db import models
import datetime
from django.conf import settings 
from django.contrib.auth.models import User
from datetime import date

class Todo(models.Model):
    titel = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    createt_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )

    def time_passed(self):
        today = date.today()
        delta = today - self.createt_at
        return delta.days