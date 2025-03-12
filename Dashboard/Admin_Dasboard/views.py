from django.shortcuts import render, redirect, get_object_or_404
from Visa.models import VisaDetails, VisaCategory, PersonType, VisaRequirements, VisaDocuments
from Umrah.models import UmrahCategory, UmrahDetails, OfferType, LimitedTimeOffer, OfferDetails

# Create your views here.


def Base (request):
    return render(request, 'base.html')


def Index (request):
    return render(request, 'index.html')

def Carsrent (request):
    return render(request, 'carsrent.html')

def Clients (request):
    return render(request, 'clients-review.html')

def CorporateClients (request):
    return render(request, 'corporateclients.html')

def Featured (request):
    return render(request, 'featured.html')

def FlightStatus (request):
    return render(request, 'flight-status.html')

def Flights (request):
    return render(request, 'flights.html')

def Footer (request):
    return render(request, 'footer.html')

def Hero (request):
    return render(request, 'hero.html')

def Media (request):
    return render(request, 'media.html')

def Navigation (request):
    return render(request, 'navigation.html')

def Newsletter (request):
    return render(request, 'newsletter.html')

def OurFeatures (request):
    return render(request, 'our-features.html')

def PackageBanner (request):
    return render(request, 'package-banner.html')

def Services (request):
    return render(request, 'services.html')

def ToursStatus (request):
    return render(request, 'tours-status.html')

def Tours (request):
    return render(request, 'tours.html')

def TrendingVisa (request):
    return render(request, 'trending-visas.html')

def UmrahBanner (request):
    return render(request, 'umrah-banner.html')

def Umrah (request):
    return render(request, 'umrah.html')

def UmrahStatus (request):
    return render(request, 'umrah-status.html')

def VisaStatus (request):
    return render(request, 'visa-status.html')




# <--- visa Starts --->


# Person Type
def Person_type(request):
    query = request.GET.get('search', '')  # Get search input
    person_types = PersonType.objects.all()  # Get all person types

    if query:
        person_types = person_types.filter(person_type__icontains=query)  # Filter search

    person = None  # Initialize person variable

    if request.method == "POST":
        person_id = request.POST.get('person_id')  # Get ID for update
        person_type_name = request.POST.get('person_type')  # Get person type name

        if person_id:  # If updating an existing entry
            person = get_object_or_404(PersonType, id=person_id)
            person.person_type = person_type_name
            person.save()
        else:  # Creating a new entry
            PersonType.objects.create(
                person_type=person_type_name
            )

        return redirect('person-type')

    context = {
        'person_types': person_types,
        'person': person,
        'search_query': query,  
    }
    
    return render(request, 'Visa/visa-person-type.html', context)


def delete_person_type(request, person_id):
    person = get_object_or_404(PersonType, id=person_id)
    person.delete()
    return redirect('person-type')





# Visa Category
def visa_category(request):
    query = request.GET.get('search', '')  # Get search input from GET request
    total_visas_num = VisaCategory.objects.count()

    if query:
        visa_categories = VisaCategory.objects.filter(visa_category__icontains=query)  # Case-insensitive search
    else:
        visa_categories = VisaCategory.objects.all()  # Show all if no search query

    if request.method == "POST":
        visa_id = request.POST.get('visa_id')  # Check if it's an update
        category_name = request.POST.get('visa_category')

        if visa_id:  # Update existing record
            category = get_object_or_404(VisaCategory, id=visa_id)
            category.visa_category = category_name
            category.save()
        else:  # Create new category
            VisaCategory.objects.create(visa_category=category_name)

        return redirect('visa-category')  # Redirect to the same page after adding/updating

    context = {
        'visa_categories': visa_categories,
        'search_query': query,  # Pass search query to template
        'total_visas_num': total_visas_num,
    }
    return render(request, 'Visa/visa-category.html', context)


def delete_category(request, category_id):
    category = get_object_or_404(VisaCategory, id=category_id)
    category.delete()
    return redirect('visa-category')





