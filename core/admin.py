from django.contrib import admin
from .models import Reservation, Ingredient, Food, Order, ItemsOrder, Event


admin.site.register(Reservation)
admin.site.register(Ingredient)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(ItemsOrder)
admin.site.register(Event)