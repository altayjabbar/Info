from django.contrib import admin
from .models import Country, CarInfo

# Register Country model with basic setup
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display country name in list view
    search_fields = ('name',)  # Search by country name


# Enhanced CarInfo admin class
@admin.register(CarInfo)
class CarInfoAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'car_nummber', 'name', 'weight_at_border', 'weight_at_silkway', 'is_food', 'terminal', 'country')
    search_fields = ('barcode', 'car_nummber', 'name')  # Enable search on barcode, car number, and name
    list_filter = ('is_food', 'terminal', 'country')  # Enable filtering by food type, terminal, and country
    ordering = ('-weight_at_border',)  # Default ordering by weight at border in descending order
    # readonly_fields = ('barcode',)  # Make barcode read-only if needed
    fieldsets = (
        (None, {
            'fields': ('barcode', 'car_nummber', 'name', 'country')
        }),
        ('Weight Information', {
            'fields': ('weight_at_border', 'weight_at_silkway')
        }),
        ('Other Details', {
            'fields': ('note', 'is_food', 'terminal')
        }),
    )

