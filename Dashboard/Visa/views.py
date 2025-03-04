from django.shortcuts import render

# Create your views here.
from Visa.models import VisaCategory, VisaDetails, VisaRequirements, VisaDocuments
from Visa.serializers import VisaCategorySerializer, VisaDetailsSerializer, VisaRequirementsSerializer, VisaDocumentsSerializer


#From Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response   
from rest_framework import status 


class VisaCategoryView(APIView):
    def get(self, request):
        visa_category = VisaCategory.objects.all()
        serializer = VisaCategorySerializer(visa_category, many=True)
        try :
            if not visa_category:
                raise Exception("No Visa Categories found")
        except Exception as e:
            category= {
                "status": "error",
                "message": str(e),
                "data": []
            }
        category= {
            "status": "success",
            "message": "Visa Categories",
            "data": serializer.data
        }
        return Response(category, status=status.HTTP_200_OK)
    
class VisaCategoryView_id(APIView):
    def get(self, request, id):
        visa_category = VisaCategory.objects.get(id=id)
        serializer = VisaCategorySerializer(visa_category)
        try :
            if not visa_category:
                raise Exception("No Visa Category found")
        except Exception as e:
            category= {
                "status": "error",
                "message": str(e),
                "data": []
            }
        category= {
            "status": "success",
            "message": "Visa Category",
            "data": serializer.data
        }
        return Response(category, status=status.HTTP_200_OK)
    


# visa Detail

class VisaDetailsView(APIView): # For List
    def get(self, request):
        visa_details = VisaDetails.objects.all()
        serializer = VisaDetailsSerializer(visa_details, many=True)
        try:
            if not visa_details.exists():
                raise Exception("No Visa Details found")
        except Exception as e:
            details = {
                "status": "error",
                "message": str(e),
                "data": []
            }
            return Response(details, status=status.HTTP_404_NOT_FOUND)

        details = {
            "status": "success",
            "message": "Visa Details",
            "data": serializer.data
        }
        return Response(details, status=status.HTTP_200_OK)

class VisaDetailsView_id(APIView): # For specific id
    def get(self, request, id):
        try:
            visa_detail = VisaDetails.objects.get(id=id)
            serializer = VisaDetailsSerializer(visa_detail)
        except VisaDetails.DoesNotExist:
            details = {
                "status": "error",
                "message": "No Visa Detail found",
                "data": []
            }
            return Response(details, status=status.HTTP_404_NOT_FOUND)

        details = {
            "status": "success",
            "message": "Visa Detail",
            "data": serializer.data
        }
        return Response(details, status=status.HTTP_200_OK)



# Visa Requirements

class VisaRequirementsView(APIView):
    def get(self, request):
        visa_requirements = VisaRequirements.objects.all()
        serializer = VisaRequirementsSerializer(visa_requirements, many=True)
        try:
            if not visa_requirements.exists():
                raise Exception("No Visa Requirements found")
        except Exception as e:
            response = {
                "status": "error",
                "message": str(e),
                "data": []
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        response = {
            "status": "success",
            "message": "Visa Requirements",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
class VisaRequirementsView_id(APIView):
    def get(self, request, id):
        try:
            visa_requirement = VisaRequirements.objects.get(id=id)
            serializer = VisaRequirementsSerializer(visa_requirement)
        except VisaRequirements.DoesNotExist:
            response = {
                "status": "error",
                "message": "No Visa Requirement found",
                "data": []
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        response = {
            "status": "success",
            "message": "Visa Requirement",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    



# Visa Documents

class VisaDocumentsView(APIView):
    def get(self, request):
        visa_documents = VisaDocuments.objects.all()
        serializer = VisaDocumentsSerializer(visa_documents, many=True)
        try:
            if not visa_documents.exists():
                raise Exception("No Visa Documents found")
        except Exception as e:
            response = {
                "status": "error",
                "message": str(e),
                "data": []
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        response = {
            "status": "success",
            "message": "Visa Documents",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

class VisaDocumentsView_id(APIView):
    def get(self, request, id):
        try:
            visa_document = VisaDocuments.objects.get(id=id)
            serializer = VisaDocumentsSerializer(visa_document)
        except VisaDocuments.DoesNotExist:
            response = {
                "status": "error",
                "message": "No Visa Document found",
                "data": []
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        response = {
            "status": "success",
            "message": "Visa Document",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)