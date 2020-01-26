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

from google.showcase_v1beta1.services.echo.client import EchoClient
from google.showcase_v1beta1.services.identity.client import IdentityClient
from google.showcase_v1beta1.services.messaging.client import MessagingClient
from google.showcase_v1beta1.services.testing.client import TestingClient
from google.showcase_v1beta1.types.echo import BlockRequest
from google.showcase_v1beta1.types.echo import BlockResponse
from google.showcase_v1beta1.types.echo import EchoRequest
from google.showcase_v1beta1.types.echo import EchoResponse
from google.showcase_v1beta1.types.echo import ExpandRequest
from google.showcase_v1beta1.types.echo import PagedExpandRequest
from google.showcase_v1beta1.types.echo import PagedExpandResponse
from google.showcase_v1beta1.types.echo import WaitMetadata
from google.showcase_v1beta1.types.echo import WaitRequest
from google.showcase_v1beta1.types.echo import WaitResponse
from google.showcase_v1beta1.types.identity import CreateUserRequest
from google.showcase_v1beta1.types.identity import DeleteUserRequest
from google.showcase_v1beta1.types.identity import GetUserRequest
from google.showcase_v1beta1.types.identity import ListUsersRequest
from google.showcase_v1beta1.types.identity import ListUsersResponse
from google.showcase_v1beta1.types.identity import UpdateUserRequest
from google.showcase_v1beta1.types.identity import User
from google.showcase_v1beta1.types.messaging import Blurb
from google.showcase_v1beta1.types.messaging import ConnectRequest
from google.showcase_v1beta1.types.messaging import CreateBlurbRequest
from google.showcase_v1beta1.types.messaging import CreateRoomRequest
from google.showcase_v1beta1.types.messaging import DeleteBlurbRequest
from google.showcase_v1beta1.types.messaging import DeleteRoomRequest
from google.showcase_v1beta1.types.messaging import GetBlurbRequest
from google.showcase_v1beta1.types.messaging import GetRoomRequest
from google.showcase_v1beta1.types.messaging import ListBlurbsRequest
from google.showcase_v1beta1.types.messaging import ListBlurbsResponse
from google.showcase_v1beta1.types.messaging import ListRoomsRequest
from google.showcase_v1beta1.types.messaging import ListRoomsResponse
from google.showcase_v1beta1.types.messaging import Room
from google.showcase_v1beta1.types.messaging import SearchBlurbsMetadata
from google.showcase_v1beta1.types.messaging import SearchBlurbsRequest
from google.showcase_v1beta1.types.messaging import SearchBlurbsResponse
from google.showcase_v1beta1.types.messaging import SendBlurbsResponse
from google.showcase_v1beta1.types.messaging import StreamBlurbsRequest
from google.showcase_v1beta1.types.messaging import StreamBlurbsResponse
from google.showcase_v1beta1.types.messaging import UpdateBlurbRequest
from google.showcase_v1beta1.types.messaging import UpdateRoomRequest
from google.showcase_v1beta1.types.testing import CreateSessionRequest
from google.showcase_v1beta1.types.testing import DeleteSessionRequest
from google.showcase_v1beta1.types.testing import DeleteTestRequest
from google.showcase_v1beta1.types.testing import GetSessionRequest
from google.showcase_v1beta1.types.testing import Issue
from google.showcase_v1beta1.types.testing import ListSessionsRequest
from google.showcase_v1beta1.types.testing import ListSessionsResponse
from google.showcase_v1beta1.types.testing import ListTestsRequest
from google.showcase_v1beta1.types.testing import ListTestsResponse
from google.showcase_v1beta1.types.testing import ReportSessionRequest
from google.showcase_v1beta1.types.testing import ReportSessionResponse
from google.showcase_v1beta1.types.testing import Session
from google.showcase_v1beta1.types.testing import Test
from google.showcase_v1beta1.types.testing import TestRun
from google.showcase_v1beta1.types.testing import VerifyTestRequest
from google.showcase_v1beta1.types.testing import VerifyTestResponse


__all__ = (
    'EchoClient',
    'IdentityClient',
    'MessagingClient',
    'TestingClient',
    'BlockRequest',
    'BlockResponse',
    'EchoRequest',
    'EchoResponse',
    'ExpandRequest',
    'PagedExpandRequest',
    'PagedExpandResponse',
    'WaitMetadata',
    'WaitRequest',
    'WaitResponse',
    'CreateUserRequest',
    'DeleteUserRequest',
    'GetUserRequest',
    'ListUsersRequest',
    'ListUsersResponse',
    'UpdateUserRequest',
    'User',
    'Blurb',
    'ConnectRequest',
    'CreateBlurbRequest',
    'CreateRoomRequest',
    'DeleteBlurbRequest',
    'DeleteRoomRequest',
    'GetBlurbRequest',
    'GetRoomRequest',
    'ListBlurbsRequest',
    'ListBlurbsResponse',
    'ListRoomsRequest',
    'ListRoomsResponse',
    'Room',
    'SearchBlurbsMetadata',
    'SearchBlurbsRequest',
    'SearchBlurbsResponse',
    'SendBlurbsResponse',
    'StreamBlurbsRequest',
    'StreamBlurbsResponse',
    'UpdateBlurbRequest',
    'UpdateRoomRequest',
    'CreateSessionRequest',
    'DeleteSessionRequest',
    'DeleteTestRequest',
    'GetSessionRequest',
    'Issue',
    'ListSessionsRequest',
    'ListSessionsResponse',
    'ListTestsRequest',
    'ListTestsResponse',
    'ReportSessionRequest',
    'ReportSessionResponse',
    'Session',
    'Test',
    'TestRun',
    'VerifyTestRequest',
    'VerifyTestResponse',
)
