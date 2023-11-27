from rest_framework.decorators import api_view
from rest_framework.response import Response

from statistic.models import BigLottery
from api.serializers import BigLotterySerializer

# Create your views here.

@api_view(['GET'])
def getBiglotterys(request):
    data = BigLottery.objects.all()
    serializer = BigLotterySerializer(data, many=True)

    return Response(serializer.data)