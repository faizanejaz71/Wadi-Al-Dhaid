from django.urls import path
from .views import (
    UmrahPackageCategoryView, UmrahPackageCategoryView_id,
    UmrahDetailsView, UmrahDetailsView_id,
    LimitedTimeOfferView, LimitedTimeOfferView_id,
    OfferDetailsView, OfferDetailsView_id
)

urlpatterns = [
    # Umrah Package Category URLs
    path('umrah-package-categories/', UmrahPackageCategoryView.as_view(), name='umrah-package-category-list'),
    path('umrah-package-categories/<int:id>/', UmrahPackageCategoryView_id.as_view(), name='umrah-package-category-detail'),

    # Umrah Details URLs
    path('umrah-details/', UmrahDetailsView.as_view(), name='umrah-details-list'),
    path('umrah-details/<int:id>/', UmrahDetailsView_id.as_view(), name='umrah-details-detail'),

    # Limited Time Offer URLs
    path('limited-time-offers/', LimitedTimeOfferView.as_view(), name='limited-time-offer-list'),
    path('limited-time-offers/<int:id>/', LimitedTimeOfferView_id.as_view(), name='limited-time-offer-detail'),

    # Offer Details URLs
    path('offer-details/', OfferDetailsView.as_view(), name='offer-details-list'),
    path('offer-details/<int:id>/', OfferDetailsView_id.as_view(), name='offer-details-detail'),
]
