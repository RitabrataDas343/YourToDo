from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    task = models.CharField(max_length=300)
    def __str__(self):
        return self.task



