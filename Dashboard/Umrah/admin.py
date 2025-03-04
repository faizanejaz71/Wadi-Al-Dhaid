from django.contrib import admin
from .models import UmrahCategory, UmrahPackage, LimitedOffer, Place


# Umrah Category Admin
@admin.register(UmrahCategory)
class UmrahCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name',)
    ordering = ('category_name',)


# Umrah Package Admin
@admin.register(UmrahPackage)
class UmrahPackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'package_name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('package_name',)
    ordering = ('package_name',)


# Inline Model for Places (to show inside Limited Offer)
class PlaceInline(admin.TabularInline):
    model = Place
    extra = 1  # Show one empty row for adding new places
    fields = ('place_name', 'description')


# Limited Offer (Hotel Details) Admin
@admin.register(LimitedOffer)
class LimitedOfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'offer_type', 'umrah_package')
    list_filter = ('umrah_package__package_name',)
    search_fields = ('offer_type', 'umrah_package__package_name')
    inlines = [PlaceInline]  # Attach Place as inline


# Place Admin
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'limited_offer')
    list_filter = ('limited_offer__umrah_package__package_name',)
    search_fields = ('place_name', 'limited_offer__umrah_package__package_name')
    ordering = ('place_name',)
