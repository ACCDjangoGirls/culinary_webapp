from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Ingredient
# Create your views here.

def home(request):
    return render(request, "home.html", {})

class SecretIndexView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    template_name = 'secret.html'

