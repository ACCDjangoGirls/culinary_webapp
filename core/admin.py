from django.contrib import admin
from .models import Reservation, Ingredient, Food, Order, ItemsOrder, Event


admin.site.register(Reservation)
admin.site.register(Ingredient)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(ItemsOrder)
#admin.site.register(Event)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventName', 'day', 'startTime', 'created_by')

    def save_model(self, request, obj, form, change):
        if not change:  
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Event, EventAdmin)
