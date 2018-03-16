from decimal import Decimal

from django.db import models


class NumberModel(models.Model):
    name = models.CharField(max_length=50)
    inum = models.IntegerField(default=0)
    fnum = models.FloatField(default=0)
    dnum = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.name
