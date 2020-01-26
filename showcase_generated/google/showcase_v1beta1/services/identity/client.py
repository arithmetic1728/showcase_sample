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

from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.showcase_v1beta1.services.identity import pagers
from google.showcase_v1beta1.types import identity

from .transports.base import IdentityTransport
from .transports.grpc import IdentityGrpcTransport


class IdentityClientMeta(type):
    """Metaclass for the Identity client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """
    _transport_registry = OrderedDict()  # type: Dict[str, Type[IdentityTransport]]
    _transport_registry['grpc'] = IdentityGrpcTransport

    def get_transport_class(cls,
            label: str = None,
            ) -> Type[IdentityTransport]:
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


class IdentityClient(metaclass=IdentityClientMeta):
    """A simple identity service."""

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
    def user_path(user_id: str,) -> str:
        """Return a fully-qualified user string."""
        return "users/{user_id}".format(user_id=user_id, )

    def __init__(self, *,
            credentials: credentials.Credentials = None,
            transport: Union[str, IdentityTransport] = None,
            client_options: ClientOptions = DEFAULT_OPTIONS,
            ) -> None:
        """Instantiate the identity client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.IdentityTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client.
        """
        if isinstance(client_options, dict):
            client_options = ClientOptions.from_dict(client_options)

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, IdentityTransport):
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

    def create_user(self,
            request: identity.CreateUserRequest = None,
            *,
            display_name: str = None,
            email: str = None,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> identity.User:
        r"""Creates a user.

        Args:
            request (:class:`~.identity.CreateUserRequest`):
                The request object. The request message for the
                google.showcase.v1beta1.Identity\CreateUser method.
            display_name (:class:`str`):
                The display_name of the user.
                This corresponds to the ``user.display_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            email (:class:`str`):
                The email address of the user.
                This corresponds to the ``user.email`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.identity.User:
                A user.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([display_name, email]):
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        request = identity.CreateUserRequest(request)
        if display_name is not None:
            request.user.display_name = display_name
        if email is not None:
            request.user.email = email

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.create_user,
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

    def get_user(self,
            request: identity.GetUserRequest = None,
            *,
            name: str = None,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> identity.User:
        r"""Retrieves the User with the given uri.

        Args:
            request (:class:`~.identity.GetUserRequest`):
                The request object. The request message for the
                google.showcase.v1beta1.Identity\GetUser method.
            name (:class:`str`):
                The resource name of the requested
                user.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.identity.User:
                A user.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([name]):
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        request = identity.GetUserRequest(request)
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.get_user,
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

    def update_user(self,
            request: identity.UpdateUserRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> identity.User:
        r"""Updates a user.

        Args:
            request (:class:`~.identity.UpdateUserRequest`):
                The request object. The request message for the
                google.showcase.v1beta1.Identity\UpdateUser method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.identity.User:
                A user.
        """
        # Create or coerce a protobuf request object.
        request = identity.UpdateUserRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.update_user,
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

    def delete_user(self,
            request: identity.DeleteUserRequest = None,
            *,
            name: str = None,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> None:
        r"""Deletes a user, their profile, and all of their
        authored messages.

        Args:
            request (:class:`~.identity.DeleteUserRequest`):
                The request object. The request message for the
                google.showcase.v1beta1.Identity\DeleteUser method.
            name (:class:`str`):
                The resource name of the user to
                delete.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([name]):
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        request = identity.DeleteUserRequest(request)
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.delete_user,
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

    def list_users(self,
            request: identity.ListUsersRequest = None,
            *,
            retry: retries.Retry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListUsersPager:
        r"""Lists all users.

        Args:
            request (:class:`~.identity.ListUsersRequest`):
                The request object. The request message for the
                google.showcase.v1beta1.Identity\ListUsers method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListUsersPager:
                The response message for the
                google.showcase.v1beta1.Identity\ListUsers
                method.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = identity.ListUsersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.list_users,
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
        response = pagers.ListUsersPager(
            method=rpc,
            request=request,
            response=response,
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
    'IdentityClient',
)
