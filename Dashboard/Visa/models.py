from django.db import models

# Create your models here.

# Visa Models


# Visa Category 
class VisaCategory(models.Model):
    visa_category = models.CharField(max_length=100)

    def __str__(self):
        return self.visa_category
        

# Visa Details
class VisaDetails(models.Model):
    visa_category = models.ForeignKey(VisaCategory, on_delete=models.CASCADE)
    country_name = models.CharField(max_length=100)
    adult_price = models.CharField(max_length=100, null=True, blank=True)
    child_price = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='visa_images')
    description = models.TextField()

    def __str__(self):
        return f"{self.country_name} ({self.visa_category.visa_category})"
    

# Visa Requirements
class VisaRequirements(models.Model):
    visa_details = models.ForeignKey(VisaDetails, on_delete=models.CASCADE)
    person_type = models.CharField(max_length=100)


    def __str__(self):
        return f"Requirements for {self.visa_details.country_name}"
    

# Visa Documents
class VisaDocuments(models.Model):
    visa_requirements = models.ForeignKey(VisaRequirements, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=100)
    document_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.document_name} for {self.visa_requirements.visa_details.country_name}"