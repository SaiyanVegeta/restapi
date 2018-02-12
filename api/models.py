from django.db import models


class places(models.Model):
    city = models.CharField(max_length=100, blank=False, default='Unknown')
    longitude = models.FloatField(blank=False, default=0.0)
    latitude = models.FloatField(blank=False , default=0.0)
    class Meta:
        ordering = ('city',)
