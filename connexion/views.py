from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from creer_compte.models import *
# Create your views here.


def connect(request):
    if request.method == 'POST':
        formulaire = LoginForm(request.POST)
        if formulaire.is_valid(request):
            pseudo = formulaire.cleaned_data['pseudo']
            mot_de_passe = formulaire.cleaned_data['mot_de_passe']
            data = authenticate(request, username=pseudo,
                                password=mot_de_passe)
            if data is not None:
                login(request, data)
                if Composteur.objects.filter(pseudo_C=pseudo).exists():  
                    return redirect('compodash',pseudo)
                else:
                    return redirect('dashboard',pseudo)
        # We pass the form to the template even if it is not valid
        return render(request, 'page1/connexion.html', {'form': formulaire})
    # We pass the form to the template for GET requests
    return render(request, 'page1/connexion.html', {'form': LoginForm()})