# Visa Details
def visa_details(request):
    query = request.GET.get('search', '')  # Get search input from GET request
    total_visas_details_num = VisaDetails.objects.count()

    if query:
        visa_detail = VisaDetails.objects.filter(country_name__icontains=query)
    else:
        visa_detail = VisaDetails.objects.all()

    visa_category = VisaCategory.objects.all()
    visa = None  # Initialize visa variable for update functionality

    if request.method == "POST":
        visa_id = request.POST.get('visa_id')  # Get visa_id for update
        category_id = request.POST.get('visa_category')
        country_name = request.POST.get('country_name')
        adult_price = request.POST.get('adult_price', '')
        child_price = request.POST.get('child_price', '')
        image = request.FILES.get('image')
        description = request.POST.get('description', '')

        category = get_object_or_404(VisaCategory, id=category_id)

        if visa_id:  # If visa_id exists, update existing visa
            visa = get_object_or_404(VisaDetails, id=visa_id)
            visa.visa_category = category
            visa.country_name = country_name
            visa.adult_price = adult_price
            visa.child_price = child_price
            if image:
                visa.image = image  # Only update image if new one is uploaded
            visa.description = description
            visa.save()
        else:  # Create a new visa entry
            visa = VisaDetails.objects.create(
                visa_category=category,
                country_name=country_name,
                adult_price=adult_price,
                child_price=child_price,
                image=image,
                description=description
            )

        return redirect('visa-details')

    context = {
        'visa_detail': visa_detail,
        'visa_category': visa_category,
        'total_visas_details_num': total_visas_details_num,
        'visa': visa,  # Send visa object for update
        'search_query': query,  # Pass search query to template

    }
    return render(request, 'Visa/visa-details.html', context)


def delete_visa_details(request, visa_id):
    visa = get_object_or_404(VisaDetails, id=visa_id)
    visa.delete()
    return redirect('visa-details')





# Visa Requirements
def visa_requirements(request):
    query = request.GET.get('search', '')  # Get search input from GET request
    total_requirements_num = VisaRequirements.objects.count()

    if query:
        visa_reqs = VisaRequirements.objects.filter(visa_details__country_name__icontains=query)
    else:
        visa_reqs = VisaRequirements.objects.all()

    visa_details = VisaDetails.objects.all()
    person_types = PersonType.objects.all()
    visa_req = None  # Initialize visa_req variable for update functionality

    if request.method == "POST":
        req_id = request.POST.get('req_id')  # Get requirement ID for update
        visa_details_id = request.POST.get('visa_details')
        person_type_id = request.POST.get('person_type')

        visa_detail = get_object_or_404(VisaDetails, id=visa_details_id)
        person_type = get_object_or_404(PersonType, id=person_type_id)

        if req_id:  # If req_id exists, update existing requirement
            visa_req = get_object_or_404(VisaRequirements, id=req_id)
            visa_req.visa_details = visa_detail
            visa_req.person_type = person_type
            visa_req.save()
        else:  # Create a new visa requirement entry
            visa_req = VisaRequirements.objects.create(
                visa_details=visa_detail,
                person_type=person_type,
            )

        return redirect('visa-requirements')

    context = {
        'visa_reqs': visa_reqs,
        'visa_details': visa_details,
        'person_types': person_types,
        'total_requirements_num': total_requirements_num,
        'visa_req': visa_req,  # Send visa_req object for update
        'search_query': query,  # Pass search query to template
    }
    return render(request, 'Visa/visa-requirement.html', context)


def delete_visa_requirement(request, req_id):
    visa_req = get_object_or_404(VisaRequirements, id=req_id)
    visa_req.delete()
    return redirect('visa-requirements')






# Create and manage Visa Documents
def visa_documents(request):
    query = request.GET.get('search', '')  # Get search input
    total_documents = VisaDocuments.objects.count()

    if query:
        documents = VisaDocuments.objects.filter(document_name__icontains=query)
    else:
        documents = VisaDocuments.objects.all()

    visa_requirements = VisaRequirements.objects.all()
    person_types = PersonType.objects.all()
    document = None  # Initialize document for update

    if request.method == "POST":
        doc_id = request.POST.get('doc_id')  # Get document ID for update
        visa_req_id = request.POST.get('visa_requirements')
        person_type_id = request.POST.get('person_type', None)
        document_name = request.POST.get('document_name')
        document_description = request.POST.get('document_description', '')

        visa_requirement = get_object_or_404(VisaRequirements, id=visa_req_id)
        person_type = None
        if person_type_id:
            person_type = get_object_or_404(PersonType, id=person_type_id)

        if doc_id:  # Update existing document
            document = get_object_or_404(VisaDocuments, id=doc_id)
            document.visa_requirements = visa_requirement
            document.person_type = person_type
            document.document_name = document_name
            document.document_description = document_description
            document.save()
        else:  # Create new document
            document = VisaDocuments.objects.create(
                visa_requirements=visa_requirement,
                person_type=person_type,
                document_name=document_name,
                document_description=document_description
            )

        return redirect('visa-documents')

    context = {
        'documents': documents,
        'visa_requirements': visa_requirements,
        'person_types': person_types,
        'total_documents': total_documents,
        'document': document,  # Send document for update
        'search_query': query,  # Pass search query to template
    }
    return render(request, 'Visa/visa-document.html', context)


