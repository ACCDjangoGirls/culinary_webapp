from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
# Create your views here.

def home(request):
    return render(request, "home.html", {})

