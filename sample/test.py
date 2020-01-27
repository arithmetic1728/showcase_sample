from unittest import mock

import grpc

import pytest

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


def test_echo_client_from_service_account_file():
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_file') as factory:
        factory.return_value = creds
        client = EchoClient.from_service_account_file("dummy/file/path.json")
        assert client._transport._credentials == creds

        client = EchoClient.from_service_account_json("dummy/file/path.json")
        assert client._transport._credentials == creds

        assert client._transport._host == 'localhost:7469'


def test_echo_client_client_options():
    # Check the default options have their expected values.
    assert EchoClient.DEFAULT_OPTIONS.api_endpoint == 'localhost:7469'

    # Check that options can be customized.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch('google.showcase_v1beta1.services.echo.EchoClient.get_transport_class') as gtc:
        transport = gtc.return_value = mock.MagicMock()
        client = EchoClient(
            client_options=options
        )
        transport.assert_called_once_with(credentials=None, host="squid.clam.whelk")


def test_echo_client_client_options_from_dict():
    with mock.patch('google.showcase_v1beta1.services.echo.EchoClient.get_transport_class') as gtc:
        transport = gtc.return_value = mock.MagicMock()
        client = EchoClient(
            client_options={'api_endpoint': 'squid.clam.whelk'}
        )
        transport.assert_called_once_with(credentials=None, host="squid.clam.whelk")


def test_echo(transport: str = 'grpc'):
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = gs_echo.EchoRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.echo),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = gs_echo.EchoResponse(
            content='content_value',
        )
        response = client.echo(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.EchoResponse)
    assert response.content == 'content_value'


def test_expand(transport: str = 'grpc'):
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = gs_echo.ExpandRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.expand),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([gs_echo.EchoResponse()])
        response = client.expand(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, gs_echo.EchoResponse)


def test_expand_flattened():
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.expand),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([gs_echo.EchoResponse()])

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.expand(
            content='content_value',
            error=status.Status(code=411),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].content == 'content_value'
        assert args[0].error == status.Status(code=411)


def test_expand_flattened_error():
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.expand(
            gs_echo.ExpandRequest(),
            content='content_value',
            error=status.Status(code=411),
        )


def test_collect(transport: str = 'grpc'):
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = gs_echo.EchoRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.collect),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = gs_echo.EchoResponse(
            content='content_value',
        )
        response = client.collect(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.EchoResponse)
    assert response.content == 'content_value'


def test_chat(transport: str = 'grpc'):
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = gs_echo.EchoRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.chat),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([gs_echo.EchoResponse()])
        response = client.chat(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, gs_echo.EchoResponse)


def test_paged_expand(transport: str = 'grpc'):
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = gs_echo.PagedExpandRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.paged_expand),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = gs_echo.PagedExpandResponse(
            next_page_token='next_page_token_value',
        )
        response = client.paged_expand(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.PagedExpandPager)
    assert response.next_page_token == 'next_page_token_value'


def test_paged_expand_pager():
    client = EchoClient(
        credentials=credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.paged_expand),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
                next_page_token='abc',
            ),
            gs_echo.PagedExpandResponse(
                responses=[],
                next_page_token='def',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                ],
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
            ),
            RuntimeError,
        )
        results = [i for i in client.paged_expand(
            request={},
        )]
        assert len(results) == 6
        assert all([isinstance(i, gs_echo.EchoResponse)
                    for i in results])

def test_paged_expand_pages():
    client = EchoClient(
        credentials=credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.paged_expand),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
                next_page_token='abc',
            ),
            gs_echo.PagedExpandResponse(
                responses=[],
                next_page_token='def',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                ],
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.paged_expand(request={}).pages)
        for page, token in zip(pages, ['abc','def','ghi', '']):
            assert page.raw_page.next_page_token == token


def test_wait(transport: str = 'grpc'):
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = gs_echo.WaitRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.wait),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name='operations/spam')
        response = client.wait(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_block(transport: str = 'grpc'):
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = gs_echo.BlockRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.block),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = gs_echo.BlockResponse(
            content='content_value',
        )
        response = client.block(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.BlockResponse)
    assert response.content == 'content_value'


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.EchoGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = EchoClient(
            credentials=credentials.AnonymousCredentials(),
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.EchoGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    client = EchoClient(transport=transport)
    assert client._transport is transport


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client._transport,
        transports.EchoGrpcTransport,
    )


def test_echo_base_transport():
    # Instantiate the base transport.
    transport = transports.EchoTransport(
        credentials=credentials.AnonymousCredentials(),
    )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        'echo',
        'expand',
        'collect',
        'chat',
        'paged_expand',
        'wait',
        'block',
        )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    # Additionally, the LRO client (a property) should
    # also raise NotImplementedError
    with pytest.raises(NotImplementedError):
        transport.operations_client


def test_echo_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, 'default') as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        client = EchoClient()
        adc.assert_called_once_with(scopes=(
        ))


def test_echo_host_no_port():
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='localhost'),
        transport='grpc',
    )
    assert client._transport._host == 'localhost:443'


def test_echo_host_with_port():
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='localhost:8000'),
        transport='grpc',
    )
    assert client._transport._host == 'localhost:8000'


def test_echo_grpc_transport_channel():
    channel = grpc.insecure_channel('http://localhost/')
    transport = transports.EchoGrpcTransport(
        channel=channel,
    )
    assert transport.grpc_channel is channel


def test_echo_grpc_lro_client():
    client = EchoClient(
        credentials=credentials.AnonymousCredentials(),
        transport='grpc',
    )
    transport = client._transport

    # Ensure that we have a api-core operations client.
    assert isinstance(
        transport.operations_client,
        operations_v1.OperationsClient,
    )

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client

