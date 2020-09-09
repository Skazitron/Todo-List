from django.shortcuts import render
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer



# Create your views here.
@api_view(['GET'])
def apiOverview(requests):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(requests):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(requests,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(requests):

    serializer = TaskSerializer(data=requests.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(requests,pk):

    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=requests.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(requests,pk):

    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Task Successfully Deleted")