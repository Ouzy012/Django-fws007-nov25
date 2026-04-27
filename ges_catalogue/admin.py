from django.contrib import admin
from .models import Categorie, Livre, Emprunt, Auteur
# Register your models here.
""" 
Basic methode
admin.site.register(Auteur) 
admin.site.register(Categorie)

"""
@admin.register(Auteur)
class AuteurSuperAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom')
    fieldsets = [
        ('Prénom & Nom', {
            'fields': ('prenom', 'nom')
        },)
    ]
    
    search_fields = ('prenom', 'nom', 'date_naissance')
    list_per_page = 10
@admin.register(Categorie)
class CategorieSuperAdmin(admin.ModelAdmin):
    list_display = ('libelle',)
    search_fields = ('libelle',)



admin.site.register(Livre)
admin.site.register(Emprunt)