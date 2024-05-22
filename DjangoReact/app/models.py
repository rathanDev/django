from django.db import models

# Create your models here.
# inherits from models.Model. In Django, all model classes should inherit from models.Model

class React(models.Model):
    employee = models.CharField(max_length=30)
    department = models.CharField(max_length=200)
    