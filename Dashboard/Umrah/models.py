from django.db import models


# Umrah Category
class UmrahCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


# Umrah Package
class UmrahPackage(models.Model):
    category = models.ForeignKey(UmrahCategory, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='umrah_images')
    description = models.TextField()

    def __str__(self):
        return f"{self.package_name} ({self.category.category_name})"


# Limited Offers (Hotel Details)
class LimitedOffer(models.Model):
    umrah_package = models.ForeignKey(UmrahPackage, on_delete=models.CASCADE)
    offer_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.offer_type} - {self.umrah_package.package_name}"


# Places (Makkah, Madinah, etc.)
class Place(models.Model):
    limited_offer = models.ForeignKey(LimitedOffer, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.place_name} ({self.limited_offer.umrah_package.package_name})"
