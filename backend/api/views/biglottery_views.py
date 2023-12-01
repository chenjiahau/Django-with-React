import csv
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

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


@api_view(['GET'])
def getStatisticByDateRange(request, start_year, end_year, start_month, end_month):
    f = request.GET.get('f')
    cond1 = Q(year__range=(start_year, end_year))
    cond2 = Q(month__range=(start_month, end_month))
    data = BigLottery.objects.filter(cond1 & cond2).order_by('-month', '-day')
    stat = {}

    for n in range(1, 50):
        stat[n] = {
            'time': 0,
            'percent': 0,
        }

    for item in data:
        stat[item.number1]['time'] += 1
        stat[item.number2]['time'] += 1
        stat[item.number3]['time'] += 1
        stat[item.number4]['time'] += 1
        stat[item.number5]['time'] += 1
        stat[item.number6]['time'] += 1

    for item in stat:
        stat[item]['percent'] = round(stat[item]['time'] / (len(data) * 6) * 100, 2)

    print(f)
    if f == '':
        return JsonResponse(stat, safe=False)
    else:
        response = HttpResponse(
            content_type='text/csv',
            headers={"Content-Disposition": 'attachment; filename="stat.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow(['Number', 'Times', 'Percent'])
        for item in stat:
            writer.writerow([item, stat[item]['time'], stat[item]['percent']])

        return response