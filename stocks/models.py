from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Stocks(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=100 ,decimal_places=2) 
    price = models.DecimalField(max_digits=100 ,decimal_places=2)
    class Meta:
        db_table = 'db_stock'

    def __str__(self):
        return self.name