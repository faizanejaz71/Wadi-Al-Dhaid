from django.contrib import admin
from .models import CarCategory, CarDetails, TermsAndConditions

@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name',)

@admin.register(CarDetails)
class CarDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_name', 'category', 'price_per_day', 'model_from', 'model_to')
    search_fields = ('car_name', 'category__category_name')
    list_filter = ('category', 'model_from', 'model_to')

@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_details', 'terms')
    search_fields = ('car_details__car_name',)

