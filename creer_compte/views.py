from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def compte(request, pk):
    message = ''  # initialize the message variable
    if pk == 'composteur':
        if request.method == 'POST':
            formulaire = Form_Composteur(request.POST)
            if formulaire.is_valid():
                enregistrer = formulaire.enregistrer()
                nom, prenom, e_mail, pseudo, NB_GSM, mot_de_passe = enregistrer
                email = formulaire.cleaned_data['email']
                # Vérifier si l'adresse e-mail est valide
                if email:
                    # Créer un message multipart
                    msg = MIMEMultipart('alternative')
                    msg['From'] = 'forgreensmart@gmail.com'
                    msg['To'] = email
                    msg['Subject'] = 'Hello'
                    # Ajouter le texte brut au message
                    text = 'Hello, click to validate'
                    part1 = MIMEText(text, 'plain')
                    msg.attach(part1)
                    # Ajouter le bouton au message en HTML
                    html = f'''
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <style>
                        #container {{
                            background: rgba(85, 204, 103, 0.533);
                            background-attachment: fixed;
                            background-size: cover;
                            box-shadow: 0 15px 30px 1px rgba(128, 128, 128, 0.31);
                            text-align: center;
                            border-radius: 5px;
                            overflow: hidden;
                            margin: 5em auto;
                            height: 350px;
                            width: 700px;
                        }}
                        .product-details {{
                            position: relative;
                            text-align: left;
                            overflow: hidden;
                            padding: 30px;
                            height: 100%;
                            float: left;
                            width: 40%;
                        }}
                        #container .product-details h2 {{
                            font-family: "Old Standard TT", serif;
                            display: inline-block;
                            position: relative;
                            color: #344055;
                        }}
                        .product-image {{
                            transition: all 0.3s ease-out;
                            display: inline-block;
                            position: relative;
                            overflow: hidden;
                            height: 100%;
                            float: right;
                            width: 50%;
                            display: inline-block;
                            
                        }}
                        #container img {{   
                            width: 100%;
                            height: 100%;
                        }}
                        </style>
                    </head>
                    <body>
                        <div id="container">
                        <div class="product-details">
                            <h1>Valider votre formulaire.</h1>
                            <button style="background-color:rgb(199, 244, 229);margin-top: 30%;font-size: 30px;"><a style="text-decoration: none;" href="{request.build_absolute_uri(reverse('map_compo', args=[pk, nom, prenom, e_mail, pseudo, NB_GSM, mot_de_passe]))}">Button validate</a></button>
                        </div>
                        <div class="product-image">
                            <img
                            src="https://scontent.ftun15-1.fna.fbcdn.net/v/t39.30808-6/311612896_109741851928485_6920381439955573733_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=0vIPa5wd-uIAX8a_-OI&_nc_oc=AQmhQOrnMotO4k2Y7PpISpQf_RPAKHY2blTN0bSFzwMVtL50wZmEkfvsKKoDBpZRqnI&_nc_ht=scontent.ftun15-1.fna&oh=00_AfDER_fAqrs5LZEwkDeE0p26sB03aP8ECQ6p01OXS682KQ&oe=6489AA93"
                            />
                        </div>
                        </div>
                    </body>
                    </html>
                    '''
                    part2 = MIMEText(html, 'html')
                    msg.attach(part2)
                    # Envoyer le message e-mail
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login('forgreensmart@gmail.com',
                                   'lblvokvmhhqbogle')
                        smtp.sendmail(msg['From'], msg['To'], msg.as_string())
                    # Afficher un message de confirmation
                    print("Test email sent successfully!")
                    message = 'Un e-mail de confirmation a été envoyé à votre adresse e-mail.'
                else:
                    # Afficher un message d'erreur si l'adresse e-mail est invalide
                    print(f"{email} is an invalid email address")
            return render(request, 'page1/inscrire.html', {'form': formulaire, 'message': message, 'pk': pk})
        return render(request, 'page1/inscrire.html', {'form': Form_Composteur(), 'message': message, 'pk': pk})
    else:
        if request.method == 'POST':
            formulaire = Form_greener(request.POST)
            if formulaire.is_valid():
                enregistrer = formulaire.enregistrer()
                nom, prenom, e_mail, pseudo, NB_GSM, mot_de_passe = enregistrer
                # Récupérer l'adresse e-mail du formulaire
                email = formulaire.cleaned_data['email']
                # Vérifier si l'adresse e-mail est valide
                if email:
                    # Créer un message multipart
                    msg = MIMEMultipart('alternative')
                    msg['From'] = 'forgreensmart@gmail.com'
                    msg['To'] = email
                    msg['Subject'] = 'Hello'
                    # Ajouter le texte brut au message
                    text = 'Hello, click to validate'
                    part1 = MIMEText(text, 'plain')
                    msg.attach(part1)
                    # Ajouter le bouton au message en HTML
                    html = f'''
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <style>
                        #container {{
                            background: rgba(85, 204, 103, 0.533);
                            background-attachment: fixed;
                            background-size: cover;
                            box-shadow: 0 15px 30px 1px rgba(128, 128, 128, 0.31);
                            text-align: center;
                            border-radius: 5px;
                            overflow: hidden;
                            margin: 5em auto;
                            height: 350px;
                            width: 700px;
                        }}
                        .product-details {{
                            position: relative;
                            text-align: left;
                            overflow: hidden;
                            padding: 30px;
                            height: 100%;
                            float: left;
                            width: 40%;
                        }}
                        #container .product-details h2 {{
                            font-family: "Old Standard TT", serif;
                            display: inline-block;
                            position: relative;
                            color: #344055;
                        }}
                        .product-image {{
                            transition: all 0.3s ease-out;
                            display: inline-block;
                            position: relative;
                            overflow: hidden;
                            height: 100%;
                            float: right;
                            width: 50%;
                            display: inline-block;
                            
                        }}
                        #container img {{   
                            width: 100%;
                            height: 100%;
                        }}
                        </style>
                    </head>
                    <body>
                        <div id="container">
                        <div class="product-details">
                            <h1>Valider votre formulaire.</h1>
                            <button style="background-color:rgb(199, 244, 229);margin-top: 30%;font-size: 30px;"><a style="text-decoration: none;" href="{request.build_absolute_uri(reverse('map', args=[pk, nom, prenom, e_mail, pseudo, NB_GSM, mot_de_passe]))}">Button validate</a></button>
                        </div>
                        <div class="product-image">
                            <img
                            src="https://scontent.ftun15-1.fna.fbcdn.net/v/t39.30808-6/311612896_109741851928485_6920381439955573733_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=0vIPa5wd-uIAX8a_-OI&_nc_oc=AQmhQOrnMotO4k2Y7PpISpQf_RPAKHY2blTN0bSFzwMVtL50wZmEkfvsKKoDBpZRqnI&_nc_ht=scontent.ftun15-1.fna&oh=00_AfDER_fAqrs5LZEwkDeE0p26sB03aP8ECQ6p01OXS682KQ&oe=6489AA93"
                            />
                        </div>
                        </div>
                    </body>
                    </html>
                    '''
                    part2 = MIMEText(html, 'html')
                    msg.attach(part2)
                    # Envoyer le message e-mail
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login('forgreensmart@gmail.com',
                                   'lblvokvmhhqbogle')
                        smtp.sendmail(msg['From'], msg['To'], msg.as_string())
                    # Afficher un message de confirmation
                    print("Test email sent successfully!")
                    message = 'Un e-mail de confirmation a été envoyé à votre adresse e-mail.'
                else:
                    # Afficher un message d'erreur si l'adresse e-mail est invalide
                    print(f"{email} is an invalid email address")
            return render(request, 'page1/inscrire.html', {'form': formulaire, 'message': message, 'pk': pk})
        return render(request, 'page1/inscrire.html', {'form': Form_greener(), 'message': message, 'pk': pk})


