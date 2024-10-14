from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('device/data/list/', views.get_device_data)
]