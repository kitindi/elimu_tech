from django.shortcuts import render
from .models import School

# Create your views here.


def home(request):
    context = {}
    return render(request, "schools/home_page.html", context)
