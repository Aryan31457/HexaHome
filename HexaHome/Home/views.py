# views.py
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .serializers import *
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from .models import *

class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer



class PropertySearchByCityView(APIView):
    def post(self, request, *args, **kwargs):
        city = request.data.get('city', None)  
        
        if city:
            properties = Property.objects.filter(city__iexact=city)  
        else:
           
            properties = Property.objects.all()
        
        
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)


