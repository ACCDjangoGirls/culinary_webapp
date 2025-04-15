from django.contrib import admin
from django.urls import include, path
from . import views
from django.views import generic
from . import views

app_name = "core"
urlpatterns = [
    path("menu/", views.MenuView.as_view(), name="menu"),
    path("admin_menu_create/", views.AdminMenuCreateView.as_view(), name="admin_menu_create"),
    path("admin_menu_update/<int:pk>", views.AdminMenuUpdateView.as_view(), name="admin_menu_update"),
    path("admin_menu_delete/<int:pk>", views.AdminMenuDeleteView.as_view(), name="admin_menu_delete"),
    path("menu_detail/<int:pk>", views.MenuDetailView.as_view(), name="menu_item"),
    path("admin_ingredient_create/", views.AdminIngredientCreateView.as_view(), name="admin_ingredient_create"),
    path("admin_ingredient_delete/<int:pk>", views.AdminIngredientDeleteView.as_view(), name="admin_ingredient_delete"),
    path("admin_ingredient_update/<int:pk>", views.AdminIngredientUpdateView.as_view(), name="admin_ingredient_update"),
    path("order/", views.OrderView.as_view(), name="order"),
    path("order_detail/<int:pk>", views.OrderDetailView.as_view(), name="order_items"),
    path("order/create/", views.OrderCreateView.as_view(), name="order_create"),
    path("order/update/<int:pk>", views.OrderUpdateView.as_view(), name="order_update"),
    path("order/delete/<int:pk>", views.OrderDeleteView.as_view(), name="order_delete"),
    path("itemsordercreate/", views.ItemsOrderCreateView.as_view(), name="itemsorder_create"),
    path("itemsorderupdate/<int:pk>", views.ItemsOrderUpdateView.as_view(), name="itemsorder_update"),
    path("itemsorderdelete/<int:pk>", views.ItemsOrderDeleteView.as_view(), name="itemsorder_delete"),
    path("reservation/", views.ReservationListView.as_view(), name="reservation"),
    path("reservation/<int:pk>", views.ReservationDetailView.as_view(), name="reservation_item"),
    path("reservation/create/", views.ReservationCreateView.as_view(), name="reservation_create"),
    path("reservation/update/<int:pk>", views.ReservationUpdateView.as_view(), name="reservation_update"),
    path("reservation/delete/<int:pk>", views.ReservationDeleteView.as_view(), name="reservation_delete"),
    path("admin_order/", views.AdminOrderView.as_view(), name="admin_orders"),
    path("about_us/", views.AboutUsView.as_view(), name="about_us"),
    path("student_spotlights/", views.SpotlightView.as_view(), name="spotlight"),
    path("news/", views.NewsListView.as_view(), name="news"),
    path("news/<int:pk>", views.NewsDetailView.as_view(), name="news_item"),
    path("admin_news_create/", views.AdminNewsCreateView.as_view(), name="admin_news_create"),
    path("admin_news_update/<int:pk>", views.AdminNewsUpdateView.as_view(), name="admin_news_update"),
    path("admin_news_delete/<int:pk>", views.AdminNewsDeleteView.as_view(), name="admin_news_delete"),
    path("event/", views.EventListView.as_view(), name="event"),
    path("event/<int:pk>", views.EventDetailView.as_view(), name="event_item"),
    path("admin_event_create/", views.AdminEventCreateView.as_view(), name="admin_event_create"),
    path("admin_event_update/<int:pk>", views.AdminEventUpdateView.as_view(), name="admin_event_update"),
    path("admin_event_delete/<int:pk>", views.AdminEventDeleteView.as_view(), name="admin_event_delete"),
]
