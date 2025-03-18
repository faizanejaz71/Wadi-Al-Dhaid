from django.urls import path
from .views import (
    NewHomeBannerAPIView
)

urlpatterns = [
    # Visa Category URLs
    path('banners/', NewHomeBannerAPIView.as_view(), name='api-new-home-banner'),

]