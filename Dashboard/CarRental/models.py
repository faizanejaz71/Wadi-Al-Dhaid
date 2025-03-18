from django.db import models
from datetime import datetime

# Car Category Model
class CarCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    

# Car Details Model
class Car(models.Model):
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE, related_name="cars")
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model_from = models.PositiveSmallIntegerField(default=2000)
    model_to = models.PositiveSmallIntegerField(default=datetime.now().year)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.brand} {self.name} ({self.model_from} - {self.model_to})"


# Car Rental Model
class CarRent(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="rental_info")
    rent_within_city_before = models.DecimalField(max_digits=10, decimal_places=2, help_text="Previous rent within the city")
    rent_within_city_after = models.DecimalField(max_digits=10, decimal_places=2, help_text="Current rent within the city")
    rent_out_of_station_before = models.DecimalField(max_digits=10, decimal_places=2, help_text="Previous rent out of station")
    rent_out_of_station_after = models.DecimalField(max_digits=10, decimal_places=2, help_text="Current rent out of station")

    def __str__(self):
        return f"Rent Details for {self.car.name} ({self.car.model_from} - {self.car.model_to})"


class CarTermsAndConditions(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="terms_conditions", null=True, blank=True)
    terms = models.TextField()

    def __str__(self):
        return f"Terms and Conditions for {self.car.name}" if self.car else "Terms and Conditions (No Car Assigned)"
