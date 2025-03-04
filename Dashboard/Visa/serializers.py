from rest_framework import serializers

from Visa.models import VisaCategory, VisaDetails, VisaRequirements, VisaDocuments


class VisaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaCategory
        fields = '__all__' 



class VisaDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaDetails
        fields = ['id', 'country_name']



class VisaRequirementsSerializer(serializers.ModelSerializer):
    visa_details = VisaDetailsSerializer()

    class Meta:
        model = VisaRequirements
        fields = '__all__'


class VisaDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaDocuments
        fields = '__all__'