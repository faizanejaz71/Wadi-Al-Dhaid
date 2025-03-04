from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UmrahCategory, UmrahPackage, LimitedOffer, Place
from .serializers import UmrahCategorySerializer, UmrahPackageSerializer, LimitedOfferSerializer, PlaceSerializer

# Umrah Category API
class UmrahCategoryView(APIView):
    def get(self, request):
        categories = UmrahCategory.objects.all()
        serializer = UmrahCategorySerializer(categories, many=True)
        return Response({"status": "success", "message": "Umrah Categories", "data": serializer.data}, status=status.HTTP_200_OK)

class UmrahCategoryView_id(APIView):
    def get(self, request, id):
        try:
            category = UmrahCategory.objects.get(id=id)
            serializer = UmrahCategorySerializer(category)
        except UmrahCategory.DoesNotExist:
            return Response({"status": "error", "message": "No Umrah Category found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Umrah Category", "data": serializer.data}, status=status.HTTP_200_OK)

# Umrah Package API
class UmrahPackageView(APIView):
    def get(self, request):
        packages = UmrahPackage.objects.all()
        serializer = UmrahPackageSerializer(packages, many=True)
        return Response({"status": "success", "message": "Umrah Packages", "data": serializer.data}, status=status.HTTP_200_OK)

class UmrahPackageView_id(APIView):
    def get(self, request, id):
        try:
            package = UmrahPackage.objects.get(id=id)
            serializer = UmrahPackageSerializer(package)
        except UmrahPackage.DoesNotExist:
            return Response({"status": "error", "message": "No Umrah Package found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Umrah Package", "data": serializer.data}, status=status.HTTP_200_OK)

# Limited Offers API
class LimitedOfferView(APIView):
    def get(self, request):
        offers = LimitedOffer.objects.all()
        serializer = LimitedOfferSerializer(offers, many=True)
        return Response({"status": "success", "message": "Limited Offers", "data": serializer.data}, status=status.HTTP_200_OK)

class LimitedOfferView_id(APIView):
    def get(self, request, id):
        try:
            offer = LimitedOffer.objects.get(id=id)
            serializer = LimitedOfferSerializer(offer)
        except LimitedOffer.DoesNotExist:
            return Response({"status": "error", "message": "No Limited Offer found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Limited Offer", "data": serializer.data}, status=status.HTTP_200_OK)

# Places API
class PlaceView(APIView):
    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response({"status": "success", "message": "Places", "data": serializer.data}, status=status.HTTP_200_OK)

class PlaceView_id(APIView):
    def get(self, request, id):
        try:
            place = Place.objects.get(id=id)
            serializer = PlaceSerializer(place)
        except Place.DoesNotExist:
            return Response({"status": "error", "message": "No Place found", "data": []}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "message": "Place", "data": serializer.data}, status=status.HTTP_200_OK)
