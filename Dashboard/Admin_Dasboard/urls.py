from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('carsrent/', views.Carsrent, name='carsrent'),
    path('clients/', views.Clients, name='clients'),
    path('corporateclients/', views.CorporateClients, name='corporateclients'),
    path('featured/', views.Featured, name='featured'),
    path('flight-status/', views.FlightStatus, name='flight-status'),
    path('flights/', views.Flights, name='flights'),
    path('footer/', views.Footer, name='footer'),
    path('hero/', views.Hero, name='hero'),
    path('media/', views.Media, name='media'),
    path('navigation/', views.Navigation, name='navigation'),
    path('newsletter/', views.Newsletter, name='newsletter'),
    path('our-features/', views.OurFeatures, name='our-features'),
    path('package-banner/', views.PackageBanner, name='package-banner'),
    path('services/', views.Services, name='services'),
    path('tours-status/', views.ToursStatus, name='tours-status'),
    path('tours/', views.Tours, name='tours'),
    path('trending-visa/', views.TrendingVisa, name='trending-visa'),
    path('umrah-banner/', views.UmrahBanner, name='umrah-banner'),
    path('umrah/', views.Umrah, name='umrah'),
    path('umrah-status/', views.UmrahStatus, name='umrah-status'),
    path('visa-status/', views.VisaStatus, name='visa-status'),
    # path('visas/', views.Visas, name='visas'),


    path('person-type/', views.Person_type, name='person-type'),
    path('category-type/', views.category_type, name='category-type'),
    path('delete-category/<int:category_id>/', views.delete_category, name='delete-category'),


    
    path('visa-details/', views.visa_details, name='visa-details'),
    path('visa-document/', views.visa_document, name='visa-document'),
    path('visa-requirement/', views.visa_requirement, name='visa-requirement'),
]