# Delete Visa Document
def delete_visa_document(request, doc_id):
    document = get_object_or_404(VisaDocuments, id=doc_id)
    document.delete()
    return redirect('visa-documents')










# <--- Umrah Starts --->


# Umrah Category

def umrah_category(request):
    query = request.GET.get('search', '')  # Get search input from GET request
    total_umrah_num = UmrahCategory.objects.count()

    if query:
        umrah_categories = UmrahCategory.objects.filter(umrah_category__icontains=query)  # Case-insensitive search
    else:
        umrah_categories = UmrahCategory.objects.all()  # Show all if no search query

    if request.method == "POST":
        umrah_id = request.POST.get('umrah_id')  # Check if it's an update
        category_name = request.POST.get('umrah_category')

        if umrah_id:  # Update existing record
            category = get_object_or_404(UmrahCategory, id=umrah_id)
            category.umrah_category = category_name
            category.save()
        else:  # Create new category
            UmrahCategory.objects.create(umrah_category=category_name)

        return redirect('umrah-category')  # Redirect to the same page after adding/updating

    context = {
        'umrah_categories': umrah_categories,
        'search_query': query,  # Pass search query to template
        'total_umrah_num': total_umrah_num,
    }
    return render(request, 'Umrah/umrah-category.html', context)


def delete_umrah_category(request, category_id):
    category = get_object_or_404(UmrahCategory, id=category_id)
    category.delete()
    return redirect('umrah-category')




#Umrah Details
def umrah_details(request):
    query = request.GET.get('search', '')  # Search functionality
    total_umrah_details_num = UmrahDetails.objects.count()

    if query:
        umrah_detail = UmrahDetails.objects.filter(package_name__icontains=query)
    else:
        umrah_detail = UmrahDetails.objects.all()

    umrah_category = UmrahCategory.objects.all()
    umrah = None  # Initialize umrah variable for update functionality

    if request.method == "POST":
        umrah_id = request.POST.get('umrah_id')  # Get umrah_id for update
        category_id = request.POST.get('umrah_category')
        package_name = request.POST.get('package_name')
        adult_price = request.POST.get('adult_price', '')
        child_price = request.POST.get('child_price', '')
        image = request.FILES.get('image')
        description = request.POST.get('description', '')

        category = get_object_or_404(UmrahCategory, id=category_id)

        if umrah_id:  # If umrah_id exists, update existing entry
            umrah = get_object_or_404(UmrahDetails, id=umrah_id)
            umrah.umrah_category = category
            umrah.package_name = package_name
            umrah.adult_price = adult_price
            umrah.child_price = child_price
            if image:
                umrah.image = image  # Only update image if new one is uploaded
            umrah.description = description
            umrah.save()
        else:  # Create a new Umrah entry
            umrah = UmrahDetails.objects.create(
                umrah_category=category,
                package_name=package_name,
                adult_price=adult_price,
                child_price=child_price,
                image=image,
                description=description
            )

        return redirect('umrah-details')

    context = {
        'umrah_detail': umrah_detail,
        'umrah_category': umrah_category,
        'total_umrah_details_num': total_umrah_details_num,
        'umrah': umrah,  # Send umrah object for update
        'search_query': query,  # Pass search query to template
    }
    return render(request, 'Umrah/umrah-details.html', context)


def delete_umrah_details(request, umrah_id):
    umrah = get_object_or_404(UmrahDetails, id=umrah_id)
    umrah.delete()
    return redirect('umrah-details')




# Offer Type View
def offer_type(request):
    query = request.GET.get('search', '')  # Get search input
    offer_types = OfferType.objects.all()  # Get all offer types

    if query:
        offer_types = offer_types.filter(offer_type__icontains=query)  # Filter search results

    offer = None  # Initialize offer variable

    if request.method == "POST":
        offer_id = request.POST.get('offer_id')  # Get ID for update
        offer_type_name = request.POST.get('offer_type')  # Get offer type name

        if offer_id:  # If updating an existing entry
            offer = get_object_or_404(OfferType, id=offer_id)
            offer.offer_type = offer_type_name
            offer.save()
        else:  # Creating a new entry
            OfferType.objects.create(
                offer_type=offer_type_name
            )

        return redirect('offer-type')

    context = {
        'offer_types': offer_types,
        'offer': offer,
        'search_query': query,  
    }
    
    return render(request, 'Umrah/umrah-offer-type.html', context)

