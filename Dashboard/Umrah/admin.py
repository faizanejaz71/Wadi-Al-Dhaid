from django.contrib import admin
from .models import UmrahCategory, UmrahDetails, OfferType, LimitedTimeOffer, OfferDetails

# Umrah Category Admin
@admin.register(UmrahCategory)
class UmrahCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'umrah_category')
    search_fields = ('category_name',)


# Umrah Details Admin
@admin.register(UmrahDetails)
class UmrahDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'package_name', 'adult_price', 'child_price', 'umrah_category')
    search_fields = ('package_name',)
    list_filter = ('umrah_category',)


# Offer Type Admin
@admin.register(OfferType)
class OfferTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'offer_type')
    search_fields = ('offer_type',)


# Limited Time Offer Admin
@admin.register(LimitedTimeOffer)
class LimitedTimeOfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'umrah_details', 'offer_type')
    search_fields = ('umrah_details__package_name', 'offer_type__offer_type')
    list_filter = ('offer_type',)


# Offer Details Admin
@admin.register(OfferDetails)
class OfferDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_name', 'city', 'hotel_name', 'address', 'limited_time_offer', 'offer_type')
    search_fields = ('document_name', 'city', 'hotel_name')
    list_filter = ('city', 'hotel_name')

