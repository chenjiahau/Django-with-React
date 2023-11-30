from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from statistic.models import (
    Log,
    BigLottery
)

# Register your models here.
class BigLotteryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Log)
admin.site.register(BigLottery, BigLotteryAdmin)