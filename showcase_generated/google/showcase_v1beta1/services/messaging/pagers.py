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

from google.showcase_v1beta1.types import messaging


class ListRoomsPager:
    """A pager for iterating through ``list_rooms`` requests.

    This class thinly wraps an initial
    :class:`~.messaging.ListRoomsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``rooms`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRooms`` requests and continue to iterate
    through the ``rooms`` field on the
    corresponding responses.

    All the usual :class:`~.messaging.ListRoomsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[[messaging.ListRoomsRequest],
                messaging.ListRoomsResponse],
            request: messaging.ListRoomsRequest,
            response: messaging.ListRoomsResponse):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.messaging.ListRoomsRequest`):
                The initial request object.
            response (:class:`~.messaging.ListRoomsResponse`):
                The initial response object.
        """
        self._method = method
        self._request = messaging.ListRoomsRequest(request)
        self._response = response

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[messaging.ListRoomsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request)
            yield self._response

    def __iter__(self) -> Iterable[messaging.Room]:
        for page in self.pages:
            yield from page.rooms

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListBlurbsPager:
    """A pager for iterating through ``list_blurbs`` requests.

    This class thinly wraps an initial
    :class:`~.messaging.ListBlurbsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``blurbs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBlurbs`` requests and continue to iterate
    through the ``blurbs`` field on the
    corresponding responses.

    All the usual :class:`~.messaging.ListBlurbsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[[messaging.ListBlurbsRequest],
                messaging.ListBlurbsResponse],
            request: messaging.ListBlurbsRequest,
            response: messaging.ListBlurbsResponse):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.messaging.ListBlurbsRequest`):
                The initial request object.
            response (:class:`~.messaging.ListBlurbsResponse`):
                The initial response object.
        """
        self._method = method
        self._request = messaging.ListBlurbsRequest(request)
        self._response = response

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[messaging.ListBlurbsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request)
            yield self._response

    def __iter__(self) -> Iterable[messaging.Blurb]:
        for page in self.pages:
            yield from page.blurbs

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
