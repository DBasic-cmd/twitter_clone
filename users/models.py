from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField(blank=True)


def __str__(self) -> str:
    return self.title