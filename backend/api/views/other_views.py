from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def hello(request):
    data = {
        "message": "Welcome to the API!",
    }

    return Response(data)