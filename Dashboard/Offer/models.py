from django.db import models

# Create your models here.


class OfferBannerImage(models.Model):
    banner_image = models.ImageField(upload_to='offer_banner/', blank=True, null=True)

    def __str__(self):
        return self.banner_image
    


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name