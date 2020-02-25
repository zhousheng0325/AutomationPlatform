from rest_framework.response import Response
class StatusResponse(Response):
    """ 统一返回结果 """
    def __init__(self, http_code=200, data=None, **kwargs):

        if 'message' not in data:
            data = {
                'message': 'OK',
                'data': data,
                'code':http_code
            }
        kwargs['data'] = data
        code = http_code
        super(StatusResponse, self).__init__(**kwargs)