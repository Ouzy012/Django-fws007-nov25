from django import forms
from .models import Categorie, Livre, Emprunt

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = [
            'libelle',
            'description'
        ]
        widgets = {
            'libelle': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex. Poème'
            }),
            'description' : forms.Textarea(attrs={                
                'rows': 4,
                'class': 'form-control',
                'placeholder': 'Description de la catégorie'
            })
        }
        labels = {
            'libelle' : "Libellé",
            'description': 'Description'
        }

        def clean_data(self):
            cleaned = super().clean()
            return cleaned