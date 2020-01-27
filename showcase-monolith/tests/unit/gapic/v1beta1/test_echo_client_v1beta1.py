# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests."""

import mock
import pytest

from google.rpc import status_pb2

from google import showcase_v1beta1
from google.longrunning import operations_pb2
from google.showcase_v1beta1.proto import echo_pb2



class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""
    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""
    def __init__(self, responses = []):
        self.responses = responses
        self.requests = []

    def unary_unary(
            self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)

    def unary_stream(
            self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)

    def stream_unary(
            self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)

    def stream_stream(
            self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestEchoClient(object):

    def test_echo(self):
        # Setup Expected Response
        content = 'content951530617'
        expected_response = {'content': content}
        expected_response = echo_pb2.EchoResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        response = client.echo()
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = echo_pb2.EchoRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_echo_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        with pytest.raises(CustomException):
            client.echo()

    def test_expand(self):
        # Setup Expected Response
        content = 'content951530617'
        expected_response = {'content': content}
        expected_response = echo_pb2.EchoResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [iter([expected_response])])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()


        response = client.expand()
        resources = list(response)
        assert len(resources) == 1
        assert expected_response == resources[0]

        assert len(channel.requests) == 1
        expected_request = echo_pb2.ExpandRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_expand_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        with pytest.raises(CustomException):
            client.expand()

    def test_paged_expand(self):
        # Setup Expected Response
        next_page_token = ''
        responses_element = {}
        responses = [responses_element]
        expected_response = {'next_page_token': next_page_token, 'responses': responses}
        expected_response = echo_pb2.PagedExpandResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        paged_list_response = client.paged_expand()
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.responses[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = echo_pb2.PagedExpandRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_paged_expand_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        paged_list_response = client.paged_expand()
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_collect(self):
        # Setup Expected Response
        content = 'content951530617'
        expected_response = {'content': content}
        expected_response = echo_pb2.EchoResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        # Setup Request
        request = {}
        request = echo_pb2.EchoRequest(**request)
        requests = [request]

        response = client.collect(requests)
        assert expected_response == response

        assert len(channel.requests) == 1
        actual_requests = channel.requests[0][1]
        assert len(actual_requests) == 1
        actual_request = list(actual_requests)[0]
        assert request == actual_request

    def test_collect_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        # Setup request
        request = {}

        request = echo_pb2.EchoRequest(**request)
        requests = [request]

        with pytest.raises(CustomException):
            client.collect(requests)

    def test_chat(self):
        # Setup Expected Response
        content = 'content951530617'
        expected_response = {'content': content}
        expected_response = echo_pb2.EchoResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [iter([expected_response])])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        # Setup Request
        request = {}
        request = echo_pb2.EchoRequest(**request)
        requests = [request]

        response = client.chat(requests)
        resources = list(response)
        assert len(resources) == 1
        assert expected_response == resources[0]

        assert len(channel.requests) == 1
        actual_requests = channel.requests[0][1]
        assert len(actual_requests) == 1
        actual_request = list(actual_requests)[0]
        assert request == actual_request

    def test_chat_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        # Setup request
        request = {}

        request = echo_pb2.EchoRequest(**request)
        requests = [request]

        with pytest.raises(CustomException):
            client.chat(requests)

    def test_wait(self):
        # Setup Expected Response
        content = 'content951530617'
        expected_response = {'content': content}
        expected_response = echo_pb2.WaitResponse(**expected_response)
        operation = operations_pb2.Operation(name='operations/test_wait', done=True)
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        response = client.wait()
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = echo_pb2.WaitRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request


    def test_wait_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(name='operations/test_wait_exception', done=True)
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        response = client.wait()
        exception = response.exception()
        assert exception.errors[0] == error

    def test_block(self):
        # Setup Expected Response
        content = 'content951530617'
        expected_response = {'content': content}
        expected_response = echo_pb2.BlockResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        response = client.block()
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = echo_pb2.BlockRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_block_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = showcase_v1beta1.EchoClient()

        with pytest.raises(CustomException):
            client.block()
