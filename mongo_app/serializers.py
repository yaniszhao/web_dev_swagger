from rest_framework import serializers
from .models import DeviceInfo
from rest_framework_mongoengine import serializers as mongo_serializers

# class DeviceInfoSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = DeviceInfo
#         fields = "__all__"

# class DeviceInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeviceInfo
#         fields = "__all__"

class DeviceInfoSerializer(mongo_serializers.DocumentSerializer):
    class Meta:
        model = DeviceInfo
        fields = "__all__"