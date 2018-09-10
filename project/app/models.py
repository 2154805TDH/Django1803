from django.db import models

# Create your models here.
class animal(models.Model):
    name = models.CharField(
        max_length=40,
    )


class Person(models.Model):
    name = models.CharField(
        max_length=40,
    )