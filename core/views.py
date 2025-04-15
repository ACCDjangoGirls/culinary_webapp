from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Menu, Ingredient
from django.urls import reverse, reverse_lazy
# Create your views here.

def home(request):
    return render(request, "home.html", {})

class MenuView(generic.ListView):
    model = Menu
    template_name = 'menu.html'

class AdminMenuCreateView(generic.edit.CreateView):
    model = Menu
    template_name = 'admin_menu_create.html'
    fields = ('foodName',)
    success_url = reverse_lazy("core:menu")

class AdminMenuDeleteView(generic.edit.DeleteView):
    model = Menu
    template_name = 'admin_menu_delete.html'
    success_url = reverse_lazy("core:menu")

class AdminMenuUpdateView(generic.edit.UpdateView):
    model = Menu
    template_name = 'admin_menu_update.html'
    fields = ('foodName',)
    success_url = reverse_lazy("core:menu")

class MenuDetailView(generic.DetailView):
    model = Menu
    template_name = 'menu_item.html'
    context_object_name = 'menu'

class AdminIngredientCreateView(generic.edit.CreateView):
    model = Ingredient
    template_name = 'admin_ingredient_create.html'
    fields = ('ingredientName',)
    success_url = reverse_lazy("core:menu")
    #def get_success_url(self):
        #return reverse_lazy("core:menu", kwargs={"pk": self.object.menu.id})

class AdminIngredientUpdateView(generic.edit.UpdateView):
    model = Ingredient
    template_name = 'admin_ingredient_update.html'
    fields = ('ingredientName',)
    success_url = reverse_lazy("core:menu")
    #def get_success_url(self):
        #return reverse_lazy("core:menu", kwargs={"pk": self.object.menu.id})

class AdminIngredientDeleteView(generic.edit.DeleteView):
    model = Ingredient
    template = 'admin_ingredient_delete.html'
    success_url = reverse_lazy("core:menu")
    #def get_success_url(self):
        #return reverse_lazy("core:menu", kwargs={"pk": self.object.menu.id})

#Django is expecting that everything in urls.py actually exists
#everything below here is just placeholder code that
#should be replaced eventually
class ToGoListView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ToGoDetailView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ToGoCreateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ToGoUpdateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ToGoDeleteView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ReservationListView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ReservationDetailView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ReservationCreateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ReservationUpdateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ReservationDeleteView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminOrderView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AboutUsView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class SpotlightView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class NewsListView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class NewsDetailView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminNewsCreateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminNewsUpdateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminNewsDeleteView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class EventListView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class EventDetailView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminEventCreateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminEventUpdateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminEventDeleteView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"

