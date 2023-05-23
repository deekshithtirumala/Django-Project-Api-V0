from django.db import models

class Response(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contectNumber = models.CharField(max_length=10)
    