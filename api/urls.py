from django.urls import path

from .views import get_provinces, get_districts, get_wards, validate

urlpatterns = [
    path('province/', get_provinces),
    path('district/', get_districts),
    path('ward/', get_wards),
    path("validate/", validate),
]
