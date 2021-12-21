# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from mainapp.models import Accommodation


class MainTemplateView(TemplateView):
    template_name = 'mainapp/index.html'


class AccommodationListView(ListView):
    template_name = 'mainapp/accommodations.html'

    def get_queryset(self):
        return Accommodation.get_items()


class AccommodationDetailView(DetailView):
    model = Accommodation
    template_name = 'mainapp/accommodation_details.html'
