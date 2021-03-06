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
from google.api_core import future
from google.api_core import operations_v1
from google.auth import credentials
from google.longrunning import operations_pb2
from google.oauth2 import service_account
from google.showcase_v1beta1.services.messaging import MessagingClient
from google.showcase_v1beta1.services.messaging import pagers
from google.showcase_v1beta1.services.messaging import transports
from google.showcase_v1beta1.types import messaging


def test_messaging_client_from_service_account_file():
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_file') as factory:
        factory.return_value = creds
        client = MessagingClient.from_service_account_file("dummy/file/path.json")
        assert client._transport._credentials == creds

        client = MessagingClient.from_service_account_json("dummy/file/path.json")
        assert client._transport._credentials == creds

        assert client._transport._host == 'localhost:7469'


def test_messaging_client_client_options():
    # Check the default options have their expected values.
    assert MessagingClient.DEFAULT_OPTIONS.api_endpoint == 'localhost:7469'

    # Check that options can be customized.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch('google.showcase_v1beta1.services.messaging.MessagingClient.get_transport_class') as gtc:
        transport = gtc.return_value = mock.MagicMock()
        client = MessagingClient(
            client_options=options
        )
        transport.assert_called_once_with(credentials=None, host="squid.clam.whelk")


def test_messaging_client_client_options_from_dict():
    with mock.patch('google.showcase_v1beta1.services.messaging.MessagingClient.get_transport_class') as gtc:
        transport = gtc.return_value = mock.MagicMock()
        client = MessagingClient(
            client_options={'api_endpoint': 'squid.clam.whelk'}
        )
        transport.assert_called_once_with(credentials=None, host="squid.clam.whelk")


def test_create_room(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.CreateRoomRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.create_room),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.Room(
            name='name_value',
            display_name='display_name_value',
            description='description_value',
        )
        response = client.create_room(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, messaging.Room)
    assert response.name == 'name_value'
    assert response.display_name == 'display_name_value'
    assert response.description == 'description_value'


def test_create_room_flattened():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.create_room),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.Room()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.create_room(
            display_name='display_name_value',
            description='description_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].room.display_name == 'display_name_value'
        assert args[0].room.description == 'description_value'


def test_create_room_flattened_error():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_room(
            messaging.CreateRoomRequest(),
            display_name='display_name_value',
            description='description_value',
        )


def test_get_room(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.GetRoomRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.get_room),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.Room(
            name='name_value',
            display_name='display_name_value',
            description='description_value',
        )
        response = client.get_room(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, messaging.Room)
    assert response.name == 'name_value'
    assert response.display_name == 'display_name_value'
    assert response.description == 'description_value'


def test_get_room_field_headers():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
  )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = messaging.GetRoomRequest(
        name='name/value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.get_room),
            '__call__') as call:
        call.return_value = messaging.Room()
        response = client.get_room(request)

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


def test_get_room_flattened():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.get_room),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.Room()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.get_room(
            name='name_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].name == 'name_value'


def test_get_room_flattened_error():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_room(
            messaging.GetRoomRequest(),
            name='name_value',
        )


def test_update_room(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.UpdateRoomRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.update_room),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.Room(
            name='name_value',
            display_name='display_name_value',
            description='description_value',
        )
        response = client.update_room(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, messaging.Room)
    assert response.name == 'name_value'
    assert response.display_name == 'display_name_value'
    assert response.description == 'description_value'


def test_delete_room(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.DeleteRoomRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.delete_room),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_room(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_room_flattened():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.delete_room),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.delete_room(
            name='name_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].name == 'name_value'


def test_delete_room_flattened_error():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_room(
            messaging.DeleteRoomRequest(),
            name='name_value',
        )


def test_list_rooms(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.ListRoomsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_rooms),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.ListRoomsResponse(
            next_page_token='next_page_token_value',
        )
        response = client.list_rooms(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListRoomsPager)
    assert response.next_page_token == 'next_page_token_value'


def test_list_rooms_pager():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_rooms),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            messaging.ListRoomsResponse(
                rooms=[
                    messaging.Room(),
                    messaging.Room(),
                    messaging.Room(),
                ],
                next_page_token='abc',
            ),
            messaging.ListRoomsResponse(
                rooms=[],
                next_page_token='def',
            ),
            messaging.ListRoomsResponse(
                rooms=[
                    messaging.Room(),
                ],
                next_page_token='ghi',
            ),
            messaging.ListRoomsResponse(
                rooms=[
                    messaging.Room(),
                    messaging.Room(),
                ],
            ),
            RuntimeError,
        )
        results = [i for i in client.list_rooms(
            request={},
        )]
        assert len(results) == 6
        assert all([isinstance(i, messaging.Room)
                    for i in results])

