from rest_framework import serializers
from .models import CarCategory, CarDetails, TermsAndConditions



# Car Category Serializer
class CarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategory
        fields = '__all__'

# Car Details Serializer
class CarDetailsSerializer(serializers.ModelSerializer):
    category = CarCategorySerializer()  # Nested serializer

    class Meta:
        model = CarDetails
        fields = '__all__'

# Terms and Conditions Serializer
class TermsAndConditionsSerializer(serializers.ModelSerializer):
    car_details = CarDetailsSerializer()

    class Meta:
        model = TermsAndConditions
        fields = '__all__'