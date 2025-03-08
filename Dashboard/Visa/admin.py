from django.contrib import admin
from .models import VisaCategory, VisaDetails, PersonType, VisaRequirements, VisaDocuments

# Visa Category Admin
@admin.register(VisaCategory)
class VisaCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'visa_category')
    search_fields = ('visa_category',)

# Visa Details Admin
@admin.register(VisaDetails)
class VisaDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'visa_category', 'country_name', 'adult_price', 'child_price')
    list_filter = ('visa_category', 'country_name')
    search_fields = ('country_name',)
    ordering = ('country_name',)

# Person Type Admin
@admin.register(PersonType)
class PersonTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'visa_details', 'person_type')
    list_filter = ('visa_details',)
    search_fields = ('person_type',)

# Visa Requirements Admin
@admin.register(VisaRequirements)
class VisaRequirementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'visa_details', 'person_type')
    list_filter = ('visa_details', 'person_type')
    search_fields = ('visa_details__country_name',)

# Visa Documents Admin
@admin.register(VisaDocuments)
class VisaDocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'visa_requirements', 'person_type', 'document_name')
    list_filter = ('visa_requirements', 'person_type')
    search_fields = ('document_name', 'visa_requirements__visa_details__country_name')
