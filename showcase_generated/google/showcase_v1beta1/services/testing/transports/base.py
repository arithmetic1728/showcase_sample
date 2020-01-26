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

import abc
import typing

from google import auth
from google.auth import credentials  # type: ignore

from google.protobuf import empty_pb2 as empty  # type: ignore
from google.showcase_v1beta1.types import testing


class TestingTransport(metaclass=abc.ABCMeta):
    """Abstract transport class for Testing."""

    AUTH_SCOPES = (
    )

    def __init__(
            self, *,
            host: str = 'localhost:7469',
            credentials: credentials.Credentials = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
        self._host = host

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials is None:
            credentials, _ = auth.default(scopes=self.AUTH_SCOPES)

        # Save the credentials.
        self._credentials = credentials

    @property
    def create_session(self) -> typing.Callable[
            [testing.CreateSessionRequest],
            testing.Session]:
        raise NotImplementedError

    @property
    def get_session(self) -> typing.Callable[
            [testing.GetSessionRequest],
            testing.Session]:
        raise NotImplementedError

    @property
    def list_sessions(self) -> typing.Callable[
            [testing.ListSessionsRequest],
            testing.ListSessionsResponse]:
        raise NotImplementedError

    @property
    def delete_session(self) -> typing.Callable[
            [testing.DeleteSessionRequest],
            empty.Empty]:
        raise NotImplementedError

    @property
    def report_session(self) -> typing.Callable[
            [testing.ReportSessionRequest],
            testing.ReportSessionResponse]:
        raise NotImplementedError

    @property
    def list_tests(self) -> typing.Callable[
            [testing.ListTestsRequest],
            testing.ListTestsResponse]:
        raise NotImplementedError

    @property
    def delete_test(self) -> typing.Callable[
            [testing.DeleteTestRequest],
            empty.Empty]:
        raise NotImplementedError

    @property
    def verify_test(self) -> typing.Callable[
            [testing.VerifyTestRequest],
            testing.VerifyTestResponse]:
        raise NotImplementedError


__all__ = (
    'TestingTransport',
)
