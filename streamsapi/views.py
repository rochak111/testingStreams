from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics

#from EcommerceApi.DjangoApi.models import Matches
from .models import Matches
from .serializers import MatchesSerializer

# Create your views here.
class ListMatches(generics.ListCreateAPIView):
<<<<<<< HEAD
    queryset = Matches.whattoshow
=======
    queryset = Matches.objects.values_list('title','description')
>>>>>>> aa63255a9bd79e372851ebad6591ce24513862b0
    serializer_class = MatchesSerializer

class DetailMatches(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matches.whattoshow
    serializer_class = MatchesSerializer
