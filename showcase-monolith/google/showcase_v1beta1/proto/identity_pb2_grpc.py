# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.showcase_v1beta1.proto import identity_pb2 as google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2


class IdentityStub(object):
  """A simple identity service.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateUser = channel.unary_unary(
        '/google.showcase.v1beta1.Identity/CreateUser',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.CreateUserRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.User.FromString,
        )
    self.GetUser = channel.unary_unary(
        '/google.showcase.v1beta1.Identity/GetUser',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.GetUserRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.User.FromString,
        )
    self.UpdateUser = channel.unary_unary(
        '/google.showcase.v1beta1.Identity/UpdateUser',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.UpdateUserRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.User.FromString,
        )
    self.DeleteUser = channel.unary_unary(
        '/google.showcase.v1beta1.Identity/DeleteUser',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.DeleteUserRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListUsers = channel.unary_unary(
        '/google.showcase.v1beta1.Identity/ListUsers',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.ListUsersRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.ListUsersResponse.FromString,
        )


class IdentityServicer(object):
  """A simple identity service.
  """

  def CreateUser(self, request, context):
    """Creates a user.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUser(self, request, context):
    """Retrieves the User with the given uri.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateUser(self, request, context):
    """Updates a user.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteUser(self, request, context):
    """Deletes a user, their profile, and all of their authored messages.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListUsers(self, request, context):
    """Lists all users.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IdentityServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateUser': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUser,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.CreateUserRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.User.SerializeToString,
      ),
      'GetUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetUser,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.GetUserRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.User.SerializeToString,
      ),
      'UpdateUser': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateUser,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.UpdateUserRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.User.SerializeToString,
      ),
      'DeleteUser': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteUser,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.DeleteUserRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListUsers': grpc.unary_unary_rpc_method_handler(
          servicer.ListUsers,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.ListUsersRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_identity__pb2.ListUsersResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.showcase.v1beta1.Identity', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
