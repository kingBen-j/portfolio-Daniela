# forms.py (avec ModelForm)
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['identite', 'email', 'type_projet', 'message', 'accepte_donnees']
        labels = {
            'identite': 'IDENTITÉ',
            'email': 'EMAIL',
            'type_projet': 'TYPE DE PROJET',
            'message': 'TON MESSAGE',
            'accepte_donnees': "J'ACCEPTE QUE MES DONNÉES SOIENT UTILISÉES POUR ME RECONTACTER",
        }
        widgets = {
            'identite': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'NOM / MARQUE...'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'TON ADRESSE EMAIL'
            }),
            'type_projet': forms.Select(attrs={
                'class': 'form-select'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'DÉCRIS TON PROJET, TES BESOINS, TES DÉLAIS...',
                'rows': 5
            }),
            'accepte_donnees': forms.CheckboxInput(attrs={
                'class': 'privacy-checkbox'
            }),
        }