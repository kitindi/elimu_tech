from django.shortcuts import render, redirect
from .forms import NewsletterForm
from .models import Job

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
    search_query = ""

    if request.GET.get("positions"):
        search_query = request.GET.get("positions")

    jobs = Job.objects.filter(title__icontains=search_query)
    context = {"jobs": jobs}
    return render(request, "schools/jobboard.html", context)


def jobdetails(request, id):
    job = Job.objects.get(id=id)

    context = {"job": job}
    return render(request, "schools/jobdetails.html", context)


def schools(request):
    return render(request, "schools/schools.html")
