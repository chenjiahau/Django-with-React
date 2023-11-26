from django.contrib import admin
from statistic.models import (
  Log,
  BigLottery
)

# Register your models here.
admin.site.register(Log)
admin.site.register(BigLottery)