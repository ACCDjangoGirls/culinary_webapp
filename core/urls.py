from django.contrib import admin
from django.urls import include, path
from . import views
from django.views import generic
from . import views
from .views import (
    ReservationListView,
    ReservationCreateView,
    ReservationUpdateView,
    ReservationDeleteView,
)


app_name = "core"
urlpatterns = [
    path("food/", views.FoodView.as_view(), name="food"),
    path(
        "admin_food_create/",
        views.AdminFoodCreateView.as_view(),
        name="admin_food_create",
    ),
    path(
        "admin_food_update/<int:pk>",
        views.AdminFoodUpdateView.as_view(),
        name="admin_food_update",
    ),
    path(
        "admin_food_delete/<int:pk>",
        views.AdminFoodDeleteView.as_view(),
        name="admin_food_delete",
    ),
    path("food_detail/<int:pk>", views.FoodDetailView.as_view(), name="food_item"),
    path(
        "admin_ingredient_create/",
        views.AdminIngredientCreateView.as_view(),
        name="admin_ingredient_create",
    ),
    path(
        "admin_ingredient_delete/<int:pk>",
        views.AdminIngredientDeleteView.as_view(),
        name="admin_ingredient_delete",
    ),
    path(
        "admin_ingredient_update/<int:pk>",
        views.AdminIngredientUpdateView.as_view(),
        name="admin_ingredient_update",
    ),
    path("order/", views.OrderView.as_view(), name="order"),
    path("order_detail/<int:pk>", views.OrderDetailView.as_view(), name="order_items"),
    path("order/create/", views.OrderCreateView, name="order_create"),
    path("order/update/<int:pk>", views.OrderUpdateView.as_view(), name="order_update"),
    path("order/delete/<int:pk>", views.OrderDeleteView.as_view(), name="order_delete"),
    path(
        "itemsordercreate/",
        views.ItemsOrderCreateView.as_view(),
        name="itemsorder_create",
    ),
    path(
        "itemsorderupdate/<int:pk>",
        views.ItemsOrderUpdateView.as_view(),
        name="itemsorder_update",
    ),
    path(
        "itemsorderdelete/<int:pk>/",
        views.ItemsOrderDeleteView.as_view(),
        name="itemsorder_delete",
    ),
    path("reservations/", ReservationListView.as_view(), name="reservation_list"),
    path(
        "reservations/<int:pk>/",
        views.ReservationDetailView.as_view(),
        name="reservation_detail",
    ),
    path(
        "reservations/create/",
        ReservationCreateView.as_view(),
        name="reservation_create",
    ),
    path(
        "reservations/<int:pk>/update/",
        ReservationUpdateView.as_view(),
        name="reservation_update",
    ),
    path(
        "reservations/<int:pk>/delete/",
        ReservationDeleteView.as_view(),
        name="reservation_delete",
    ),
    path("about_us/", views.AboutUsView.as_view(), name="about_us"),
    path("student_spotlights/", views.SpotlightView.as_view(), name="spotlight"),
    path("news/", views.NewsListView.as_view(), name="news"),
    path("news/<int:pk>", views.NewsDetailView.as_view(), name="news_item"),
    path(
        "admin_news_create/",
        views.AdminNewsCreateView.as_view(),
        name="admin_news_create",
    ),
    path(
        "admin_news_update/<int:pk>",
        views.AdminNewsUpdateView.as_view(),
        name="admin_news_update",
    ),
    path(
        "admin_news_delete/<int:pk>",
        views.AdminNewsDeleteView.as_view(),
        name="admin_news_delete",
    ),
    path("event/", views.EventListView.as_view(), name="event"),
    path("event/<int:pk>", views.EventDetailView.as_view(), name="event_item"),
    path(
        "admin_event_create/",
        views.AdminEventCreateView.as_view(),
        name="admin_event_create",
    ),
    path(
        "admin_event_update/<int:pk>",
        views.AdminEventUpdateView.as_view(),
        name="admin_event_update",
    ),
    path(
        "admin_event_delete/<int:pk>",
        views.AdminEventDeleteView.as_view(),
        name="admin_event_delete",
    ),
]