def test_list_rooms_pages():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_rooms),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            messaging.ListRoomsResponse(
                rooms=[
                    messaging.Room(),
                    messaging.Room(),
                    messaging.Room(),
                ],
                next_page_token='abc',
            ),
            messaging.ListRoomsResponse(
                rooms=[],
                next_page_token='def',
            ),
            messaging.ListRoomsResponse(
                rooms=[
                    messaging.Room(),
                ],
                next_page_token='ghi',
            ),
            messaging.ListRoomsResponse(
                rooms=[
                    messaging.Room(),
                    messaging.Room(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_rooms(request={}).pages)
        for page, token in zip(pages, ['abc','def','ghi', '']):
            assert page.raw_page.next_page_token == token


def test_create_blurb(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.CreateBlurbRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.create_blurb),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.Blurb(
            name='name_value',
            user='user_value',
            text='text_value',
            image=b'image_blob',
        )
        response = client.create_blurb(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, messaging.Blurb)
    assert response.name == 'name_value'
    assert response.user == 'user_value'
    assert response.text == 'text_value'
    assert response.image == b'image_blob'


def test_create_blurb_flattened():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.create_blurb),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.Blurb()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.create_blurb(
            parent='parent_value',
            user='user_value',
            text='text_value',
            image=b'image_blob',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].parent == 'parent_value'
        assert args[0].blurb.user == 'user_value'
        assert args[0].blurb.text == 'text_value'
        assert args[0].blurb.image == b'image_blob'


def test_create_blurb_flattened_error():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_blurb(
            messaging.CreateBlurbRequest(),
            parent='parent_value',
            user='user_value',
            text='text_value',
            image=b'image_blob',
        )


def test_get_blurb(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.GetBlurbRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.get_blurb),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.Blurb(
            name='name_value',
            user='user_value',
            text='text_value',
            image=b'image_blob',
        )
        response = client.get_blurb(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, messaging.Blurb)
    assert response.name == 'name_value'
    assert response.user == 'user_value'
    assert response.text == 'text_value'
    assert response.image == b'image_blob'


def test_get_blurb_field_headers():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
  )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = messaging.GetBlurbRequest(
        name='name/value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.get_blurb),
            '__call__') as call:
        call.return_value = messaging.Blurb()
        response = client.get_blurb(request)

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


def test_get_blurb_flattened():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.get_blurb),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.Blurb()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.get_blurb(
            name='name_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].name == 'name_value'


def test_get_blurb_flattened_error():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_blurb(
            messaging.GetBlurbRequest(),
            name='name_value',
        )


def test_update_blurb(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.UpdateBlurbRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.update_blurb),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.Blurb(
            name='name_value',
            user='user_value',
            text='text_value',
            image=b'image_blob',
        )
        response = client.update_blurb(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, messaging.Blurb)
    assert response.name == 'name_value'
    assert response.user == 'user_value'
    assert response.text == 'text_value'
    assert response.image == b'image_blob'


def test_delete_blurb(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.DeleteBlurbRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.delete_blurb),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_blurb(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_blurb_flattened():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.delete_blurb),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.delete_blurb(
            name='name_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].name == 'name_value'


def test_delete_blurb_flattened_error():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_blurb(
            messaging.DeleteBlurbRequest(),
            name='name_value',
        )


def test_list_blurbs(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.ListBlurbsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_blurbs),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.ListBlurbsResponse(
            next_page_token='next_page_token_value',
        )
        response = client.list_blurbs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListBlurbsPager)
    assert response.next_page_token == 'next_page_token_value'


def test_list_blurbs_field_headers():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
  )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = messaging.ListBlurbsRequest(
        parent='parent/value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_blurbs),
            '__call__') as call:
        call.return_value = messaging.ListBlurbsResponse()
        response = client.list_blurbs(request)

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


def test_list_blurbs_flattened():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_blurbs),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.ListBlurbsResponse()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.list_blurbs(
            parent='parent_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].parent == 'parent_value'


def test_list_blurbs_flattened_error():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_blurbs(
            messaging.ListBlurbsRequest(),
            parent='parent_value',
        )


def test_list_blurbs_pager():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_blurbs),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            messaging.ListBlurbsResponse(
                blurbs=[
                    messaging.Blurb(),
                    messaging.Blurb(),
                    messaging.Blurb(),
                ],
                next_page_token='abc',
            ),
            messaging.ListBlurbsResponse(
                blurbs=[],
                next_page_token='def',
            ),
            messaging.ListBlurbsResponse(
                blurbs=[
                    messaging.Blurb(),
                ],
                next_page_token='ghi',
            ),
            messaging.ListBlurbsResponse(
                blurbs=[
                    messaging.Blurb(),
                    messaging.Blurb(),
                ],
            ),
            RuntimeError,
        )
        results = [i for i in client.list_blurbs(
            request={},
        )]
        assert len(results) == 6
        assert all([isinstance(i, messaging.Blurb)
                    for i in results])

