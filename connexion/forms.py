from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from creer_compte.models import *

class LoginForm(forms.Form):
    pseudo = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'pseudo',
                'name': 'pseudo',
                'placeholder': 'Pseudo',
                'class': "form-control shadow-lg p-6 mb-6 rounded",
                'style': "font-size: 20px"
            }
        )
    )
    mot_de_passe = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'name': 'password',
                'placeholder': 'Mot de passe',
                'class': "form-control shadow-lg p-6 mb-6 rounded",
                'style': "font-size: 20px"
            }
        )
    )
    def is_valid(self, request):
        pseudo = self.data['pseudo']
        mot_de_passe = self.data['mot_de_passe']
        try:
            data = Composteur.objects.get(pseudo_C=pseudo)
            if User.objects.filter(username=pseudo).exists():
                user = authenticate(request, username=pseudo,password=mot_de_passe)
                if user is None:
                    self.add_error(
                        "mot_de_passe", "Les mots de passe ne correspondent pas.")
                else:
                    validation = data.Validation
                    if validation is None or validation == False:
                        self.add_error(
                            "mot_de_passe", "Veuillez attendre que l'administration valide le projet")
            else:
                self.add_error("pseudo", "Ce compte n'existe pas.")
        except Composteur.DoesNotExist:
            if User.objects.filter(username=pseudo).exists():
                user = authenticate(request, username=pseudo,
                                    password=mot_de_passe)
                if user is None:
                    self.add_error(
                        "mot_de_passe", "Les mots de passe ne correspondent pas.")
            else:
                self.add_error("pseudo", "Ce compte n'existe pas.")
        return super(LoginForm, self).is_valid()