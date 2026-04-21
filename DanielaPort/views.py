
from .forms import ContactForm
from django.shortcuts import render,redirect
from django.contrib import messages


def home(request):
    
    context = {
        'titre':'Mon Portfolio Django'
    }
    return render(request,'index.html',context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Pour un Form simple
            identite = form.cleaned_data['identite']
            email = form.cleaned_data['email']
            type_projet = form.cleaned_data['type_projet']
            message = form.cleaned_data['message']
            accepte_donnees = form.cleaned_data['accepte_donnees']
            
            # Traitement (envoi d'email, sauvegarde, etc.)
            # Exemple: envoyer un email
            # send_mail(...)
            
            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('contact')
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = ContactForm()
    
    return render(request, 'index.html', {'form': form})