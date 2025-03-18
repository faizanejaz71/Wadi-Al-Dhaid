# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from .models import CarCategory, CarDetails, TermsAndConditions
# from .serializers import CarCategorySerializer, CarDetailsSerializer, TermsAndConditionsSerializer

# # -------------------- Car Category APIs -------------------- #
# # Get All Car Categories
# class CarCategoryListView(APIView):
#     def get(self, request):
#         categories = CarCategory.objects.all()
#         serializer = CarCategorySerializer(categories, many=True)
#         return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

# # Get Car Category by ID
# class CarCategoryDetailView(APIView):
#     def get(self, request, id):
#         category = get_object_or_404(CarCategory, id=id)
#         serializer = CarCategorySerializer(category)
#         return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

# # -------------------- Car Details APIs -------------------- #
# # Get All Car Details
# class CarDetailsListView(APIView):
#     def get(self, request):
#         cars = CarDetails.objects.all()
#         serializer = CarDetailsSerializer(cars, many=True)
#         return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

# # Get Car Details by ID
# class CarDetailsDetailView(APIView):
#     def get(self, request, id):
#         car = get_object_or_404(CarDetails, id=id)
#         serializer = CarDetailsSerializer(car)
#         return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

# # -------------------- Terms & Conditions APIs -------------------- #
# # Get All Terms & Conditions
# class TermsAndConditionsListView(APIView):
#     def get(self, request):
#         terms = TermsAndConditions.objects.all()
#         serializer = TermsAndConditionsSerializer(terms, many=True)
#         return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

# # Get Terms & Conditions by ID
# class TermsAndConditionsDetailView(APIView):
#     def get(self, request, id):
#         terms = get_object_or_404(TermsAndConditions, id=id)
#         serializer = TermsAndConditionsSerializer(terms)
#         return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)



from django.shortcuts import render

# Create your views here.


def Indext (request):
    return render(request, 'index.html')