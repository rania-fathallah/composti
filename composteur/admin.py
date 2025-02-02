from django.contrib import admin
from.models import *
# Register your models here.

@admin.register(TransactionCoins)
class transactionCoinsAdmin(admin.ModelAdmin):
    list_display = ( 'pseudo_G', 'quantite','totale_point', 'timestamp')