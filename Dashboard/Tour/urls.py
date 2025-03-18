# from django.urls import path
# from .views import (TourCategoryView, TourCategoryView_id, 
#                     TourPackageView, TourPackageView_id, 
#                     TourLimitedOfferView, TourLimitedOfferView_id,
#                     TourPlaceView, TourPlaceView_id,
#                     VisaRequirementsView, VisaRequirementsView_id,
#                     VisaDocumentsView, VisaDocumentsView_id,
#                     ItineraryDayView, ItineraryDayView_id,
#                     TermsAndConditionsView, TermsAndConditionsView_id)

# urlpatterns = [
#     # Tour Category URLs
#     path('tour-categories/', TourCategoryView.as_view(), name='tour-category-list'),
#     path('tour-categories/<int:id>/', TourCategoryView_id.as_view(), name='tour-category-detail'),

#     # Tour Package URLs
#     path('tour-packages/', TourPackageView.as_view(), name='tour-package-list'),
#     path('tour-packages/<int:id>/', TourPackageView_id.as_view(), name='tour-package-detail'),

#     # Tour Limited Offer URLs
#     path('tour-limited-offers/', TourLimitedOfferView.as_view(), name='tour-limited-offer-list'),
#     path('tour-limited-offers/<int:id>/', TourLimitedOfferView_id.as_view(), name='tour-limited-offer-detail'),

#     # Tour Place URLs
#     path('tour-places/', TourPlaceView.as_view(), name='tour-place-list'),
#     path('tour-places/<int:id>/', TourPlaceView_id.as_view(), name='tour-place-detail'),

#     # Visa Requirements
#     path('visa-requirements/', VisaRequirementsView.as_view(), name='visa-requirement-list'),
#     path('visa-requirements/<int:id>/', VisaRequirementsView_id.as_view(), name='visa-requirement-detail'),

#     # Visa Documents
#     path('visa-documents/', VisaDocumentsView.as_view(), name='visa-document-list'),
#     path('visa-documents/<int:id>/', VisaDocumentsView_id.as_view(), name='visa-document-detail'),

#     # Itinerary Days
#     path('itinerary-days/', ItineraryDayView.as_view(), name='itinerary-day-list'),
#     path('itinerary-days/<int:id>/', ItineraryDayView_id.as_view(), name='itinerary-day-detail'),

#     # Terms and Conditions
#     path('terms-and-conditions/', TermsAndConditionsView.as_view(), name='terms-conditions-list'),
#     path('terms-and-conditions/<int:id>/', TermsAndConditionsView_id.as_view(), name='terms-conditions-detail'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='tour_home'),
]