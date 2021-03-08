from django.db import models

class City(models.Model):

    city = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
       return self.city

    class Meta:
        verbose_name_plural = 'Cities'