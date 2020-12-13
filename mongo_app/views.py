from django.shortcuts import render
from mongo_app.models import DeviceInfo
from django.shortcuts import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.

from drf_yasg.utils import swagger_auto_schema
from django.db import transaction
from django.views.generic import View
from rest_framework.generics import GenericAPIView
from .serializers import DeviceInfoSerializer
from rest_framework import viewsets

class DeviceInfoListView(GenericAPIView):
    queryset = DeviceInfo.objects.all()
    serializer_class = DeviceInfoSerializer

    @swagger_auto_schema(
        operation_summary='我是 GET 的摘要',
        operation_description='我是 GET 的說明',
        #这里参数是自动读取的，也可以自定义，需要查阅资料
    )
    def get(self, request, *args, **krgs):
        res = self.get_queryset()
        serializer = self.serializer_class(res, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

    # def get(self, request):
    # """
    # 或者所有设备信息
    # :param request:
    # :return:
    # """
    # res = DeviceInfo.objects.all()
    # res_list = []
    # for dev in res:
    #     print(dev.dev_name)
    #     dev_dict = {}
    #     dev_dict["dev_id"] = dev.dev_id
    #     dev_dict["dev_name"] = dev.dev_name
    #     dev_dict["dev_desc"] = dev.dev_desc
    #     dev_dict["dev_paras"] = dev.dev_paras
    #     res_list.append(dev_dict)
    # return HttpResponse(json.dumps(res_list), content_type='application/json')

    @swagger_auto_schema(
        operation_summary='我是 POST 的摘要',
        operation_description='我是 POST 的說明',
    )
    def post(self, request, *args, **krgs):
        data = request.data
        try:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            # with transaction.atomic():
            #     serializer.save()
            serializer.save()
            data = serializer.data
            return JsonResponse(data)
        except Exception as e:
            data = {'error': str(e)}
            JsonResponse(data)
            raise e


    # def post(self, request, *args, **krgs):
    #     data = request.data
    #     print(data)
    #     dev = DeviceInfo(dev_name='dev9', dev_desc="device 9", dev_paras=['A', 'B', 'C']).save()
    #     print(dev.dev_name)
    #     # dev.save()
    #     dev_dict = {}
    #     dev_dict["result"] = "dev add ok!"
    #     dev_dict["dev info"] = {
    #         "dev_id": dev.dev_id,
    #         "dev_name": dev.dev_name,
    #         "dev_desc": dev.dev_desc,
    #         "dev_paras": dev.dev_paras,
    #     }
    #     # return HttpResponse('dev_add successful')
    #     return HttpResponse(JsonResponse(dev_dict))

    def put(request):
        """
        更新一条设备信息，根据完整的数据
        :param request:
        :return:
        """
        # res = DeviceInfo.objects.get(dev_name="dev_1").update(dev_name="dev_11")
        # dev = DeviceInfo.objects.filter(dev_name="dev_1").first()
        dev = DeviceInfo.objects(dev_name="dev_11").first()
        if dev:
            print(dev.dev_name)
            # res.update(dev_name="dev_11")
            # dev.update(raw={"dev_name": "dev_121"}
            dev.dev_name = "dev_121"
            # dev.update()
            dev.save()
            return HttpResponse('dev_update successful')
        else:
            return HttpResponse('dev_update failed')

    def patch(request):
        """
        更新一条设备信息，根据指定的字段
        :param request:
        :return:
        """
        # res = DeviceInfo.objects.get(dev_name="dev_1").update(dev_name="dev_11")
        # dev = DeviceInfo.objects.filter(dev_name="dev_1").first()
        dev = DeviceInfo.objects(dev_name="dev_11").first()
        if dev:
            print(dev.dev_name)
            # res.update(dev_name="dev_11")
            # dev.update(raw={"dev_name": "dev_121"}
            dev.dev_name = "dev_121"
            # dev.update()
            dev.save()
            return HttpResponse('dev_update successful')
        else:
            return HttpResponse('dev_update failed')

    def delete(request):
        """
        删除一条设备信息
        :param request:
        :return:
        """
        dev = DeviceInfo.objects(dev_name="dev2233").first()
        print(dev.dev_name)
        dev_dict = {}
        dev_dict["dev_id"] = dev.dev_id
        dev_dict["dev_name"] = dev.dev_name
        dev_dict["dev_desc"] = dev.dev_desc
        dev_dict["dev_paras"] = dev.dev_paras
        dev.delete()
        # return HttpResponse(json.dumps(dev_dict), content_type='application/json')
        return HttpResponse(JsonResponse(dev_dict))
