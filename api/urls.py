from django.urls import path

from .views import get_provinces, get_districts, get_wards, validate, help

urlpatterns = [
    path('', help),
    path('provinces/', get_provinces),
    path('districts/', get_districts),
    path('wards/', get_wards),
    path("validate/", validate),
]
