from datetime import timezone

from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import serializers
from .models.general import ProjectManager, ProjectServer, ProjectDataServer


class ProjectServerSerializer(serializers.ModelSerializer):
    """
    项目服务器序列化
    """

    class Meta:
        model = ProjectServer
        fields = '__all__'
        extra_kwargs = {
            "name":{"required":False},
            "ip_url":{"required":False},
            "desc": {"required": False},
            "custom_variable": {"required": False},

        }


    def create(self, validated_data):
        return ProjectServer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.env = validated_data.get("env",instance.env)
        instance.ip_url = validated_data.get("ip_url",instance.ip_url)
        instance.desc = validated_data.get("desc",instance.desc)
        instance.custom_variable = validated_data.get('custom_variable',instance.custom_variable)
        instance.save()
        return instance

class ProjectDataServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDataServer
        fields = '__all__'
        extra_kwargs = {
            "name": {"required": False},
            "ip": {"required": False},
            "desc": {"required": False},
            "pwd": {"required": False},
            "port": {"required": False},
            "username": {"required": False},
            "custom_variable": {"required": False},
        }

class ProjectManagerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='person_charge.username', read_only=True)
    server_testevn = ProjectServerSerializer(source="get_server_test_env",many=True, read_only=True)
    server_developmentenv = ProjectServerSerializer(source="get_server_development_env",many=True, read_only=True)
    server_preproductenv = ProjectServerSerializer(source="get_server_preprouduct_env",many=True, read_only=True)
    server_productevn =  ProjectServerSerializer(source="get_server_product_evn",many=True, read_only=True)

    data_testevn = ProjectServerSerializer(source="get_data_test_env", many=True, read_only=True)
    data_developmentenv = ProjectServerSerializer(source="get_data_development_env", many=True, read_only=True)
    data_preproductenv = ProjectServerSerializer(source="get_data_preprouduct_env", many=True, read_only=True)
    data_productevn = ProjectServerSerializer(source="get_data_product_evn", many=True, read_only=True)
    class Meta:
        model = ProjectManager
        exclude = ("is_delete",)
        extra_kwargs = {
            'name': {'required': False},
            'start_time': {'required': False},
            'end_time': {'required': False},
        }
    def create(self, validated_data):
        return ProjectManager.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.level = validated_data.get('level', instance.level)
        instance.name = validated_data.get('name', instance.name)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.person_charge = validated_data.get('person_charge', instance.person_charge)
        instance.save()
        return instance

    def to_representation(self, instance):
        print("===to_representation===", instance, type(instance))
        print("====sava保存之后序列化调用=======")
        return super(ProjectManagerSerializer, self).to_representation(instance)

    def to_internal_value(self, instance):
        """将客户端传来的 json 数据 parse 给 Model"""
        print("===to_internal_value===", instance, type(instance))
        return super(ProjectManagerSerializer, self).to_internal_value(instance)

    # def __init__(self, instance=None, user=None, backend=None, user_status=None, **kwargs):
    #     self.user = user
    #     self.backend = backend
    #     self.user_status = user_status
    #     super(ProjectManagerSerializer, self).__init__(instance, **kwargs)

class ProjectManagerlistSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='person_charge.username', read_only=True)
    class Meta:
        model = ProjectManager
        exclude = ("is_delete",)


class ProjectUpdataEnvSerializer(serializers.ModelSerializer):
    pass

    # pro_databases = ProjectDataServerSerializer(many=True, required=True)
    # pro_servers = ProjectServerSerializer(many=True, required=True)
    #
    # class Meta:
    #     model = ProjectEnvironment
    #     fields = '__all__'

    # @transaction.atomic
    # def update(self, instance, validated_data):
    #     #服务端环境操作
    #
    #     for pro_servers in validated_data.get("pro_servers"):
    #        dict= {"name": pro_servers.get("name"), "ip_url": pro_servers.get("ip_url"), "desc": pro_servers.get("desc"), \
    #          "custom_variable": pro_servers.get("custom_variable"), "pro_env_id": instance.id
    #          }
    #        ProjectServer.objects.create(**dict)
    #
    #     #数据库环境操作
    #     databases = instance.pro_databases.all()
    #     databases_id = [database.id for database in databases]
    #     ProjectDataServer.objects.filter(id__in=databases_id).delete()
    #
    #     for pro_database in validated_data.get("pro_databases"):
    #         dict ={"name":pro_database.get("name"),"custom_variable":pro_database.get("custom_variable"),"ip":pro_database.get("ip"),\
    #                "pwd":pro_database.get("pwd"),"port":pro_database.get("port"),"pro_env_id": instance.id,"username":pro_database.get('username')
    #                }
    #         ProjectDataServer.objects.create(**dict)
    #
    #     return instance


