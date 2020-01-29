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

channel = grpc.insecure_channel('localhost:50051')
transport = transports.EchoGrpcTransport(channel=channel)

def test_echo():
  client = EchoClient(transport=transport)
  request = gs_echo.EchoRequest(content='hello world')
  response = client.echo(request)
  print("got response")
  print(response)


def test_expand():
  client = EchoClient(transport=transport)
  request = gs_echo.ExpandRequest(content='one two three four')
  response = client.expand(request)
  print("got response")
  print(response)
  for message in response:
    print(message)


def test_collect():
  client = EchoClient(transport=transport)

  content = 'The rain in Spain stays mainly on the Plain!'
  requests = content.split(' ')
  requests = map(lambda s: gs_echo.EchoRequest(content=s), requests)
  response = client.collect(iter(requests))

  print(response)

def test_chat():
  client = EchoClient(transport=transport)

  content = 'The rain in Spain stays mainly on the Plain!'
  requests = content.split(' ')
  requests = map(lambda s: gs_echo.EchoRequest(content=s), requests)
  responses = client.chat(iter(requests))
  for res in responses:
    print(res)
  print("trailing metadata...")
  print(responses.trailing_metadata())

test_echo()
test_expand()
test_collect()
test_chat()
