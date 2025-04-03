# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import offboard_pb2 as offboard_dot_offboard__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in offboard/offboard_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class OffboardServiceStub(object):
    """*
    Control a drone with position, velocity, attitude or motor commands.

    The module is called offboard because the commands can be sent from external sources
    as opposed to onboard control right inside the autopilot "board".

    Client code must specify a setpoint before starting offboard mode.
    Mavsdk automatically sends setpoints at 20Hz (PX4 Offboard mode requires that setpoints
    are minimally sent at 2Hz).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Start = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/Start',
                request_serializer=offboard_dot_offboard__pb2.StartRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.StartResponse.FromString,
                _registered_method=True)
        self.Stop = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/Stop',
                request_serializer=offboard_dot_offboard__pb2.StopRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.StopResponse.FromString,
                _registered_method=True)
        self.IsActive = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/IsActive',
                request_serializer=offboard_dot_offboard__pb2.IsActiveRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.IsActiveResponse.FromString,
                _registered_method=True)
        self.SetAttitude = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/SetAttitude',
                request_serializer=offboard_dot_offboard__pb2.SetAttitudeRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.SetAttitudeResponse.FromString,
                _registered_method=True)
        self.SetActuatorControl = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/SetActuatorControl',
                request_serializer=offboard_dot_offboard__pb2.SetActuatorControlRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.SetActuatorControlResponse.FromString,
                _registered_method=True)
        self.SetAttitudeRate = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/SetAttitudeRate',
                request_serializer=offboard_dot_offboard__pb2.SetAttitudeRateRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.SetAttitudeRateResponse.FromString,
                _registered_method=True)
        self.SetPositionNed = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/SetPositionNed',
                request_serializer=offboard_dot_offboard__pb2.SetPositionNedRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.SetPositionNedResponse.FromString,
                _registered_method=True)
        self.SetPositionGlobal = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/SetPositionGlobal',
                request_serializer=offboard_dot_offboard__pb2.SetPositionGlobalRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.SetPositionGlobalResponse.FromString,
                _registered_method=True)
        self.SetVelocityBody = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/SetVelocityBody',
                request_serializer=offboard_dot_offboard__pb2.SetVelocityBodyRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.SetVelocityBodyResponse.FromString,
                _registered_method=True)
        self.SetVelocityNed = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/SetVelocityNed',
                request_serializer=offboard_dot_offboard__pb2.SetVelocityNedRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.SetVelocityNedResponse.FromString,
                _registered_method=True)
        self.SetPositionVelocityNed = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/SetPositionVelocityNed',
                request_serializer=offboard_dot_offboard__pb2.SetPositionVelocityNedRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.SetPositionVelocityNedResponse.FromString,
                _registered_method=True)
        self.SetPositionVelocityAccelerationNed = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/SetPositionVelocityAccelerationNed',
                request_serializer=offboard_dot_offboard__pb2.SetPositionVelocityAccelerationNedRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.SetPositionVelocityAccelerationNedResponse.FromString,
                _registered_method=True)
        self.SetAccelerationNed = channel.unary_unary(
                '/mavsdk.rpc.offboard.OffboardService/SetAccelerationNed',
                request_serializer=offboard_dot_offboard__pb2.SetAccelerationNedRequest.SerializeToString,
                response_deserializer=offboard_dot_offboard__pb2.SetAccelerationNedResponse.FromString,
                _registered_method=True)


class OffboardServiceServicer(object):
    """*
    Control a drone with position, velocity, attitude or motor commands.

    The module is called offboard because the commands can be sent from external sources
    as opposed to onboard control right inside the autopilot "board".

    Client code must specify a setpoint before starting offboard mode.
    Mavsdk automatically sends setpoints at 20Hz (PX4 Offboard mode requires that setpoints
    are minimally sent at 2Hz).
    """

    def Start(self, request, context):
        """
        Start offboard control.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """
        Stop offboard control.

        The vehicle will be put into Hold mode: https://docs.px4.io/en/flight_modes/hold.html
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsActive(self, request, context):
        """
        Check if offboard control is active.

        True means that the vehicle is in offboard mode and we are actively sending
        setpoints.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttitude(self, request, context):
        """
        Set the attitude in terms of roll, pitch and yaw in degrees with thrust.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetActuatorControl(self, request, context):
        """
        Set direct actuator control values to groups #0 and #1.

        First 8 controls will go to control group 0, the following 8 controls to control group 1 (if
        actuator_control.num_controls more than 8).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttitudeRate(self, request, context):
        """
        Set the attitude rate in terms of pitch, roll and yaw angular rate along with thrust.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPositionNed(self, request, context):
        """
        Set the position in NED coordinates and yaw.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPositionGlobal(self, request, context):
        """
        Set the position in Global coordinates (latitude, longitude, altitude) and yaw
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetVelocityBody(self, request, context):
        """
        Set the velocity in body coordinates and yaw angular rate. Not available for fixed-wing aircraft.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetVelocityNed(self, request, context):
        """
        Set the velocity in NED coordinates and yaw. Not available for fixed-wing aircraft.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPositionVelocityNed(self, request, context):
        """
        Set the position in NED coordinates, with the velocity to be used as feed-forward.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPositionVelocityAccelerationNed(self, request, context):
        """
        Set the position, velocity and acceleration in NED coordinates, with velocity and acceleration used as feed-forward.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccelerationNed(self, request, context):
        """
        Set the acceleration in NED coordinates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OffboardServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=offboard_dot_offboard__pb2.StartRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.StartResponse.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=offboard_dot_offboard__pb2.StopRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.StopResponse.SerializeToString,
            ),
            'IsActive': grpc.unary_unary_rpc_method_handler(
                    servicer.IsActive,
                    request_deserializer=offboard_dot_offboard__pb2.IsActiveRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.IsActiveResponse.SerializeToString,
            ),
            'SetAttitude': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttitude,
                    request_deserializer=offboard_dot_offboard__pb2.SetAttitudeRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.SetAttitudeResponse.SerializeToString,
            ),
            'SetActuatorControl': grpc.unary_unary_rpc_method_handler(
                    servicer.SetActuatorControl,
                    request_deserializer=offboard_dot_offboard__pb2.SetActuatorControlRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.SetActuatorControlResponse.SerializeToString,
            ),
            'SetAttitudeRate': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttitudeRate,
                    request_deserializer=offboard_dot_offboard__pb2.SetAttitudeRateRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.SetAttitudeRateResponse.SerializeToString,
            ),
            'SetPositionNed': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPositionNed,
                    request_deserializer=offboard_dot_offboard__pb2.SetPositionNedRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.SetPositionNedResponse.SerializeToString,
            ),
            'SetPositionGlobal': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPositionGlobal,
                    request_deserializer=offboard_dot_offboard__pb2.SetPositionGlobalRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.SetPositionGlobalResponse.SerializeToString,
            ),
            'SetVelocityBody': grpc.unary_unary_rpc_method_handler(
                    servicer.SetVelocityBody,
                    request_deserializer=offboard_dot_offboard__pb2.SetVelocityBodyRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.SetVelocityBodyResponse.SerializeToString,
            ),
            'SetVelocityNed': grpc.unary_unary_rpc_method_handler(
                    servicer.SetVelocityNed,
                    request_deserializer=offboard_dot_offboard__pb2.SetVelocityNedRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.SetVelocityNedResponse.SerializeToString,
            ),
            'SetPositionVelocityNed': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPositionVelocityNed,
                    request_deserializer=offboard_dot_offboard__pb2.SetPositionVelocityNedRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.SetPositionVelocityNedResponse.SerializeToString,
            ),
            'SetPositionVelocityAccelerationNed': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPositionVelocityAccelerationNed,
                    request_deserializer=offboard_dot_offboard__pb2.SetPositionVelocityAccelerationNedRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.SetPositionVelocityAccelerationNedResponse.SerializeToString,
            ),
            'SetAccelerationNed': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAccelerationNed,
                    request_deserializer=offboard_dot_offboard__pb2.SetAccelerationNedRequest.FromString,
                    response_serializer=offboard_dot_offboard__pb2.SetAccelerationNedResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.offboard.OffboardService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OffboardService(object):
    """*
    Control a drone with position, velocity, attitude or motor commands.

    The module is called offboard because the commands can be sent from external sources
    as opposed to onboard control right inside the autopilot "board".

    Client code must specify a setpoint before starting offboard mode.
    Mavsdk automatically sends setpoints at 20Hz (PX4 Offboard mode requires that setpoints
    are minimally sent at 2Hz).
    """

    @staticmethod
    def Start(request,
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
            '/mavsdk.rpc.offboard.OffboardService/Start',
            offboard_dot_offboard__pb2.StartRequest.SerializeToString,
            offboard_dot_offboard__pb2.StartResponse.FromString,
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
    def Stop(request,
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
            '/mavsdk.rpc.offboard.OffboardService/Stop',
            offboard_dot_offboard__pb2.StopRequest.SerializeToString,
            offboard_dot_offboard__pb2.StopResponse.FromString,
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
    def IsActive(request,
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
            '/mavsdk.rpc.offboard.OffboardService/IsActive',
            offboard_dot_offboard__pb2.IsActiveRequest.SerializeToString,
            offboard_dot_offboard__pb2.IsActiveResponse.FromString,
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
    def SetAttitude(request,
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
            '/mavsdk.rpc.offboard.OffboardService/SetAttitude',
            offboard_dot_offboard__pb2.SetAttitudeRequest.SerializeToString,
            offboard_dot_offboard__pb2.SetAttitudeResponse.FromString,
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
    def SetActuatorControl(request,
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
            '/mavsdk.rpc.offboard.OffboardService/SetActuatorControl',
            offboard_dot_offboard__pb2.SetActuatorControlRequest.SerializeToString,
            offboard_dot_offboard__pb2.SetActuatorControlResponse.FromString,
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
    def SetAttitudeRate(request,
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
            '/mavsdk.rpc.offboard.OffboardService/SetAttitudeRate',
            offboard_dot_offboard__pb2.SetAttitudeRateRequest.SerializeToString,
            offboard_dot_offboard__pb2.SetAttitudeRateResponse.FromString,
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
    def SetPositionNed(request,
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
            '/mavsdk.rpc.offboard.OffboardService/SetPositionNed',
            offboard_dot_offboard__pb2.SetPositionNedRequest.SerializeToString,
            offboard_dot_offboard__pb2.SetPositionNedResponse.FromString,
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
    def SetPositionGlobal(request,
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
            '/mavsdk.rpc.offboard.OffboardService/SetPositionGlobal',
            offboard_dot_offboard__pb2.SetPositionGlobalRequest.SerializeToString,
            offboard_dot_offboard__pb2.SetPositionGlobalResponse.FromString,
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
    def SetVelocityBody(request,
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
            '/mavsdk.rpc.offboard.OffboardService/SetVelocityBody',
            offboard_dot_offboard__pb2.SetVelocityBodyRequest.SerializeToString,
            offboard_dot_offboard__pb2.SetVelocityBodyResponse.FromString,
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
    def SetVelocityNed(request,
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
            '/mavsdk.rpc.offboard.OffboardService/SetVelocityNed',
            offboard_dot_offboard__pb2.SetVelocityNedRequest.SerializeToString,
            offboard_dot_offboard__pb2.SetVelocityNedResponse.FromString,
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
    def SetPositionVelocityNed(request,
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
            '/mavsdk.rpc.offboard.OffboardService/SetPositionVelocityNed',
            offboard_dot_offboard__pb2.SetPositionVelocityNedRequest.SerializeToString,
            offboard_dot_offboard__pb2.SetPositionVelocityNedResponse.FromString,
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
    def SetPositionVelocityAccelerationNed(request,
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
            '/mavsdk.rpc.offboard.OffboardService/SetPositionVelocityAccelerationNed',
            offboard_dot_offboard__pb2.SetPositionVelocityAccelerationNedRequest.SerializeToString,
            offboard_dot_offboard__pb2.SetPositionVelocityAccelerationNedResponse.FromString,
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
    def SetAccelerationNed(request,
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
            '/mavsdk.rpc.offboard.OffboardService/SetAccelerationNed',
            offboard_dot_offboard__pb2.SetAccelerationNedRequest.SerializeToString,
            offboard_dot_offboard__pb2.SetAccelerationNedResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
