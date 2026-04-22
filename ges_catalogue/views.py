from django.shortcuts import render
from .models import Categorie
from django.views.generic import ListView

# Create your views here.
#FBV (Function Based View)

def accueil(request):    
    return render(request, 'pages/accueil.html')

def categories(request):
    categories = Categorie.objects.all()
    print(categories)
    return render(request, "pages/categorie/index.html", {
        'categorie': categories
    })

def createCategorie(request):
    return render(request, "pages/categorie/create.html")

def showCategorie(request, id):
    return render(request, "pages/categorie/show.html")

def livres(request):
    return render(request, "pages/livre/index.html")

def emprunts(request):
    return render(request, "pages/emprunt/index.html")


