from django.shortcuts import render
from .service.annuaireService import *
from annuaire.models import Contact

contactsLocal = [
       {
          "nom": "Cassidy",
          "prenom": "Hammond",
          "telephone": "03 94 96 50 97"
        },
        {
          "nom": "Charde",
          "prenom": "Hyde",
          "telephone": "03 44 84 02 60"
        },
        {
          "nom": "Dorian",
          "prenom": "Bailey",
          "telephone": "03 78 24 49 97"
        },
        {
          "nom": "Vivien",
          "prenom": "Duffy",
          "telephone": "03 26 81 80 44"
        },
        {
          "nom": "Ivory",
          "prenom": "Colon",
          "telephone": "03 85 87 65 55"
        }
    ]


contactsDb = getAllcontacts()
contactsParticulier = getContactsParticulier()
contactsEntreprise = getContactsEntreprise()

def findContact (contacts, nom,prenom):
  for contact in contacts:
    # Switch case to know if contact is from DB or JSON
      if isinstance(contact,Contact):
        if contact.nom == nom and contact.prenom == prenom :
          return contact  
      elif isinstance(contact,dict):      
        if contact["nom"] == nom and contact["prenom"] == prenom :
          return contact
    
def annuaireListParticulier (request):
  return render (request, "annuaire/list.html", {"contacts":contactsParticulier})

def annuaireListEntreprise (request):
  return render (request, "annuaire/list.html", {"contacts":contactsEntreprise})

def home (request):
  return render (request, "annuaire/home.html")  

def contact (request):
  nom = request.GET.get('nom')
  prenom = request.GET.get('prenom')
  return render (request, "annuaire/contact.html", {"contact": findContact(contactsDb, nom,prenom)})