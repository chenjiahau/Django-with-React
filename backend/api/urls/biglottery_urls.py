from django.urls import path
from api.views import biglottery_views as views

urlpatterns = [
    path('', views.getBiglotterys, name='biglottery'),
    path('statistic/<int:month>', views.getByMonth, name='biglottery-statistics'),
]