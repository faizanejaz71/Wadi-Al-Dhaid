# from django.db import models


# # Umrah Category
# class UmrahCategory(models.Model):
#     category_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.category_name


# # Umrah Package
# class UmrahPackage(models.Model):
#     category = models.ForeignKey(UmrahCategory, on_delete=models.CASCADE)
#     package_name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     image = models.ImageField(upload_to='umrah_images')
#     description = models.TextField()

#     def __str__(self):
#         return f"{self.package_name} ({self.category.category_name})"


# # Limited Offers (Hotel Details)
# class LimitedOffer(models.Model):
#     umrah_package = models.ForeignKey(UmrahPackage, on_delete=models.CASCADE)
#     offer_type = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.offer_type} - {self.umrah_package.package_name}"


# # Places (Makkah, Madinah, etc.)
# class Place(models.Model):
#     limited_offer = models.ForeignKey(LimitedOffer, on_delete=models.CASCADE)
#     place_name = models.CharField(max_length=100)
#     description = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.place_name} ({self.limited_offer.umrah_package.package_name})"


from django.db import models

# Umrah Package Category
class UmrahPackageCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


# Umrah Details
class UmrahDetails(models.Model):
    umrah_package_category = models.ForeignKey(UmrahPackageCategory, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=100)
    adult_price = models.DecimalField(max_digits=10, decimal_places=2)
    child_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='umrah_images')
    description = models.TextField()

    def __str__(self):
        return f"{self.package_name} ({self.umrah_package_category.category_name})"


# Offer Type (Special Discounts, Group Offers, etc.)
class OfferType(models.Model):
    umrah_details = models.ForeignKey(UmrahDetails, on_delete=models.CASCADE, null=True, blank=True)
    offer_type = models.CharField(max_length=100)

    def __str__(self):
        return self.offer_type


# Limited Time Offer (e.g., Seasonal or Short-Term Offers)
class LimitedTimeOffer(models.Model):
    umrah_details = models.ForeignKey(UmrahDetails, on_delete=models.CASCADE)
    offer_type = models.ForeignKey(OfferType, on_delete=models.CASCADE)

    def __str__(self):
        return f"Limited Time Offer for {self.umrah_details.package_name}"


# Offer Details (Added ImageField & Title)
class OfferDetails(models.Model):
    limited_time_offer = models.ForeignKey(LimitedTimeOffer, on_delete=models.CASCADE)
    offer_type = models.ForeignKey(OfferType, on_delete=models.CASCADE, null=True, blank=True)
    document_name = models.CharField(max_length=100)
    document_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='offer_images', null=True, blank=True)  # Added Image Field
    title = models.CharField(max_length=255, null=True, blank=True)  # Added Title Field

    def __str__(self):
        return f"{self.document_name} for {self.limited_time_offer.umrah_details.package_name}"
