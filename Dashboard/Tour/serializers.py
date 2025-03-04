from rest_framework import serializers
from .models import TourCategory, TourPackage, TourLimitedOffer, TourPlace, VisaRequirements, VisaDocuments, ItineraryDay, TermsAndConditions

class TourCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourCategory
        fields = '__all__'

class TourPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields = '__all__'

class TourLimitedOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourLimitedOffer
        fields = '__all__'



class TourPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPlace
        fields = '__all__'

class VisaRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaRequirements
        fields = '__all__'

class VisaDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaDocuments
        fields = '__all__'

class ItineraryDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryDay
        fields = '__all__'

class TermsAndConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsAndConditions
        fields = '__all__'
