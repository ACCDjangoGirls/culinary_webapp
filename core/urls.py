from django.contrib import admin
from django.urls import include, path
from . import views
from django.views import generic
from . import views

app_name = "core"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("menu/", views.MenuView.as_view(), name="menu"),
    path("admin_menu_create/", views.AdminMenuCreateView.as_view(), name="admin_menu_create"),
    path("admin_menu_update/<int:pk>", views.AdminMenuUpdateView.as_view(), name="admin_menu_update"),
    path("admin_menu_delete/<int:pk>", views.AdminMenuDeleteView.as_view(), name="admin_menu_delete"),
    path("togo/", views.ToGoListView.as_view(), name="togo"),
    path("togo/<int:pk>", views.ToGoDetailView.as_view(), name="togo_item"),
    path("togo/create/", views.ToGoCreateView.as_view(), name="togo_create"),
    path("togo/update/<int:pk>", views.ToGoUpdateView.as_view(), name="togo_update"),
    path("togo/delete/<int:pk>", views.ToGoDeleteView.as_view(), name="togo_delete"),
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
]
