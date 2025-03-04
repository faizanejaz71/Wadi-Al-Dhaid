from django.db import models
from datetime import datetime

# Create your models here.

class CarCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    

class CarDetails(models.Model):
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=100)
    price_per_day = models.IntegerField()
    #Model from to to
    model_from = models.PositiveSmallIntegerField(default=2000)
    model_to = models.PositiveSmallIntegerField(default=datetime.now().year)
    image = models.ImageField(upload_to='car_images')
    description = models.TextField()

    def __str__(self):
        return f"{self.car_name} ({self.category.category_name})"
    


# Terms and Conditions
class TermsAndConditions(models.Model):
    car_details = models.ForeignKey(CarDetails, on_delete=models.CASCADE)
    terms = models.TextField()

    def __str__(self):
        return f"Terms and Conditions for {self.car_details.car_name}"