from django.db import models

class Customer(models.Model):
    name = models.TextField()
    profession = models.TextField()
    description = models.TextField()
