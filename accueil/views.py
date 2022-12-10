from django.shortcuts import render
from django.http import HttpResponse
import datetime
import django.core.management.commands.runserver as runserver



date_now = datetime.date.today()

def index (request) :
  return render(request, "accueil/helloWorld.html",{"date":date_now})


# request GET param => /?n1=x&n2=y
def sum (request):
  try:
    n1 = request.GET.get('n1')
    n2 = request.GET.get('n2')
    total = int(n1) + int(n2)
    return render (request, "accueil/sum.html", {"number_1": n1,"number_2":n2,"total": total })
  except :
    return render (request, "accueil/sum.html", {"erreur":"Veuillez respecter le format /?n1=x(int)&n2=y(int) " })


def sumWithRegex (request, n1,n2):
  total = int(n1) + int(n2)
  return render (request, "accueil/sum.html", {"number_1":n1,"number_2":n2,"total": total })