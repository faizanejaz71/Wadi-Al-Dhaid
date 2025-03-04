from rest_framework import serializers
from .models import UmrahCategory, UmrahPackage, LimitedOffer, Place

class UmrahCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UmrahCategory
        fields = '__all__'

class UmrahPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmrahPackage
        fields = '__all__'

class LimitedOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = LimitedOffer
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
