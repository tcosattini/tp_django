from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='annuaireHome'),
path('/particulier', views.annuaireListParticulier, name='annuaireListParticulier'),
path('/entreprise', views.annuaireListEntreprise, name='annuaireListEntreprise'),
path('/contact', views.contact, name='annuaireContact')
]