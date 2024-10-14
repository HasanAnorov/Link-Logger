from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from user_agents import parse
from django import http

from main.models import DeviceData
from .serializers import DeviceDataSerializer

def get_device_info(request):
    # Get user agent
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    parsed_ua = parse(user_agent)
    
    # Get IP address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    device_info = {
        "ip_address": ip,
        "browser": parsed_ua.browser.family,
        "browser_version": parsed_ua.browser.version_string,
        "os": parsed_ua.os.family,
        "os_version": parsed_ua.os.version_string,
        "device": parsed_ua.device.family,
        "is_mobile": parsed_ua.is_mobile,
        "is_tablet": parsed_ua.is_tablet,
        "is_touch_capable": parsed_ua.is_touch_capable,
        "is_pc": parsed_ua.is_pc,
        "is_bot": parsed_ua.is_bot
    }
    return device_info

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
    return http.HttpResponse("<b>Welcome</b>")

@api_view(['GET'])
def get_device_data(request):
    devices = DeviceData.objects.all().order_by('-created')
    serializer = DeviceDataSerializer(devices, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)