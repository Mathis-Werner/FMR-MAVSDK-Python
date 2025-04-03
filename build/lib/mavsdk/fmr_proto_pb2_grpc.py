# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import fmr_proto_pb2 as fmr__proto_dot_fmr__proto__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in fmr_proto/fmr_proto_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FmrServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribePosition = channel.unary_stream(
                '/mavsdk.rpc.camera.FmrService/SubscribePosition',
                request_serializer=fmr__proto_dot_fmr__proto__pb2.SubscribeGPSInfoRequest.SerializeToString,
                response_deserializer=fmr__proto_dot_fmr__proto__pb2.GPSInfoResponse.FromString,
                _registered_method=True)
        self.SetRatePosition = channel.unary_unary(
                '/mavsdk.rpc.camera.FmrService/SetRatePosition',
                request_serializer=fmr__proto_dot_fmr__proto__pb2.SetRateGPSInfoRequest.SerializeToString,
                response_deserializer=fmr__proto_dot_fmr__proto__pb2.SetRateGPSInfoResponse.FromString,
                _registered_method=True)


class FmrServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SubscribePosition(self, request, context):
        """Subscribe to 'position' updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetRatePosition(self, request, context):
        """Set rate to 'position' updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FmrServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribePosition': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribePosition,
                    request_deserializer=fmr__proto_dot_fmr__proto__pb2.SubscribeGPSInfoRequest.FromString,
                    response_serializer=fmr__proto_dot_fmr__proto__pb2.GPSInfoResponse.SerializeToString,
            ),
            'SetRatePosition': grpc.unary_unary_rpc_method_handler(
                    servicer.SetRatePosition,
                    request_deserializer=fmr__proto_dot_fmr__proto__pb2.SetRateGPSInfoRequest.FromString,
                    response_serializer=fmr__proto_dot_fmr__proto__pb2.SetRateGPSInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.camera.FmrService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('mavsdk.rpc.camera.FmrService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FmrService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SubscribePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/mavsdk.rpc.camera.FmrService/SubscribePosition',
            fmr__proto_dot_fmr__proto__pb2.SubscribeGPSInfoRequest.SerializeToString,
            fmr__proto_dot_fmr__proto__pb2.GPSInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetRatePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mavsdk.rpc.camera.FmrService/SetRatePosition',
            fmr__proto_dot_fmr__proto__pb2.SetRateGPSInfoRequest.SerializeToString,
            fmr__proto_dot_fmr__proto__pb2.SetRateGPSInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
