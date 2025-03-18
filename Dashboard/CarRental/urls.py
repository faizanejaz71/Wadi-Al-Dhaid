# from django.urls import path
# from .views import (
#     CarCategoryListView, CarCategoryDetailView,
#     CarDetailsListView, CarDetailsDetailView,
#     TermsAndConditionsListView, TermsAndConditionsDetailView
# )

# urlpatterns = [
#     # Car Category URLs
#     path('car-categories/', CarCategoryListView.as_view(), name='car-category-list'),
#     path('car-categories/<int:id>/', CarCategoryDetailView.as_view(), name='car-category-detail'),

#     # Car Details URLs
#     path('car-details/', CarDetailsListView.as_view(), name='car-details-list'),
#     path('car-details/<int:id>/', CarDetailsDetailView.as_view(), name='car-details-detail'),

#     # Terms and Conditions URLs
#     path('terms-and-conditions/', TermsAndConditionsListView.as_view(), name='terms-list'),
#     path('terms-and-conditions/<int:id>/', TermsAndConditionsDetailView.as_view(), name='terms-detail'),
# ]



from django.urls import path
from . import views

urlpatterns = [
    path('indext', views.Indext, name='Indext'),
]