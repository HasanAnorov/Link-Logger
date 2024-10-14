from django.db import models

# Create your models here.

class DeviceData(models.Model):
    ip = models.CharField(max_length=50)
    browser = models.CharField(max_length=50)
    browser_version = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    os_version = models.CharField(max_length=50, null=True)
    device = models.CharField(max_length=50)
    is_mobile = models.BooleanField(default=False)
    is_tablet = models.BooleanField(default=False)
    is_touch_capable = models.BooleanField(default=False)
    is_pc = models.BooleanField(default=False)
    is_bot = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip
