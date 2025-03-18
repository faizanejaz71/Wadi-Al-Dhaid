from rest_framework import serializers
from .models import NewHomeBanner

class NewHomeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewHomeBanner
        fields = '__all__'
