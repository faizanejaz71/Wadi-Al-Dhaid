from django.urls import path
from .views import (UmrahCategoryView, UmrahCategoryView_id, 
                    UmrahPackageView, UmrahPackageView_id, 
                    LimitedOfferView, LimitedOfferView_id, 
                    PlaceView, PlaceView_id)

urlpatterns = [
    # Umrah Category URLs
    path('umrah-categories/', UmrahCategoryView.as_view(), name='umrah-category-list'),
    path('umrah-categories/<int:id>/', UmrahCategoryView_id.as_view(), name='umrah-category-detail'),

    # Umrah Package URLs
    path('umrah-packages/', UmrahPackageView.as_view(), name='umrah-package-list'),
    path('umrah-packages/<int:id>/', UmrahPackageView_id.as_view(), name='umrah-package-detail'),

    # Limited Offer URLs
    path('limited-offers/', LimitedOfferView.as_view(), name='limited-offer-list'),
    path('limited-offers/<int:id>/', LimitedOfferView_id.as_view(), name='limited-offer-detail'),

    # Places URLs
    path('places/', PlaceView.as_view(), name='place-list'),
    path('places/<int:id>/', PlaceView_id.as_view(), name='place-detail'),
]
