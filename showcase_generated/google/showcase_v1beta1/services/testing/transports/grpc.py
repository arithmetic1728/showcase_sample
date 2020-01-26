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

from typing import Callable, Dict

from google.api_core import grpc_helpers   # type: ignore
from google.auth import credentials        # type: ignore

import grpc  # type: ignore

from google.protobuf import empty_pb2 as empty  # type: ignore
from google.showcase_v1beta1.types import testing

from .base import TestingTransport


class TestingGrpcTransport(TestingTransport):
    """gRPC backend transport for Testing.

    A service to facilitate running discrete sets of tests
    against Showcase.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    def __init__(self, *,
            host: str = 'localhost:7469',
            credentials: credentials.Credentials = None,
            channel: grpc.Channel = None) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
        """
        # Sanity check: Ensure that channel and credentials are not both
        # provided.
        if channel:
            credentials = False

        # Run the base constructor.
        super().__init__(host=host, credentials=credentials)
        self._stubs = {}  # type: Dict[str, Callable]

        # If a channel was explicitly provided, set it.
        if channel:
            self._grpc_channel = channel

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Sanity check: Only create a new channel if we do not already
        # have one.
        if not hasattr(self, '_grpc_channel'):
            self._grpc_channel = grpc_helpers.create_channel(
                self._host,
                credentials=self._credentials,
                scopes=self.AUTH_SCOPES,
            )

        # Return the channel from cache.
        return self._grpc_channel

    @property
    def create_session(self) -> Callable[
            [testing.CreateSessionRequest],
            testing.Session]:
        r"""Return a callable for the create session method over gRPC.

        Creates a new testing session.

        Returns:
            Callable[[~.CreateSessionRequest],
                    ~.Session]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_session' not in self._stubs:
            self._stubs['create_session'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Testing/CreateSession',
                request_serializer=testing.CreateSessionRequest.serialize,
                response_deserializer=testing.Session.deserialize,
            )
        return self._stubs['create_session']

    @property
    def get_session(self) -> Callable[
            [testing.GetSessionRequest],
            testing.Session]:
        r"""Return a callable for the get session method over gRPC.

        Gets a testing session.

        Returns:
            Callable[[~.GetSessionRequest],
                    ~.Session]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_session' not in self._stubs:
            self._stubs['get_session'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Testing/GetSession',
                request_serializer=testing.GetSessionRequest.serialize,
                response_deserializer=testing.Session.deserialize,
            )
        return self._stubs['get_session']

    @property
    def list_sessions(self) -> Callable[
            [testing.ListSessionsRequest],
            testing.ListSessionsResponse]:
        r"""Return a callable for the list sessions method over gRPC.

        Lists the current test sessions.

        Returns:
            Callable[[~.ListSessionsRequest],
                    ~.ListSessionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_sessions' not in self._stubs:
            self._stubs['list_sessions'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Testing/ListSessions',
                request_serializer=testing.ListSessionsRequest.serialize,
                response_deserializer=testing.ListSessionsResponse.deserialize,
            )
        return self._stubs['list_sessions']

    @property
    def delete_session(self) -> Callable[
            [testing.DeleteSessionRequest],
            empty.Empty]:
        r"""Return a callable for the delete session method over gRPC.

        Delete a test session.

        Returns:
            Callable[[~.DeleteSessionRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_session' not in self._stubs:
            self._stubs['delete_session'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Testing/DeleteSession',
                request_serializer=testing.DeleteSessionRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs['delete_session']

    @property
    def report_session(self) -> Callable[
            [testing.ReportSessionRequest],
            testing.ReportSessionResponse]:
        r"""Return a callable for the report session method over gRPC.

        Report on the status of a session.
        This generates a report detailing which tests have been
        completed, and an overall rollup.

        Returns:
            Callable[[~.ReportSessionRequest],
                    ~.ReportSessionResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'report_session' not in self._stubs:
            self._stubs['report_session'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Testing/ReportSession',
                request_serializer=testing.ReportSessionRequest.serialize,
                response_deserializer=testing.ReportSessionResponse.deserialize,
            )
        return self._stubs['report_session']

    @property
    def list_tests(self) -> Callable[
            [testing.ListTestsRequest],
            testing.ListTestsResponse]:
        r"""Return a callable for the list tests method over gRPC.

        List the tests of a sessesion.

        Returns:
            Callable[[~.ListTestsRequest],
                    ~.ListTestsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_tests' not in self._stubs:
            self._stubs['list_tests'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Testing/ListTests',
                request_serializer=testing.ListTestsRequest.serialize,
                response_deserializer=testing.ListTestsResponse.deserialize,
            )
        return self._stubs['list_tests']

    @property
    def delete_test(self) -> Callable[
            [testing.DeleteTestRequest],
            empty.Empty]:
        r"""Return a callable for the delete test method over gRPC.

        Explicitly decline to implement a test.

        This removes the test from subsequent ``ListTests`` calls, and
        attempting to do the test will error.

        This method will error if attempting to delete a required test.

        Returns:
            Callable[[~.DeleteTestRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_test' not in self._stubs:
            self._stubs['delete_test'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Testing/DeleteTest',
                request_serializer=testing.DeleteTestRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs['delete_test']

    @property
    def verify_test(self) -> Callable[
            [testing.VerifyTestRequest],
            testing.VerifyTestResponse]:
        r"""Return a callable for the verify test method over gRPC.

        Register a response to a test.
        In cases where a test involves registering a final
        answer at the end of the test, this method provides the
        means to do so.

        Returns:
            Callable[[~.VerifyTestRequest],
                    ~.VerifyTestResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'verify_test' not in self._stubs:
            self._stubs['verify_test'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Testing/VerifyTest',
                request_serializer=testing.VerifyTestRequest.serialize,
                response_deserializer=testing.VerifyTestResponse.deserialize,
            )
        return self._stubs['verify_test']


__all__ = (
    'TestingGrpcTransport',
)
