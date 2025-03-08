from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Visa.models import VisaCategory, VisaDetails, PersonType, VisaRequirements, VisaDocuments
from Visa.serializers import VisaCategorySerializer, VisaDetailsSerializer, PersonTypeSerializer, VisaRequirementsSerializer, VisaDocumentsSerializer

# Visa Category Views
class VisaCategoryView(APIView):
    def get(self, request):
        categories = VisaCategory.objects.all()
        serializer = VisaCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VisaCategoryDetailView(APIView):
    def get(self, request, id):
        category = get_object_or_404(VisaCategory, id=id)
        serializer = VisaCategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Visa Details Views
class VisaDetailsView(APIView):
    def get(self, request):
        details = VisaDetails.objects.all()
        serializer = VisaDetailsSerializer(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VisaDetailsDetailView(APIView):
    def get(self, request, id):
        detail = get_object_or_404(VisaDetails, id=id)
        serializer = VisaDetailsSerializer(detail)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Person Type Views
class PersonTypeView(APIView):
    def get(self, request):
        persons = PersonType.objects.all()
        serializer = PersonTypeSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PersonTypeDetailView(APIView):
    def get(self, request, id):
        person = get_object_or_404(PersonType, id=id)
        serializer = PersonTypeSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Visa Requirements Views
class VisaRequirementsView(APIView):
    def get(self, request):
        requirements = VisaRequirements.objects.all()
        serializer = VisaRequirementsSerializer(requirements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VisaRequirementsDetailView(APIView):
    def get(self, request, id):
        requirement = get_object_or_404(VisaRequirements, id=id)
        serializer = VisaRequirementsSerializer(requirement)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Visa Documents Views
class VisaDocumentsView(APIView):
    def get(self, request):
        documents = VisaDocuments.objects.all()
        serializer = VisaDocumentsSerializer(documents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VisaDocumentsDetailView(APIView):
    def get(self, request, id):
        document = get_object_or_404(VisaDocuments, id=id)
        serializer = VisaDocumentsSerializer(document)
        return Response(serializer.data, status=status.HTTP_200_OK)
