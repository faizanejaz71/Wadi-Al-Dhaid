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
    # path('umrah-banner/', views.UmrahBanner, name='umrah-banner'),
    path('umrah/', views.Umrah, name='umrah'),
    path('umrah-status/', views.UmrahStatus, name='umrah-status'),
    path('visa-status/', views.VisaStatus, name='visa-status'),
    # path('visas/', views.Visas, name='visas'),

# visa_person_type
    path('person-type/', views.Person_type, name='person-type'),
    path('delete-person-type/<int:person_id>/', views.delete_person_type, name='delete-person'),


# visa_category
    path('visa-category/', views.visa_category, name='visa-category'),
    path('delete-category/<int:category_id>/', views.delete_category, name='delete-category'),
    

    # Visa_details
    path('visa-details/', views.visa_details, name='visa-details'),
    path('delete-visa-details/<int:visa_id>/', views.delete_visa_details, name='delete-visa-details'),


    # Visa Requirements
    path('visa-requirements/', views.visa_requirements, name='visa-requirements'),
    path('delete-visa-requirement/<int:req_id>/', views.delete_visa_requirement, name='delete-visa-requirement'),




    # Visa Documents
    path('visa-documents/',views.visa_documents, name='visa-documents'),  # List, Search, Create, Update
    path('visa-documents/delete/<int:doc_id>/', views.delete_visa_document, name='delete-visa-document'),  # Delete






    # Umrah Category
    path('umrah-category/', views.umrah_category, name='umrah-category'),
    path('delete-umrah-category/<int:category_id>/', views.delete_umrah_category, name='delete-umrah-category'),




    #Umrah Details
    path('umrah-details/', views.umrah_details, name='umrah-details'),
    path('delete-umrah/<int:umrah_id>/', views.delete_umrah_details, name='delete-umrah'),



    # Offer type
    path('offer-type/', views.offer_type, name='offer-type'),
    path('delete-offer-type/<int:offer_id>/', views.delete_offer_type, name='delete-offer-type'),




    #Limited Time offer
    path('limited-time-offers/', views.limited_time_offers, name='limited-time-offers'),
    path('delete-limited-time-offer/<int:offer_id>/', views.delete_limited_time_offer, name='delete-limited-time-offer'),



    # Offer Details
    path('offer-details/', views.offer_details, name='offer-details'),
    path('offer-details/delete/<int:offer_id>/', views.delete_offer_details, name='delete-offer-details'),



    # Tour Category
    path('tour-category/', views.tour_category, name='tour-category'),
    path('tour-category/delete/<int:category_id>/', views.delete_tour_category, name='delete-tour-category'),



    # Tour Package Details
    path('tour-packages/', views.tour_package_details, name='tour-package-details'),
    path('tour-packages/delete/<int:tour_id>/', views.delete_tour_package, name='delete-tour-package'),




    # Itinerary Activities
    path('itinerary-activities/', views.itinerary_activity_list, name='itinerary-activity-list'),
    path('itinerary-activities/delete/<int:activity_id>/', views.delete_itinerary_activity, name='delete-itinerary-activity'),






    # Itinerary Meals
    path('itinerary-meals/', views.itinerary_meal_list, name='itinerary-meal-list'),
    path('itinerary-meals/delete/<int:activity_id>/', views.delete_itinerary_meal, name='delete-itinerary-meal'),


    

    # Itinerary Details
    path('itinerary-details/', views.itinerary_details, name='itinerary-details'),
    path('delete-itinerary/<int:itinerary_id>/', views.delete_itinerary, name='delete-itinerary'),




    # Hotel Service
    path('hotel-services/', views.hotel_service_list, name='hotel-service-list'),
    path('hotel-services/delete/<int:service_id>/', views.delete_hotel_service, name='delete-hotel-service'), 




    # Hotel Details
    path('hotels/', views.hotel_details, name='hotel-details'),  # Hotel details page
    path('hotels/delete/<int:hotel_id>/', views.delete_hotel, name='delete-hotel'),  # Delete a hotel



    # Visa Requiremnts
    path('visa-requirements/', views.visa_requirements, name='visa-requirements'),  # Visa requirements page
    path('visa-requirements/delete/<int:requirement_id>/', views.delete_visa_requirement, name='delete-visa-requirement'),  # Delete a visa requirement



    # Inclusion/Exclusion
    path('inclusion-exclusion/', views.inclusion_exclusion, name='inclusion-exclusion'),
    path('delete-inclusion-exclusion/<int:item_id>/', views.delete_inclusion_exclusion, name='delete-inclusion-exclusion'),



    # Terms & Condition
    path('terms-conditions/', views.terms_conditions, name='terms-conditions'),
    path('terms-conditions/delete/<int:item_id>/', views.delete_terms_conditions, name='delete-terms-conditions'),





    # Car Rentals

    # Category
    path('car-category/', views.car_category, name='car-category'),  # List, search, add, update
    path('delete-car-category/<int:category_id>/', views.delete_car_category, name='delete-car-category'),  # Delete



    # Car Details
    path('car-details/', views.car_details, name='car-details'),  # View for car details
    path('delete-car/<int:car_id>/', views.delete_car, name='delete-car'),  # Delete car






    # Car Rents
    path('car-rent/', views.car_rent, name='car-rent'),  # View for listing and updating car rent details
    path('delete-car-rent/<int:rent_id>/', views.delete_car_rent, name='delete-car-rent'),




    # Car Terms Condition
    path('car-terms-and-conditions/', views.car_terms_and_conditions, name='car-terms-and-conditions'),  # List, Search, Add, Update
    path('delete-car-terms-and-conditions/<int:terms_id>/', views.delete_car_terms_and_conditions, name='delete-car-terms-and-conditions'),





    # <-- Navbar -->
    # Logo
    path('navbar-logo/', views.navbar_logo, name='navbar-logo'),
    path('delete-logo/<int:logo_id>/', views.delete_logo, name='delete-logo'),




    # Nav-links
    path('navlinks/', views.navlinks_list, name='navlinks-list'),
    path('navlinks/delete/<int:navlink_id>/', views.delete_navlink, name='delete-navlink'),



    # NewHomeBanner 
    path('banners/', views.new_home_banner, name='new-home-banner'),
    path('banners/delete/<int:banner_id>/', views.delete_banner, name='delete-banner'),


    # Counters
    path('counters/', views.counter_list, name='counter-list'),
    path('counters/delete/<int:counter_id>/', views.delete_counter, name='delete-counter'),




    # Offer_Videos
    path('offer-videos/', views.offer_videos, name='offer-videos'),  # List, Search, Create, Update
    path('offer-videos/delete/<int:video_id>/', views.delete_offer_video, name='delete-offer-video'),  # Delete





    # Seo_Point_Box
    path('seo-point-box/', views.seo_point_box, name='seo-point-box'),  # View & CRUD operations
    path('seo-point-box/delete/<int:box_id>/', views.delete_seo_point_box, name='delete-seo-point-box'),  # Delete operation



    # Tour_Videos
    path('tour-videos/', views.tour_videos, name='tour-videos'),
    path('delete-tour-video/<int:video_id>/', views.delete_tour_video, name='delete-tour-video'),




    path('umrah-banners/', views.umrah_banner_list, name='umrah-banners'),
    path('umrah-banners/delete/<int:banner_id>/', views.delete_umrah_banner, name='delete-umrah-banner'),








    path('why-book-us/', views.why_book_us, name='why-book-us'),
    path('delete-why-book-us/<int:section_id>/', views.delete_why_book_us, name='delete-why-book-us'),
]
