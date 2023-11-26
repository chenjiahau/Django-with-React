from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from statistic.models import BigLottery
from .serializers import BigLotterySerializer

# Create your views here.

@api_view(['GET'])
def hello(request):
    data = {
        "message": "Welcome to the API!",
    }

    return Response(data)

@api_view(['GET'])
def getBiglotterys(request):
    data = BigLottery.objects.all()
    serializer = BigLotterySerializer(data, many=True)

    return Response(serializer.data)