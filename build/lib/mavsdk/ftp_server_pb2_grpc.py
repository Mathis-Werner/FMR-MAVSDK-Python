# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import ftp_server_pb2 as ftp__server_dot_ftp__server__pb2

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
        + f' but the generated code in ftp_server/ftp_server_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FtpServerServiceStub(object):
    """Provide files or directories to transfer.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetRootDir = channel.unary_unary(
                '/mavsdk.rpc.ftp_server.FtpServerService/SetRootDir',
                request_serializer=ftp__server_dot_ftp__server__pb2.SetRootDirRequest.SerializeToString,
                response_deserializer=ftp__server_dot_ftp__server__pb2.SetRootDirResponse.FromString,
                _registered_method=True)


class FtpServerServiceServicer(object):
    """Provide files or directories to transfer.
    """

    def SetRootDir(self, request, context):
        """
        Set root directory.
        
        This is the directory that can then be accessed by a client.
        The directory needs to exist when this is called.
        The permissions are the same as the file permission for the user running the server.
        The root directory can't be changed while an FTP process is in progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FtpServerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetRootDir': grpc.unary_unary_rpc_method_handler(
                    servicer.SetRootDir,
                    request_deserializer=ftp__server_dot_ftp__server__pb2.SetRootDirRequest.FromString,
                    response_serializer=ftp__server_dot_ftp__server__pb2.SetRootDirResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.ftp_server.FtpServerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('mavsdk.rpc.ftp_server.FtpServerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FtpServerService(object):
    """Provide files or directories to transfer.
    """

    @staticmethod
    def SetRootDir(request,
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
            '/mavsdk.rpc.ftp_server.FtpServerService/SetRootDir',
            ftp__server_dot_ftp__server__pb2.SetRootDirRequest.SerializeToString,
            ftp__server_dot_ftp__server__pb2.SetRootDirResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
