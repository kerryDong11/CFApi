
# Create your views here.
import json
from django.shortcuts import render, HttpResponse

from rest_framework.views import APIView    #导入APIView 

from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from .models import Student
from .models import User

from .serializers import StudentSerializers
from .serializers import UserSerializers
# class PythonWebDemo(object):
#     @staticmethod
#     def webtest(request):
#         data = {}
#         jsontext = request.GET.get('jsontext', 2)
#         # functionname=json.loads(jsontext)["functionname"]
#         filename = json.loads(jsontext)["title"]
#         compareyear = json.loads(jsontext)["year"]
#         data['filename'] = filename
#         data['compareyear'] = compareyear
#         sample = json.dumps(data)
#         #sample = json.dumps(data)
#         return HttpResponse(sample, content_type="application/json")

class StudentViewSet(viewsets.ModelViewSet):

    # 指定结果集并设置排序
    queryset = Student.objects.all().order_by('-pk')
    # 指定序列化的类
    serializer_class = StudentSerializers

# ListCreateAPIView 获取列表数据，创建数据的类视图
# 获取全部用户
class UsersAPIView(ListCreateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


# 获取单个用户
class UserAPIView(ListCreateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
