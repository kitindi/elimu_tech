from django.shortcuts import render, redirect
from .forms import NewsletterForm

# Create your views here.


def home(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home-page")
    form = NewsletterForm()
    context = {"form": form}
    return render(request, "schools/home_page.html", context)


def jobboard(request):
    return render(request, "schools/jobboard.html")


def schools(request):
    return render(request, "schools/schools.html")
