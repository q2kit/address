from django.contrib import admin

from api.models import Province, District, Ward

# Register your models here.

class DistrictInline(admin.TabularInline):
    model = District


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    inlines = [DistrictInline]


class WardInline(admin.TabularInline):
    model = Ward


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'province')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'province')
    inlines = [WardInline]


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'district')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')