# Delete Offer Type View
def delete_offer_type(request, offer_id):
    offer = get_object_or_404(OfferType, id=offer_id)
    offer.delete()
    return redirect('offer-type')





# Limited Time Offer 
def limited_time_offers(request):
    query = request.GET.get('search', '')  # Search functionality
    total_offers_num = LimitedTimeOffer.objects.count()

    if query:
        offers = LimitedTimeOffer.objects.filter(umrah_details__package_name__icontains=query)
    else:
        offers = LimitedTimeOffer.objects.all()

    umrah_details = UmrahDetails.objects.all()
    offer_types = OfferType.objects.all()
    limited_offer = None  # Initialize variable for update functionality

    if request.method == "POST":
        offer_id = request.POST.get('offer_id')  # Get offer ID for update
        umrah_details_id = request.POST.get('umrah_details')
        offer_type_id = request.POST.get('offer_type')

        umrah_detail = get_object_or_404(UmrahDetails, id=umrah_details_id)
        offer_type = get_object_or_404(OfferType, id=offer_type_id)

        if offer_id:  # Update existing offer
            limited_offer = get_object_or_404(LimitedTimeOffer, id=offer_id)
            limited_offer.umrah_details = umrah_detail
            limited_offer.offer_type = offer_type
            limited_offer.save()
        else:  # Create new offer
            limited_offer = LimitedTimeOffer.objects.create(
                umrah_details=umrah_detail,
                offer_type=offer_type,
            )

        return redirect('limited-time-offers')

    context = {
        'offers': offers,
        'umrah_details': umrah_details,
        'offer_types': offer_types,
        'total_offers_num': total_offers_num,
        'limited_offer': limited_offer,
        'search_query': query,
    }
    return render(request, 'umrah/umrah-limited-time-offer.html', context)

def delete_limited_time_offer(request, offer_id):
    offer = get_object_or_404(LimitedTimeOffer, id=offer_id)
    offer.delete()
    return redirect('limited-time-offers')





# Offer Details
def offer_details(request):
    query = request.GET.get('search', '')  # Search functionality
    total_offers = OfferDetails.objects.count()

    if query:
        offers = OfferDetails.objects.filter(document_name__icontains=query)
    else:
        offers = OfferDetails.objects.all()

    offer_types = OfferType.objects.all()
    limited_offers = LimitedTimeOffer.objects.all()
    offer = None  # Initialize offer variable for update functionality

    if request.method == "POST":
        offer_id = request.POST.get('offer_id')  # Get offer_id for update
        offer_type_id = request.POST.get('offer_type')
        limited_offer_id = request.POST.get('limited_offer')
        document_name = request.POST.get('document_name')
        city = request.POST.get('city', '')
        hotel_name = request.POST.get('hotel_name', '')
        address = request.POST.get('address', '')
        description = request.POST.get('description', '')

        offer_type = get_object_or_404(OfferType, id=offer_type_id) if offer_type_id else None
        limited_offer = get_object_or_404(LimitedTimeOffer, id=limited_offer_id)

        if offer_id:  # If offer_id exists, update existing entry
            offer = get_object_or_404(OfferDetails, id=offer_id)
            offer.offer_type = offer_type
            offer.limited_time_offer = limited_offer
            offer.document_name = document_name
            offer.city = city
            offer.hotel_name = hotel_name
            offer.address = address
            offer.description = description
            offer.save()
        else:  # Create a new Offer entry
            offer = OfferDetails.objects.create(
                offer_type=offer_type,
                limited_time_offer=limited_offer,
                document_name=document_name,
                city=city,
                hotel_name=hotel_name,
                address=address,
                description=description
            )

        return redirect('offer-details')

    context = {
        'offers': offers,
        'offer_types': offer_types,
        'limited_offers': limited_offers,
        'total_offers': total_offers,
        'offer': offer,  # Send offer object for update
        'search_query': query,  # Pass search query to template
    }
    return render(request, 'umrah/offer-details.html', context)


def delete_offer_details(request, offer_id):
    offer = get_object_or_404(OfferDetails, id=offer_id)
    offer.delete()
    return redirect('offer-details')