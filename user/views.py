from django.contrib.gis.geos import Point
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import modifer
from .block import Blockchain
from decimal import Decimal
from creer_compte.models import Composteur,Greeneur
from .models import Déshets
from composteur.models import TransactionCoins

@login_required(login_url='login')
def gestion(request, pseudo):
    greeneur = Greeneur.objects.get(pseudo_G=pseudo)
    transaction=Déshets.objects.filter(pseudo_G=pseudo).order_by('-timestamp')
    if request.method == 'POST':
        gestions = request.POST.get('gestion')
        delete = request.POST.get('delete')
        if gestions:
            delet_demande=Déshets.objects.get(id=delete)
            print(delet_demande)
            delet_demande.delete()
            return render(request, 'greener/gestion.html', {'user': greeneur, 'pseudo': pseudo,'Transaction':transaction})
    return render(request, 'greener/gestion.html', {'user': greeneur, 'pseudo': pseudo,'Transaction':transaction})

@login_required(login_url='login')
def dashboard(request, pseudo):
    greeneur = Greeneur.objects.get(pseudo_G=pseudo)
    Transaction_Coins=TransactionCoins.objects.all().order_by('-timestamp')
    return render(request, 'greener/dashboard.html', {'pseudo': pseudo,"user":greeneur,'Transaction_Coins':Transaction_Coins})

@login_required(login_url='login')
def profile(request, pseudo):
    profile = Greeneur.objects.get(pseudo_G=pseudo)
    if request.method == 'POST':
        formulaire = modifer(request.POST)
        if formulaire.is_valid():
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
        return render(request, 'greener/profile.html', {'form': formulaire, 'pseudo': pseudo, 'user': profile})
    return render(request, 'greener/profile.html', {'form': modifer(), 'pseudo': pseudo, 'user': profile})

blockchain = Blockchain()
@login_required(login_url='login')
def surfer(request, pseudo):
    greeneur = Greeneur.objects.get(pseudo_G=pseudo)
    if request.method == 'POST':
        date = request.POST.get('date')
        heure = request.POST.get('appt')
        carboné= Decimal(request.POST.get('carbone'))
        azoté= Decimal(request.POST.get('azote'))
        animaux= Decimal(request.POST.get('animaux'))
        totale_dechet= Decimal(request.POST.get('totale_dechet'))
        totale_point= Decimal(request.POST.get('totale_point'))
        if carboné!=0 or azoté!=0 or animaux!=0:
            composteur = Composteur.objects.get(pseudo_C=greeneur.pseudo_C)
            blockchain.add_transaction(greeneur,composteur,animaux,azoté,carboné,date,heure,totale_point,totale_dechet)
            return redirect("gestion",pseudo)        
        else:
            message = "Impossible de faire l envoi sans déclaration des déchets."
            return render(request, 'greener/surfer.html', {'pseudo': pseudo, 'message':message,"user":greeneur}) 
    return render(request, 'greener/surfer.html', {'pseudo': pseudo,"user":greeneur})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def changer_com(request, pseudo):
    greeneur = Greeneur.objects.get(pseudo_G=pseudo)
    composteur = Composteur.objects.filter(Validation=True)
    if request.method == 'POST':
        compo_pseudo = request.POST.get('composteur')
        if compo_pseudo:
            compo=Composteur.objects.get(pseudo_C=compo_pseudo)
            greeneur.pseudo_C=compo
            greeneur.save()
            message="enregistré avec succès"
            return render(request, 'greener/changer_compo.html', {'user': greeneur, 'pseudo': pseudo,'composteur':composteur,'message':message})
        else:
            message="Choisir votre composteur"
            return render(request, 'greener/changer_compo.html', {'user': greeneur, 'pseudo': pseudo,'composteur':composteur,'message':message})
    return render(request, 'greener/changer_compo.html', {'user': greeneur, 'pseudo': pseudo,'composteur':composteur})
