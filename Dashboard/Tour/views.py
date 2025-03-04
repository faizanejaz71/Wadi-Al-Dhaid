from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TourCategory, TourPackage, TourLimitedOffer, TourPlace, VisaRequirements, VisaDocuments, ItineraryDay, TermsAndConditions
from .serializers import TourCategorySerializer, TourPackageSerializer, TourLimitedOfferSerializer, TourPlaceSerializer, VisaRequirementsSerializer, VisaDocumentsSerializer, ItineraryDaySerializer, TermsAndConditionsSerializer

# Tour Category API
class TourCategoryView(APIView):
    def get(self, request):
        categories = TourCategory.objects.all()
        serializer = TourCategorySerializer(categories, many=True)
        return Response({"status": "success", "message": "Tour Categories", "data": serializer.data}, status=status.HTTP_200_OK)

class TourCategoryView_id(APIView):
    def get(self, request, id):
        try:
            category = TourCategory.objects.get(id=id)
            serializer = TourCategorySerializer(category)
        except TourCategory.DoesNotExist:
            return Response({"status": "error", "message": "No Tour Category found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Tour Category", "data": serializer.data}, status=status.HTTP_200_OK)

# Tour Package API
class TourPackageView(APIView):
    def get(self, request):
        packages = TourPackage.objects.all()
        serializer = TourPackageSerializer(packages, many=True)
        return Response({"status": "success", "message": "Tour Packages", "data": serializer.data}, status=status.HTTP_200_OK)

class TourPackageView_id(APIView):
    def get(self, request, id):
        try:
            package = TourPackage.objects.get(id=id)
            serializer = TourPackageSerializer(package)
        except TourPackage.DoesNotExist:
            return Response({"status": "error", "message": "No Tour Package found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Tour Package", "data": serializer.data}, status=status.HTTP_200_OK)

# Tour Limited Offers API
class TourLimitedOfferView(APIView):
    def get(self, request):
        offers = TourLimitedOffer.objects.all()
        serializer = TourLimitedOfferSerializer(offers, many=True)
        return Response({"status": "success", "message": "Tour Limited Offers", "data": serializer.data}, status=status.HTTP_200_OK)

class TourLimitedOfferView_id(APIView):
    def get(self, request, id):
        try:
            offer = TourLimitedOffer.objects.get(id=id)
            serializer = TourLimitedOfferSerializer(offer)
        except TourLimitedOffer.DoesNotExist:
            return Response({"status": "error", "message": "No Tour Limited Offer found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Tour Limited Offer", "data": serializer.data}, status=status.HTTP_200_OK)


# Tour Place API
class TourPlaceView(APIView):
    def get(self, request):
        places = TourPlace.objects.all()
        serializer = TourPlaceSerializer(places, many=True)
        return Response({"status": "success", "message": "Tour Places", "data": serializer.data}, status=status.HTTP_200_OK)

class TourPlaceView_id(APIView):
    def get(self, request, id):
        try:
            place = TourPlace.objects.get(id=id)
            serializer = TourPlaceSerializer(place)
        except TourPlace.DoesNotExist:
            return Response({"status": "error", "message": "No Tour Place found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Tour Place", "data": serializer.data}, status=status.HTTP_200_OK)

# Visa Requirements API
class VisaRequirementsView(APIView):
    def get(self, request):
        requirements = VisaRequirements.objects.all()
        serializer = VisaRequirementsSerializer(requirements, many=True)
        return Response({"status": "success", "message": "Visa Requirements", "data": serializer.data}, status=status.HTTP_200_OK)

class VisaRequirementsView_id(APIView):
    def get(self, request, id):
        try:
            requirement = VisaRequirements.objects.get(id=id)
            serializer = VisaRequirementsSerializer(requirement)
        except VisaRequirements.DoesNotExist:
            return Response({"status": "error", "message": "No Visa Requirement found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Visa Requirement", "data": serializer.data}, status=status.HTTP_200_OK)

# Visa Documents API
class VisaDocumentsView(APIView):
    def get(self, request):
        documents = VisaDocuments.objects.all()
        serializer = VisaDocumentsSerializer(documents, many=True)
        return Response({"status": "success", "message": "Visa Documents", "data": serializer.data}, status=status.HTTP_200_OK)

class VisaDocumentsView_id(APIView):
    def get(self, request, id):
        try:
            document = VisaDocuments.objects.get(id=id)
            serializer = VisaDocumentsSerializer(document)
        except VisaDocuments.DoesNotExist:
            return Response({"status": "error", "message": "No Visa Document found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Visa Document", "data": serializer.data}, status=status.HTTP_200_OK)

# Itinerary Days API
class ItineraryDayView(APIView):
    def get(self, request):
        itinerary_days = ItineraryDay.objects.all()
        serializer = ItineraryDaySerializer(itinerary_days, many=True)
        return Response({"status": "success", "message": "Itinerary Days", "data": serializer.data}, status=status.HTTP_200_OK)

class ItineraryDayView_id(APIView):
    def get(self, request, id):
        try:
            itinerary = ItineraryDay.objects.get(id=id)
            serializer = ItineraryDaySerializer(itinerary)
        except ItineraryDay.DoesNotExist:
            return Response({"status": "error", "message": "No Itinerary found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Itinerary", "data": serializer.data}, status=status.HTTP_200_OK)

# Terms and Conditions API
class TermsAndConditionsView(APIView):
    def get(self, request):
        terms = TermsAndConditions.objects.all()
        serializer = TermsAndConditionsSerializer(terms, many=True)
        return Response({"status": "success", "message": "Terms and Conditions", "data": serializer.data}, status=status.HTTP_200_OK)

class TermsAndConditionsView_id(APIView):
    def get(self, request, id):
        try:
            term = TermsAndConditions.objects.get(id=id)
            serializer = TermsAndConditionsSerializer(term)
        except TermsAndConditions.DoesNotExist:
            return Response({"status": "error", "message": "No Terms and Conditions found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Terms and Conditions", "data": serializer.data}, status=status.HTTP_200_OK)