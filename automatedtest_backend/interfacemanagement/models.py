from django.db import models
from projectmanagent.models.general import ProjectManager
from jsonfield import JSONField



# Create your models here.

class InterfaceModule(models.Model):
    """
    项目模块的模型
    """
    name = models.CharField(max_length=20, verbose_name="name", help_text="模块名")
    top = models.BooleanField(default=False, verbose_name="置顶", help_text="置顶")
    is_delete = models.BooleanField(default=False, verbose_name="删除", help_text="删除")
    project = models.ForeignKey(ProjectManager, related_name='inter_module', on_delete=models.CASCADE,
                                verbose_name="项目id", help_text="项目ID")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "模块"
        verbose_name_plural = verbose_name
        db_table = "module_db"


class RequestAgreement:
    HTTP = 1
    HTTPS = 2
    MQTT = 3
class RequestWay:
    """
    请求方式
    """
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4
class BodyFormat:
    """
    body格式
    """
    NONE = 0
    FORM_DATA = 1
    FORM_URLENCODED = 2
    RAW = 3
    BINARY = 4
class BodyMessageFormat:
    """
    请求体报文格式
    """
    TEXT = 1
    JSON = 2
    JAVASCRIPT = 3
    XML = 4
    HTML = 5
class InterFaceType:
    INTERFACE = 1
    FLOW = 2





class InterfaceModel(models.Model):
    """
    项目接口的模型
    """
    # 请求体格式
    bodyformat_choice = [
        (BodyFormat.NONE, "none"), (BodyFormat.FORM_DATA, "form-data"),
        (BodyFormat.RAW, "raw"), (BodyFormat.FORM_URLENCODED, "x-www-form-urlencoded"),
        (BodyFormat.BINARY, "binary")
    ]
    # 请求报文格式
    bodymessage_choice = [
        (BodyMessageFormat.TEXT, "text"), (BodyMessageFormat.JAVASCRIPT, "javascript"),
        (BodyMessageFormat.JSON, "json"), (BodyMessageFormat.HTML, "html"),
        (BodyMessageFormat.XML, "xml")
    ]

    request_protocol_choice = [
        (RequestAgreement.HTTP, "http"), (RequestAgreement.HTTPS, "https")
    ]
    request_way_choice = [
        (RequestWay.GET, "get"), (RequestWay.POST, "post"), (RequestWay.PUT, "put"),
        (RequestWay.DELETE, "delete")
    ]

    interface_type = [(InterFaceType.INTERFACE,"interface"),(InterFaceType.FLOW,"flow")]
    process_and_interface = models.ManyToManyField('InterfaceModel',through='InterfaceFlowModel',related_name='flow',help_text="关联数据")
    interface_type = models.IntegerField(choices=interface_type,help_text="接口类型",default=InterFaceType.INTERFACE)
    name = models.CharField(max_length=20, verbose_name="name", null=True, blank=True, help_text="接口名")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="修改时间", help_text="修改时间")
    modifier = models.CharField(max_length=20, default="暂定", verbose_name="修改人", help_text="修改人")
    desc = models.TextField(max_length=400, verbose_name="接口描述", help_text="接口描述", null=True, blank=True)
    path_url = models.CharField(max_length=200, verbose_name="接口路径", help_text="接口路径", null=True, blank=True)
    port = models.IntegerField(verbose_name="端口", default=8000, null=True, blank=True, help_text="端口")
    request_protocol = models.IntegerField(choices=request_protocol_choice, null=True, blank=True,
                                           default=RequestAgreement.HTTP, verbose_name="请求协议", help_text="请求协议")
    request_way = models.IntegerField(choices=request_way_choice, null=True, blank=True, default=RequestWay.GET,
                                      verbose_name="请求方式", help_text="请求方式")
    bodyformat = models.IntegerField(choices=bodyformat_choice, null=True, blank=True, verbose_name="请求体格式",
                                     help_text="请求体格式")
    bodymessageformat = models.IntegerField(choices=bodymessage_choice, null=True, blank=True, verbose_name="请求报文格式",
                                            help_text="报文格式")
    project = models.ForeignKey(ProjectManager, related_name="project_subs_interface", on_delete=models.CASCADE,
                                verbose_name="关联项目")
    intermodule = models.ForeignKey(InterfaceModule, related_name="subs_interface", on_delete=models.CASCADE,
                                    verbose_name="模块", help_text="模块")

    params = JSONField(null=True, blank=True, verbose_name="参数" + '{"key":"value"}')
    headerparams = JSONField(null=True, blank=True, verbose_name="请求头参数")
    bodyparams = JSONField(null=True, blank=True, verbose_name="请求体")
    preprocessing = JSONField(null=True,blank=True,verbose_name="前置处理")
    postprocessing = JSONField(null=True,blank=True,verbose_name="后置处理")
    assertion = JSONField(null=True,blank=True,verbose_name="断言处理")



    @property
    def get_flow_sub(self):
        return self.process_and_interface


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "接口"
        verbose_name_plural = verbose_name
        db_table = "interface_db"


class InterfaceFlowModel(models.Model):
    from_interfacemodel = models.ForeignKey('InterfaceModel',on_delete=models.CASCADE,related_name="from_interface")
    to_interfacemodel = models.ForeignKey('InterfaceModel',on_delete=models.CASCADE,related_name="to_interface")
    step = models.CharField(max_length=10)
    class Meta:
        verbose_name = "接口流程关系"
        verbose_name_plural = verbose_name
        unique_together = (('from_interfacemodel', 'to_interfacemodel'),)
        ordering = ['step']
        db_table = "interfaceflow_db"




class KeysModel(models.Model):
    key_choice = ((1, "变量"), (2, "函数"), (3, "运算符"))

    name = models.CharField(max_length=40, verbose_name="关键字名")
    value = models.CharField(max_length=100,verbose_name="关键字值",blank=True,null=True)
    count = models.IntegerField(verbose_name="参数个数")
    params_constraint = JSONField(verbose_name="""参数约束[{"paramname":"name"},{"paramname":"height"}
]""")
    keytype = models.IntegerField(choices=key_choice, default= 1,verbose_name="关键字类型")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "关键字"
        verbose_name_plural = verbose_name
        db_table = "keys_db"
