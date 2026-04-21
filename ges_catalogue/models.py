from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
Auteur (nom, prenom, date de Naissance, bibliographie)
Categorie (libelle, description)
Livre (titre, resume, auteur, categories, date pub, exemplaire)
Emprunt (livre, utilisateur, date emprunt, date prevu, date reel)
"""

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True)
    bibliographie = models.TextField(blank=True)

class Categorie(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, max_length=500)

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    isnb = models.CharField(max_length=12, unique=True, blank=True)
    auteur = models.ForeignKey(
        Auteur,
        on_delete=models.CASCADE,
        related_name='livres'
    )

    categorie = models.ManyToManyField(
        Categorie,
        related_name= 'livres',
        blank=True
    )

    date_publication = models.DateField()
    nombre_exemplaires = models.PositiveIntegerField(default=1)
    resume = models.TextField(max_length=300)

    class Meta:
        #verbose_name = "livre_biblio"
        ordering = ["-date_publication"]

    def __str__(self):
        return self.titre
    
    @property
    def disponible(self):
        if self.nombre_exemplaires > 0:
            return True
        else:
            return False


class Emprunt(models.Model):
    livre = models.ForeignKey(
        Livre,
        on_delete=models.CASCADE,
        related_name='emprunts'
    )

    utilisateur = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='emprunts'
    )
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour_prevue = models.DateField()
    date_retour_reelle = models.DateField(null=True, blank=True)

