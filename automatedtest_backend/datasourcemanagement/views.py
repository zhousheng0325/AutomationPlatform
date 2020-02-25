from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from common.my_pagination import StandardPageNumberPagination
from common.myresponse import StatusResponse
from common.utils.login_util import login_decorator
from .models import CaseFile
from .serializers import UploadFileSerializer
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin
# Create your views here.
from datasourcemanagement.forms import FileForm
from common.my_excel import ExcelImport

class UploadView(GenericAPIView, CreateModelMixin, UpdateModelMixin, ListModelMixin):

    serializer_class = UploadFileSerializer
    pagination_class = StandardPageNumberPagination
    def get_queryset(self):
        if self.request.method == "GET":
            project_id = self.request.query_params.get("project", None)
            if project_id is not None:
                return CaseFile.objects.filter(project_id=project_id)
            return CaseFile.objects.all()
        return CaseFile.objects.all()

    @method_decorator(login_decorator)
    def post(self, request):
        ExcelImport.get_cases(request)
        return StatusResponse(http_code=200, data=self.create(request).data)

    @method_decorator(login_decorator)
    def put(self, request, pk):
        ExcelImport.get_cases(request)
        return StatusResponse(http_code=200, data=self.update(self.request, pk).data)

    @method_decorator(login_decorator)
    def get(self, request):
        return StatusResponse(http_code=200, data=self.list(self.request).data)

    @method_decorator(login_decorator)
    def delete(self, request):
        ids = request.data.get("ids", None)
        try:
            query = CaseFile.objects.filter(id__in=ids).all()
            if query.count() < 1:
                return StatusResponse(http_code=200, data={"success": "请选择要删除的数据"})
            for instance in query:
                instance.file_name.delete(False)
                instance.delete()
        except:
            return StatusResponse(http_code=200, data={"success": "删除失败"})
        return StatusResponse(http_code=200, data={"success": "删除成功"})
