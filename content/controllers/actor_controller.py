from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from content.forms import ActorForm
from content.models.actor import Actor

def list_actor(request):
    actors = Actor.objects.all()
    context = {
        'actors': actors,
    }
    return render(request, 'actor/actor.html', context=context)

def add_actor(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('actors'))
    else:
        form = ActorForm()
    
    context = {
        'form': form
    }   
    return render(request, 'actor/actor_form.html', context = context)

def info_actor(request, actor_id):
    actor = Actor.objects.get(pk=actor_id)
    context = {
        'actor':
        actor
    }
    return render(request, 'actor/actor_details.html', context=context)

def edit_actor(request, actor_id):
    if request.method == 'POST':
        actor = Actor.objects.get(pk=actor_id)
        form = ActorForm(request.POST, instance= actor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('actors'))
    else:
        actor = Actor.objects.get(pk=actor_id)
        fields = model_to_dict(actor)
        form = ActorForm(initial=fields, instance=actor)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'actor/actor_form.html', context=context)

def delete_actor(request, actor_id):
    actor = Actor.objects.get(pk=actor_id)
    if request.method == 'POST':
        actor.delete()
        return HttpResponseRedirect(reverse('actors'))
    context = {
        'actors': actor,
    }
    return render(request, 'actor/actor_delete_form.html', context=context)
