from django.db import models
from user.models import ApiUser, User


class ProjectManager(models.Model):
    """
    项目管理
    """
    level_status = ((1, '低'), (2, '中'), (3, '高'))
    name = models.CharField(max_length=20, verbose_name="项目名称",help_text='项目名称')
    start_time = models.CharField(max_length=50, verbose_name="项目开始时间",help_text="开始时间")
    end_time = models.CharField(max_length=50, verbose_name="项目结束时间",help_text="结束时间")
    status = models.BooleanField(default=True,help_text="项目状态 ")
    level = models.IntegerField(choices=level_status, default=3, verbose_name="项目优先级",help_text="项目优先级")
    desc = models.TextField(max_length=400, verbose_name="项目描述", null=True, blank=True,help_text="项目描述")
    person_charge = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="项目负责人",help_text="负责人")
    is_delete = models.BooleanField(default=False,verbose_name="是否删除",help_text="删除")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "项目管理"
        verbose_name_plural = verbose_name
        db_table = "project_manager"
        ordering = ["id"]

    @property
    def get_server_test_env(self):
        return self.servers_env.filter(env=1)
    @property
    def get_server_development_env(self):
        return  self.servers_env.filter(env=2)
    @property
    def get_server_preprouduct_env(self):
        return self.servers_env.filter(env=3)
    @property
    def get_server_product_evn(self):
        return self.servers_env.filter(env=4)

    @property
    def get_data_test_env(self):
        return self.data_env.filter(env=1)
    @property
    def get_data_development_env(self):
        return self.data_env.filter(env=2)
    @property
    def get_data_preprouduct_env(self):
        return self.data_env.filter(env=3)
    @property
    def get_data_product_evn(self):
        return self.data_env.filter(env=4)

class ProjectServer(models.Model):
    """
    服务器
    """
    TEST_ENV = 1  # 测试环境
    DEVELOPMENT_ENV = 2  # 开发环境
    PREPRODUCT_ENV = 3  # 预生产环境
    PRODUCT_ENV = 4  # 生产环境
    env_choice = [
        (TEST_ENV, "测试环境"),
        (DEVELOPMENT_ENV, "开发环境"),
        (PREPRODUCT_ENV, "预生产环境"),
        (PRODUCT_ENV, "生产环境"),
    ]

    project = models.ForeignKey(ProjectManager, on_delete=models.CASCADE, related_name="servers_env", verbose_name="项目",help_text="项目Id")
    env = models.IntegerField(choices=env_choice, default=TEST_ENV, verbose_name="环境", help_text="项目环境")
    name = models.CharField(max_length=30, verbose_name="服务器名",help_text="服务器名")
    ip_url = models.CharField(max_length=50, verbose_name="ip_or_url",help_text="ip_or_url")
    desc = models.CharField(max_length=200, verbose_name="环境描述",help_text="环境描述")
    custom_variable = models.CharField(max_length=30, verbose_name="自定义变量",help_text="自定义变量")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "服务器"
        verbose_name_plural = verbose_name
        db_table = "project_server"
        ordering = ["id"]
        unique_together = ("project", "env")

class ProjectDataServer(models.Model):
    """
    数据库
    """
    TEST_ENV = 1  # 测试环境
    DEVELOPMENT_ENV = 2  # 开发环境
    PREPRODUCT_ENV = 3  # 预生产环境
    PRODUCT_ENV = 4  # 生产环境
    env_choice = [
        (TEST_ENV, "测试环境"),
        (DEVELOPMENT_ENV, "开发环境"),
        (PREPRODUCT_ENV, "预生产环境"),
        (PRODUCT_ENV, "生产环境"),
    ]

    project = models.ForeignKey(ProjectManager, on_delete=models.CASCADE, related_name="data_env", verbose_name="项目",
                                help_text="项目Id")
    env = models.IntegerField(choices=env_choice, default=TEST_ENV, verbose_name="环境", help_text="项目环境")
    name = models.CharField(max_length=30, verbose_name="数据库名", blank=True,help_text="数据名")
    custom_variable = models.CharField(max_length=30, verbose_name="自定义变量",help_text="自定义变量")
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="ip",help_text="数据库IP")
    port = models.IntegerField(verbose_name="端口",help_text="端口",default=8080)
    pwd = models.CharField(max_length=20, verbose_name="密码",help_text="密码")
    username = models.CharField(max_length=30,verbose_name="用户名",blank=True,help_text="用户名")

    class Meta:
        verbose_name = "数据库"
        verbose_name_plural = verbose_name
        db_table = "project_db"
        ordering = ["id"]
        unique_together = ("project", "env")
