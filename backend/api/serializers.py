from rest_framework import serializers
from statistic.models import BigLottery

class BigLotterySerializer(serializers.ModelSerializer):
    class Meta:
        model=BigLottery
        fields=['period', 'number1', 'number2', 'number3', 'number4', 'number5', 'number6']