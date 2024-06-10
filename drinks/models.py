from django.db import models

class Drink(models.Model):
    def __init__(self):
        name = models.CharField(max_length=200)
        description = models.CharField(max_length=500)