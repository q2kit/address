from django.urls import path

from .views import get_provinces, get_districts, get_wards, validate, help

urlpatterns = [
    path('help/', help),
    path('', get_provinces),
    path('<str:province_id>/', get_districts),
    path('<str:province_id>/<str:district_id>/', get_wards),
    path('<str:province_id>/<str:district_id>/<str:ward_id>/', validate),
]
