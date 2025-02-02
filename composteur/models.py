from django.db import models
from django.utils import timezone
from creer_compte.models import *
from user.models import Déshets
# Create your models here.

class TransactionCoins(models.Model):
    Identification = models.ForeignKey(Déshets,on_delete=models.CASCADE,null=True)
    pseudo_G = models.ForeignKey(Greeneur,on_delete=models.CASCADE,null=True)
    totale_point=models.DecimalField(max_digits=10,null=True,decimal_places=2)
    quantite = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    timestamp = models.DateTimeField(default=timezone.now)
