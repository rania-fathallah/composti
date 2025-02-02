from django.urls import path
from . import views

urlpatterns=[
    path('<str:pseudo>/',views.gestion,name='gestion'),
    path('<str:pseudo>/dashboard/',views.dashboard,name='dashboard'),
    path('<str:pseudo>/profile/',views.profile,name='profile'),
    path('<str:pseudo>/surfer/',views.surfer,name='store'),
    path('<str:pseudo>/changer composteur/',views.changer_com,name='changer'),
    path('', views.logout_view, name='logout'),
]