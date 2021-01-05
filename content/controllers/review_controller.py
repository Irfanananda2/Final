from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from content.models.review import Review
from content.forms import ReviewForm
from django.contrib.auth.decorators import login_required

def list_review(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'review/review.html', context=context)

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('reviews'))
    else:
        form = ReviewForm()

    context = {
        'form': form
    }
    return render(request, 'review/review_form.html', context=context)

@login_required
def edit_review(request, review_id):
    if request.method == 'POST':
        review = Review.objects.get(pk=review_id)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reviews'))
    else:
        review = Review.objects.get(pk=review_id)
        fields = model_to_dict(review)
        form = ReviewForm(initial=fields, instance=review)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'review/review_form.html', context=context)

@login_required
def delete_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    if request.method == 'POST':
        review.delete()
        return HttpResponseRedirect(reverse('reviews'))
    context = {
        'reviews': review,
    }
    return render(request, 'review/review_delete_form.html', context=context)