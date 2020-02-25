from .models import ApiUser, User
from rest_framework import serializers


class ApiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id','email', 'username', 'mobile')


class UserSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(label='确认密码', write_only=True,required=True)
    class Meta:
        model = User
        fields = ('email', 'mobile', "username", "password")
        extra_kwargs = {
            'email': {'required': False},
            'mobile': {'required': True},
            'username': {'required': True},
            'password': {'required': True, "write_only": True},
        }

    def create(self, validated_data):
        # del validated_data["password2"]
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    # def validate(self, attrs):
    #     if attrs["password"]!=attrs["password2"]:
    #         raise serializers.ValidationError("密码不一致")
    #
    #     return attrs
