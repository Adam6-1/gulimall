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

    # 模拟数据查询
    context ={

        'name': '马上双11，点击有惊喜'
    }
    return render(request, 'book/index.html',context=context)

