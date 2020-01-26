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

from typing import Any, Callable, Iterable

from google.showcase_v1beta1.types import testing


class ListSessionsPager:
    """A pager for iterating through ``list_sessions`` requests.

    This class thinly wraps an initial
    :class:`~.testing.ListSessionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``sessions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSessions`` requests and continue to iterate
    through the ``sessions`` field on the
    corresponding responses.

    All the usual :class:`~.testing.ListSessionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[[testing.ListSessionsRequest],
                testing.ListSessionsResponse],
            request: testing.ListSessionsRequest,
            response: testing.ListSessionsResponse):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.testing.ListSessionsRequest`):
                The initial request object.
            response (:class:`~.testing.ListSessionsResponse`):
                The initial response object.
        """
        self._method = method
        self._request = testing.ListSessionsRequest(request)
        self._response = response

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[testing.ListSessionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request)
            yield self._response

    def __iter__(self) -> Iterable[testing.Session]:
        for page in self.pages:
            yield from page.sessions

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListTestsPager:
    """A pager for iterating through ``list_tests`` requests.

    This class thinly wraps an initial
    :class:`~.testing.ListTestsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``tests`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTests`` requests and continue to iterate
    through the ``tests`` field on the
    corresponding responses.

    All the usual :class:`~.testing.ListTestsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[[testing.ListTestsRequest],
                testing.ListTestsResponse],
            request: testing.ListTestsRequest,
            response: testing.ListTestsResponse):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.testing.ListTestsRequest`):
                The initial request object.
            response (:class:`~.testing.ListTestsResponse`):
                The initial response object.
        """
        self._method = method
        self._request = testing.ListTestsRequest(request)
        self._response = response

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[testing.ListTestsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request)
            yield self._response

    def __iter__(self) -> Iterable[testing.Test]:
        for page in self.pages:
            yield from page.tests

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
