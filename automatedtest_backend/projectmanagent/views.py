from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import viewsets

from common.my_pagination import StandardPageNumberPagination
from .models.general import ProjectManager, ProjectServer, ProjectDataServer
from common.myresponse import StatusResponse

from rest_framework.mixins import CreateModelMixin, \
    UpdateModelMixin, ListModelMixin, DestroyModelMixin, \
    RetrieveModelMixin

from .serializers import ProjectManagerSerializer, ProjectServerSerializer, \
    ProjectUpdataEnvSerializer, ProjectManagerlistSerializer, ProjectDataServerSerializer

from common.utils.login_util import login_decorator


# Create your views here.
# 单个项目添加 获取 修改

class ProjectManagerView(GenericAPIView, CreateModelMixin,
                         UpdateModelMixin,
                         RetrieveModelMixin):
    """
    post:
    创建项目

    get:
    通过id获取一条项目记录

    put:
    通过id修改一条项目记录

    """
    def get_serializer_class(self):
        return ProjectManagerSerializer

    def get_queryset(self):
        return ProjectManager.objects.filter(is_delete=False)

    @method_decorator(login_decorator)
    def post(self, request):
        """创建项目"""
        response = self.create(request)
        return StatusResponse(200, response.data)

    @method_decorator(login_decorator)
    def get(self, request, pk):
        """获取项目"""
        return self.retrieve(request)

    @method_decorator(login_decorator)
    def put(self, request, pk):

        return StatusResponse(200, self.update(request).data)


# 项目列表的获取
class ProjectObtainView(GenericAPIView, ListModelMixin):
    """
    get:
    获取项目列表
    """
    pagination_class = StandardPageNumberPagination

    def get_serializer_class(self):
        return ProjectManagerlistSerializer

    def get_queryset(self):
        return ProjectManager.objects.filter(is_delete=False).order_by('id')

    @method_decorator(login_decorator)
    def get(self, request):
          return StatusResponse(200, self.list(request).data)


# 项目批量删除
class ProjectBatchDeleteView(APIView):
    """
    put:
    批量删除
    """
    @method_decorator(login_decorator)
    def put(self, request):
        ids = request.data.get('ids')
        try:
            p = ProjectManager.objects.filter(id__in=ids).update(is_delete=True)
        except Exception as e:
            return StatusResponse(400, {"tip": "更新失败"})
        else:
            if p == 0:
                return StatusResponse(400, {"tip": "当前无更新"})
            else:
                return StatusResponse(200, {"tip": "更新成功"})


# 项目批量改变状态
class ProjectBatchStatusView(APIView):
    """
    put:
    批量改变项目状态
    """

    @method_decorator(login_decorator)
    def put(self, request):
        ids = request.data.get('ids')
        status = request.data.get('status')
        try:
            if status == 1:
                count = ProjectManager.objects.filter(id__in=ids).update(status=True)
            else:
                count = ProjectManager.objects.filter(id__in=ids).update(status=False)

        except ProjectManager.DoesNotExist:
            return StatusResponse(400, {"tip": "不存在"})
        else:
            if count == 0:
                return StatusResponse(400, {"tip": "当前无更新"})
            else:
                return StatusResponse(200, {"tip": "更新成功"})


# 单个服务的增删查改
class ProjectServerView(viewsets.ViewSet):
    def update(self, request, pk):
        try:
            proserver = ProjectServer.objects.get(id=pk)
        except ProjectServer.DoesNotExist:
            return StatusResponse(http_code=400, data={"tip": "服务不存在"})
        serializer = ProjectServerSerializer(instance=proserver, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return StatusResponse(data=serializer.data, http_code=200)
    def delete(self, request, pk):
        try:
            proserver = ProjectServer.objects.get(id=pk)
            proserver.delete()
        except ProjectServer.DoesNotExist:
            return StatusResponse(http_code=400, data={"tip": "项目不存在"})
        return StatusResponse(http_code=200, data={"tip": "删除成功"})
    def create(self, request):
        serializer = ProjectServerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return StatusResponse(data=serializer.data, http_code=200)
    def retrieve(self, request, pk):
        try:
            proserver = ProjectServer.objects.get(id=pk)
        except ProjectServer.DoesNotExist:
            return StatusResponse(http_code=400, data={"tip": "项目不存在"})
        serializer = ProjectServerSerializer(instance=proserver)
        return  StatusResponse(data=serializer.data,http_code=200)

#单个数据库的添加和删除
class ProjectServerDataView(viewsets.ViewSet):
    def update(self, request, pk):
        try:
            proserverdata = ProjectDataServer.objects.get(id=pk)
        except ProjectDataServer.DoesNotExist:
            return StatusResponse(http_code=400, data={"tip": "服务不存在"})
        serializer = ProjectDataServerSerializer(instance=proserverdata, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return StatusResponse(data=serializer.data, http_code=200)
    def delete(self, request, pk):
        try:
            proserver_data = ProjectDataServer.objects.get(id=pk)
            proserver_data.delete()
        except ProjectDataServer.DoesNotExist:
            return StatusResponse(http_code=400, data={"tip": "项目不存在"})
        return StatusResponse(http_code=200, data={"tip": "删除成功"})
    def create(self, request):
        serializer = ProjectDataServerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return StatusResponse(data=serializer.data, http_code=200)

    def retrieve(self, request, pk):
        try:
            proserver_data = ProjectDataServer.objects.get(id=pk)
        except ProjectDataServer.DoesNotExist:
            return StatusResponse(http_code=400, data={"tip": "项目不存在"})
        serializer = ProjectDataServerSerializer(instance=proserver_data)
        return  StatusResponse(data=serializer.data,http_code=200)







#项目服务和数据库的批量添加

# 更新环境
class ProjectEvnView(viewsets.ViewSet):
    """
    put:
    更新项目
    """
    @method_decorator(login_decorator)
    def update(self, request, env, envid):
        pass
        # try:
        #     pro_env = ProjectEnvironment.objects.filter(env=env, id=envid).first()
        # except ProjectEnvironment.DoesNotExist:
        #     raise
        # else:
        #     serializer = ProjectUpdataEnvSerializer(instance=pro_env, data=request.data)
        #     serializer.is_valid(raise_exception=True)
        #     serializer.save()
        #     return StatusResponse(200, serializer.data)
