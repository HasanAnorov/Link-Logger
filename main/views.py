from django.shortcuts import render
from .models import DeviceData
from main.api.views import *

# Create your views here.
def index(request):
    data = get_device_info(request)
    DeviceData.objects.create(
        ip = data.get('ip_address'),
        browser = data.get('browser'),
        browser_version = data.get('browser_version'),
        os = data.get('os'),
        os_version = data.get('os_version'),
        device = data.get('device'),
        is_mobile = data.get('is_mobile'),
        is_tablet = data.get('is_tablet'),
        is_touch_capable = data.get('is_touch_capable'),
        is_pc = data.get('is_pc'),
        is_bot = data.get('is_bot'),
    )
    return render(request, "index.html")