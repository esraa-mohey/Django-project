from django.contrib import admin

from .models import stations
#from Region.admin import RegionAdmin

@admin.register(stations)
class SatationAdmin (admin.ModelAdmin):
     list_display =['idS','operationCode','name']
