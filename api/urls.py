from django.urls import path, re_path

from .views import get_provinces, get_districts, get_wards, validate, help_view

urlpatterns = [
    # path('help/', help),
    re_path(r'^help(/.*)?$', help_view),
    path('', get_provinces),
    path('<str:province_id>/', get_districts),
    path('<str:province_id>/<str:district_id>/', get_wards),
    path('<str:province_id>/<str:district_id>/<str:ward_id>/', validate),
]
