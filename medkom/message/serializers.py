from message.models import Queue, Log
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = '__all__'

class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'