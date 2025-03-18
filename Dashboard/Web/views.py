from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NewHomeBanner
from .serializers import NewHomeBannerSerializer

class NewHomeBannerAPIView(APIView):
    def get(self, request):
        query = request.GET.get('search', '').strip()  # Get and clean search input
        total_banners = NewHomeBanner.objects.count()  # Count total banners

        if query:
            banners = NewHomeBanner.objects.filter(title__icontains=query)  # Case-insensitive search
        else:
            banners = NewHomeBanner.objects.all()  # Show all if no search query

        if banners.exists():
            serializer = NewHomeBannerSerializer(banners, many=True)
            return Response({
                'status': 'success',
                'message': 'Banners retrieved successfully.',
                'totalBanners': total_banners,
                'searchQuery': query,
                'banners': serializer.data,
                'status_code': status.HTTP_200_OK,
                
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'error',
                'message': 'No banners found.',
                'totalBanners': 0,
                'searchQuery': query,
                'banners': []
            }, status=status.HTTP_404_NOT_FOUND)
