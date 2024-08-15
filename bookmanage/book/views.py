from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    # 1. 获取参数
    # 2. 编写查询代码
    # 3. 处理查询结果
    # 4. ��染模板并返回
    # 5. 注意：返回的 HttpResponse 一定要是 str 类型
    return HttpResponse("index")
