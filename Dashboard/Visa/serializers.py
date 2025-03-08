from rest_framework import serializers
from Visa.models import VisaCategory, VisaDetails, PersonType, VisaRequirements, VisaDocuments

class VisaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaCategory
        fields = '__all__'

class VisaDetailsSerializer(serializers.ModelSerializer):
    visa_category = VisaCategorySerializer()

    class Meta:
        model = VisaDetails
        fields = '__all__'

class PersonTypeSerializer(serializers.ModelSerializer):
    visa_details = VisaDetailsSerializer()

    class Meta:
        model = PersonType
        fields = '__all__'

class VisaRequirementsSerializer(serializers.ModelSerializer):
    visa_details = VisaDetailsSerializer()
    person_type = PersonTypeSerializer()

    class Meta:
        model = VisaRequirements
        fields = '__all__'

class VisaDocumentsSerializer(serializers.ModelSerializer):
    visa_requirements = VisaRequirementsSerializer()
    person_type = PersonTypeSerializer()

    class Meta:
        model = VisaDocuments
        fields = '__all__'
