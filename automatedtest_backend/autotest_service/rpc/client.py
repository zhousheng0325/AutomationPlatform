import grpc
import autotest_pb2
import autotest_pb2_grpc
import time

def feed_articles(stub):
    # 构建rpc调用的调用参数
    interface_request = autotest_pb2.AutotestRequest()
    interface_request.interface_id.extend([1,2,3])
    interface_request.case_id.extend([4, 5, 6])
    interface_request.name = "test1"
    # 通过stub进行方法调用，并接收调用返回值

    ret = stub.autotest_interface(interface_request)
    print(ret.name)
    print('ret={}'.format(ret))

def run():
    """
    rpc客户端调用的方法
    """
    # 使用with语句连接rpc服务器
    with grpc.insecure_channel('127.0.0.1:8001') as channel:
        # 创建调用rpc远端服务的辅助对象stub
        stub = autotest_pb2_grpc.AutoTestStub(channel)
        # 通过stub进行rpc调用
        feed_articles(stub)
if __name__ == '__main__':
    run()