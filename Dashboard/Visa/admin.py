from django.contrib import admin
from .models import VisaCategory, VisaDetails, VisaRequirements, VisaDocuments

# Visa Category Admin
@admin.register(VisaCategory)
class VisaCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'visa_category')  # Show ID and Visa Category in admin list
    search_fields = ('visa_category',)  # Enable search by category name
    ordering = ('visa_category',)  # Order by category name


# Visa Details Admin
@admin.register(VisaDetails)
class VisaDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_name', 'visa_category', 'adult_price')  # Show important fields
    list_filter = ('visa_category',)  # Filter by visa category
    search_fields = ('country_name',)  # Search by country name
    ordering = ('country_name',)


# Inline Model for Visa Documents (to show inside Visa Requirements)
class VisaDocumentsInline(admin.TabularInline):  # Inline editing for documents
    model = VisaDocuments
    extra = 1  # Show one empty row for adding new documents
    fields = ('document_name', 'document_description')  # Fields to display


# Visa Requirements Admin
@admin.register(VisaRequirements)
class VisaRequirementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'visa_details', 'person_type')  # Display visa requirement details
    list_filter = ('visa_details__country_name',)  # Filter by country name
    search_fields = ('visa_details__country_name', 'person_type')  # Search by country/person type
    inlines = [VisaDocumentsInline]  # Attach VisaDocuments as inline


# Visa Documents Admin
@admin.register(VisaDocuments)
class VisaDocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_name', 'visa_requirements', 'document_description')  # Show fields
    list_filter = ('visa_requirements__visa_details__country_name',)  # Filter by country name
    search_fields = ('document_name', 'visa_requirements__visa_details__country_name')  # Search by document name & country
    ordering = ('document_name',)
