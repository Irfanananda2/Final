from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import requests
import re



def Call_TVMAZE(request):
    url = "http://api.tvmaze.com/shows"
    response = requests.get(url).json()
    context = {
        'response': response,
    }
    return render(request, 'API/API.html', context=context)
