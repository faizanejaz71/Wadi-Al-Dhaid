from django.db import models
from django.core.validators import RegexValidator



#Navbar
class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')
    
    def __str__(self):
        return f"Logo {self.id}"

class NavLinks(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

class Dropdown(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name







# New Home Banner


class NewHomeBanner(models.Model):
    title = models.CharField(max_length=255, help_text="Enter banner title")
    gif_image = models.ImageField(upload_to='banners/gifs/', help_text="Upload a GIF file")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Counter(models.Model):
    name = models.CharField(max_length=50)
    half = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
    

class OfferVideo(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='offer_videos/')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class SeoPointBox(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='seobox_icon/')
    

    def __str__(self):
        return self.title
    


class TourVideo(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='tour_videos/')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title







class UmrahBanner(models.Model):
    title = models.CharField(max_length=255, help_text="Enter banner title")
    image = models.ImageField(upload_to='banners/umrah/', help_text="Upload an image (any format)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class WhyBookUs(models.Model):
    title = models.CharField(max_length=255, help_text="Enter section title")
    description = models.TextField(help_text="Enter a brief description")
    image = models.ImageField(upload_to='whybookus/', help_text="Upload an image (any format)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return self.title
    

