from django.db import models

class HistoricalData(models.Model):
    time = models.CharField(max_length=30)
    day = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    
