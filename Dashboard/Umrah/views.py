from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UmrahPackageCategory, UmrahDetails, LimitedTimeOffer, OfferDetails
from .serializers import (
    UmrahPackageCategorySerializer,
    UmrahDetailsSerializer,
    LimitedTimeOfferSerializer,
    OfferDetailsSerializer
)

# Umrah Package Category API
class UmrahPackageCategoryView(APIView):
    def get(self, request):
        categories = UmrahPackageCategory.objects.all()
        serializer = UmrahPackageCategorySerializer(categories, many=True)
        return Response({"status": "success", "message": "Umrah Package Categories", "data": serializer.data}, status=status.HTTP_200_OK)

class UmrahPackageCategoryView_id(APIView):
    def get(self, request, id):
        try:
            category = UmrahPackageCategory.objects.get(id=id)
            serializer = UmrahPackageCategorySerializer(category)
        except UmrahPackageCategory.DoesNotExist:
            return Response({"status": "error", "message": "No Umrah Package Category found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Umrah Package Category", "data": serializer.data}, status=status.HTTP_200_OK)

# Umrah Details API
class UmrahDetailsView(APIView):
    def get(self, request):
        packages = UmrahDetails.objects.all()
        serializer = UmrahDetailsSerializer(packages, many=True)
        return Response({"status": "success", "message": "Umrah Packages", "data": serializer.data}, status=status.HTTP_200_OK)

class UmrahDetailsView_id(APIView):
    def get(self, request, id):
        try:
            package = UmrahDetails.objects.get(id=id)
            serializer = UmrahDetailsSerializer(package)
        except UmrahDetails.DoesNotExist:
            return Response({"status": "error", "message": "No Umrah Package found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Umrah Package", "data": serializer.data}, status=status.HTTP_200_OK)

# Limited Time Offers API
class LimitedTimeOfferView(APIView):
    def get(self, request):
        offers = LimitedTimeOffer.objects.all()
        serializer = LimitedTimeOfferSerializer(offers, many=True)
        return Response({"status": "success", "message": "Limited Time Offers", "data": serializer.data}, status=status.HTTP_200_OK)

class LimitedTimeOfferView_id(APIView):
    def get(self, request, id):
        try:
            offer = LimitedTimeOffer.objects.get(id=id)
            serializer = LimitedTimeOfferSerializer(offer)
        except LimitedTimeOffer.DoesNotExist:
            return Response({"status": "error", "message": "No Limited Time Offer found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Limited Time Offer", "data": serializer.data}, status=status.HTTP_200_OK)

# Offer Details API
class OfferDetailsView(APIView):
    def get(self, request):
        offer_details = OfferDetails.objects.all()
        serializer = OfferDetailsSerializer(offer_details, many=True)
        return Response({"status": "success", "message": "Offer Details", "data": serializer.data}, status=status.HTTP_200_OK)

class OfferDetailsView_id(APIView):
    def get(self, request, id):
        try:
            offer_detail = OfferDetails.objects.get(id=id)
            serializer = OfferDetailsSerializer(offer_detail)
        except OfferDetails.DoesNotExist:
            return Response({"status": "error", "message": "No Offer Details found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Offer Details", "data": serializer.data}, status=status.HTTP_200_OK)
    