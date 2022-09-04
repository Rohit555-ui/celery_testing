from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
# from .tasks import test
import datetime
from .models import Language, Framework
from django.db.models import Q
import redis
import json
from redis.commands.json.path import Path


# Create your views here.
# from celery_testing.celery import debug_task
from .tasks import test
class CeleryTask(APIView):
    def get(self, request):
        filter_dict = {
            "name": "python",
            "code": "PY"
        }
        # lan = Language.objects.filter(**filter_dict).filter(Q(author__icontains="uu") | Q(description__icontains="uu"))
        # lan1 = Language.objects.filter(name="python", code="PY")
        # print(lan.query)
        # print(lan1.query)
        # test.apply_async(eta=datetime.datetime.now() + datetime.timedelta(seconds=1))
        # l1 = Language.objects.filter(name="rr")
        # l2 = Language.objects.filter(code="code")
        # l11 = l1.filter(name="a")
        # l12 = l1.filter(name="b")
        # print()
        # print(connection.queries)
        from django.utils.timezone import now

        test.apply_async(eta=now())
        return Response({"status": "success"})
    
    
class RedisConnect(APIView):
    def post(self, request):
        client = redis.Redis(host='localhost', port=6379, db=0)
        dict_to_save = {'a':{
            'value': 100,
            'time': 'current_time'
        }}
        client.set("a_value", json.dumps(dict_to_save))
        result = client.get("a_value")
        result = json.loads(result.decode("utf-8"))
        print(result['a']['value'])
        return Response({"status": "success"})