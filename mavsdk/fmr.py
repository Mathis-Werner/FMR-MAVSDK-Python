# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import fmr_pb2, fmr_pb2_grpc
from enum import Enum


class GpsInfo:
    """
     GPSinfo type in global coordinates.

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
        """ Initializes the GpsInfo object """
        self.time_week_ms = time_week_ms
        self.time_week = time_week

    def __eq__(self, to_compare):
        """ Checks if two GpsInfo are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # GpsInfo object
            return \
                (self.time_week_ms == to_compare.time_week_ms) and \
                (self.time_week == to_compare.time_week)

        except AttributeError:
            return False

    def __str__(self):
        """ GpsInfo in string representation """
        struct_repr = ", ".join([
                "time_week_ms: " + str(self.time_week_ms),
                "time_week: " + str(self.time_week)
                ])

        return f"GpsInfo: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcGpsInfo):
        """ Translates a gRPC struct to the SDK equivalent """
        return GpsInfo(
                
                rpcGpsInfo.time_week_ms,
                
                
                rpcGpsInfo.time_week
                )

    def translate_to_rpc(self, rpcGpsInfo):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcGpsInfo.time_week_ms = self.time_week_ms
            
        
        
        
            
        rpcGpsInfo.time_week = self.time_week
            
        
        


class GpsInfoResult:
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
            if self == GpsInfoResult.Result.UNKNOWN:
                return fmr_pb2.GpsInfoResult.RESULT_UNKNOWN
            if self == GpsInfoResult.Result.SUCCESS:
                return fmr_pb2.GpsInfoResult.RESULT_SUCCESS
            if self == GpsInfoResult.Result.NO_SYSTEM:
                return fmr_pb2.GpsInfoResult.RESULT_NO_SYSTEM
            if self == GpsInfoResult.Result.CONNECTION_ERROR:
                return fmr_pb2.GpsInfoResult.RESULT_CONNECTION_ERROR
            if self == GpsInfoResult.Result.BUSY:
                return fmr_pb2.GpsInfoResult.RESULT_BUSY
            if self == GpsInfoResult.Result.COMMAND_DENIED:
                return fmr_pb2.GpsInfoResult.RESULT_COMMAND_DENIED
            if self == GpsInfoResult.Result.TIMEOUT:
                return fmr_pb2.GpsInfoResult.RESULT_TIMEOUT
            if self == GpsInfoResult.Result.UNSUPPORTED:
                return fmr_pb2.GpsInfoResult.RESULT_UNSUPPORTED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == fmr_pb2.GpsInfoResult.RESULT_UNKNOWN:
                return GpsInfoResult.Result.UNKNOWN
            if rpc_enum_value == fmr_pb2.GpsInfoResult.RESULT_SUCCESS:
                return GpsInfoResult.Result.SUCCESS
            if rpc_enum_value == fmr_pb2.GpsInfoResult.RESULT_NO_SYSTEM:
                return GpsInfoResult.Result.NO_SYSTEM
            if rpc_enum_value == fmr_pb2.GpsInfoResult.RESULT_CONNECTION_ERROR:
                return GpsInfoResult.Result.CONNECTION_ERROR
            if rpc_enum_value == fmr_pb2.GpsInfoResult.RESULT_BUSY:
                return GpsInfoResult.Result.BUSY
            if rpc_enum_value == fmr_pb2.GpsInfoResult.RESULT_COMMAND_DENIED:
                return GpsInfoResult.Result.COMMAND_DENIED
            if rpc_enum_value == fmr_pb2.GpsInfoResult.RESULT_TIMEOUT:
                return GpsInfoResult.Result.TIMEOUT
            if rpc_enum_value == fmr_pb2.GpsInfoResult.RESULT_UNSUPPORTED:
                return GpsInfoResult.Result.UNSUPPORTED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the GpsInfoResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two GpsInfoResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # GpsInfoResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ GpsInfoResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"GpsInfoResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcGpsInfoResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return GpsInfoResult(
                
                GpsInfoResult.Result.translate_from_rpc(rpcGpsInfoResult.result),
                
                
                rpcGpsInfoResult.result_str
                )

    def translate_to_rpc(self, rpcGpsInfoResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcGpsInfoResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcGpsInfoResult.result_str = self.result_str
            
        
        



class FmrError(Exception):
    """ Raised when a FmrResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Fmr(AsyncBase):
    """
 

     Generated by dcsdkgen - MAVSDK Fmr API
    """

    # Plugin name
    name = "Fmr"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = fmr_pb2_grpc.FmrServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return FmrResult.translate_from_rpc(response.fmr_result)
    

    async def gps_info(self):
        """
         Subscribe to 'GPSInfo' updates.

         Yields
         -------
         gpsinfo : GpsInfo
              The next GPSinfo

         
        """

        request = fmr_pb2.SubscribeGpsInfoRequest()
        gps_info_stream = self._stub.SubscribeGpsInfo(request)

        try:
            async for response in gps_info_stream:
                

            
                yield GpsInfo.translate_from_rpc(response.gpsinfo)
        finally:
            gps_info_stream.cancel()

    async def set_rate_gps_info(self, rate_hz):
        """
         Set rate to 'GpsInfo' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         FmrError
             If the request fails. The error contains the reason for the failure.
        """

        request = fmr_pb2.SetRateGpsInfoRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateGpsInfo(request)

        
        result = self._extract_result(response)

        if result.result != FmrResult.Result.SUCCESS:
            raise FmrError(result, "set_rate_gps_info()", rate_hz)
        