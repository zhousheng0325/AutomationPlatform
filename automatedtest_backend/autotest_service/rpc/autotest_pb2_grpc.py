# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from .import autotest_pb2 as autotest__pb2


class AutoTestStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.autotest_interface = channel.unary_unary(
        '/AutoTest/autotest_interface',
        request_serializer=autotest__pb2.AutotestRequest.SerializeToString,
        response_deserializer=autotest__pb2.AutotestResponse.FromString,
        )


class AutoTestServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def autotest_interface(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AutoTestServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'autotest_interface': grpc.unary_unary_rpc_method_handler(
          servicer.autotest_interface,
          request_deserializer=autotest__pb2.AutotestRequest.FromString,
          response_serializer=autotest__pb2.AutotestResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'AutoTest', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
