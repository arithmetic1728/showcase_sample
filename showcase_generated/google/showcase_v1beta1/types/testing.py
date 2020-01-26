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

import proto  # type: ignore


__protobuf__ = proto.module(
    package='google.showcase.v1beta1',
    manifest={
        'Session',
        'CreateSessionRequest',
        'GetSessionRequest',
        'ListSessionsRequest',
        'ListSessionsResponse',
        'DeleteSessionRequest',
        'ReportSessionRequest',
        'ReportSessionResponse',
        'Test',
        'Issue',
        'ListTestsRequest',
        'ListTestsResponse',
        'TestRun',
        'DeleteTestRequest',
        'VerifyTestRequest',
        'VerifyTestResponse',
    },
)


class Session(proto.Message):
    r"""A session is a suite of tests, generally being made in the
    context of testing code generation.

    A session defines tests it may expect, based on which version of
    the code generation spec is in use.

    Attributes:
        name (str):
            The name of the session. The ID must conform to ^[a-z]+$ If
            this is not provided, Showcase chooses one at random.
        version (~.testing.Session.Version):
            Required. The version this session is using.
    """
    class Version(proto.Enum):
        r"""The specification versions understood by Showcase."""
        VERSION_UNSPECIFIED = 0
        V1_LATEST = 1
        V1_0 = 2

    name = proto.Field(proto.STRING, number=1)
    version = proto.Field(proto.ENUM, number=2,
        enum=Version,
    )


class CreateSessionRequest(proto.Message):
    r"""The request for the CreateSession method.

    Attributes:
        session (~.testing.Session):
            The session to be created.
            Sessions are immutable once they are created
            (although they can be deleted).
    """

    session = proto.Field(proto.MESSAGE, number=1,
        message=Session,
    )


class GetSessionRequest(proto.Message):
    r"""The request for the GetSession method.

    Attributes:
        name (str):
            The session to be retrieved.
    """

    name = proto.Field(proto.STRING, number=1)


class ListSessionsRequest(proto.Message):
    r"""The request for the ListSessions method.

    Attributes:
        page_size (int):
            The maximum number of sessions to return per
            page.
        page_token (str):
            The page token, for retrieving subsequent
            pages.
    """

    page_size = proto.Field(proto.INT32, number=1)
    page_token = proto.Field(proto.STRING, number=2)


class ListSessionsResponse(proto.Message):
    r"""Response for the ListSessions method.

    Attributes:
        sessions (Sequence[~.testing.Session]):
            The sessions being returned.
        next_page_token (str):
            The next page token, if any.
            An empty value here means the last page has been
            reached.
    """

    @property
    def raw_page(self):
        return self

    sessions = proto.RepeatedField(proto.MESSAGE, number=1,
        message=Session,
    )
    next_page_token = proto.Field(proto.STRING, number=2)


class DeleteSessionRequest(proto.Message):
    r"""Request for the DeleteSession method.

    Attributes:
        name (str):
            The session to be deleted.
    """

    name = proto.Field(proto.STRING, number=1)


class ReportSessionRequest(proto.Message):
    r"""Request message for reporting on a session.

    Attributes:
        name (str):
            The session to be reported on.
    """

    name = proto.Field(proto.STRING, number=1)


class ReportSessionResponse(proto.Message):
    r"""Response message for reporting on a session.

    Attributes:
        result (~.testing.ReportSessionResponse.Result):
            The state of the report.
        test_runs (Sequence[~.testing.TestRun]):
            The test runs of this session.
    """
    class Result(proto.Enum):
        r"""The topline state of the report."""
        RESULT_UNSPECIFIED = 0
        PASSED = 1
        FAILED = 2
        INCOMPLETE = 3

    result = proto.Field(proto.ENUM, number=1,
        enum=Result,
    )
    test_runs = proto.RepeatedField(proto.MESSAGE, number=2,
        message='TestRun',
    )


