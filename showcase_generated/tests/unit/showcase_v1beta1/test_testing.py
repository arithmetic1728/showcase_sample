# -*- coding: utf-8 -*-

# Copyright (C) 2019  Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from unittest import mock

import grpc

import pytest

from google import auth
from google.api_core import client_options
from google.auth import credentials
from google.oauth2 import service_account
from google.showcase_v1beta1.services.testing import TestingClient
from google.showcase_v1beta1.services.testing import pagers
from google.showcase_v1beta1.services.testing import transports
from google.showcase_v1beta1.types import testing


def test_testing_client_from_service_account_file():
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_file') as factory:
        factory.return_value = creds
        client = TestingClient.from_service_account_file("dummy/file/path.json")
        assert client._transport._credentials == creds

        client = TestingClient.from_service_account_json("dummy/file/path.json")
        assert client._transport._credentials == creds

        assert client._transport._host == 'localhost:7469'


def test_testing_client_client_options():
    # Check the default options have their expected values.
    assert TestingClient.DEFAULT_OPTIONS.api_endpoint == 'localhost:7469'

    # Check that options can be customized.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch('google.showcase_v1beta1.services.testing.TestingClient.get_transport_class') as gtc:
        transport = gtc.return_value = mock.MagicMock()
        client = TestingClient(
            client_options=options
        )
        transport.assert_called_once_with(credentials=None, host="squid.clam.whelk")


def test_testing_client_client_options_from_dict():
    with mock.patch('google.showcase_v1beta1.services.testing.TestingClient.get_transport_class') as gtc:
        transport = gtc.return_value = mock.MagicMock()
        client = TestingClient(
            client_options={'api_endpoint': 'squid.clam.whelk'}
        )
        transport.assert_called_once_with(credentials=None, host="squid.clam.whelk")


def test_create_session(transport: str = 'grpc'):
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = testing.CreateSessionRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.create_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = testing.Session(
            name='name_value',
            version=testing.Session.Version.V1_LATEST,
        )
        response = client.create_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.Session)
    assert response.name == 'name_value'
    assert response.version == testing.Session.Version.V1_LATEST


def test_get_session(transport: str = 'grpc'):
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = testing.GetSessionRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.get_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = testing.Session(
            name='name_value',
            version=testing.Session.Version.V1_LATEST,
        )
        response = client.get_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.Session)
    assert response.name == 'name_value'
    assert response.version == testing.Session.Version.V1_LATEST


def test_get_session_field_headers():
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
  )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.GetSessionRequest(
        name='name/value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.get_session),
            '__call__') as call:
        call.return_value = testing.Session()
        response = client.get_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'name=name/value',
    ) in kw['metadata']


def test_list_sessions(transport: str = 'grpc'):
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = testing.ListSessionsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_sessions),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = testing.ListSessionsResponse(
            next_page_token='next_page_token_value',
        )
        response = client.list_sessions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListSessionsPager)
    assert response.next_page_token == 'next_page_token_value'


def test_list_sessions_pager():
    client = TestingClient(
        credentials=credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_sessions),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                    testing.Session(),
                ],
                next_page_token='abc',
            ),
            testing.ListSessionsResponse(
                sessions=[],
                next_page_token='def',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                ],
                next_page_token='ghi',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                ],
            ),
            RuntimeError,
        )
        results = [i for i in client.list_sessions(
            request={},
        )]
        assert len(results) == 6
        assert all([isinstance(i, testing.Session)
                    for i in results])

def test_list_sessions_pages():
    client = TestingClient(
        credentials=credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_sessions),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                    testing.Session(),
                ],
                next_page_token='abc',
            ),
            testing.ListSessionsResponse(
                sessions=[],
                next_page_token='def',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                ],
                next_page_token='ghi',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_sessions(request={}).pages)
        for page, token in zip(pages, ['abc','def','ghi', '']):
            assert page.raw_page.next_page_token == token


def test_delete_session(transport: str = 'grpc'):
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = testing.DeleteSessionRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.delete_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_report_session(transport: str = 'grpc'):
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = testing.ReportSessionRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.report_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = testing.ReportSessionResponse(
            result=testing.ReportSessionResponse.Result.PASSED,
        )
        response = client.report_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.ReportSessionResponse)
    assert response.result == testing.ReportSessionResponse.Result.PASSED


def test_list_tests(transport: str = 'grpc'):
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = testing.ListTestsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_tests),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = testing.ListTestsResponse(
            next_page_token='next_page_token_value',
        )
        response = client.list_tests(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListTestsPager)
    assert response.next_page_token == 'next_page_token_value'


def test_list_tests_field_headers():
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
  )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.ListTestsRequest(
        parent='parent/value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_tests),
            '__call__') as call:
        call.return_value = testing.ListTestsResponse()
        response = client.list_tests(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'parent=parent/value',
    ) in kw['metadata']


def test_list_tests_pager():
    client = TestingClient(
        credentials=credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_tests),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                    testing.Test(),
                ],
                next_page_token='abc',
            ),
            testing.ListTestsResponse(
                tests=[],
                next_page_token='def',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                ],
                next_page_token='ghi',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                ],
            ),
            RuntimeError,
        )
        results = [i for i in client.list_tests(
            request={},
        )]
        assert len(results) == 6
        assert all([isinstance(i, testing.Test)
                    for i in results])

def test_list_tests_pages():
    client = TestingClient(
        credentials=credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_tests),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                    testing.Test(),
                ],
                next_page_token='abc',
            ),
            testing.ListTestsResponse(
                tests=[],
                next_page_token='def',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                ],
                next_page_token='ghi',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_tests(request={}).pages)
        for page, token in zip(pages, ['abc','def','ghi', '']):
            assert page.raw_page.next_page_token == token


def test_delete_test(transport: str = 'grpc'):
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = testing.DeleteTestRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.delete_test),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_verify_test(transport: str = 'grpc'):
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = testing.VerifyTestRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.verify_test),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = testing.VerifyTestResponse(
        )
        response = client.verify_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.VerifyTestResponse)


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.TestingGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = TestingClient(
            credentials=credentials.AnonymousCredentials(),
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.TestingGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    client = TestingClient(transport=transport)
    assert client._transport is transport


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client._transport,
        transports.TestingGrpcTransport,
    )


def test_testing_base_transport():
    # Instantiate the base transport.
    transport = transports.TestingTransport(
        credentials=credentials.AnonymousCredentials(),
    )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        'create_session',
        'get_session',
        'list_sessions',
        'delete_session',
        'report_session',
        'list_tests',
        'delete_test',
        'verify_test',
        )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())


def test_testing_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, 'default') as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        client = TestingClient()
        adc.assert_called_once_with(scopes=(
        ))


def test_testing_host_no_port():
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='localhost'),
        transport='grpc',
    )
    assert client._transport._host == 'localhost:443'


def test_testing_host_with_port():
    client = TestingClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='localhost:8000'),
        transport='grpc',
    )
    assert client._transport._host == 'localhost:8000'


def test_testing_grpc_transport_channel():
    channel = grpc.insecure_channel('http://localhost/')
    transport = transports.TestingGrpcTransport(
        channel=channel,
    )
    assert transport.grpc_channel is channel


def test_session_path():
  session = "squid"

  expected = "sessions/{session}".format(session=session, )
  actual = TestingClient.session_path(session)
  assert expected == actual
