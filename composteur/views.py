from .models import TransactionCoins
from .block import Blockchain
from user.models import Déshets
from django.contrib.gis.geos import Point
from django.shortcuts import render, redirect
from creer_compte.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from.forms import modifer
from datetime import date


@login_required(login_url='login')
def gestion(request, pseudo):
    user = Composteur.objects.get(pseudo_C=pseudo)
    transaction=Déshets.objects.filter(pseudo_C=pseudo,valider=True).order_by('-timestamp')
    return render(request, 'composteur/gestion_deshet.html', {'user': user, 'pseudo': pseudo,'Transaction':transaction})


@login_required(login_url='login')
def dashboard(request, pseudo):
    composteur = Composteur.objects.get(pseudo_C=pseudo)
    Transaction_Coins=TransactionCoins.objects.all().order_by('-timestamp')
    transaction = Déshets.objects.filter(valider=False,pseudo_C=pseudo)
    quantite = 0
    for i in transaction:
        quantite += i.quantite
    return render(request, 'composteur/dashboard.html', {'pseudo': pseudo, 'user': composteur,'quantite':quantite,'Transaction_Coins':Transaction_Coins})


@login_required(login_url='login')
def profile(request, pseudo):
    profile = Composteur.objects.get(pseudo_C=pseudo)
    if request.method == 'POST':
        formulaire = modifer(request.POST)
        if formulaire.is_valid(pseudo):
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            telephone = request.POST.get('telephone')
            lat = request.POST.get('lat')
            lng = request.POST.get('lng')
            image = request.FILES.get('image')
            if lat or lng:
                point = Point(x=float(lng), y=float(lat))
                profile.position = point
                profile.lat = lat
                profile.lng = lng
            if image:
                profile.image = image     
            profile.nom = nom
            profile.prenom = prenom
            profile.NB_GSM = telephone
            profile.save()
        return render(request, 'composteur/profil.html', {'form': formulaire, 'pseudo': pseudo, 'user': profile})
    return render(request, 'composteur/profil.html', {'form': modifer(), 'pseudo': pseudo, 'user': profile})


@login_required(login_url='login')
def demande(request, pseudo):
    compo = Composteur.objects.get(pseudo_C=pseudo)
    produits = Déshets.objects.filter(pseudo_C=pseudo,valider=False).order_by('-timestamp')
    greenermap = Déshets.objects.filter(date_disponible=date.today(),valider=False)
    return render(request, 'composteur/demande.html', {'pseudo': pseudo, 'produit': produits,'greener_position': greenermap,'user':compo})


blockchain = Blockchain()
@login_required(login_url='login')
def inspecter(request, pseudo, id):
    transaction = Déshets.objects.get(id=id)
    masquer = transaction.valider
    greener = Greeneur.objects.get(pseudo_G=transaction.pseudo_G)
    composteur = Composteur.objects.get(pseudo_C=pseudo)
    if request.method == 'POST':
        valider = request.POST.get('valider')
        if valider == 'oui':
            transaction_coins = TransactionCoins.objects.filter(Identification=id).exists()
            if not transaction_coins:
                transaction.valider = True
                transaction.save()
                blockchain.add_transaction(transaction, greener, transaction.quantite, transaction.totale_point)
                greener.quantite += transaction.quantite
                greener.portfeuille += transaction.totale_point
                greener.save()
                composteur.quantite += transaction.quantite
                composteur.save()
            return redirect('compostore', pseudo)
        else:
            transaction.delete()
            return redirect('compostore', pseudo)

    return render(request, 'composteur/inspecter.html', {"user": composteur, 'pseudo': pseudo, 'greener': greener, 'transaction': transaction, "masquer": masquer})

def logout_view(request):
    logout(request)
    return redirect('login')

