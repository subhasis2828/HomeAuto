from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Device,UserDevice
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='index')
def getdevicestatus(request,pk):
    try:
        device = Device.objects.get(deviceId=pk)
        dict_  = {"deviceId":device.deviceId,
                "light":device.lightStatus,
                "fan":device.fanStatus}
        return JsonResponse(dict_)

    except Device.DoesNotExist:

        return JsonResponse({"message":"no devices found"})
@login_required(login_url='index')
def togglelight(request,pk):
    try:
        device = Device.objects.get(deviceId=pk)
        if device.lightStatus==0:
            device.lightStatus =1
        else:
            device.lightStatus =0
        device.save()
        dict_  = {"deviceId":device.deviceId,
                "light":device.lightStatus,
                "fan":device.fanStatus}
        return JsonResponse(dict_)

    except Device.DoesNotExist:

        return JsonResponse({"message":"no devices found"})
@login_required(login_url='index')
def togglefan(request,pk):
    try:
        device = Device.objects.get(deviceId=pk)
        if device.fanStatus==0:
            device.fanStatus =1
        else:
            device.fanStatus =0
        device.save()
        dict_  = {"deviceId":device.deviceId,
                "light":device.lightStatus,
                "fan":device.fanStatus}
        return JsonResponse(dict_)

    except Device.DoesNotExist:

        return JsonResponse({"message":"no devices found"})
