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

from collections import OrderedDict
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions # type: ignore
from google.api_core import exceptions                 # type: ignore
from google.api_core import gapic_v1                   # type: ignore
from google.api_core import retry as retries           # type: ignore
from google.auth import credentials                    # type: ignore
from google.oauth2 import service_account              # type: ignore

from google.showcase_v1beta1.services.testing import pagers
from google.showcase_v1beta1.types import testing

from .transports.base import TestingTransport
from .transports.grpc import TestingGrpcTransport


class TestingClientMeta(type):
    """Metaclass for the Testing client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """
    _transport_registry = OrderedDict()  # type: Dict[str, Type[TestingTransport]]
    _transport_registry['grpc'] = TestingGrpcTransport

    def get_transport_class(cls,
            label: str = None,
            ) -> Type[TestingTransport]:
        """Return an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class TestingClient(metaclass=TestingClientMeta):
    """A service to facilitate running discrete sets of tests
    against Showcase.
    """

    DEFAULT_OPTIONS = ClientOptions.ClientOptions(api_endpoint='localhost:7469')

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            {@api.name}: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename)
        kwargs['credentials'] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @staticmethod
    def session_path(session: str,) -> str:
        """Return a fully-qualified session string."""
        return "sessions/{session}".format(session=session, )

    def __init__(self, *,
            credentials: credentials.Credentials = None,
            transport: Union[str, TestingTransport] = None,
            client_options: ClientOptions = DEFAULT_OPTIONS,
            ) -> None:
        """Instantiate the testing client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.TestingTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client.
        """
        if isinstance(client_options, dict):
            client_options = ClientOptions.from_dict(client_options)

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, TestingTransport):
            if credentials:
                raise ValueError('When providing a transport instance, '
                                 'provide its credentials directly.')
            self._transport = transport
        else:
            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                host=client_options.api_endpoint or 'localhost:7469',
            )

    def create_session(self,
            request: testing.CreateSessionRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> testing.Session:
        r"""Creates a new testing session.

        Args:
            request (:class:`~.testing.CreateSessionRequest`):
                The request object. The request for the CreateSession
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.testing.Session:
                A session is a suite of tests,
                generally being made in the context of
                testing code generation.
                A session defines tests it may expect,
                based on which version of the code
                generation spec is in use.

        """
        # Create or coerce a protobuf request object.
        request = testing.CreateSessionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.create_session,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_session(self,
            request: testing.GetSessionRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> testing.Session:
        r"""Gets a testing session.

        Args:
            request (:class:`~.testing.GetSessionRequest`):
                The request object. The request for the GetSession
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.testing.Session:
                A session is a suite of tests,
                generally being made in the context of
                testing code generation.
                A session defines tests it may expect,
                based on which version of the code
                generation spec is in use.

        """
        # Create or coerce a protobuf request object.
        request = testing.GetSessionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.get_session,
            default_timeout=None,
            client_info=_client_info,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ('name', request.name),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_sessions(self,
            request: testing.ListSessionsRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListSessionsPager:
        r"""Lists the current test sessions.

        Args:
            request (:class:`~.testing.ListSessionsRequest`):
                The request object. The request for the ListSessions
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListSessionsPager:
                Response for the ListSessions method.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = testing.ListSessionsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.list_sessions,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListSessionsPager(
            method=rpc,
            request=request,
            response=response,
        )

        # Done; return the response.
        return response

    def delete_session(self,
            request: testing.DeleteSessionRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> None:
        r"""Delete a test session.

        Args:
            request (:class:`~.testing.DeleteSessionRequest`):
                The request object. Request for the DeleteSession
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        request = testing.DeleteSessionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.delete_session,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def report_session(self,
            request: testing.ReportSessionRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> testing.ReportSessionResponse:
        r"""Report on the status of a session.
        This generates a report detailing which tests have been
        completed, and an overall rollup.

        Args:
            request (:class:`~.testing.ReportSessionRequest`):
                The request object. Request message for reporting on a
                session.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.testing.ReportSessionResponse:
                Response message for reporting on a
                session.

        """
        # Create or coerce a protobuf request object.
        request = testing.ReportSessionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.report_session,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_tests(self,
            request: testing.ListTestsRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListTestsPager:
        r"""List the tests of a sessesion.

        Args:
            request (:class:`~.testing.ListTestsRequest`):
                The request object. The request for the ListTests
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListTestsPager:
                The response for the ListTests
                method.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = testing.ListTestsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.list_tests,
            default_timeout=None,
            client_info=_client_info,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ('parent', request.parent),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListTestsPager(
            method=rpc,
            request=request,
            response=response,
        )

        # Done; return the response.
        return response

    def delete_test(self,
            request: testing.DeleteTestRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> None:
        r"""Explicitly decline to implement a test.

        This removes the test from subsequent ``ListTests`` calls, and
        attempting to do the test will error.

        This method will error if attempting to delete a required test.

        Args:
            request (:class:`~.testing.DeleteTestRequest`):
                The request object. Request message for deleting a test.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        request = testing.DeleteTestRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.delete_test,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def verify_test(self,
            request: testing.VerifyTestRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> testing.VerifyTestResponse:
        r"""Register a response to a test.
        In cases where a test involves registering a final
        answer at the end of the test, this method provides the
        means to do so.

        Args:
            request (:class:`~.testing.VerifyTestRequest`):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.testing.VerifyTestResponse:

        """
        # Create or coerce a protobuf request object.
        request = testing.VerifyTestRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.verify_test,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response





try:
    _client_info = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'google-showcase',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    _client_info = gapic_v1.client_info.ClientInfo()


__all__ = (
    'TestingClient',
)
