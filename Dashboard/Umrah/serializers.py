from rest_framework import serializers
from .models import UmrahPackageCategory, UmrahDetails, LimitedTimeOffer, OfferDetails

# Umrah Package Category Serializer
class UmrahPackageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UmrahPackageCategory
        fields = '__all__'

# Umrah Details Serializer
class UmrahDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmrahDetails
        fields = '__all__'

# Limited Time Offer Serializer
class LimitedTimeOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = LimitedTimeOffer
        fields = '__all__'

# Offer Details Serializer (Includes Image & Title Fields)
class OfferDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferDetails
        fields = '__all__'
