from django.contrib import admin
from django.contrib.gis import admin
# Register your models here.
from .models import Snippet,Houses,Farms,Property_1,Property_2,Identity,Well

admin.site.register(Houses, admin.GeoModelAdmin)
admin.site.register(Well, admin.GeoModelAdmin)
admin.site.register(Identity)
admin.site.register(Farms, admin.GeoModelAdmin)
admin.site.register(Property_1)
admin.site.register(Property_2)
admin.site.register(Snippet)


