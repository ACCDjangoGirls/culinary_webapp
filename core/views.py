from .models import Food, Ingredient, Order, ItemsOrder, Reservation, Event, News
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import IngredientForm, ReservationForm, OrderForm, EventForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


def home(request):
    return render(request, "home.html", {})


class FoodView(generic.ListView):
    model = Food
    template_name = "food.html"


class AdminFoodCreateView(generic.edit.CreateView):
    model = Food
    template_name = "admin_food_create.html"
    fields = "__all__"

    def form_valid(self, form):
        food_item = form.save(commit=False)
        food_item.save()
        form.save_m2m()
        return super().form_valid(form)

    success_url = reverse_lazy("core:food")


class AdminFoodDeleteView(generic.edit.DeleteView):
    model = Food
    template_name = "admin_food_delete.html"
    success_url = reverse_lazy("core:food")


class AdminFoodUpdateView(generic.edit.UpdateView):
    model = Food
    template_name = "admin_food_update.html"
    fields = "__all__"
    success_url = reverse_lazy("core:food")


class FoodDetailView(generic.DetailView):
    model = Food
    template_name = "food_item.html"
    context_object_name = "food"


class AdminIngredientCreateView(generic.edit.CreateView):
    model = Ingredient
    template_name = "admin_ingredient_create.html"
    form_class = IngredientForm
    success_url = reverse_lazy("core:food")

    def form_valid(self, form):
        ingredient = form.save(commit=False)
        ingredient.save()
        food = form.cleaned_data["food"]
        food.ingredients.add(ingredient)
        return super().form_valid(form)


class AdminIngredientUpdateView(generic.edit.UpdateView):
    model = Ingredient
    template_name = "admin_ingredient_update.html"
    fields = "__all__"
    success_url = reverse_lazy("core:food")


class AdminIngredientDeleteView(generic.edit.DeleteView):
    model = Ingredient
    template_name = "admin_ingredient_delete.html"
    success_url = reverse_lazy("core:food")


class OrderView(generic.ListView):
    model = Order
    template_name = "order.html"


def OrderCreateView(request):
    if request.method == "POST":

        name = escape(request.POST["name"])
        owner = request.user
        time = escape(request.POST["time"])
        notes = escape(request.POST["notes"])

        o = Order(hostName=name, owner=owner, time=time, notes=notes)
        o.save()

        # note - using the custom django function getlist() here, which
        # handles checkboxes. Note, we don't need escape here because the input
        # will just be numbers. To make sure of that, I'm casting to an int
        # before get_object_or_404, which has its own escaping built in.
        food_id = request.POST.getlist("food item")

        for i in food_id:

            food = get_object_or_404(Food, pk=int(i))

            io = ItemsOrder(foodName=food, quantity=1, order=o)
            io.save()

        return HttpResponseRedirect(
            reverse_lazy("core:order_items", kwargs={"pk": o.id})
        )
    else:
        core_food = Food.objects.all()

        return render(request, "order_create.html", {"core_food": core_food})


class OrderDeleteView(generic.edit.DeleteView):
    model = Order
    template_name = "order_delete.html"
    success_url = reverse_lazy("core:order")


class OrderUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Order
    template_name = "order_update.html"
    form_class = OrderForm
    success_url = reverse_lazy("core:order")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OrderUpdateView, self).form_valid(form)


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "order_items.html"


class ItemsOrderCreateView(generic.edit.CreateView):
    model = ItemsOrder
    template_name = "itemsorder_create.html"
    fields = "__all__"
    success_url = reverse_lazy("core:order")


class ItemsOrderUpdateView(generic.edit.UpdateView):
    model = ItemsOrder
    template_name = "itemsorder_update.html"
    fields = "__all__"
    success_url = reverse_lazy("core:order")


class ItemsOrderDeleteView(generic.edit.DeleteView):
    model = ItemsOrder
    template = "itemsorder_delete.html"
    success_url = reverse_lazy("core:order")


class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = "core/reservation_list.html"
    context_object_name = "object_list"


class ReservationDetailView(DetailView):
    model = Reservation
    template_name = "reservation_detail.html"


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "core/reservation_create.html"
    success_url = reverse_lazy("core:reservation_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        if not form.cleaned_data.get("hostName"):
            form.instance.hostName = self.request.user.get_full_name()
        return super().form_valid(form)


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "core/reservation_create.html"
    success_url = reverse_lazy("core:reservation_list")


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservation
    template_name = "core/reservation_delete.html"
    success_url = reverse_lazy("core:reservation_list")


class EventListView(generic.ListView):
    model = Event
    template_name = "event.html"


class AdminEventCreateView(
    LoginRequiredMixin, UserPassesTestMixin, generic.edit.CreateView
):
    model = Event
    template_name = "admin_event_create.html"
    form_class = EventForm
    success_url = reverse_lazy("core:event")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class AdminEventDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, generic.edit.DeleteView
):
    model = Event
    template_name = "admin_event_delete.html"
    success_url = reverse_lazy("core:event")

    def test_func(self):
        return self.request.user.is_superuser


class AdminEventUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView
):
    model = Event
    template_name = "admin_event_update.html"
    form_class = EventForm
    success_url = reverse_lazy("core:event")

    def test_func(self):
        return self.request.user.is_superuser


class EventDetailView(generic.DetailView):
    model = Event
    template_name = "event_item.html"


class AboutUsView(generic.TemplateView):
    template_name = "about_us.html"


class NewsDetailView(generic.DetailView):
    model = News
    template_name = "news_item.html"


class NewsListView(generic.ListView):
    model = News
    template_name = "news.html"


class AdminNewsCreateView(generic.edit.CreateView):
    model = News
    template_name = "admin_news_create.html"
    fields = "__all__"
    success_url = reverse_lazy("core:news")


class AdminNewsDeleteView(generic.edit.DeleteView):
    model = News
    template_name = "admin_news_delete.html"
    success_url = reverse_lazy("core:news")


class AdminNewsUpdateView(generic.edit.UpdateView):
    model = Event
    template_name = "admin_news_update.html"
    fields = "__all__"
    success_url = reverse_lazy("core:news")


# Staff users (is_staff=True) are considered admin-level users who can access
# additional management views, such as creating, Update and Delete event.
# Non-staff users (is_staff=False) are regular authenticated users with limited access.


# Django is expecting that everything in urls.py actually exists
# everything below here is just placeholder code that
# should be replaced eventually
class SpotlightView(generic.TemplateView):
    template_name = "NOT_A_REAL_TEMPLATE.html"
