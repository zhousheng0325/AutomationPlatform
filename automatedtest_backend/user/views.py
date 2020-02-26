import os
from datetime import datetime, timedelta

from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.viewsets import GenericViewSet, mixins

from common.jwt_util import generate_jwt
from .serializers import ApiUser, ApiUserSerializer, UserSerializer
from common.myresponse import StatusResponse
from rest_framework.generics import GenericAPIView
from .models import User
from common.utils.login_util import login_decorator


# Create your views here.

@method_decorator(login_decorator,name="list")
class UsersOptionsView(GenericViewSet, mixins.ListModelMixin):
    """
    list:
    返回用户列表
    """
    serializer_class = ApiUserSerializer
    queryset = User.objects.filter(is_superuser=0,is_active=1).all()

    def list(self, request, *args, **kwargs):
        return StatusResponse(data=super().list(request).data)



class UserLoginView(GenericAPIView):
    def _generate_tokens(self, user_id, with_refresh_token=True):
        """
        生成token 和refresh_token
        :param user_id: 用户id
        :return: token, refresh_token
        """
        # 颁发JWT
        now = datetime.utcnow()
        expiry = now + timedelta(hours=float(os.environ['JWT_EXPIRY_HOURS']))
        token = generate_jwt({'user_id': user_id, 'refresh': False}, expiry)

        refresh_token = None
        if with_refresh_token:
            refresh_expiry = now + timedelta(days=float(os.environ['JWT_REFRESH_DAYS']))
            refresh_token = generate_jwt({'user_id': user_id, 'refresh': True}, refresh_expiry)
        return token, refresh_token

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        try:
          user = User.objects.get(username=username)
        except User.DoesNotExist as e:
            return StatusResponse(http_code=400,data={"tip": "用户不存在"})

        if user is not None and user.check_password(password):
            token, refresh_token = self._generate_tokens(user.id, with_refresh_token=True)
            data = {
                "token": token,
                "refresh_token": refresh_token,
                "id": user.id,
                "username": user.username
            }
            response = StatusResponse(data=data, http_code=201)
            return response
        return StatusResponse(http_code=400,data={"tip":"登录失败"})
    def put(self,request):
        if request.user_id and request.refresh:
            token,refresh_token =  self._generate_tokens(request.user_id, with_refresh_token=False)
            data ={
                "id":request.user_id,
                "token":token
            }
            response = StatusResponse(data=data, http_code=201)
            return response
        else:
            return StatusResponse(http_code=401, data={"tip": "token刷新失败"})

class UserRegistView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return StatusResponse(http_code=200,data=serializer.data)
