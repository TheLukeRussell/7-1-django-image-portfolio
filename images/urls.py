from django.urls import path
from .views import Images

urlpatterns  = [
    path('', Images.as_view(), name = 'images'),
]