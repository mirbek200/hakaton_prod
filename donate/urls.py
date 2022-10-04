from django.urls import path
from .views import DonateApiView

urlpatterns = [
    path('donate/', DonateApiView.as_view(), name='donate')
]