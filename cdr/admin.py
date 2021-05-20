from django.contrib import admin
from .models import Cdr,Client,Facture
# Register your models here.
admin.site.register(Cdr)
admin.site.register(Client)
admin.site.register(Facture)