from django.http import JsonResponse

from api.models import *


def help(request):
    return JsonResponse({
        "api": [
            {
                "path": "/provinces/",
                "method": "GET",
                "description": "Get all provinces",
            },
            {
                "path": "/districts?province_id=xxx",
                "method": "GET",
                "description": "Get all districts by province_id",
            },
            {
                "path": "/wards?district_id=xxx",
                "method": "GET",
                "description": "Get all wards by district_id",
            },
            {
                "path": "/validate?province_id=xxx&district_id=xxx&ward_id=xxx",
                "method": "GET",
                "description": "Validate province_id, district_id, ward_id",
            },
        ]
    })

def get_provinces(request):
    provinces = Province.objects.all()
    return JsonResponse({'provinces': list(provinces.values())})

def get_districts(request):
    province_id = request.GET.get('province_id')
    if not province_id:
        districts = District.objects.all()
    else:
        try:
            province_id = int(province_id)
        except:
            province_id = -1
        districts = District.objects.filter(province_id=province_id)
    return JsonResponse({'districts': list(districts.values())})

def get_wards(request):
    district_id = request.GET.get('district_id')
    if not district_id:
        wards = Ward.objects.all()
    else:
        try:
            district_id = int(district_id)
        except:
            district_id = -1
        wards = Ward.objects.filter(district_id=district_id)

    return JsonResponse({'wards': list(wards.values())})

def validate(request):
    province_id = request.GET.get('province_id')
    district_id = request.GET.get('district_id')
    ward_id = request.GET.get('ward_id')
    try:
        if province_id and district_id and ward_id:
            if Ward.objects.filter(id=ward_id, district_id=district_id, province_id=province_id).exists():
                return JsonResponse({'result': True})
    except:
        return JsonResponse({'result': False})
