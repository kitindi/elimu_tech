from django.shortcuts import render, redirect
from .models import School
from .forms import NewsletterForm

# Create your views here.


def home(request):
    form = NewsletterForm()
    context = {"form": form}
    return render(request, "schools/home_page.html", context)
