from django.db import models

# Create your models here.
class Top(models.Model):
    characterName = models.CharField(max_length=300, blank=True)