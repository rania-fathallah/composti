from django.db import models
from django.utils import timezone
from creer_compte.models import *
# Create your models here.

class Déshets(models.Model):
    pseudo_C=models.ForeignKey(Composteur,on_delete=models.CASCADE,null=True)
    pseudo_G = models.ForeignKey(Greeneur,on_delete=models.CASCADE,null=True)
    animaux=models.DecimalField(max_digits=10, decimal_places=2)
    azoté=models.DecimalField(max_digits=10, decimal_places=2)
    carboné=models.DecimalField(max_digits=10, decimal_places=2)
    date_disponible = models.DateField()
    heure_disponible = models.TimeField()
    totale_point=models.DecimalField(max_digits=10,null=True,decimal_places=2)
    quantite = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    timestamp = models.DateTimeField(default=timezone.now)
    valider=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pseudo_G}-->({self.carboné}kg carboné//{self.azoté}kg gazoté//{self.animaux}kg animaux//)-->{self.pseudo_C}==={self.timestamp}"

