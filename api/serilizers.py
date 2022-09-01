from rest_framework import serializers
from .models import Stats

class StatsSerializer(serializers.Serializer):
    class Meta:
        model = Stats
        fields = '__all__'
