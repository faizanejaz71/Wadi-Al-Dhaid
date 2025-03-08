from django.db import models


# Tour Category
class TourCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


# Tour Package
class TourPackage(models.Model):
    category = models.ForeignKey(TourCategory, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='tour_images')
    description = models.TextField()

    def __str__(self):
        return f"{self.package_name} ({self.category.category_name})"


# Limited Offers (Hotel Details for Tours)
class TourLimitedOffer(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    offer_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.offer_type} - {self.tour_package.package_name}"


# Places (Cities, Attractions)
class TourPlace(models.Model):
    tour_limited_offer = models.ForeignKey(TourLimitedOffer, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.place_name} ({self.tour_limited_offer.tour_package.package_name})"


# Visa Requirements
class VisaRequirements(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    person_type = models.CharField(max_length=100)

    def __str__(self):
        return f"Visa Requirements for {self.tour_package.country_name}"


# Visa Documents
class VisaDocuments(models.Model):
    visa_requirement = models.ForeignKey(VisaRequirements, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=100)
    document_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.document_name} - {self.visa_requirement.tour_package.country_name}"


# Itinerary (Days)
class ItineraryDay(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    day = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Day {self.day} - {self.tour_package.package_name}"


# Terms and Conditions
class TermsAndConditions(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.tour_package.package_name}"


# Booking Form
class BookingForm(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    flying_from = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"Booking by {self.name} for {self.tour_package.package_name}"




























# from django.db import models

# # Tour Category 
# class TourCategory(models.Model):
#     category_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.category_name

# # Tour Details
# class TourDetails(models.Model):
#     category = models.ForeignKey(TourCategory, on_delete=models.CASCADE)
#     country_name = models.CharField(max_length=100)
#     package_name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     image = models.ImageField(upload_to='tour_images')
#     description = models.TextField()

#     def __str__(self):
#         return f"{self.package_name} ({self.category.category_name})"

# # Offer Type
# class OfferType(models.Model):
#     tour_details = models.ForeignKey(TourDetails, on_delete=models.CASCADE)
#     offer_type = models.CharField(max_length=100)

#     def __str__(self):
#         return self.offer_type  

# # Tour Limited Offers
# class TourLimitedOffer(models.Model):
#     tour_details = models.ForeignKey(TourDetails, on_delete=models.CASCADE)
#     offer_type = models.ForeignKey(OfferType, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.offer_type.offer_type} - {self.tour_details.package_name}"

# # Tour Places
# class TourPlaces(models.Model):
#     tour_limited_offer = models.ForeignKey(TourLimitedOffer, on_delete=models.CASCADE)
#     place_name = models.CharField(max_length=100)
#     description = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return self.place_name

# # Person Type
# class PersonType(models.Model):
#     tour_details = models.ForeignKey(TourDetails, on_delete=models.CASCADE)
#     person_type = models.CharField(max_length=100)

#     def __str__(self):
#         return self.person_type  

# # Visa Requirements
# class TourVisaRequirements(models.Model):
#     tour_details = models.ForeignKey(TourDetails, on_delete=models.CASCADE)
#     person_type = models.ForeignKey(PersonType, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Visa Requirements for {self.tour_details.country_name}"

# # Visa Documents
# class TourVisaDocuments(models.Model):
#     tour_visa_requirements = models.ForeignKey(TourVisaRequirements, on_delete=models.CASCADE)
#     person_type = models.ForeignKey(PersonType, on_delete=models.CASCADE, null=True, blank=True)
#     document_name = models.CharField(max_length=100)
#     document_description = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.document_name} for {self.tour_visa_requirements.tour_details.country_name}"

# # Itinerary Days
# class ItineraryDay(models.Model):
#     tour_details = models.ForeignKey(TourDetails, on_delete=models.CASCADE)
#     day = models.PositiveIntegerField()
#     title = models.CharField(max_length=100)
#     description = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f"Day {self.day} - {self.tour_details.package_name}"

# # Terms and Conditions
# class TourTermsAndConditions(models.Model):
#     tour_details = models.ForeignKey(TourDetails, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     description = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.title} - {self.tour_details.package_name}"

# # Booking Form
# class TourBookingForm(models.Model):
#     tour_details = models.ForeignKey(TourDetails, on_delete=models.CASCADE)
#     flying_from = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     mobile_number = models.CharField(max_length=15)
#     email = models.EmailField()

#     def __str__(self):
#         return f"Booking by {self.name} for {self.tour_details.package_name}"
