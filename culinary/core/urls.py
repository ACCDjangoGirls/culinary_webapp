from . import views
from django.urls import path, include

urlpatterns = [
      path('', views.home, name='home'),
      path('secret/', views.SecretIndexView.as_view(template_name="core/secret.html"), name ='secret'),
        ]
