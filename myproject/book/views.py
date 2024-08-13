from django.shortcuts import render

# Create your views here.

"""
视图函数有2个要求：
    1、视图函数的第一个参数就是接收请求
"""

from django.http import HttpRequest
from django.http import HttpResponse


# 期望用户输入127.0.0.1:8000/index/
def index(request):
    return HttpResponse("ok")

