from django.shortcuts import render, redirect, get_object_or_404
from .models import Categorie
from .forms import CategorieForm
from django.contrib import messages
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
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        #Vérifier la validation du formulaire
        if form.is_valid():
            data = form.save()
            messages.success(
                request,
                f"La catégorie {data.libelle} a été enregistré avec succès"
            )
            return redirect('categorie.index')
    else :
        form = CategorieForm()
    return render(request, "pages/categorie/create.html", {
        'form': form,        
    })

def getCategoryById(request, id):
    try:
        return Categorie.objects.get(id=id)
    except Categorie.DoesNotExist:
        #"Creer une page pour afficher que la ressource est introuvable"
        return render(request, "404.html")

def showCategorie(request, id):
    categorie = getCategoryById(request, id)
    return render(request, "pages/categorie/show.html", {
        'categorie': categorie
    })

def updateCategorie(request, id):
    categorie = getCategoryById(request, id)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "La catégorie a été modifiée avec succès"
            )
            return redirect('categorie.index')
    else:
        form = CategorieForm(instance=categorie)
        return render(request, "pages/categorie/update.html", {
            'categorie': categorie,
            'form': form
        })

def deleteCategorie(request, id):
    categorie = getCategoryById(request, id)
    categorie.delete()
    messages.success(
        request,
        "La catégorie a été supprimée avec succès"
    )
    return redirect('categorie.index')

def livres(request):
    return render(request, "pages/livre/index.html")

def emprunts(request):
    return render(request, "pages/emprunt/index.html")


