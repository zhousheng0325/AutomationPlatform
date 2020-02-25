from django.db import models
class BaseModel(models.Model):
    created = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    class Meta:
        abstract = True