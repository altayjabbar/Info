from django.contrib import admin

# Register your models here.
from .models import Country,CarInfo
admin.site.register(CarInfo)
admin.site.register(Country)
