from rest_framework import serializers
from .models import places


class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = places
        fields = ('id', 'city', 'longitude', 'latitude',)

        
''' class PlacesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    city = serializers.CharField(required=True, allow_blank=False, max_length=100)
    longitude = serializers.FloatField((required=True, allow_blank=False)
    latitude = serializers.FloatField((required=True, allow_blank=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return places.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.city = validated_data.get('city', instance.city)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.save()
        return instance '''


