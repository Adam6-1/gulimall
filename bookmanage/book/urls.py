from django.urls import path
from book.views import index
# 路由views中的请求
urlpatterns = [
    path('index/', index)
]