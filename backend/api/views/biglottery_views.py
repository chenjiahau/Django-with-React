import csv
import json
from datetime import datetime
from dateutil import relativedelta

from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response

from statistic.models import BigLottery
from api.serializers import BigLotterySerializer

def getData(start_year, end_year, start_month, end_month):
    start_date = int(str(start_year) + str(start_month if start_month > 10 else "0" + str(start_month)) + str('01'))
    end_date = int(str(end_year) + str(end_month if end_month > 10 else "0" + str(end_month)) + str('31'))
    data = BigLottery.objects.filter(date__range=[start_date, end_date]).order_by('-date', '-month', '-day')

    return data

def getStatistics(data):
    statistic_list = []

    for n in range(1, 50):
        statistic_list.append({
            'number': n,
            'time': 0,
            'percent': 0,
        })

    for item in data:
        statistic_list[item.number1-1]['time'] += 1
        statistic_list[item.number2-1]['time'] += 1
        statistic_list[item.number3-1]['time'] += 1
        statistic_list[item.number4-1]['time'] += 1
        statistic_list[item.number5-1]['time'] += 1
        statistic_list[item.number6-1]['time'] += 1

    statistic_list.sort(key=lambda x: x['time'], reverse=True)

    return statistic_list

def getStatisticsByTime(now_date, months_ago, statistic_list):
    time_group = []
    for item in statistic_list:
        time_group.append(item['time'])
    time_group = list(set(time_group))

    time_list = []
    total_times = 0
    for time in time_group:
        total_times += time

        time_list.append({
            'time': time,
            'percent': 0,
            'numbers': [],
            'number_date': []
        })

    for time in time_list:
        time['percent'] = round((time['time'] / total_times) * 100)

    for item in statistic_list:
        for time in time_list:
            if item['time'] == time['time']:
                time['numbers'].append(item['number'])

    for time in time_list:
        time['numbers'].sort()

    statistic = {
        'end_date': now_date.strftime('%Y-%m-%d'),
        'start_date': months_ago.strftime('%Y-%m-%d'),
        'time_list': time_list
    }

    return statistic

# Create your views here.

@api_view(['GET'])
def getBiglotterys(request):
    data = BigLottery.objects.all()
    serializer = BigLotterySerializer(data, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getByMonth(request, month):
    now_date = datetime.today()
    months_ago = now_date - relativedelta.relativedelta(months=month)

    start_year = months_ago.year
    end_year = now_date.year
    start_month = months_ago.month
    end_month = now_date.month

    data = getData(start_year, end_year, start_month, end_month)
    statistic_list = getStatistics(data)
    statistic = getStatisticsByTime(now_date, months_ago, statistic_list)

    for time_item in statistic['time_list']:
        for number in time_item['numbers']:
            number_data = {}
            for data_item in data:
                if (number == data_item.number1):
                    number_data = {
                        'number': data_item.number1,
                        'last_date': data_item.date,
                    }
                    break
                elif (number == data_item.number2):
                    number_data = {
                        'number': data_item.number2,
                        'date': data_item.date,
                    }
                    break
                elif (number == data_item.number3):
                    number_data = {
                        'number': data_item.number3,
                        'last_date': data_item.date,
                    }
                    break
                elif (number == data_item.number4):
                    number_data = {
                        'number': data_item.number4,
                        'last_date': data_item.date,
                    }
                    break
                elif (number == data_item.number5):
                    number_data = {
                        'number': data_item.number5,
                        'last_date': data_item.date,
                    }
                    break
                elif (number == data_item.number6):
                    number_data = {
                        'last_date': data_item.date,
                        'month': data_item.month,
                        'day': data_item.day,
                        'number': data_item.number6,
                    }
                    break

            time_item['number_date'].append(number_data)

    return JsonResponse(statistic, safe=False)

