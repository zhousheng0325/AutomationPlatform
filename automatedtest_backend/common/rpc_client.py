import grpc
from django.utils.functional import SimpleLazyObject
client = SimpleLazyObject(lambda:grpc.insecure_channel('127.0.0.1:8001'))

