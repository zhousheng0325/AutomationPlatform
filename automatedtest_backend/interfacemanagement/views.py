from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, ListCreateAPIView

from common.my_pagination import StandardPageNumberPagination
from common.utils.login_util import login_decorator
from .models import InterfaceModule, InterfaceModel, KeysModel, InterfaceFlowModel
from .serializers import InterfaceModuleSerializer, InterfaceSerializer, KeysSerializer, InterfaceCaseSerializer, \
    FlowSerializer
from common.myresponse import StatusResponse

from common.rpc_client import client
from autotest_service.rpc import autotest_pb2_grpc,autotest_pb2
from autotest_service.celery_task.autotask.tasks import test_script



# Create your views here.

class InterfaceModuleView(ModelViewSet):

    def get_queryset(self):
        project = self.request.query_params.get('project', None) or self.request.data.get('project')
        queryset = InterfaceModule.objects.filter(is_delete=False, project_id=project).all()
        return queryset

    serializer_class = InterfaceModuleSerializer

    @method_decorator(login_decorator)
    def list(self, request, *args, **kwargs):
        return StatusResponse(http_code=200, data=super().list(request, *args, **kwargs).data)

    @method_decorator(login_decorator)
    def create(self, request, *args, **kwargs):
        return StatusResponse(http_code=200, data=super().create(request, *args, **kwargs).data)

    @method_decorator(login_decorator)
    def update(self, request, *args, **kwargs):
        return StatusResponse(http_code=200, data=super().update(request, *args, **kwargs).data)


class InterfaceView(ModelViewSet):
    pagination_class = StandardPageNumberPagination

    def get_queryset(self):
        if self.action == "list":
            intermodule = self.request.query_params.get('intermodule', None) or self.request.data.get('intermodule')
            project = self.request.query_params.get('project', None) or self.request.data.get('project')
            if intermodule is not None:
                query = InterfaceModel.objects.filter(intermodule_id=intermodule).all()
            elif project is not None:
                query = InterfaceModel.objects.filter(project_id=intermodule).all()
            else:
                query = InterfaceModel.objects.all()
            return query
        else:
            query = InterfaceModel.objects.all()
            return query

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FlowSerializer
        else:
            return InterfaceSerializer

    @method_decorator(login_decorator)
    def create(self, request, *args, **kwargs):
        print(request.data)
        return StatusResponse(http_code=200, data=super().create(request, *args, **kwargs).data)

    @method_decorator(login_decorator)
    def list(self, request, *args, **kwargs):
        return StatusResponse(http_code=200, data=super().list(request, *args, **kwargs).data)

    @method_decorator(login_decorator)
    def update(self, request, *args, **kwargs):
        return StatusResponse(http_code=200, data=super().update(request, *args, **kwargs).data)

    def retrieve(self, request, pk):
        flow = InterfaceFlowModel.objects.filter(from_interfacemodel=pk).all()
        serializer = self.get_serializer(flow, many=True)
        return StatusResponse(http_code=200, data=serializer.data)

    @method_decorator(login_decorator)
    def delete(self, request):
        try:
            ids = request.data.get("ids")
            print("====ids====", request.data)
            InterfaceModel.objects.filter(id__in=ids).delete()
        except Exception as e:
            return StatusResponse(http_code=400, data={"tip": "删除失败"})
        return StatusResponse(http_code=200, data={"tip": "ok"})


class InterfaceGetCaseView(GenericAPIView):
    queryset = InterfaceModel.objects.all()
    serializer_class = InterfaceCaseSerializer

    @method_decorator(login_decorator)
    def get(self, request, pk):
        object = self.get_object()
        serilaizer = self.get_serializer(object)
        return StatusResponse(http_code=200, data=serilaizer.data)


class KeysView(ModelViewSet):
    queryset = KeysModel.objects.all()
    serializer_class = KeysSerializer

    @method_decorator(login_decorator)
    def list(self, request, *args, **kwargs):
        return StatusResponse(http_code=200, data=super().list(request, *args, **kwargs).data)


class InterfacExecuteResult(GenericAPIView):

    def send_executeid(self, *args, **kwargs):
        stub = autotest_pb2_grpc.AutoTestStub(client)
        interface_request = autotest_pb2.AutotestRequest()
        interface_request.interface_id.extend([1, 2, 3])
        interface_request.case_id.extend([4, 5, 6])
        interface_request.name = "test1"
       # 通过stub进行方法调用，并接收调用返回值
        ret = stub.autotest_interface(interface_request)
        print(ret.name)

    def post(self, request):
        #self.send_executeid()
        test_script.delay([1,2],name="zhangsan",age=18)
        return StatusResponse(http_code=200, data={"tip": "执行成功"})
