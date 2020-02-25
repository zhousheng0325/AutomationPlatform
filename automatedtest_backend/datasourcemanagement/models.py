import datetime

from django.db import models
from jsonfield import JSONField

from common.utils.basemodel import BaseModel

# Create your models here.
from django.utils import timezone

from interfacemanagement.models import InterfaceModel
from projectmanagent.models.general import ProjectManager


class CaseFile(BaseModel):
    title = models.CharField(max_length=30,verbose_name="文件名",default="文件名")
    file_name = models.FileField(upload_to='case/',verbose_name="文件路径")
    interface = models.OneToOneField(InterfaceModel,related_name="case",on_delete=models.DO_NOTHING,default=None,verbose_name="接口",null=True,blank=True)
    project = models.ForeignKey(ProjectManager,on_delete=models.DO_NOTHING,default=None,verbose_name="关联项目",null=True,blank=True)
    exclelist = JSONField(null=True,blank=True,verbose_name="数据源列表")
    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = "数据源"
        verbose_name_plural = verbose_name
        db_table = "datasources_db"
        ordering =["id",]
    @property
    def get_interfacename(self):
        return self.interface.name


