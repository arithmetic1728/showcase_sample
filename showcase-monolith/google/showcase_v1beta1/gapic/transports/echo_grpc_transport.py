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


import google.api_core.grpc_helpers
import google.api_core.operations_v1

from google.showcase_v1beta1.proto import echo_pb2_grpc


class EchoGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.showcase.v1beta1 Echo API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """
    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = (
        'https://www.googleapis.com/auth/cloud-platform',
    )

    def __init__(self, channel=None, credentials=None,
                 address='localhost:7469'):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                'The `channel` and `credentials` arguments are mutually '
                'exclusive.',
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    'grpc.max_send_message_length': -1,
                    'grpc.max_receive_message_length': -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            'echo_stub': echo_pb2_grpc.EchoStub(channel),
        }

        # Because this API includes a method that returns a
        # long-running operation (proto: google.longrunning.Operation),
        # instantiate an LRO client.
        self._operations_client = google.api_core.operations_v1.OperationsClient(channel)

    @classmethod
    def create_channel(
                cls,
                address='localhost:7469',
                credentials=None,
                **kwargs):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address,
            credentials=credentials,
            scopes=cls._OAUTH_SCOPES,
            **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def echo(self):
        """Return the gRPC stub for :meth:`EchoClient.echo`.

        This method simply echos the request. This method is showcases unary rpcs.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['echo_stub'].Echo

    @property
    def expand(self):
        """Return the gRPC stub for :meth:`EchoClient.expand`.

        This method split the given content into words and will pass each word back
        through the stream. This method showcases server-side streaming rpcs.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['echo_stub'].Expand

    @property
    def paged_expand(self):
        """Return the gRPC stub for :meth:`EchoClient.paged_expand`.

        This is similar to the Expand method but instead of returning a stream of
        expanded words, this method returns a paged list of expanded words.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['echo_stub'].PagedExpand

    @property
    def collect(self):
        """Return the gRPC stub for :meth:`EchoClient.collect`.

        This method will collect the words given to it. When the stream is closed
        by the client, this method will return the a concatenation of the strings
        passed to it. This method showcases client-side streaming rpcs.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['echo_stub'].Collect

    @property
    def chat(self):
        """Return the gRPC stub for :meth:`EchoClient.chat`.

        This method, upon receiving a request on the stream, the same content will
        be passed  back on the stream. This method showcases bidirectional
        streaming rpcs.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['echo_stub'].Chat

    @property
    def wait(self):
        """Return the gRPC stub for :meth:`EchoClient.wait`.

        This method will wait the requested amount of and then return.
        This method showcases how a client handles a request timing out.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['echo_stub'].Wait

    @property
    def block(self):
        """Return the gRPC stub for :meth:`EchoClient.block`.

        This method will block (wait) for the requested amount of time
        and then return the response or error.
        This method showcases how a client handles delays or retries.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['echo_stub'].Block