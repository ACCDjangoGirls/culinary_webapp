from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
# Create your views here.

def home(request):
    return render(request, "home.html", {})


#Django is expecting that everything in urls.py actually exists
#everything below here is just placeholder code that
#should be replaced eventually
class HomeView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class MenuView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminMenuCreateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminMenuUpdateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminMenuDeleteView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ToGoListView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ToGoDetailView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ToGoCreateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ToGoUpdateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ToGoDeleteView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ReservationListView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ReservationDetailView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ReservationCreateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ReservationUpdateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class ReservationDeleteView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminOrderView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AboutUsView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class SpotlightView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class NewsListView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class NewsDetailView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminNewsCreateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminNewsUpdateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminNewsDeleteView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class EventListView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class EventDetailView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminEventCreateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminEventUpdateView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"
class AdminEventDeleteView(generic.TemplateView): template_name = "NOT_A_REAL_TEMPLATE.html"

