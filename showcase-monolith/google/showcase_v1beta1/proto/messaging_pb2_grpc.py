# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.showcase_v1beta1.proto import messaging_pb2 as google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2


class MessagingStub(object):
  """A simple messaging service that implements chat rooms and profile posts.

  This messaging service showcases the features that API clients
  generated by gapic-generators implement.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateRoom = channel.unary_unary(
        '/google.showcase.v1beta1.Messaging/CreateRoom',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.CreateRoomRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.Room.FromString,
        )
    self.GetRoom = channel.unary_unary(
        '/google.showcase.v1beta1.Messaging/GetRoom',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.GetRoomRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.Room.FromString,
        )
    self.UpdateRoom = channel.unary_unary(
        '/google.showcase.v1beta1.Messaging/UpdateRoom',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.UpdateRoomRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.Room.FromString,
        )
    self.DeleteRoom = channel.unary_unary(
        '/google.showcase.v1beta1.Messaging/DeleteRoom',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.DeleteRoomRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListRooms = channel.unary_unary(
        '/google.showcase.v1beta1.Messaging/ListRooms',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.ListRoomsRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.ListRoomsResponse.FromString,
        )
    self.CreateBlurb = channel.unary_unary(
        '/google.showcase.v1beta1.Messaging/CreateBlurb',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.CreateBlurbRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.Blurb.FromString,
        )
    self.GetBlurb = channel.unary_unary(
        '/google.showcase.v1beta1.Messaging/GetBlurb',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.GetBlurbRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.Blurb.FromString,
        )
    self.UpdateBlurb = channel.unary_unary(
        '/google.showcase.v1beta1.Messaging/UpdateBlurb',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.UpdateBlurbRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.Blurb.FromString,
        )
    self.DeleteBlurb = channel.unary_unary(
        '/google.showcase.v1beta1.Messaging/DeleteBlurb',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.DeleteBlurbRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListBlurbs = channel.unary_unary(
        '/google.showcase.v1beta1.Messaging/ListBlurbs',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.ListBlurbsRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.ListBlurbsResponse.FromString,
        )
    self.SearchBlurbs = channel.unary_unary(
        '/google.showcase.v1beta1.Messaging/SearchBlurbs',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.SearchBlurbsRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.StreamBlurbs = channel.unary_stream(
        '/google.showcase.v1beta1.Messaging/StreamBlurbs',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.StreamBlurbsRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.StreamBlurbsResponse.FromString,
        )
    self.SendBlurbs = channel.stream_unary(
        '/google.showcase.v1beta1.Messaging/SendBlurbs',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.CreateBlurbRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.SendBlurbsResponse.FromString,
        )
    self.Connect = channel.stream_stream(
        '/google.showcase.v1beta1.Messaging/Connect',
        request_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.ConnectRequest.SerializeToString,
        response_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.StreamBlurbsResponse.FromString,
        )


class MessagingServicer(object):
  """A simple messaging service that implements chat rooms and profile posts.

  This messaging service showcases the features that API clients
  generated by gapic-generators implement.
  """

  def CreateRoom(self, request, context):
    """Creates a room.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRoom(self, request, context):
    """Retrieves the Room with the given resource name.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateRoom(self, request, context):
    """Updates a room.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteRoom(self, request, context):
    """Deletes a room and all of its blurbs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListRooms(self, request, context):
    """Lists all chat rooms.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateBlurb(self, request, context):
    """Creates a blurb. If the parent is a room, the blurb is understood to be a
    message in that room. If the parent is a profile, the blurb is understood
    to be a post on the profile.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlurb(self, request, context):
    """Retrieves the Blurb with the given resource name.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateBlurb(self, request, context):
    """Updates a blurb.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteBlurb(self, request, context):
    """Deletes a blurb.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListBlurbs(self, request, context):
    """Lists blurbs for a specific chat room or user profile depending on the
    parent resource name.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchBlurbs(self, request, context):
    """This method searches through all blurbs across all rooms and profiles
    for blurbs containing to words found in the query. Only posts that
    contain an exact match of a queried word will be returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamBlurbs(self, request, context):
    """This returns a stream that emits the blurbs that are created for a
    particular chat room or user profile.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendBlurbs(self, request_iterator, context):
    """This is a stream to create multiple blurbs. If an invalid blurb is
    requested to be created, the stream will close with an error.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Connect(self, request_iterator, context):
    """This method starts a bidirectional stream that receives all blurbs that
    are being created after the stream has started and sends requests to create
    blurbs. If an invalid blurb is requested to be created, the stream will
    close with an error.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MessagingServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateRoom': grpc.unary_unary_rpc_method_handler(
          servicer.CreateRoom,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.CreateRoomRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.Room.SerializeToString,
      ),
      'GetRoom': grpc.unary_unary_rpc_method_handler(
          servicer.GetRoom,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.GetRoomRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.Room.SerializeToString,
      ),
      'UpdateRoom': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateRoom,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.UpdateRoomRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.Room.SerializeToString,
      ),
      'DeleteRoom': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteRoom,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.DeleteRoomRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListRooms': grpc.unary_unary_rpc_method_handler(
          servicer.ListRooms,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.ListRoomsRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.ListRoomsResponse.SerializeToString,
      ),
      'CreateBlurb': grpc.unary_unary_rpc_method_handler(
          servicer.CreateBlurb,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.CreateBlurbRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.Blurb.SerializeToString,
      ),
      'GetBlurb': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlurb,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.GetBlurbRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.Blurb.SerializeToString,
      ),
      'UpdateBlurb': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateBlurb,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.UpdateBlurbRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.Blurb.SerializeToString,
      ),
      'DeleteBlurb': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteBlurb,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.DeleteBlurbRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListBlurbs': grpc.unary_unary_rpc_method_handler(
          servicer.ListBlurbs,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.ListBlurbsRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.ListBlurbsResponse.SerializeToString,
      ),
      'SearchBlurbs': grpc.unary_unary_rpc_method_handler(
          servicer.SearchBlurbs,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.SearchBlurbsRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'StreamBlurbs': grpc.unary_stream_rpc_method_handler(
          servicer.StreamBlurbs,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.StreamBlurbsRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.StreamBlurbsResponse.SerializeToString,
      ),
      'SendBlurbs': grpc.stream_unary_rpc_method_handler(
          servicer.SendBlurbs,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.CreateBlurbRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.SendBlurbsResponse.SerializeToString,
      ),
      'Connect': grpc.stream_stream_rpc_method_handler(
          servicer.Connect,
          request_deserializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.ConnectRequest.FromString,
          response_serializer=google_dot_showcase__v1beta1_dot_proto_dot_messaging__pb2.StreamBlurbsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.showcase.v1beta1.Messaging', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))