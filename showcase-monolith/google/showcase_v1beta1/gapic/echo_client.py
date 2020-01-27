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

"""Accesses the google.showcase.v1beta1 Echo API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.grpc_helpers
import google.api_core.operation
import google.api_core.operations_v1
import google.api_core.page_iterator
import google.api_core.protobuf_helpers
import grpc

from google.longrunning import operations_pb2
from google.protobuf import duration_pb2
from google.protobuf import timestamp_pb2
from google.rpc import status_pb2
from google.showcase_v1beta1.gapic import echo_client_config
from google.showcase_v1beta1.gapic.transports import echo_grpc_transport
from google.showcase_v1beta1.proto import echo_pb2
from google.showcase_v1beta1.proto import echo_pb2_grpc



_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    'google-showcase',
).version


class EchoClient(object):
    """
    This service is used showcase the four main types of rpcs - unary, server
    side streaming, client side streaming, and bidirectional streaming. This
    service also exposes methods that explicitly implement server delay, and
    paginated calls. Set the 'showcase-trailer' metadata key on any method
    to have the values echoed in the response trailers.
    """

    SERVICE_ADDRESS = 'localhost:7469'
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = 'google.showcase.v1beta1.Echo'


    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            EchoClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename)
        kwargs['credentials'] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    def __init__(self, transport=None, channel=None, credentials=None,
            client_config=None, client_info=None, client_options=None):
        """Constructor.

        Args:
            transport (Union[~.EchoGrpcTransport,
                    Callable[[~.Credentials, type], ~.EchoGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn('The `client_config` argument is deprecated.',
                          PendingDeprecationWarning, stacklevel=2)
        else:
            client_config = echo_client_config.config

        if channel:
            warnings.warn('The `channel` argument is deprecated; use '
                          '`transport` instead.',
                          PendingDeprecationWarning, stacklevel=2)

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(client_options)
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=echo_grpc_transport.EchoGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        'Received both a transport instance and '
                        'credentials; these are mutually exclusive.'
                    )
                self.transport = transport
        else:
            self.transport = echo_grpc_transport.EchoGrpcTransport(
                address=api_endpoint,
                channel=channel,
                credentials=credentials,
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION,
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config['interfaces'][self._INTERFACE_NAME],
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def echo(
            self,
            content=None,
            error=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        This method simply echos the request. This method is showcases unary rpcs.

        Example:
            >>> from google import showcase_v1beta1
            >>>
            >>> client = showcase_v1beta1.EchoClient()
            >>>
            >>> response = client.echo()

        Args:
            content (str): The content to be echoed by the server.
            error (Union[dict, ~google.showcase_v1beta1.types.Status]): The error to be thrown by the server.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.showcase_v1beta1.types.Status`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.showcase_v1beta1.types.EchoResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'echo' not in self._inner_api_calls:
            self._inner_api_calls['echo'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.echo,
                default_retry=self._method_configs['Echo'].retry,
                default_timeout=self._method_configs['Echo'].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            content=content,
            error=error,
        )

        request = echo_pb2.EchoRequest(
            content=content,
            error=error,
        )
        return self._inner_api_calls['echo'](request, retry=retry, timeout=timeout, metadata=metadata)

    def expand(
            self,
            content=None,
            error=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        This method split the given content into words and will pass each word back
        through the stream. This method showcases server-side streaming rpcs.

        Example:
            >>> from google import showcase_v1beta1
            >>>
            >>> client = showcase_v1beta1.EchoClient()
            >>>
            >>> for element in client.expand():
            ...     # process element
            ...     pass

        Args:
            content (str): The content that will be split into words and returned on the stream.
            error (Union[dict, ~google.showcase_v1beta1.types.Status]): The error that is thrown after all words are sent on the stream.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.showcase_v1beta1.types.Status`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            Iterable[~google.showcase_v1beta1.types.EchoResponse].

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'expand' not in self._inner_api_calls:
            self._inner_api_calls['expand'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.expand,
                default_retry=self._method_configs['Expand'].retry,
                default_timeout=self._method_configs['Expand'].timeout,
                client_info=self._client_info,
            )

        request = echo_pb2.ExpandRequest(
            content=content,
            error=error,
        )
        return self._inner_api_calls['expand'](request, retry=retry, timeout=timeout, metadata=metadata)

    def paged_expand(
            self,
            content=None,
            page_size=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        This is similar to the Expand method but instead of returning a stream of
        expanded words, this method returns a paged list of expanded words.

        Example:
            >>> from google import showcase_v1beta1
            >>>
            >>> client = showcase_v1beta1.EchoClient()
            >>>
            >>> # Iterate over all results
            >>> for element in client.paged_expand():
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.paged_expand().pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            content (str): The string to expand.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.showcase_v1beta1.types.EchoResponse` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'paged_expand' not in self._inner_api_calls:
            self._inner_api_calls['paged_expand'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.paged_expand,
                default_retry=self._method_configs['PagedExpand'].retry,
                default_timeout=self._method_configs['PagedExpand'].timeout,
                client_info=self._client_info,
            )

        request = echo_pb2.PagedExpandRequest(
            content=content,
            page_size=page_size,
        )
        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(self._inner_api_calls['paged_expand'], retry=retry, timeout=timeout, metadata=metadata),
            request=request,
            items_field='responses',
            request_token_field='page_token',
            response_token_field='next_page_token',
        )
        return iterator

    def collect(
            self,
            requests,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        This method will collect the words given to it. When the stream is closed
        by the client, this method will return the a concatenation of the strings
        passed to it. This method showcases client-side streaming rpcs.

        EXPERIMENTAL: This method interface might change in the future.

        Example:
            >>> from google import showcase_v1beta1
            >>>
            >>> client = showcase_v1beta1.EchoClient()
            >>>
            >>> request = {}
            >>>
            >>> requests = [request]
            >>> response = client.collect(requests)

        Args:
            requests (iterator[dict|google.showcase_v1beta1.proto.echo_pb2.EchoRequest]): The input objects. If a dict is provided, it must be of the
                same form as the protobuf message :class:`~google.showcase_v1beta1.types.EchoRequest`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.showcase_v1beta1.types.EchoResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'collect' not in self._inner_api_calls:
            self._inner_api_calls['collect'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.collect,
                default_retry=self._method_configs['Collect'].retry,
                default_timeout=self._method_configs['Collect'].timeout,
                client_info=self._client_info,
            )

        return self._inner_api_calls['collect'](requests, retry=retry, timeout=timeout, metadata=metadata)

    def chat(
            self,
            requests,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        This method, upon receiving a request on the stream, the same content will
        be passed  back on the stream. This method showcases bidirectional
        streaming rpcs.

        EXPERIMENTAL: This method interface might change in the future.

        Example:
            >>> from google import showcase_v1beta1
            >>>
            >>> client = showcase_v1beta1.EchoClient()
            >>>
            >>> request = {}
            >>>
            >>> requests = [request]
            >>> for element in client.chat(requests):
            ...     # process element
            ...     pass

        Args:
            requests (iterator[dict|google.showcase_v1beta1.proto.echo_pb2.EchoRequest]): The input objects. If a dict is provided, it must be of the
                same form as the protobuf message :class:`~google.showcase_v1beta1.types.EchoRequest`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            Iterable[~google.showcase_v1beta1.types.EchoResponse].

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'chat' not in self._inner_api_calls:
            self._inner_api_calls['chat'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.chat,
                default_retry=self._method_configs['Chat'].retry,
                default_timeout=self._method_configs['Chat'].timeout,
                client_info=self._client_info,
            )

        return self._inner_api_calls['chat'](requests, retry=retry, timeout=timeout, metadata=metadata)

    def wait(
            self,
            end_time=None,
            ttl=None,
            error=None,
            success=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        This method will wait the requested amount of and then return.
        This method showcases how a client handles a request timing out.

        Example:
            >>> from google import showcase_v1beta1
            >>>
            >>> client = showcase_v1beta1.EchoClient()
            >>>
            >>> response = client.wait()
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            end_time (Union[dict, ~google.showcase_v1beta1.types.Timestamp]): The time that this operation will complete.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.showcase_v1beta1.types.Timestamp`
            ttl (Union[dict, ~google.showcase_v1beta1.types.Duration]): The duration of this operation.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.showcase_v1beta1.types.Duration`
            error (Union[dict, ~google.showcase_v1beta1.types.Status]): The error that will be returned by the server. If this code is specified
                to be the OK rpc code, an empty response will be returned.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.showcase_v1beta1.types.Status`
            success (Union[dict, ~google.showcase_v1beta1.types.WaitResponse]): The response to be returned on operation completion.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.showcase_v1beta1.types.WaitResponse`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.showcase_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'wait' not in self._inner_api_calls:
            self._inner_api_calls['wait'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.wait,
                default_retry=self._method_configs['Wait'].retry,
                default_timeout=self._method_configs['Wait'].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            end_time=end_time,
            ttl=ttl,
        )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            error=error,
            success=success,
        )

        request = echo_pb2.WaitRequest(
            end_time=end_time,
            ttl=ttl,
            error=error,
            success=success,
        )
        operation = self._inner_api_calls['wait'](request, retry=retry, timeout=timeout, metadata=metadata)
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            echo_pb2.WaitResponse,
            metadata_type=echo_pb2.WaitMetadata,
        )

    def block(
            self,
            response_delay=None,
            error=None,
            success=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        This method will block (wait) for the requested amount of time
        and then return the response or error.
        This method showcases how a client handles delays or retries.

        Example:
            >>> from google import showcase_v1beta1
            >>>
            >>> client = showcase_v1beta1.EchoClient()
            >>>
            >>> response = client.block()

        Args:
            response_delay (Union[dict, ~google.showcase_v1beta1.types.Duration]): The amount of time to block before returning a response.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.showcase_v1beta1.types.Duration`
            error (Union[dict, ~google.showcase_v1beta1.types.Status]): The error that will be returned by the server. If this code is specified
                to be the OK rpc code, an empty response will be returned.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.showcase_v1beta1.types.Status`
            success (Union[dict, ~google.showcase_v1beta1.types.BlockResponse]): The response to be returned that will signify successful method call.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.showcase_v1beta1.types.BlockResponse`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.showcase_v1beta1.types.BlockResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'block' not in self._inner_api_calls:
            self._inner_api_calls['block'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.block,
                default_retry=self._method_configs['Block'].retry,
                default_timeout=self._method_configs['Block'].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            error=error,
            success=success,
        )

        request = echo_pb2.BlockRequest(
            response_delay=response_delay,
            error=error,
            success=success,
        )
        return self._inner_api_calls['block'](request, retry=retry, timeout=timeout, metadata=metadata)
