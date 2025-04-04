# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import component_information_pb2, component_information_pb2_grpc
from enum import Enum


class FloatParam:
    """
     Meta information for parameter of type float.

     Parameters
     ----------
     name : std::string
          Name (max 16 chars)

     short_description : std::string
          Short description

     long_description : std::string
          Long description

     unit : std::string
          Unit

     decimal_places : int32_t
          Decimal places for user to show

     start_value : float
          Current/starting value

     default_value : float
          Default value

     min_value : float
          Minimum value

     max_value : float
          Maximum value

     """

    

    def __init__(
            self,
            name,
            short_description,
            long_description,
            unit,
            decimal_places,
            start_value,
            default_value,
            min_value,
            max_value):
        """ Initializes the FloatParam object """
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.unit = unit
        self.decimal_places = decimal_places
        self.start_value = start_value
        self.default_value = default_value
        self.min_value = min_value
        self.max_value = max_value

    def __eq__(self, to_compare):
        """ Checks if two FloatParam are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # FloatParam object
            return \
                (self.name == to_compare.name) and \
                (self.short_description == to_compare.short_description) and \
                (self.long_description == to_compare.long_description) and \
                (self.unit == to_compare.unit) and \
                (self.decimal_places == to_compare.decimal_places) and \
                (self.start_value == to_compare.start_value) and \
                (self.default_value == to_compare.default_value) and \
                (self.min_value == to_compare.min_value) and \
                (self.max_value == to_compare.max_value)

        except AttributeError:
            return False

    def __str__(self):
        """ FloatParam in string representation """
        struct_repr = ", ".join([
                "name: " + str(self.name),
                "short_description: " + str(self.short_description),
                "long_description: " + str(self.long_description),
                "unit: " + str(self.unit),
                "decimal_places: " + str(self.decimal_places),
                "start_value: " + str(self.start_value),
                "default_value: " + str(self.default_value),
                "min_value: " + str(self.min_value),
                "max_value: " + str(self.max_value)
                ])

        return f"FloatParam: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcFloatParam):
        """ Translates a gRPC struct to the SDK equivalent """
        return FloatParam(
                
                rpcFloatParam.name,
                
                
                rpcFloatParam.short_description,
                
                
                rpcFloatParam.long_description,
                
                
                rpcFloatParam.unit,
                
                
                rpcFloatParam.decimal_places,
                
                
                rpcFloatParam.start_value,
                
                
                rpcFloatParam.default_value,
                
                
                rpcFloatParam.min_value,
                
                
                rpcFloatParam.max_value
                )

    def translate_to_rpc(self, rpcFloatParam):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcFloatParam.name = self.name
            
        
        
        
            
        rpcFloatParam.short_description = self.short_description
            
        
        
        
            
        rpcFloatParam.long_description = self.long_description
            
        
        
        
            
        rpcFloatParam.unit = self.unit
            
        
        
        
            
        rpcFloatParam.decimal_places = self.decimal_places
            
        
        
        
            
        rpcFloatParam.start_value = self.start_value
            
        
        
        
            
        rpcFloatParam.default_value = self.default_value
            
        
        
        
            
        rpcFloatParam.min_value = self.min_value
            
        
        
        
            
        rpcFloatParam.max_value = self.max_value
            
        
        


class FloatParamUpdate:
    """
     A float param that has been updated.

     Parameters
     ----------
     name : std::string
          Name of param that changed

     value : float
          New value of param

     """

    

    def __init__(
            self,
            name,
            value):
        """ Initializes the FloatParamUpdate object """
        self.name = name
        self.value = value

    def __eq__(self, to_compare):
        """ Checks if two FloatParamUpdate are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # FloatParamUpdate object
            return \
                (self.name == to_compare.name) and \
                (self.value == to_compare.value)

        except AttributeError:
            return False

    def __str__(self):
        """ FloatParamUpdate in string representation """
        struct_repr = ", ".join([
                "name: " + str(self.name),
                "value: " + str(self.value)
                ])

        return f"FloatParamUpdate: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcFloatParamUpdate):
        """ Translates a gRPC struct to the SDK equivalent """
        return FloatParamUpdate(
                
                rpcFloatParamUpdate.name,
                
                
                rpcFloatParamUpdate.value
                )

    def translate_to_rpc(self, rpcFloatParamUpdate):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcFloatParamUpdate.name = self.name
            
        
        
        
            
        rpcFloatParamUpdate.value = self.value
            
        
        


class ComponentInformationResult:
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
         Possible results returned for param requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request succeeded

         NO_SYSTEM
              No system is connected

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2

        def translate_to_rpc(self):
            if self == ComponentInformationResult.Result.UNKNOWN:
                return component_information_pb2.ComponentInformationResult.RESULT_UNKNOWN
            if self == ComponentInformationResult.Result.SUCCESS:
                return component_information_pb2.ComponentInformationResult.RESULT_SUCCESS
            if self == ComponentInformationResult.Result.NO_SYSTEM:
                return component_information_pb2.ComponentInformationResult.RESULT_NO_SYSTEM

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == component_information_pb2.ComponentInformationResult.RESULT_UNKNOWN:
                return ComponentInformationResult.Result.UNKNOWN
            if rpc_enum_value == component_information_pb2.ComponentInformationResult.RESULT_SUCCESS:
                return ComponentInformationResult.Result.SUCCESS
            if rpc_enum_value == component_information_pb2.ComponentInformationResult.RESULT_NO_SYSTEM:
                return ComponentInformationResult.Result.NO_SYSTEM

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ComponentInformationResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two ComponentInformationResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ComponentInformationResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ ComponentInformationResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"ComponentInformationResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcComponentInformationResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return ComponentInformationResult(
                
                ComponentInformationResult.Result.translate_from_rpc(rpcComponentInformationResult.result),
                
                
                rpcComponentInformationResult.result_str
                )

    def translate_to_rpc(self, rpcComponentInformationResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcComponentInformationResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcComponentInformationResult.result_str = self.result_str
            
        
        



class ComponentInformationError(Exception):
    """ Raised when a ComponentInformationResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class ComponentInformation(AsyncBase):
    """
     Access component information such as parameters.

     Generated by dcsdkgen - MAVSDK ComponentInformation API
    """

    # Plugin name
    name = "ComponentInformation"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = component_information_pb2_grpc.ComponentInformationServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return ComponentInformationResult.translate_from_rpc(response.component_information_result)
    

    async def access_float_params(self):
        """
         List available float params.

         Returns
         -------
         params : [FloatParam]
              Float param definitions

         Raises
         ------
         ComponentInformationError
             If the request fails. The error contains the reason for the failure.
        """

        request = component_information_pb2.AccessFloatParamsRequest()
        response = await self._stub.AccessFloatParams(request)

        
        result = self._extract_result(response)

        if result.result != ComponentInformationResult.Result.SUCCESS:
            raise ComponentInformationError(result, "access_float_params()")
        

        params = []
        for params_rpc in response.params:
            params.append(FloatParam.translate_from_rpc(params_rpc))

        return params
            

    async def float_param(self):
        """
         Subscribe to float param changes/updates.

         Yields
         -------
         param_update : FloatParamUpdate
              A param update

         
        """

        request = component_information_pb2.SubscribeFloatParamRequest()
        float_param_stream = self._stub.SubscribeFloatParam(request)

        try:
            async for response in float_param_stream:
                

            
                yield FloatParamUpdate.translate_from_rpc(response.param_update)
        finally:
            float_param_stream.cancel()