from .models import Menu, Ingredient, Order, ItemsOrder, Reservation, Event
from django.urls import reverse_lazy

from .models import Food, Ingredient, Order, ItemsOrder, Reservation, Event, News
from django.urls import reverse, reverse_lazy

from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from .forms import IngredientForm, ReservationForm
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

# Add admin permissions check mixin.
class AdminRequireMixin(LoginRequiredMixin):
    """Varify that the current user is staff."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


def home(request):
    return render(request, "home.html", {})

class FoodView(generic.ListView):
    model = Food
    template_name = 'food.html'


    # Add filtering for available items.
    def get_queryset(self):
        return Menu.objects.filter(available=True)

class AdminMenuCreateView(AdminRequireMixin, generic.CreateView):
    model = Menu
    template_name = 'admin_menu_create.html'

class AdminFoodCreateView(generic.edit.CreateView):
    model = Food
    template_name = 'admin_food_create.html'

    fields = '__all__'
    success_url = reverse_lazy("core:menu")
    
    def form_valid(self, form):
      
        response = super().form_valid(form)
        messages.success(self.request, f'Menu itme "{self.object.foodName}" created successfully.')
        return response
        #menu_item = form.save(commit=False)
        #menu_item.save()
        #form.save_m2m()

class AdminMenuDeleteView(AdminRequireMixin, generic.DeleteView):
    model = Menu
    template_name = 'admin_menu_delete.html'
    success_url = reverse_lazy("core:menu")

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, f'Menu item "{self.object.foodName}" deleted successfully.')
        return response

class AdminMenuUpdateView(AdminRequireMixin, generic.UpdateView):
    model = Menu
    template_name = 'admin_menu_update.html'
    
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


    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Menu item "{self.object.foodName}" updated successfully.')
        return response
    

class MenuDetailView(generic.DetailView):
    model = Menu
    template_name = 'menu_item.html'
    context_object_name = 'menu'

class FoodDetailView(generic.DetailView):
    model = Food
    template_name = 'food_item.html'
    context_object_name = 'food'


class AdminIngredientCreateView(AdminRequireMixin, generic.CreateView):
    model = Ingredient
    template_name = 'admin_ingredient_create.html'
    form_class = IngredientForm
    success_url = reverse_lazy("core:food")
    
    def form_valid(self, form):

        ingredient = form.save()
        menu = form.cleaned_data['menu']
        if menu:
            menu.ingredients.add(ingredient)
        messages.success(self.request, f'Ingredient "{ingredient.ingredientName}" crated successfully.')

        ingredient = form.save(commit=False)
        ingredient.save() 
        food = form.cleaned_data['food']
        food.ingredients.add(ingredient) 

        return super().form_valid(form)
    
    #def get_success_url(self):
        #return reverse_lazy("core:menu", kwargs={"pk": self.object.menu.id})

class AdminIngredientUpdateView(AdminRequireMixin, generic.edit.UpdateView):
    model = Ingredient
    template_name = 'admin_ingredient_update.html'
    fields = '__all__'
    success_url = reverse_lazy("core:food")
    #def get_success_url(self):
        #return reverse_lazy("core:menu", kwargs={"pk": self.object.menu.id})

class AdminIngredientDeleteView(AdminRequireMixin, generic.edit.DeleteView):
    model = Ingredient
    template_name = 'admin_ingredient_delete.html'

    success_url = reverse_lazy("core:menu")

    success_url = reverse_lazy("core:food")

    #def get_success_url(self):
        #return reverse_lazy("core:menu", kwargs={"pk": self.object.menu.id})

class OrderView(generic.ListView):
    model = Order
    template_name = 'order.html'

class OrderCreateView(generic.edit.CreateView):
    model = Order
    template_name = 'order_create.html'
    fields = '__all__'
    success_url = reverse_lazy("core:order")

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
    context_object_name = 'reservations'
    paginate_by = 10

    def get_queryset(self):
        return Reservation.objects.filter(
            date__gte=timezone.now().date()
        ).order_by('date', 'time')
    

class ReservationCreateView(generic.edit.CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_create.html'
    success_url = reverse_lazy("core:reservation")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Reservation created successfully.')
        return response

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

