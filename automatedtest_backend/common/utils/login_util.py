from common.myresponse import StatusResponse

def login_decorator(func):
    def wrapper(request, *args, **kwargs):
        # if not request.user_id :#没有用户信息退出
        #     return StatusResponse(http_code=403,data={"tip":"用户需要认证"})
        # elif request.refresh:
        #     return StatusResponse(http_code=401,data={"tip":"请刷新token"})
        # else:
            return func(request, *args, **kwargs)

    return wrapper