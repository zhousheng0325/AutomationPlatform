from common.jwt_util import verify_jwt


def jwt_token_middleware(get_response):
    # One-time configuration and initialization.
    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        request.user_id = None
        request.refresh = None
        token = request.META.get('HTTP_AUTHORIZATION')

        if token is not None and token.startswith('AUTOTEST '):
            token = token[9:]
            payload = verify_jwt(token)  # 获取到用户的信息
            if payload is not None:
                request.user_id = payload.get("user_id",None)
                request.refresh = payload.get("refresh",None)
        response = get_response(request)

        return response

    return middleware
