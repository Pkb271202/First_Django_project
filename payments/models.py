from django.db import models


class Payment(models.Model):
    mode = models.CharField(max_length=50, default='')
    amount = models.FloatField(default=0)

