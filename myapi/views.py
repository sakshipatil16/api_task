from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task
from django.http import JsonResponse
from datetime import datetime
import requests


# Create your views here.

class TaskList(APIView):    
   
    def get(self,request):
        date=datetime.now()
        tasks=Task.objects.filter(date='2020-06-23 17:51:00')
        if tasks.exists():
            for url in tasks:          
                response=requests.get(url)           
            return Response(status=200)
        else:           
            return Response(status=404) 
        
        serializer= TaskSerializer(tasks, many=True)

      
def ping(request):
    data={
        'status':'OK'
    }
    return JsonResponse(data)