from django.shortcuts import render, redirect, get_object_or_404
from Visa.models import VisaDetails, VisaCategory

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

# def Visas (request):
#     visa = VisaDetails.objects.all() 
#     context = {
#         'visa': visa
#     }
#     return render(request, 'visas.html', context)


def Person_type (request):
    return render(request, 'Visa/person-type.html')


def category_type(request):
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

        return redirect('category-type')  # Redirect to the same page after adding/updating

    context = {
        'visa_categories': visa_categories,
        'search_query': query,  # Pass search query to template
        'total_visas_num': total_visas_num,
    }
    return render(request, 'Visa/category-type.html', context)


def delete_category(request, category_id):
    category = get_object_or_404(VisaCategory, id=category_id)
    category.delete()
    return redirect('category-type')


def visa_details(request):
    query = request.GET.get('search', '')  # Get search input from GET request
    total_visas = VisaDetails.objects.count()

    if query:
        visa_detail = VisaDetails.objects.filter(country_name__icontains=query)  # Case-insensitive search
    else:
        visa_detail = VisaDetails.objects.all()  # Show all if no search query

    visa_category = VisaCategory.objects.all()

    if request.method == "POST":
        visa_id = request.POST.get('visa_id')  # Check if it's an update
        category_id = request.POST.get('visa_category')
        country_name = request.POST.get('country_name')
        adult_price = request.POST.get('adult_price', '')
        child_price = request.POST.get('child_price', '')
        image = request.FILES.get('image')
        description = request.POST.get('description', '')

        category = get_object_or_404(VisaCategory, id=category_id)

        if visa_id:  # Update existing record
            visa = get_object_or_404(VisaDetails, id=visa_id)
            visa.visa_category = category
            visa.country_name = country_name
            visa.adult_price = adult_price
            visa.child_price = child_price
            if image:
                visa.image = image  # Only update image if a new one is uploaded
            visa.description = description
            visa.save()
        else:  # Create new visa entry
            VisaDetails.objects.create(
                visa_category=category,
                country_name=country_name,
                adult_price=adult_price,
                child_price=child_price,
                image=image,
                description=description
            )

        return redirect('visa-details')  # Redirect to the same page after adding/updating

    context = {
        'visa_detail': visa_detail,
        'visa_category': visa_category,
        'total_visas': total_visas
    }
    return render(request, 'Visa/visa-details.html', context)


def visa_document (request):
    return render(request, 'Visa/visa-document.html')   


def visa_requirement (request):
    return render(request, 'Visa/visa-requirement.html')