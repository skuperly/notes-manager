from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    owner = models.ForeignKey(
        User, related_name="notes", on_delete=models.CASCADE, null=True)
