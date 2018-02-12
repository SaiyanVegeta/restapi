from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import places
from .serializers import PlacesSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models.query import EmptyQuerySet

@api_view(['GET', 'POST'])
def places_list(request,format=None):
    """
    List all cities , or add a new city.
    """
    if request.method == 'GET':
        place = places.objects.all()
        serializer = PlacesSerializer(place, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlacesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def places_detail(request, pk,format=None):
    """
    Retrieve, update or delete a location.
    """
    try:
        place = places.objects.get(pk=pk)
    except places.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlacesSerializer(place)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PlacesSerializer(place, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def places_near(request, pk,format=None):
    """
    Places near the city.
    """
    try:
        place=places.objects.get(city__iexact=str(pk))
    except places.DoesNotExist:
        try:
            place=places.objects.get(city__icontains=str(pk))
        except places.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        lo = place.__dict__['longitude']
        la = place.__dict__['latitude']
        nearby = places.objects.filter(latitude__lt=la+0.5).filter(latitude__gt=la-0.5).filter(longitude__lt=lo+0.5).filter(longitude__gt=lo-0.5)
        serializer = PlacesSerializer(nearby, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlacesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

