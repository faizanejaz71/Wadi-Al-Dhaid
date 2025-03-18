from django.contrib import admin
from .models import CarCategory, Car, CarRent, CarTermsAndConditions

# Car Category Admin
@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name',)
    ordering = ('category_name',)


# Car Admin
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'category', 'model_from', 'model_to')
    list_filter = ('brand', 'category', 'model_from', 'model_to')
    search_fields = ('name', 'brand', 'category__category_name')
    ordering = ('brand', 'name')
    readonly_fields = ('model_from', 'model_to')  # Prevent accidental modification

    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'name', 'brand', 'description')
        }),
        ('Model Details', {
            'fields': ('model_from', 'model_to')
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )


# Car Rent Admin
@admin.register(CarRent)
class CarRentAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'rent_within_city_after', 'rent_out_of_station_after')
    list_filter = ('car__brand', 'car__category')
    search_fields = ('car__name', 'car__brand')
    ordering = ('car',)

    fieldsets = (
        ('Car Information', {
            'fields': ('car',)
        }),
        ('Rent Prices (Within City)', {
            'fields': ('rent_within_city_before', 'rent_within_city_after')
        }),
        ('Rent Prices (Out of Station)', {
            'fields': ('rent_out_of_station_before', 'rent_out_of_station_after')
        }),
    )


# Terms & Conditions Admin
@admin.register(CarTermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'short_terms')
    search_fields = ('car__name',)

    def short_terms(self, obj):
        return obj.terms[:50] + "..." if len(obj.terms) > 50 else obj.terms
    short_terms.short_description = "Terms & Conditions (Preview)"
