from django.db import models

# Umrah Package Category
class UmrahCategory(models.Model):
    umrah_category = models.CharField(max_length=100)

    def __str__(self):
        return self.umrah_category


# Umrah Details
class UmrahDetails(models.Model):
    umrah_category = models.ForeignKey(UmrahCategory, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=100)
    adult_price = models.CharField(max_length=100, null=True, blank=True)
    child_price = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='umrah_images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.package_name} ({self.umrah_category.umrah_category})"


# Offer Type (Replaces PersonType)
class OfferType(models.Model):
    offer_type = models.CharField(max_length=100)

    def __str__(self):
        return self.offer_type


# Limited Time Offers (Replaces UmrahRequirements)
class LimitedTimeOffer(models.Model):
    umrah_details = models.ForeignKey(UmrahDetails, on_delete=models.CASCADE)
    offer_type = models.ForeignKey(OfferType, on_delete=models.CASCADE)
    # offer_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Limited Offer for {self.umrah_details.package_name} ({self.offer_type.offer_type})"


# Offer Details (Replaces UmrahDocuments)
class OfferDetails(models.Model):
    limited_time_offer = models.ForeignKey(LimitedTimeOffer, on_delete=models.CASCADE)
    offer_type = models.ForeignKey(OfferType, on_delete=models.CASCADE, null=True, blank=True)
    document_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    hotel_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.document_name} - {self.limited_time_offer.umrah_details.package_name}"