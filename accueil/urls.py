from django.urls import path, re_path, include
from . import views


urlpatterns = [
path('', views.index, name='index'),
# request GET param => /?n1=x&n2=y
path('sum', views.sum, name='sum'),
re_path(r'^sum/(?P<n1>[0-9])(?P<n2>[0-9])/$', views.sumWithRegex),
path("annuaire", include("annuaire.urls"))
]