def maps(request, variable, nom, prenom, e_mail, pseudo, NB_GSM, mot_de_passe):
    composteur = Composteur.objects.filter(Validation=True)
    if request.method == 'POST':
        formulaire = position(request.POST)
        if formulaire.is_valid(pseudo):
            compo_psoude = request.POST.get('composteur')
            if compo_psoude:
                formulaire.enregistrer_greener(
                    nom, prenom, e_mail, pseudo, NB_GSM, mot_de_passe, compo_psoude)
                return redirect('login')
            else:
                message = "Choisir votre composteur"
                return render(request, 'page1/maps.html', {'form': formulaire, 'composteur': composteur, "message": message})
        return render(request, 'page1/maps.html', {'form': formulaire, 'composteur': composteur})
    return render(request, 'page1/maps.html', {'form': position(), 'composteur': composteur})


def maps2(request, variable, nom, prenom, e_mail, pseudo, NB_GSM, mot_de_passe):
    if request.method == 'POST':
        formulaire = position(request.POST)
        if formulaire.is_valid(pseudo):
            formulaire.enregistrer_composteur(
                nom, prenom, e_mail, pseudo, NB_GSM, mot_de_passe)
            return redirect('login')
        return render(request, 'page1/map_compo.html', {'form': formulaire})
    return render(request, 'page1/map_compo.html', {'form': position()})
