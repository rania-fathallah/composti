from django.contrib.gis.db import models

# Create your models here.
class Composteur(models.Model):
    nom = models.CharField(max_length=100, null=True)
    prenom = models.CharField(max_length=100, null=True)
    NB_GSM = models.CharField(max_length=100, null=True)
    pseudo_C = models.CharField(max_length=100, primary_key=True)
    e_mail = models.EmailField(max_length=100, null=True)
    position = models.PointField(null=True)
    lat = models.CharField(max_length=100, null=True)
    lng = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='profile_pics',null=True,blank=True )
    quantite = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    Validation = models.BooleanField(default=False)
    def __str__(self):
        return self.pseudo_C

    
class Greeneur(models.Model):   
    nom = models.CharField(max_length=100, null=True)
    prenom = models.CharField(max_length=100, null=True)
    NB_GSM = models.CharField(max_length=100, null=True)
    pseudo_G = models.CharField(max_length=100,primary_key=True)
    e_mail = models.EmailField(max_length=100, null=True)
    position = models.PointField(null=True)
    lat = models.CharField(max_length=100, null=True)
    lng = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='profile_pics',null=True,blank=True)
    portfeuille = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantite = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    pseudo_C =models.ForeignKey(Composteur,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.pseudo_G
