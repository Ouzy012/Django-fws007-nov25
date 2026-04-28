from django import forms
from .models import Categorie, Livre, Emprunt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        
class InscriptionForm(UserCreationForm):
    email = forms.EmailField(label='Adresse Email', required=True)
    fisrt_name = forms.CharField(label='Prénom', max_length=30, required=True)
    last_name = forms.CharField(label='Nom', max_length=20, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'fisrt_name', 'last_name', 'password1', 'password2')

        def clean_email(self):
            email = self.cleaned_data('email')
            if User.objects.filter(email=email).exists():
                return forms.ValidationError("L'adresse email est déjà utilisé")
            return email
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data('email')
            user.fisrt_name = self.cleaned_data('fisrt_name')
            user.last_name = self.cleaned_data('last_name')
            if commit:
                user.save()
            return user