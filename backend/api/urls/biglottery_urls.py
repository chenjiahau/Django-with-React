from django.urls import path
from api.views import biglottery_views as views

urlpatterns = [
    path('', views.getBiglotterys, name='biglottery'),
    path('stat/<int:start_year>/<int:end_year>/<int:start_month>/<int:end_month>', views.getStatisticByDateRange, name='getStatisticByDateRange'),
]