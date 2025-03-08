from django.contrib import admin
from .models import (
    UmrahPackageCategory, UmrahDetails, OfferType,
    LimitedTimeOffer, OfferDetails
)

@admin.register(UmrahPackageCategory)
class UmrahPackageCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')

@admin.register(UmrahDetails)
class UmrahDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'umrah_package_category', 'package_name', 'adult_price')

@admin.register(OfferType)
class OfferTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'umrah_details', 'offer_type')

@admin.register(LimitedTimeOffer)
class LimitedTimeOfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'umrah_details', 'offer_type')

@admin.register(OfferDetails)
class OfferDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'limited_time_offer', 'offer_type', 'document_name', 'title')
