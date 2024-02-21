from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=20)
    services = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name