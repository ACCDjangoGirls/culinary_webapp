from django.contrib import admin
# from .models import Reservation, Ingredient, Menu, Order, ItemsOrder, Event
from .models import Menu, Ingredient, Order, ItemsOrder, Reservation, Event, News



admin.site.register(Reservation)
admin.site.register(Ingredient)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(ItemsOrder)
admin.site.register(Event)
admin.site.register(News)