from django.urls import path
from django.contrib.auth import views as mdp
from . import views

urlpatterns=[
    path('', views.connect, name='login'),
    path('reset_password/', mdp.PasswordResetView.as_view(template_name="page1/reset_password.html"), name="reset_password"),
    path('reset_password_done/', mdp.PasswordResetDoneView.as_view(template_name="page1/reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', mdp.PasswordResetConfirmView.as_view(template_name="page1/reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', mdp.PasswordResetCompleteView.as_view(template_name="page1/reset_complete.html"), name='password_reset_complete'),
]
