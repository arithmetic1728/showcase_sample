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

channel = grpc.insecure_channel('localhost:7469')
transport = transports.EchoGrpcTransport(channel=channel)
client = EchoClient(transport=transport)
request = gs_echo.EchoRequest(content='hello world')
response = client.echo(request)
print(response)
