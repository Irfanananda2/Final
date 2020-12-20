from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from content.forms import CountryForm
from content.models.country import Country

def list_country(request):
    countrys = Country.objects.all()
    context = {
        'countrys' : countrys,
    }
    return render(request, 'country/countrys.html', context=context)
    
def add_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('countrys'))
    else:
        form = CountryForm()

    context = {
        'form' : form
    }
    return render(request, 'country/country_form.html', context=context)

def edit_country(request, country_id):
    if request.method == 'POST':
        country = Country.objects.get(pk=country_id)
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('countrys'))
    else:
        country = Country.objects.get(pk=country_id)
        fields = model_to_dict(country)
        form = CountryForm(initial=fields, instance=country)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'country/country_form.html', context=context)

def delete_country(request, country_id):
    country = Country.objects.get(pk=country_id)
    if request.method == 'POST':
        country.delete()
        return HttpResponseRedirect(reverse('countrys'))
    context = {
        'country': country
    }
    return render(request, 'country/country_delete_form.html', context=context)