from django.contrib import admin
from.models import *
# Register your models here.
@admin.register(Composteur)
class composteurAdmin(admin.ModelAdmin):
    list_display = ('pseudo_C', 'e_mail','NB_GSM', 'position','Validation')

@admin.register(Greeneur)
class greeneurAdmin(admin.ModelAdmin):
    list_display = ( 'pseudo_G', 'e_mail','NB_GSM', 'position','portfeuille','quantite')