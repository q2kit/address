from django.http import JsonResponse

from api.models import *


def help(request):
    return JsonResponse({
        "api": [
            {
                "path": "/",
                "method": "GET",
                "description": "Get all provinces",
            },
            {
                "path": "/province_id/",
                "method": "GET",
                "description": "Get all districts by province_id",
            },
            {
                "path": "/province_id/district_id/",
                "method": "GET",
                "description": "Get all wards by district_id",
            },
            {
                "path": "/province_id/district_id/ward_id/",
                "method": "GET",
                "description": "Validate province_id, district_id, ward_id",
            },
        ]
    })

def get_provinces(request):
    provinces = Province.objects.all()
    return JsonResponse({'provinces': list(provinces.values())})

def get_districts(request, province_id):
    try:
        province = Province.objects.get(id=int(province_id))
    except:
        return JsonResponse({'error': 'Invalid province'})
    districts = province.districts.all()
    return JsonResponse({'province': province.to_json(), 'districts': list(districts.values())})


def get_wards(request, province_id, district_id):
    try:
        province = Province.objects.get(id=int(province_id))
    except:
        return JsonResponse({'error': 'Invalid province'})
    try:
        district = District.objects.get(id=int(district_id))
    except:
        return JsonResponse({'error': 'Invalid district'})
    if district.province != province:
        return JsonResponse({'error': 'District does not belong to province'})
    wards = district.wards.all()
    if not wards:
        return JsonResponse({
            'province': province.to_json(),
            'district': district.to_json(),
            'wards': [{'id': -1, 'name': 'There are no wards in this district.'}]
        })
    return JsonResponse({'province': province.to_json(), 'district': district.to_json(), 'wards': list(wards.values())})

def validate(request, province_id, district_id, ward_id):
    try:
        province = Province.objects.get(id=int(province_id))
    except:
        return JsonResponse({'error': 'Invalid province'})
    try:
        district = District.objects.get(id=int(district_id))
    except:
        return JsonResponse({'error': 'Invalid district'})
    if district.province != province:
        return JsonResponse({'error': 'District does not belong to province'})
    if ward_id == '-1':
        return JsonResponse({'province': province.to_json(), 'district': district.to_json()})
    try:
        ward = Ward.objects.get(id=int(ward_id))
    except:
        return JsonResponse({'error': 'Invalid ward'})
    if ward.district != district:
        return JsonResponse({'error': 'Ward does not belong to district'})
    return JsonResponse({'province': province.to_json(), 'district': district.to_json(), 'ward': ward.to_json()})