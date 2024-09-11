from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','titel', 'description', 'createt_at']