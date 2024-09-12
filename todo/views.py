#from http.client import HTTPResponse
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import TodoSerializer
from .models import Todo
from django.core import serializers
from datetime import date


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-createt_at')
    serializer_class = TodoSerializer
    permission_classes = []  # permissions.IsAuthenticated

    def create(self, request,):# *args, **kwargs):
        today = date.today()
        todo = Todo.objects.create(
            titel = request.POST.get('titel',''),
            description = request.POST.get('description', ''),
            createt_at = request.POST.get('createt_at', today),
            user = request.user,
        )
        serialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serialized_obj, content_type = 'application/json')