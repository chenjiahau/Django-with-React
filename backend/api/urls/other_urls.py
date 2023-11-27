from django.urls import path
from api.views import other_views as views

urlpatterns = [
    path('', views.hello, name='other'),
]