class Test(proto.Message):
    r"""

    Attributes:
        name (str):
            The name of the test. The tests/\* portion of the names are
            hard-coded, and do not change from session to session.
        expectation_level (~.testing.Test.ExpectationLevel):
            The expectation level for this test.
        description (str):
            A description of the test.
        blueprints (Sequence[~.testing.Test.Blueprint]):
            The blueprints that will satisfy this test.
            There may be multiple blueprints that can signal
            to the server that this test case is being
            exercised. Although multiple blueprints are
            specified, only a single blueprint needs to be
            run to signal that the test case was exercised.
    """
    class ExpectationLevel(proto.Enum):
        r"""Whether or not a test is required, recommended, or optional."""
        EXPECTATION_LEVEL_UNSPECIFIED = 0
        REQUIRED = 1
        RECOMMENDED = 2
        OPTIONAL = 3

    class Blueprint(proto.Message):
        r"""A blueprint is an explicit definition of methods and requests
        that are needed to be made to test this specific test case.
        Ideally this would be represented by something more robust like
        CEL, but as of writing this, I am unsure if CEL is ready.

        Attributes:
            name (str):
                The name of this blueprint.
            description (str):
                A description of this blueprint.
            request (~.testing.Test.Blueprint.Invocation):
                The initial request to trigger this test.
            additional_requests (Sequence[~.testing.Test.Blueprint.Invocation]):
                An ordered list of method calls that can be
                called to trigger this test.
        """
        class Invocation(proto.Message):
            r"""A message representing a method invocation.

            Attributes:
                method (str):
                    The fully qualified name of the showcase
                    method to be invoked.
                serialized_request (bytes):
                    The request to be made if a specific request
                    is necessary.
            """

            method = proto.Field(proto.STRING, number=1)
            serialized_request = proto.Field(proto.BYTES, number=2)

        name = proto.Field(proto.STRING, number=1)
        description = proto.Field(proto.STRING, number=2)
        request = proto.Field(proto.MESSAGE, number=3,
            message='Test.Blueprint.Invocation',
        )
        additional_requests = proto.RepeatedField(proto.MESSAGE, number=4,
            message='Test.Blueprint.Invocation',
        )

    name = proto.Field(proto.STRING, number=1)
    expectation_level = proto.Field(proto.ENUM, number=2,
        enum=ExpectationLevel,
    )
    description = proto.Field(proto.STRING, number=3)
    blueprints = proto.RepeatedField(proto.MESSAGE, number=4,
        message=Blueprint,
    )


class Issue(proto.Message):
    r"""An issue found in the test.

    Attributes:
        type (~.testing.Issue.Type):
            The type of the issue.
        severity (~.testing.Issue.Severity):
            The severity of the issue.
        description (str):
            A description of the issue.
    """
    class Type(proto.Enum):
        r"""The different potential types of issues."""
        TYPE_UNSPECIFIED = 0
        SKIPPED = 1
        PENDING = 2
        INCORRECT_CONFIRMATION = 3

    class Severity(proto.Enum):
        r"""Severity levels."""
        SEVERITY_UNSPECIFIED = 0
        ERROR = 1
        WARNING = 2

    type = proto.Field(proto.ENUM, number=1,
        enum=Type,
    )
    severity = proto.Field(proto.ENUM, number=2,
        enum=Severity,
    )
    description = proto.Field(proto.STRING, number=3)


class ListTestsRequest(proto.Message):
    r"""The request for the ListTests method.

    Attributes:
        parent (str):
            The session.
        page_size (int):
            The maximum number of tests to return per
            page.
        page_token (str):
            The page token, for retrieving subsequent
            pages.
    """

    parent = proto.Field(proto.STRING, number=1)
    page_size = proto.Field(proto.INT32, number=2)
    page_token = proto.Field(proto.STRING, number=3)


class ListTestsResponse(proto.Message):
    r"""The response for the ListTests method.

    Attributes:
        tests (Sequence[~.testing.Test]):
            The tests being returned.
        next_page_token (str):
            The next page token, if any.
            An empty value here means the last page has been
            reached.
    """

    @property
    def raw_page(self):
        return self

    tests = proto.RepeatedField(proto.MESSAGE, number=1,
        message=Test,
    )
    next_page_token = proto.Field(proto.STRING, number=2)


class TestRun(proto.Message):
    r"""A TestRun is the result of running a Test.

    Attributes:
        test (str):
            The name of the test. The tests/\* portion of the names are
            hard-coded, and do not change from session to session.
        issue (~.testing.Issue):
            An issue found with the test run. If empty,
            this test run was successful.
    """

    test = proto.Field(proto.STRING, number=1)
    issue = proto.Field(proto.MESSAGE, number=2,
        message=Issue,
    )


class DeleteTestRequest(proto.Message):
    r"""Request message for deleting a test.

    Attributes:
        name (str):
            The test to be deleted.
    """

    name = proto.Field(proto.STRING, number=1)


class VerifyTestRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            The test to have an answer registered to it.
        answer (bytes):
            The answer from the test.
        answers (Sequence[bytes]):
            The answers from the test if multiple are to
            be checked
    """

    name = proto.Field(proto.STRING, number=1)
    answer = proto.Field(proto.BYTES, number=2)
    answers = proto.RepeatedField(proto.BYTES, number=3)


class VerifyTestResponse(proto.Message):
    r"""

    Attributes:
        issue (~.testing.Issue):
            An issue if check answer was unsuccessful.
            This will be empty if the check answer
            succeeded.
    """

    issue = proto.Field(proto.MESSAGE, number=1,
        message=Issue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
