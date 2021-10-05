from django.contrib import admin
from .models import Provinces, Departements, ChefLieuProvince, Region

# Register your models here.

admin.site.register(Provinces)
admin.site.register(ChefLieuProvince)
admin.site.register(Departements)
admin.site.register(Region)
