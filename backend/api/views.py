from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def hello(request):
    data = {
        "message": "Welcome to the API!",
    }

    return JsonResponse(data)