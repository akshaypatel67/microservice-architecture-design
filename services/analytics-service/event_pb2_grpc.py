# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import event_pb2 as event__pb2


class EventServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateEvent = channel.unary_unary(
                '/event.EventService/CreateEvent',
                request_serializer=event__pb2.Event.SerializeToString,
                response_deserializer=event__pb2.Response.FromString,
                )
        self.GetEvent = channel.unary_unary(
                '/event.EventService/GetEvent',
                request_serializer=event__pb2.EventId.SerializeToString,
                response_deserializer=event__pb2.Event.FromString,
                )
        self.UpdateEvent = channel.unary_unary(
                '/event.EventService/UpdateEvent',
                request_serializer=event__pb2.Event.SerializeToString,
                response_deserializer=event__pb2.Response.FromString,
                )
        self.DeleteEvent = channel.unary_unary(
                '/event.EventService/DeleteEvent',
                request_serializer=event__pb2.EventId.SerializeToString,
                response_deserializer=event__pb2.Response.FromString,
                )
        self.ListEvents = channel.unary_stream(
                '/event.EventService/ListEvents',
                request_serializer=event__pb2.Empty.SerializeToString,
                response_deserializer=event__pb2.Event.FromString,
                )


class EventServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEvents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEvent,
                    request_deserializer=event__pb2.Event.FromString,
                    response_serializer=event__pb2.Response.SerializeToString,
            ),
            'GetEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEvent,
                    request_deserializer=event__pb2.EventId.FromString,
                    response_serializer=event__pb2.Event.SerializeToString,
            ),
            'UpdateEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEvent,
                    request_deserializer=event__pb2.Event.FromString,
                    response_serializer=event__pb2.Response.SerializeToString,
            ),
            'DeleteEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteEvent,
                    request_deserializer=event__pb2.EventId.FromString,
                    response_serializer=event__pb2.Response.SerializeToString,
            ),
            'ListEvents': grpc.unary_stream_rpc_method_handler(
                    servicer.ListEvents,
                    request_deserializer=event__pb2.Empty.FromString,
                    response_serializer=event__pb2.Event.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'event.EventService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EventService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event.EventService/CreateEvent',
            event__pb2.Event.SerializeToString,
            event__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event.EventService/GetEvent',
            event__pb2.EventId.SerializeToString,
            event__pb2.Event.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event.EventService/UpdateEvent',
            event__pb2.Event.SerializeToString,
            event__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event.EventService/DeleteEvent',
            event__pb2.EventId.SerializeToString,
            event__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/event.EventService/ListEvents',
            event__pb2.Empty.SerializeToString,
            event__pb2.Event.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)