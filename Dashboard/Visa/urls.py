from django.urls import path
from .views import VisaCategoryView, VisaCategoryView_id, VisaDetailsView, VisaDetailsView_id, VisaRequirementsView, VisaRequirementsView_id, VisaDocumentsView, VisaDocumentsView_id

urlpatterns = [

    #Visa Category
    path('visa-categories/', VisaCategoryView.as_view(), name='visa-category-list'),
    path('visa-categories/<int:id>/', VisaCategoryView_id.as_view(), name='visa-category-detail'),

    #Visa Details
    path('visa-details/', VisaDetailsView.as_view(), name='visa-details-list'),
    path('visa-details/<int:id>/', VisaDetailsView_id.as_view(), name='visa-details-detail'),

    #Visa Requirements
    path('visa-requirements/', VisaRequirementsView.as_view(), name='visa-requirements-list'),
    path('visa-requirements/<int:id>/', VisaRequirementsView_id.as_view(), name='visa-requirements-detail'),

    #Visa Documents
    path('visa-documents/', VisaDocumentsView.as_view(), name='visa-documents-list'),
    path('visa-documents/<int:id>/', VisaDocumentsView_id.as_view(), name='visa-documents-detail'),

]