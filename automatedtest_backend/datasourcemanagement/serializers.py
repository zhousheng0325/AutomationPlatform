from rest_framework import serializers
from .models import CaseFile

class UploadFileSerializer(serializers.ModelSerializer):

    interfacename = serializers.CharField(source='get_interfacename',read_only=True)
    exclelist = serializers.JSONField(required=False)
    class Meta:
        model = CaseFile
        extra_kwargs = {
            'file_name': {"required": False}
        }
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title",instance.title)
        instance.file_name = validated_data.get("file_name",instance.file_name)
        instance.interface = validated_data.get('interface',instance.interface)
        instance.exclelist = validated_data.get('exclelist',instance.exclelist)
        instance.save()
        return instance
    def create(self, validated_data):
        return CaseFile.objects.create(**validated_data)
    #在传递参数前进行解绑
    def to_internal_value(self, instance):
        interface_id = instance.get("interface",None)
        if interface_id is not None:
            casefile =  CaseFile.objects.filter(interface_id=interface_id).first()
            if casefile is not  None:
                casefile.interface_id = None
                casefile.save()
        return super(UploadFileSerializer, self).to_internal_value(instance)




