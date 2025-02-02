from django import forms
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from .models import *

class Form_Composteur(forms.Form):
    nom = forms.CharField(required=True, max_length=Composteur._meta.get_field(
        'nom').max_length, widget=forms.TextInput(attrs={'id': "nom", 'name': "nom", 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px", 'placeholder': 'Nom'}))
    prenom = forms.CharField(required=True, max_length=Composteur._meta.get_field(
        'prenom').max_length, widget=forms.TextInput(attrs={'id': 'prenom', 'name': 'prenom', 'placeholder': 'Prénom', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    telephone = forms.CharField(required=True, max_length=Composteur._meta.get_field(
        'NB_GSM').max_length, widget=forms.TextInput(attrs={'id': 'NB_GSM', 'name': 'NB_GSM', 'placeholder': 'Téléphone', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    pseudo = forms.CharField(required=True, max_length=Composteur._meta.get_field(
        'pseudo_C').max_length, widget=forms.TextInput(attrs={'id': 'pseudo', 'name': 'pseudo', 'placeholder': 'Pseudo', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    email = forms.EmailField(max_length=Composteur._meta.get_field(
        'e_mail').max_length, required=True, widget=forms.EmailInput(attrs={'id': 'email', 'name': 'email', 'placeholder': 'E-Mail', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password', 'name': 'password', 'placeholder': 'Mot de passe', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    confirmation_mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password1', 'name': 'password1', 'placeholder': 'Re-saisir le mot de passe', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))

    def is_valid(self):
        nom = self.data['nom']
        if any(char.isdigit() for char in nom):
            self.add_error("nom", "Nom est incorrect!")
        prenom = self.data['prenom']
        if any(char.isdigit() for char in prenom):
            self.add_error("prenom", "Prenom est incorrect!")
        pseudo = self.data['pseudo']
        if Composteur.objects.filter(pseudo_C=pseudo).exists() or User.objects.filter(username=pseudo).exists():
            self.add_error("pseudo", "pseudo déja existant!")
        email = self.data['email']
        if Composteur.objects.filter(e_mail=email).exists() or User.objects.filter(email=email).exists():
            self.add_error("email", "email déja existant!")
        telephone = self.data['telephone']
        if not telephone.isdigit():
            self.add_error("telephone", "Téléphone est incorrect!")
        mot_de_passe = self.data['mot_de_passe']
        if len(mot_de_passe) < 8:
            self.add_error(
                "mot_de_passe", "Le mot de passe doit contenir au moins 8 caractères.")
        confirmation_mot_de_passe = self.data['confirmation_mot_de_passe']
        if confirmation_mot_de_passe != mot_de_passe:
            self.add_error("confirmation_mot_de_passe",
                           "Les mots de passe ne correspondent pas.")
        value = super(Form_Composteur,self).is_valid()
        return value

    def enregistrer(self):
        nom = self.cleaned_data['nom']
        prenom = self.cleaned_data['prenom']
        email = self.cleaned_data['email']
        pseudo = self.cleaned_data['pseudo']
        telephone = self.cleaned_data['telephone']
        confirmation_mot_de_passe = self.cleaned_data['confirmation_mot_de_passe']
        return nom ,prenom,email,pseudo,telephone,confirmation_mot_de_passe
    

class Form_greener(forms.Form):
    nom = forms.CharField(required=True, max_length=Greeneur._meta.get_field(
        'nom').max_length, widget=forms.TextInput(attrs={'id': "nom", 'name': "nom", 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px", 'placeholder': 'Nom'}))
    prenom = forms.CharField(required=True, max_length=Greeneur._meta.get_field(
        'prenom').max_length, widget=forms.TextInput(attrs={'id': 'prenom', 'name': 'prenom', 'placeholder': 'Prénom', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    telephone = forms.CharField(required=True, max_length=Greeneur._meta.get_field(
        'NB_GSM').max_length, widget=forms.TextInput(attrs={'id': 'NB_GSM', 'name': 'NB_GSM', 'placeholder': 'Téléphone', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    pseudo = forms.CharField(required=True, max_length=Greeneur._meta.get_field(
        'pseudo_G').max_length, widget=forms.TextInput(attrs={'id': 'pseudo', 'name': 'pseudo', 'placeholder': 'Pseudo', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    email = forms.EmailField(max_length=Greeneur._meta.get_field(
        'e_mail').max_length, required=True, widget=forms.EmailInput(attrs={'id': 'email', 'name': 'email', 'placeholder': 'E-Mail', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password', 'name': 'password', 'placeholder': 'Mot de passe', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    confirmation_mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password1', 'name': 'password1', 'placeholder': 'Re-saisir le mot de passe', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))

    def is_valid(self):
        nom = self.data['nom']
        if any(char.isdigit() for char in nom):
            self.add_error("nom", "Nom est incorrect!")
        prenom = self.data['prenom']
        if any(char.isdigit() for char in prenom):
            self.add_error("prenom", "Prenom est incorrect!")
        pseudo = self.data['pseudo']
        if Greeneur.objects.filter(pseudo_G=pseudo).exists() or User.objects.filter(username=pseudo).exists():
            self.add_error("pseudo", "pseudo déja existant!")
        email = self.data['email']
        if Greeneur.objects.filter(e_mail=email).exists() or User.objects.filter(email=email).exists():
            self.add_error("email", "email déja existant!")
        telephone = self.data['telephone']
        if not telephone.isdigit():
            self.add_error("telephone", "Téléphone est incorrect!")
        mot_de_passe = self.data['mot_de_passe']
        if len(mot_de_passe) < 8:
            self.add_error(
                "mot_de_passe", "Le mot de passe doit contenir au moins 8 caractères.")
        confirmation_mot_de_passe = self.data['confirmation_mot_de_passe']
        if confirmation_mot_de_passe != mot_de_passe:
            self.add_error("confirmation_mot_de_passe",
                           "Les mots de passe ne correspondent pas.")
        value = super(Form_greener, self).is_valid()
        return value

    def enregistrer(self):
        nom = self.cleaned_data['nom']
        prenom = self.cleaned_data['prenom']
        email = self.cleaned_data['email']
        pseudo = self.cleaned_data['pseudo']
        telephone = self.cleaned_data['telephone']
        confirmation_mot_de_passe = self.cleaned_data['confirmation_mot_de_passe']
        return nom ,prenom,email,pseudo,telephone,confirmation_mot_de_passe


class position(forms.Form):
    latitude = forms.FloatField(required=False, widget=forms.TextInput(
        attrs={'id': 'lat', 'name': 'lat'}))
    longitude = forms.FloatField(required=False, widget=forms.TextInput(
        attrs={'id': 'lng', 'name': 'lng'}))
    pseudo = forms.CharField(required=False, widget=forms.HiddenInput())


    def is_valid(self,pseudo):
        lat = self.data['latitude']
        lng = self.data['longitude']
        if Composteur.objects.filter(pseudo_C=pseudo).exists()or Greeneur.objects.filter(pseudo_G=pseudo).exists() or User.objects.filter(username=pseudo).exists():
            self.add_error("pseudo","cette personne existe deja")
        if lat == '' or lng == '':
            self.add_error("latitude", "")
        value = super(position, self).is_valid()
        return value

    def enregistrer_composteur(self, nom, prenom, e_mail, pseudo, NB_GSM, mot_de_passe):
        lat = self.cleaned_data['latitude']
        lng = self.cleaned_data['longitude']
        point = Point(x=float(lng), y=float(lat))
        data = Composteur(nom=nom, prenom=prenom, e_mail=e_mail, pseudo_C=pseudo, NB_GSM=NB_GSM ,position=point,lat=lat,lng=lng)
        try:
            data.save()
            user = User.objects.create_user(pseudo, e_mail, mot_de_passe)
            user.save()
        except Exception as e:
            data.delete()
            raise e

    def enregistrer_greener(self, nom, prenom, e_mail, pseudo, NB_GSM, mot_de_passe,compo_psoude):
        lat = self.cleaned_data['latitude']
        lng = self.cleaned_data['longitude']
        point = Point(x=float(lng), y=float(lat))
        compo = Composteur.objects.get(pseudo_C=compo_psoude)
        data = Greeneur(nom=nom, prenom=prenom, e_mail=e_mail, pseudo_G=pseudo, NB_GSM=NB_GSM,position=point,pseudo_C=compo,lat=lat,lng=lng)
        try:
            data.save()
            user = User.objects.create_user(pseudo, e_mail, mot_de_passe)
            user.save()
        except Exception as e:
            data.delete()
            raise e


