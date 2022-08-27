from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from students.models import student_details
from rest_framework.decorators import api_view
from .serializers import Studentserializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        getobj = student_details.objects.all()
        serializer = Studentserializer(getobj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    