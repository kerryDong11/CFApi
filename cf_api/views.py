
# Create your views here.
import json
from django.shortcuts import render, HttpResponse


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
