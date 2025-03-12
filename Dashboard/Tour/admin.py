from django.contrib import admin
from .models import (
    TourCategory, TourPackage, ItineraryService, ItineraryMeals, ItineraryDetail,
    HotelService, HotelDetail, VisaRequirement, InclusionExclusion, TermsAndConditions, BookingForm
)

# Inline for Itinerary in TourPackage
class ItineraryInline(admin.TabularInline):
    model = ItineraryDetail
    extra = 1  # Show one empty form by default

# Inline for Hotels in TourPackage
class HotelInline(admin.TabularInline):
    model = HotelDetail
    extra = 1

# Inline for Visa Requirements in TourPackage
class VisaRequirementInline(admin.TabularInline):
    model = VisaRequirement
    extra = 1

# Inline for Inclusion/Exclusion in TourPackage
class InclusionExclusionInline(admin.TabularInline):
    model = InclusionExclusion
    extra = 1

# Tour Package Admin
@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'country_name', 'price', 'category')
    search_fields = ('package_name', 'country_name')
    list_filter = ('category', 'country_name')
    inlines = [ItineraryInline, HotelInline, VisaRequirementInline, InclusionExclusionInline]

# Tour Category Admin
@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)

# Itinerary Services Admin
@admin.register(ItineraryService)
class ItineraryServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ItineraryMeals)
class ItineraryMealsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
@admin.register(ItineraryDetail)
class ItineraryDetailAdmin(admin.ModelAdmin):
    list_display = ('day', 'title', 'tour_package')  # Customize fields
    search_fields = ('title', 'tour_package__package_name')
    list_filter = ('tour_package',)

# Hotel Services Admin
@admin.register(HotelService)
class HotelServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(HotelDetail)
class HotelDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'ratings', 'address')
    search_fields = ('name', 'address')
    list_filter = ('ratings',)

# Visa Requirement Admin
@admin.register(VisaRequirement)
class VisaRequirementAdmin(admin.ModelAdmin):
    list_display = ('person_type', 'document_name', 'tour_package')
    search_fields = ('person_type', 'document_name')
    list_filter = ('tour_package',)

# Inclusion/Exclusion Admin
@admin.register(InclusionExclusion)
class InclusionExclusionAdmin(admin.ModelAdmin):
    list_display = ('name', 'tour_package')
    search_fields = ('name', 'tour_package__package_name')
    list_filter = ('tour_package',)

# Terms & Conditions Admin
@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('tour_package',)
    search_fields = ('tour_package__package_name',)

# Booking Form Admin
@admin.register(BookingForm)
class BookingFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'tour_package', 'mobile_number', 'email')
    search_fields = ('name', 'tour_package__package_name', 'mobile_number', 'email')
    list_filter = ('tour_package',)
