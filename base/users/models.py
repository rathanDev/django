from django.db import models


class User(models.Model):
    name = models.TextField()
    profession = models.TextField()
    description = models.TextField()

