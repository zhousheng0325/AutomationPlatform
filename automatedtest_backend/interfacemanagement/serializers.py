from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from .models import InterfaceModule, InterfaceModel, KeysModel, InterfaceFlowModel



class InterfaceModuleSerializer(serializers.ModelSerializer):
    """
    模块的管理
    """
    class Meta:
        model = InterfaceModule
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': False},
        }
    def create(self, validated_data):
       return InterfaceModule.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.get("top"):
            InterfaceModule.objects.filter(top=1).update(top=0)
        instance.is_delete = validated_data.get('is_delete',instance.is_delete)
        instance.name = validated_data.get("name",instance.name)
        instance.top = validated_data.get("top",instance.top)
        instance.save()
        return instance

class InterfaceflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterfaceModel
        fields = ('id','name')

class FlowSerializer(serializers.ModelSerializer):
    step = serializers.CharField(max_length=20,help_text="步骤")
    to_interfacemodel = InterfaceflowSerializer(read_only=True)
    class Meta:
        model = InterfaceFlowModel
        fields = ("step",'to_interfacemodel')

class InterfaceSerializer(serializers.ModelSerializer):
    """
    接口管理
    """
    params = serializers.JSONField(required=False)
    headerparams = serializers.JSONField(required=False)
    bodyparams = serializers.JSONField(required=False)
    process_and_interface = PrimaryKeyRelatedField(help_text='关联数据', required=False,many=True, queryset=InterfaceModel.objects.all())
    url = serializers.CharField(source="case.file_name", read_only=True)
    class Meta:
        model = InterfaceModel
        fields ='__all__'
        extra_kwargs = {
            "interface_type":{"required":True}
        }
    def create(self, validated_data):
        print(validated_data)
        process_and_interface =  validated_data.get("process_and_interface")
        interface_type = validated_data.get("interface_type",1)
        if process_and_interface and interface_type==2:
            del validated_data["process_and_interface"]
            interface_obj = InterfaceModel.objects.create(**validated_data)
            for i in range(0,len(process_and_interface)):
                step = "步骤"+str(i+1)
                try:
                    InterfaceFlowModel.objects.create(from_interfacemodel=interface_obj,\
                                                  to_interfacemodel=process_and_interface[i],step=step)
                except:
                   raise serializers.ValidationError({"error":"数据已存在"})

            return interface_obj
        else:
            return  InterfaceModel.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.modifier = validated_data.get("modifier",instance.modifier)
        instance.desc = validated_data.get("desc",instance.desc)
        instance.path_url = validated_data.get('path_url',instance.path_url)
        instance.port = validated_data.get('port',instance.port)
        instance.request_agreement = validated_data.get('request_protocol',instance.request_protocol)
        instance.request_way_choice = validated_data.get('request_way_choice',instance.request_way_choice)
        instance.bodyformat = validated_data.get('bodyformat',instance.bodyformat)
        instance.params = validated_data.get('params',instance.params)
        instance.headerparams = validated_data.get('headerparams',instance.headerparams)
        instance.bodyparams = validated_data.get('bodyparams',instance.bodyparams)
        instance.preprocessing = validated_data.get('preprocessing',instance.preprocessing)
        instance.postprocessing = validated_data.get('postprocessing',instance.postprocessing)
        instance.assertion = validated_data.get('assertion',instance.assertion)

        instance.save()

        if instance.interface_type == 2:
            #先清空
            instance.process_and_interface.clear()
            flow_and_interface = validated_data.get("process_and_interface")
            for i in range(0, len(flow_and_interface)):
                step = "步骤" + str(i + 1)
                try:
                    InterfaceFlowModel.objects.create(from_interfacemodel=instance, \
                                                      to_interfacemodel=flow_and_interface[i], step=step)
                except:
                    raise serializers.ValidationError({"error": "数据已存在"})
        return  instance

class InterfaceCaseSerializer(serializers.ModelSerializer):
    excle_list = serializers.JSONField(source="case.exclelist", read_only=True)
    url = serializers.CharField(source="case.file_name",read_only=True)
    class Meta:
        model = InterfaceModel
        fields = ('id','excle_list',"url")

class KeysSerializer(serializers.ModelSerializer):
    params_constraint = serializers.JSONField(required=False)

    class Meta:
        model = KeysModel
        fields = '__all__'
