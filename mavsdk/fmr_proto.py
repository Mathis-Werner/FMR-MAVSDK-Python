# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import fmr_proto_pb2, fmr_proto_pb2_grpc
from enum import Enum


class GPSInfo:
    """
     Position type in global coordinates.

     Parameters
     ----------
     time_week_ms : double
          GPS time (from start of GPS week)

     time_week : double
          GPS week number

     """

    

    def __init__(
            self,
            time_week_ms,
            time_week):
        """ Initializes the GPSInfo object """
        self.time_week_ms = time_week_ms
        self.time_week = time_week

    def __eq__(self, to_compare):
        """ Checks if two GPSInfo are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # GPSInfo object
            return \
                (self.time_week_ms == to_compare.time_week_ms) and \
                (self.time_week == to_compare.time_week)

        except AttributeError:
            return False

    def __str__(self):
        """ GPSInfo in string representation """
        struct_repr = ", ".join([
                "time_week_ms: " + str(self.time_week_ms),
                "time_week: " + str(self.time_week)
                ])

        return f"GPSInfo: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcGPSInfo):
        """ Translates a gRPC struct to the SDK equivalent """
        return GPSInfo(
                
                rpcGPSInfo.time_week_ms,
                
                
                rpcGPSInfo.time_week
                )

    def translate_to_rpc(self, rpcGPSInfo):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcGPSInfo.time_week_ms = self.time_week_ms
            
        
        
        
            
        rpcGPSInfo.time_week = self.time_week
            
        
        


class TelemetryResult:
    """
     Result type.

     Parameters
     ----------
     result : Result
          Result enum value

     result_str : std::string
          Human-readable English string describing the result

     """

    
    
    class Result(Enum):
        """
         Possible results returned for telemetry requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Success: the telemetry command was accepted by the vehicle

         NO_SYSTEM
              No system connected

         CONNECTION_ERROR
              Connection error

         BUSY
              Vehicle is busy

         COMMAND_DENIED
              Command refused by vehicle

         TIMEOUT
              Request timed out

         UNSUPPORTED
              Request not supported

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        COMMAND_DENIED = 5
        TIMEOUT = 6
        UNSUPPORTED = 7

        def translate_to_rpc(self):
            if self == TelemetryResult.Result.UNKNOWN:
                return fmr_proto_pb2.TelemetryResult.RESULT_UNKNOWN
            if self == TelemetryResult.Result.SUCCESS:
                return fmr_proto_pb2.TelemetryResult.RESULT_SUCCESS
            if self == TelemetryResult.Result.NO_SYSTEM:
                return fmr_proto_pb2.TelemetryResult.RESULT_NO_SYSTEM
            if self == TelemetryResult.Result.CONNECTION_ERROR:
                return fmr_proto_pb2.TelemetryResult.RESULT_CONNECTION_ERROR
            if self == TelemetryResult.Result.BUSY:
                return fmr_proto_pb2.TelemetryResult.RESULT_BUSY
            if self == TelemetryResult.Result.COMMAND_DENIED:
                return fmr_proto_pb2.TelemetryResult.RESULT_COMMAND_DENIED
            if self == TelemetryResult.Result.TIMEOUT:
                return fmr_proto_pb2.TelemetryResult.RESULT_TIMEOUT
            if self == TelemetryResult.Result.UNSUPPORTED:
                return fmr_proto_pb2.TelemetryResult.RESULT_UNSUPPORTED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == fmr_proto_pb2.TelemetryResult.RESULT_UNKNOWN:
                return TelemetryResult.Result.UNKNOWN
            if rpc_enum_value == fmr_proto_pb2.TelemetryResult.RESULT_SUCCESS:
                return TelemetryResult.Result.SUCCESS
            if rpc_enum_value == fmr_proto_pb2.TelemetryResult.RESULT_NO_SYSTEM:
                return TelemetryResult.Result.NO_SYSTEM
            if rpc_enum_value == fmr_proto_pb2.TelemetryResult.RESULT_CONNECTION_ERROR:
                return TelemetryResult.Result.CONNECTION_ERROR
            if rpc_enum_value == fmr_proto_pb2.TelemetryResult.RESULT_BUSY:
                return TelemetryResult.Result.BUSY
            if rpc_enum_value == fmr_proto_pb2.TelemetryResult.RESULT_COMMAND_DENIED:
                return TelemetryResult.Result.COMMAND_DENIED
            if rpc_enum_value == fmr_proto_pb2.TelemetryResult.RESULT_TIMEOUT:
                return TelemetryResult.Result.TIMEOUT
            if rpc_enum_value == fmr_proto_pb2.TelemetryResult.RESULT_UNSUPPORTED:
                return TelemetryResult.Result.UNSUPPORTED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the TelemetryResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two TelemetryResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # TelemetryResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ TelemetryResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"TelemetryResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcTelemetryResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return TelemetryResult(
                
                Result.translate_from_rpc(rpcTelemetryResult.result),
                
                
                rpcTelemetryResult.result_str
                )

    def translate_to_rpc(self, rpcTelemetryResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcTelemetryResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcTelemetryResult.result_str = self.result_str
            
        
        



class FmrProtoError(Exception):
    """ Raised when a FmrProtoResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class FmrProto(AsyncBase):
    """
 

     Generated by dcsdkgen - MAVSDK FmrProto API
    """

    # Plugin name
    name = "FmrProto"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = fmr_proto_pb2_grpc.FmrProtoServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return FmrProtoResult.translate_from_rpc(response.fmr_proto_result)
    

    async def position(self):
        """
         Subscribe to 'position' updates.

         Yields
         -------
         gpsinfo : GPSInfo
              The next position

         
        """

        request = fmr_proto_pb2.SubscribePositionRequest()
        position_stream = self._stub.SubscribePosition(request)

        try:
            async for response in position_stream:
                

            
                yield GPSInfo.translate_from_rpc(response.gpsinfo)
        finally:
            position_stream.cancel()

    async def set_rate_position(self, rate_hz):
        """
         Set rate to 'position' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         FmrProtoError
             If the request fails. The error contains the reason for the failure.
        """

        request = fmr_proto_pb2.SetRatePositionRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRatePosition(request)

        
        result = self._extract_result(response)

        if result.result != FmrProtoResult.Result.SUCCESS:
            raise FmrProtoError(result, "set_rate_position()", rate_hz)
        