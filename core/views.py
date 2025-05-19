from .models import Food, Ingredient, Order, ItemsOrder, Reservation, Event, News
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.html import escape

from .forms import IngredientForm, OrderForm

def home(request):
    return render(request, "home.html", {})

class FoodView(generic.ListView):
    model = Food
    template_name = 'food.html'

class AdminFoodCreateView(generic.edit.CreateView):
    model = Food
    template_name = 'admin_food_create.html'
    fields = '__all__'
    
    def form_valid(self, form):
        food_item = form.save(commit=False)
        food_item.save()
        form.save_m2m()
        return super().form_valid(form)
    
    success_url = reverse_lazy("core:food")

class AdminFoodDeleteView(generic.edit.DeleteView):
    model = Food
    template_name = 'admin_food_delete.html'
    success_url = reverse_lazy("core:food")

class AdminFoodUpdateView(generic.edit.UpdateView):
    model = Food
    template_name = 'admin_food_update.html'
    fields = '__all__'
    success_url = reverse_lazy("core:food")

class FoodDetailView(generic.DetailView):
    model = Food
    template_name = 'food_item.html'
    context_object_name = 'food'

class AdminIngredientCreateView(generic.edit.CreateView):
    model = Ingredient
    template_name = 'admin_ingredient_create.html'
    form_class = IngredientForm
    success_url = reverse_lazy("core:food")
    
    def form_valid(self, form):
        ingredient = form.save(commit=False)
        ingredient.save() 
        food = form.cleaned_data['food']
        food.ingredients.add(ingredient) 
        return super().form_valid(form)
    
    #def get_success_url(self):
        #return reverse_lazy("core:menu", kwargs={"pk": self.object.menu.id})

class AdminIngredientUpdateView(generic.edit.UpdateView):
    model = Ingredient
    template_name = 'admin_ingredient_update.html'
    fields = '__all__'
    success_url = reverse_lazy("core:food")
    #def get_success_url(self):
        #return reverse_lazy("core:menu", kwargs={"pk": self.object.menu.id})

class AdminIngredientDeleteView(generic.edit.DeleteView):
    model = Ingredient
    template_name = 'admin_ingredient_delete.html'
    success_url = reverse_lazy("core:food")
    #def get_success_url(self):
        #return reverse_lazy("core:menu", kwargs={"pk": self.object.menu.id})

class OrderView(generic.ListView):
    model = Order
    template_name = 'order.html'

def OrderCreateView(request):
    if request.method == "POST":
        print(request.POST)
        name = escape(request.POST["name"])
        owner = request.user
        time = escape(request.POST["time"])
        notes = escape(request.POST["notes"])

        o = Order(name=name, owner=owner, time=time, notes=notes)
        o.save()

        food_id = escape(request.POST["food item"])
        print(food_id, "##########")
        for i in food_id:
            print(i, "@@@@@")
            food = get_object_or_404(Food, pk=i)

            io = ItemsOrder(foodName=food, quantity=1, order=o)
            io.save()
            
        return HttpResponseRedirect(reverse("core:order"))
    else: 
        core_food = Food.objects.all()

        return render(request, "order_create.html", {"core_food": core_food})

class OrderDeleteView(generic.edit.DeleteView):
    model = Order
    template_name = 'order_delete.html'
    success_url = reverse_lazy("core:order")

class OrderUpdateView(generic.edit.UpdateView):
    model = Order
    template_name = 'order_update.html'
    fields = '__all__'
    success_url = reverse_lazy("core:order")

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order_items.html'

class ItemsOrderCreateView(generic.edit.CreateView):
    model = ItemsOrder
    template_name = 'itemsorder_create.html'
    fields = '__all__'
    success_url = reverse_lazy("core:order")
    #def get_success_url(self):
        #return reverse_lazy("core:menu", kwargs={"pk": self.object.menu.id})

class ItemsOrderUpdateView(generic.edit.UpdateView):
    model = ItemsOrder
    template_name = 'itemsorder_update.html'
    fields = '__all__'
    success_url = reverse_lazy("core:order")
    #def get_success_url(self):
        #return reverse_lazy("core:menu", kwargs={"pk": self.object.menu.id})

class ItemsOrderDeleteView(generic.edit.DeleteView):
    model = ItemsOrder
    template = 'itemsorder_delete.html'
    success_url = reverse_lazy("core:order")
    #def get_success_url(self):
        #return reverse_lazy("core:menu", kwargs={"pk": self.object.menu.id})

class ReservationListView(generic.ListView):
    model = Reservation
    template_name = 'reservation.html'

class ReservationCreateView(generic.edit.CreateView):
    model = Reservation
    template_name = 'reservation_create.html'
    fields = '__all__'
    success_url = reverse_lazy("core:reservation")

class ReservationDeleteView(generic.edit.DeleteView):
    model = Reservation
    template_name = 'reservation_delete.html'
    success_url = reverse_lazy("core:reservation")

class ReservationUpdateView(generic.edit.UpdateView):
    model = Reservation
    template_name = 'reservation_update.html'
    fields = '__all__'
    success_url = reverse_lazy("core:reservation")

class ReservationDetailView(generic.DetailView):
    model = Reservation
    template_name = 'reservation_item.html'

class EventListView(generic.ListView):
    model = Event
    template_name = 'event.html'

class AdminEventCreateView(generic.edit.CreateView):
    model = Event
    template_name = 'admin_event_create.html'
    fields = '__all__'
    success_url = reverse_lazy("core:event")

class AdminEventDeleteView(generic.edit.DeleteView):
    model = Event
    template_name = 'admin_event_delete.html'
    success_url = reverse_lazy("core:event")

class AdminEventUpdateView(generic.edit.UpdateView):
    model = Event
    template_name = 'admin_event_update.html'
    fields = '__all__'
    success_url = reverse_lazy("core:event")

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'event_item.html'

class AboutUsView(generic.TemplateView):
    template_name = 'about_us.html'
    
class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news_item.html'

class NewsListView(generic.ListView):
    model = News
    template_name = 'news.html'

class AdminNewsCreateView(generic.edit.CreateView):
    model = News
    template_name = 'admin_news_create.html'
    fields = '__all__'
    success_url = reverse_lazy("core:news")

class AdminNewsDeleteView(generic.edit.DeleteView):
    model = News
    template_name = 'admin_news_delete.html'
    success_url = reverse_lazy("core:news")

class AdminNewsUpdateView(generic.edit.UpdateView):
    model = Event
    template_name = 'admin_news_update.html'
    fields = '__all__'
    success_url = reverse_lazy("core:news")

#Django is expecting that everything in urls.py actually exists
#everything below here is just placeholder code that
#should be replaced eventually
class SpotlightView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"

