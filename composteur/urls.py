from django.urls import path
from . import views

urlpatterns=[
    path('<str:pseudo>/inspecter/<str:id>',views.inspecter,name='inspecter'),
    path('<str:pseudo>/dashboard/',views.dashboard,name='compodash'),
    path('<str:pseudo>/profile/',views.profile,name='compoprof'),
    path('<str:pseudo>/demande/',views.demande,name='compostore'),
    path('<str:pseudo>/gestio_des_deshets/',views.gestion,name='gestiondesh'),
    path('', views.logout_view, name='logout'),
]