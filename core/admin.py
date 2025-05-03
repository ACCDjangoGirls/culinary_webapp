from django.contrib import admin
from .models import Menu, Ingredient, Order, ItemsOrder, Reservation, Event, News, NewsImage

# class NewsImageInline(admin.TabularInline):
#     model = NewsImage
#     extra = 1

# class NewsAdmin(admin.ModelAdmin):
#     inlines = [NewsImageInline]

admin.site.register(Reservation)
admin.site.register(Ingredient)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(ItemsOrder)
admin.site.register(Event)

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageInline]

admin.site.register(News, NewsAdmin)
admin.site.register(NewsImage) 