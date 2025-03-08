from django.urls import path
from .views import (
    VisaCategoryView, VisaCategoryDetailView,
    VisaDetailsView, VisaDetailsDetailView,
    PersonTypeView, PersonTypeDetailView,
    VisaRequirementsView, VisaRequirementsDetailView,
    VisaDocumentsView, VisaDocumentsDetailView
)

urlpatterns = [
    # Visa Category URLs
    path('visa-categories/', VisaCategoryView.as_view(), name='visa-category-list'),
    path('visa-categories/<int:id>/', VisaCategoryDetailView.as_view(), name='visa-category-detail'),

    # Visa Details URLs
    path('visa-details/', VisaDetailsView.as_view(), name='visa-details-list'),
    path('visa-details/<int:id>/', VisaDetailsDetailView.as_view(), name='visa-details-detail'),

    # Person Type URLs
    path('person-types/', PersonTypeView.as_view(), name='person-type-list'),
    path('person-types/<int:id>/', PersonTypeDetailView.as_view(), name='person-type-detail'),

    # Visa Requirements URLs
    path('visa-requirements/', VisaRequirementsView.as_view(), name='visa-requirements-list'),
    path('visa-requirements/<int:id>/', VisaRequirementsDetailView.as_view(), name='visa-requirements-detail'),

    # Visa Documents URLs
    path('visa-documents/', VisaDocumentsView.as_view(), name='visa-documents-list'),
    path('visa-documents/<int:id>/', VisaDocumentsDetailView.as_view(), name='visa-documents-detail'),
]
