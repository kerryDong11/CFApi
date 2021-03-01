
# Create your views here.
import json
from django.shortcuts import render, HttpResponse

from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers

class PythonWebDemo(object):
    @staticmethod
    def webtest(request):
        data = {}
        jsontext = request.GET.get('jsontext', 2)
        # functionname=json.loads(jsontext)["functionname"]
        filename = json.loads(jsontext)["title"]
        compareyear = json.loads(jsontext)["year"]
        data['filename'] = filename
        data['compareyear'] = compareyear
        sample = json.dumps(data)
        #sample = json.dumps(data)
        return HttpResponse(sample, content_type="application/json")

class StudentViewSet(viewsets.ModelViewSet):

    # 指定结果集并设置排序
    queryset = Student.objects.all().order_by('-pk')
    # 指定序列化的类
    serializer_class = StudentSerializers