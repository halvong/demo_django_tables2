from django.db import models
from django.urls import reverse

class Publisher(models.Model):
    name = models.CharField(max_length=50)

class Source(models.Model):
    name = models.CharField(max_length=100)

class RevenueRecord(models.Model):
    date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    clicks = models.IntegerField()
    revenue = models.FloatField()

    def get_absolute_url(self):
        return reverse('demo:get_date', args=[self.date.year, self.date.month, self.date.day ])