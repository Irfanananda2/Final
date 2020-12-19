from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from content.forms import CountryForm
from content.models.country import Country

def list_country(request):
    countrys = Country.object.all()
    context = {
        'countrys' : countrys,
    }
    return render(request, 'countrys.html', context=context)
    
