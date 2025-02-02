from django.urls import path
from . import views

urlpatterns=[
    path('<str:pk>',views.compte,name='compte'),
    path('<str:variable>/map/<str:nom>/<str:prenom>/<str:e_mail>/<str:pseudo>/<str:NB_GSM>/<str:mot_de_passe>',views.maps,name='map'),
    path('<str:variable>/map1/<str:nom>/<str:prenom>/<str:e_mail>/<str:pseudo>/<str:NB_GSM>/<str:mot_de_passe>',views.maps2,name='map_compo')
]