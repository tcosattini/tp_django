from annuaire.models import Contact

def getAllcontacts() -> Contact :
  contacts = Contact.objects.all()
  return contacts

def getContactsParticulier () -> Contact :
  contacts = Contact.objects.filter(entreprise=0)
  return contacts

def getContactsEntreprise () -> Contact :
  contacts = Contact.objects.filter(entreprise=1)
  return contacts