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
from google.showcase_v1beta1.types import identity

from .base import IdentityTransport


class IdentityGrpcTransport(IdentityTransport):
    """gRPC backend transport for Identity.

    A simple identity service.

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
    def create_user(self) -> Callable[
            [identity.CreateUserRequest],
            identity.User]:
        r"""Return a callable for the create user method over gRPC.

        Creates a user.

        Returns:
            Callable[[~.CreateUserRequest],
                    ~.User]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_user' not in self._stubs:
            self._stubs['create_user'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Identity/CreateUser',
                request_serializer=identity.CreateUserRequest.serialize,
                response_deserializer=identity.User.deserialize,
            )
        return self._stubs['create_user']

    @property
    def get_user(self) -> Callable[
            [identity.GetUserRequest],
            identity.User]:
        r"""Return a callable for the get user method over gRPC.

        Retrieves the User with the given uri.

        Returns:
            Callable[[~.GetUserRequest],
                    ~.User]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_user' not in self._stubs:
            self._stubs['get_user'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Identity/GetUser',
                request_serializer=identity.GetUserRequest.serialize,
                response_deserializer=identity.User.deserialize,
            )
        return self._stubs['get_user']

    @property
    def update_user(self) -> Callable[
            [identity.UpdateUserRequest],
            identity.User]:
        r"""Return a callable for the update user method over gRPC.

        Updates a user.

        Returns:
            Callable[[~.UpdateUserRequest],
                    ~.User]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_user' not in self._stubs:
            self._stubs['update_user'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Identity/UpdateUser',
                request_serializer=identity.UpdateUserRequest.serialize,
                response_deserializer=identity.User.deserialize,
            )
        return self._stubs['update_user']

    @property
    def delete_user(self) -> Callable[
            [identity.DeleteUserRequest],
            empty.Empty]:
        r"""Return a callable for the delete user method over gRPC.

        Deletes a user, their profile, and all of their
        authored messages.

        Returns:
            Callable[[~.DeleteUserRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_user' not in self._stubs:
            self._stubs['delete_user'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Identity/DeleteUser',
                request_serializer=identity.DeleteUserRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs['delete_user']

    @property
    def list_users(self) -> Callable[
            [identity.ListUsersRequest],
            identity.ListUsersResponse]:
        r"""Return a callable for the list users method over gRPC.

        Lists all users.

        Returns:
            Callable[[~.ListUsersRequest],
                    ~.ListUsersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_users' not in self._stubs:
            self._stubs['list_users'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Identity/ListUsers',
                request_serializer=identity.ListUsersRequest.serialize,
                response_deserializer=identity.ListUsersResponse.deserialize,
            )
        return self._stubs['list_users']


__all__ = (
    'IdentityGrpcTransport',
)
