from django.urls import path

from mainapp.views import AccommodationDetailView, AccommodationListView

app_name = 'mainapp'

urlpatterns = [
    path('', AccommodationListView.as_view(), name='index'),
    path('accommodation_detail/<int:pk>/', AccommodationDetailView.as_view(), name='accommodation')
]