def test_list_blurbs_pages():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.list_blurbs),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            messaging.ListBlurbsResponse(
                blurbs=[
                    messaging.Blurb(),
                    messaging.Blurb(),
                    messaging.Blurb(),
                ],
                next_page_token='abc',
            ),
            messaging.ListBlurbsResponse(
                blurbs=[],
                next_page_token='def',
            ),
            messaging.ListBlurbsResponse(
                blurbs=[
                    messaging.Blurb(),
                ],
                next_page_token='ghi',
            ),
            messaging.ListBlurbsResponse(
                blurbs=[
                    messaging.Blurb(),
                    messaging.Blurb(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_blurbs(request={}).pages)
        for page, token in zip(pages, ['abc','def','ghi', '']):
            assert page.raw_page.next_page_token == token


def test_search_blurbs(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.SearchBlurbsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.search_blurbs),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name='operations/spam')
        response = client.search_blurbs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_search_blurbs_flattened():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.search_blurbs),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name='operations/op')

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.search_blurbs(
            query='query_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].query == 'query_value'


def test_search_blurbs_flattened_error():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.search_blurbs(
            messaging.SearchBlurbsRequest(),
            query='query_value',
        )


def test_search_blurbs_raw_page_lro():
    response = messaging.SearchBlurbsResponse()
    assert response.raw_page is response


def test_stream_blurbs(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.StreamBlurbsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.stream_blurbs),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([messaging.StreamBlurbsResponse()])
        response = client.stream_blurbs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, messaging.StreamBlurbsResponse)


def test_send_blurbs(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.CreateBlurbRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.send_blurbs),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = messaging.SendBlurbsResponse(
            names=['names_value'],
        )
        response = client.send_blurbs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, messaging.SendBlurbsResponse)
    assert response.names == ['names_value']


def test_connect(transport: str = 'grpc'):
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = messaging.ConnectRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client._transport.connect),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([messaging.StreamBlurbsResponse()])
        response = client.connect(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, messaging.StreamBlurbsResponse)


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.MessagingGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = MessagingClient(
            credentials=credentials.AnonymousCredentials(),
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.MessagingGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    client = MessagingClient(transport=transport)
    assert client._transport is transport


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client._transport,
        transports.MessagingGrpcTransport,
    )


def test_messaging_base_transport():
    # Instantiate the base transport.
    transport = transports.MessagingTransport(
        credentials=credentials.AnonymousCredentials(),
    )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        'create_room',
        'get_room',
        'update_room',
        'delete_room',
        'list_rooms',
        'create_blurb',
        'get_blurb',
        'update_blurb',
        'delete_blurb',
        'list_blurbs',
        'search_blurbs',
        'stream_blurbs',
        'send_blurbs',
        'connect',
        )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    # Additionally, the LRO client (a property) should
    # also raise NotImplementedError
    with pytest.raises(NotImplementedError):
        transport.operations_client


def test_messaging_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, 'default') as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        client = MessagingClient()
        adc.assert_called_once_with(scopes=(
        ))


def test_messaging_host_no_port():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='localhost'),
        transport='grpc',
    )
    assert client._transport._host == 'localhost:443'


def test_messaging_host_with_port():
    client = MessagingClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='localhost:8000'),
        transport='grpc',
    )
    assert client._transport._host == 'localhost:8000'


def test_messaging_grpc_transport_channel():
    channel = grpc.insecure_channel('http://localhost/')
    transport = transports.MessagingGrpcTransport(
        channel=channel,
    )
    assert transport.grpc_channel is channel


def test_messaging_grpc_lro_client():
    client = MessagingClient(
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

def test_room_path():
  room_id = "squid"

  expected = "rooms/{room_id}".format(room_id=room_id, )
  actual = MessagingClient.room_path(room_id)
  assert expected == actual

def test_blurb_path():
  room_id = "squid"
  blurb_id = "clam"

  expected = "rooms/{room_id}/blurbs/{blurb_id}".format(room_id=room_id, blurb_id=blurb_id, )
  actual = MessagingClient.blurb_path(room_id, blurb_id)
  assert expected == actual
