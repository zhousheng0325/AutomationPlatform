import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import autotest_pb2
from rpc.autotest_pb2_grpc import AutoTestServicer, add_AutoTestServicer_to_server
from celery_task.autotask.tasks import test_script


import grpc
from concurrent.futures import ThreadPoolExecutor
import time


class AutoTestServicer1(AutoTestServicer):

    def autotest_interface(self, request, context):
        """
        :param request:
         request.interface_id表示接口id
         request.case_id表示用例id
        :param context:
        :return:
        """
        print("=============server==================")
        interface_id = [id for id in request.interface_id]
        interface_name = request.name
        case_id = [id for id in request.case_id]
        response = autotest_pb2.AutotestResponse()
        # 异步任务调用
        test_script.delay(interface_id, case_id)
        response.interface_id.extend(interface_id)
        response.name = interface_name
        return response


def serve():
    """
    rpc服务端启动方法
    """
    # 创建一个rpc服务器
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    # 向服务器中添加被调用的服务方法
    add_AutoTestServicer_to_server(AutoTestServicer1(), server)
    # 微服务器绑定ip地址和端口
    server.add_insecure_port('127.0.0.1:8001')
    # 启动rpc服务
    server.start()
    # start()不会阻塞，此处需要加上循环睡眠 防止程序退出
    while True:
        time.sleep(10)


if __name__ == '__main__':
    serve()
