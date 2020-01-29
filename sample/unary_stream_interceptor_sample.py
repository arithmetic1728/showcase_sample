import grpc

from google import auth
from google.api_core import client_options
from google.api_core import future
from google.api_core import operations_v1
from google.auth import credentials
from google.longrunning import operations_pb2
from google.oauth2 import service_account
from google.rpc import status_pb2 as status  # type: ignore
from google.showcase_v1beta1.services.echo import EchoClient
from google.showcase_v1beta1.services.echo import pagers
from google.showcase_v1beta1.services.echo import transports
from google.showcase_v1beta1.types import echo
from google.showcase_v1beta1.types import echo as gs_echo

import client_interceptor

def run_should_fail():
  print("================= should fail with 'Access denied!' ====================")
  channel = grpc.insecure_channel('localhost:50051')
  transport = transports.EchoGrpcTransport(channel=channel)
  client = EchoClient(transport=transport)
  try:
    request = gs_echo.ExpandRequest(content='one two three four')
    responses = client.expand(request)
    for message in responses:
      print(message)
    print("trailing metadata...")
    print(responses.trailing_metadata())
  except:
      print(sys.exc_info())

def run_should_pass():
  print("================= should pass ====================")
  header_adder_interceptor = client_interceptor.header_adder_interceptor(
        'one-time-password', '42')
  channel = grpc.insecure_channel('localhost:50051')
  intercept_channel = grpc.intercept_channel(channel, header_adder_interceptor)
  transport = transports.EchoGrpcTransport(channel=intercept_channel)
  client = EchoClient(transport=transport)
  request = gs_echo.ExpandRequest(content='one two three four')
  responses = client.expand(request)
  for message in responses:
    print(message)
  print("trailing metadata...")
  print(responses.trailing_metadata())

run_should_pass()
run_should_fail()
