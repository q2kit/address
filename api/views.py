from django.http import JsonResponse

from api.models import *

def get_provinces(request):
    provinces = Province.objects.all()
    return JsonResponse({'provinces': list(provinces.values())})

def get_districts(request):
    province_id = request.GET.get('province_id')
    districts = District.objects.filter(province_id=province_id)
    return JsonResponse({'districts': list(districts.values())})

def get_wards(request):
    district_id = request.GET.get('district_id')
    wards = Ward.objects.filter(district_id=district_id)
    return JsonResponse({'wards': list(wards.values())})

def validate(request):
    province_id = request.GET.get('province_id')
    district_id = request.GET.get('district_id')
    ward_id = request.GET.get('ward_id')
    if province_id and district_id and ward_id:
        if Ward.objects.filter(id=ward_id, district_id=district_id, province_id=province_id).exists():
            return JsonResponse({'result': True})
    return JsonResponse({'result': False})