from import_export import resources
from .models import BigLottery

class BigLotteryResource(resources.ModelResource):
    class Meta:
        model = BigLottery
        fields = ('period', 'date', 'year', 'month', 'day', 'day_of_week', 'number1', 'number2', 'number3', 'number4', 'number5', 'number6', 'special_number')