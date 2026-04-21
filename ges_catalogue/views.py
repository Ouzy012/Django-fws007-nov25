from django.shortcuts import render
from .models import Categorie
from django.views.generic import ListView

# Create your views here.
#FBV (Function Based View)

def accueil(request):
    categories = Categorie.objects.all()
    return render(request, 'layouts/base.html', {
        "categories": categories
    })

def details(request, id):
    print(id)

#CBV (Class Based View)
class Home(ListView):
    model = Categorie
    template_name = 'pages/accueil.html'


