from django.contrib import admin
from .models import Reservation, Ingredient, Foods, Order, ItemsOrder, Event


admin.site.register(Reservation)
admin.site.register(Ingredient)
admin.site.register(Foods)
admin.site.register(Order)
admin.site.register(ItemsOrder)
admin.site.register(Event)