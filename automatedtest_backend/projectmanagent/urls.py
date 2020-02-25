"""automatedtest_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    3. Add a URL to urlpatterns:  path(')
"""

from django.urls import path
from .views import ProjectManagerView, ProjectObtainView, \
    ProjectBatchDeleteView, ProjectBatchStatusView, ProjectEvnView, ProjectServerView, ProjectServerDataView

urlpatterns = [

    path('operation/', ProjectManagerView.as_view()),  # 新建项目
    path('operation/<int:pk>/', ProjectManagerView.as_view()),  # 获取单个和修改数据
    path('obtain/',ProjectObtainView.as_view()),#获取项目列表

    path('batch/delete/',ProjectBatchDeleteView.as_view()),#批量删除项目
    path('batch/status/',ProjectBatchStatusView.as_view()),#批量的更改项目状态
    
    #项目服务器环境管理
    path('projectserver/<int:pk>/',ProjectServerView.as_view({'put':'update',"get":"retrieve","delete":"delete"})),
    path('projectserver/',ProjectServerView.as_view({'post':'create'})),

    #项目数据库环境的管理
    path('projectdatabase/<int:pk>/', ProjectServerDataView.as_view({'put': 'update', "get": "retrieve", "delete": "delete"})),
    path('projectdatabase/', ProjectServerDataView.as_view({'post': 'create'}))


]
