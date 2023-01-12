from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["POST"])
def create_assest(request):
    assest_object = Assest.objects.all()
    serializer = SnippetSerializer(assest_object, many=True)
    return Response({"payload":serializer})



