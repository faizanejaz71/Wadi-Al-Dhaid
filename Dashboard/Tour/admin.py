from django.contrib import admin
from .models import (
    TourCategory, TourPackage, TourLimitedOffer, TourPlace,
    VisaRequirements, VisaDocuments, ItineraryDay,
    TermsAndConditions, BookingForm
)


# Tour Category Admin
@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name',)


# Tour Package Admin
@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'package_name', 'country_name', 'category', 'price')
    list_filter = ('category', 'country_name')
    search_fields = ('package_name', 'country_name')


# Inline Model for Tour Places (Inside Limited Offers)
class TourPlaceInline(admin.TabularInline):
    model = TourPlace
    extra = 1
    fields = ('place_name', 'description')


# Tour Limited Offer Admin
@admin.register(TourLimitedOffer)
class TourLimitedOfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'offer_type', 'tour_package')
    list_filter = ('tour_package__package_name',)
    search_fields = ('offer_type', 'tour_package__package_name')
    inlines = [TourPlaceInline]


# Tour Place Admin
@admin.register(TourPlace)
class TourPlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'tour_limited_offer')
    search_fields = ('place_name',)


# Inline Model for Visa Documents (Inside Visa Requirements)
class VisaDocumentsInline(admin.TabularInline):
    model = VisaDocuments
    extra = 1
    fields = ('document_name', 'document_description')


# Visa Requirements Admin
@admin.register(VisaRequirements)
class VisaRequirementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'person_type', 'tour_package')
    list_filter = ('tour_package__package_name',)
    search_fields = ('person_type', 'tour_package__package_name')
    inlines = [VisaDocumentsInline]


# Visa Documents Admin
@admin.register(VisaDocuments)
class VisaDocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_name', 'visa_requirement')
    search_fields = ('document_name',)


# Itinerary Admin
@admin.register(ItineraryDay)
class ItineraryDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'day', 'title', 'tour_package')
    list_filter = ('tour_package__package_name',)
    search_fields = ('title', 'tour_package__package_name')


# Terms and Conditions Admin
@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tour_package')
    search_fields = ('title', 'tour_package__package_name')


# Booking Form Admin
@admin.register(BookingForm)
class BookingFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile_number', 'email', 'tour_package')
    search_fields = ('name', 'email', 'tour_package__package_name')
