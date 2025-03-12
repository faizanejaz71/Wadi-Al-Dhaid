from django.db import models

# Tour Category
class TourCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


# Tour Package
class TourPackage(models.Model):
    category = models.ForeignKey(TourCategory, on_delete=models.PROTECT, null=True, blank=True)
    package_name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField for better pricing
    image = models.ImageField(upload_to='tour_packages/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.package_name} ({self.category.category_name})"















# Itinerary Details

class ItineraryService(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class ItineraryMeals(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class ItineraryDetail(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)  # Linked to Tour Package
    day = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    activities = models.ManyToManyField(ItineraryService, related_name="itinerary_services", blank=True)
    meals = models.ManyToManyField(ItineraryMeals, related_name="itinerary_meals", blank=True)
    image = models.ImageField(upload_to='itineraries/', blank=True, null=True)

    def __str__(self):
        return f"Day {self.day}: {self.title}"
















# Hotel Details
class HotelService(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class HotelDetail(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)  # Linked to Tour Package
    name = models.CharField(max_length=255)
    ratings = models.DecimalField(max_digits=3, decimal_places=1)
    address = models.TextField()
    services = models.ManyToManyField(HotelService, related_name="hotel_services", blank=True)
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)

    def __str__(self):
        return self.name















# Visa Requirements
class VisaRequirement(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)  # Linked to Tour Package
    person_type = models.CharField(max_length=255)
    document_name = models.CharField(max_length=255)
    document_details = models.TextField()

    def __str__(self):
        return f"{self.person_type} - {self.document_name}"













class InclusionExclusion(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)  # Linked to Tour Package
    name = models.CharField(max_length=255)  # Example: "Included" or "Not Included"
    details = models.TextField()  # Example: "Airfare, Visa, Accommodation, Meals, etc."

    def __str__(self):
        return f"{self.name} - {self.tour_package.package_name}"
    















    
# Terms and Conditions
class TermsAndConditions(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)  # Linked to Tour Package
    details = models.TextField(null=True, blank=True)  # Terms & Conditions content

    def __str__(self):
        return f"Terms for {self.tour_package.package_name}"



# Booking Form
class BookingForm(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    flying_from = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"Booking by {self.name} for {self.tour_package.package_name}"
