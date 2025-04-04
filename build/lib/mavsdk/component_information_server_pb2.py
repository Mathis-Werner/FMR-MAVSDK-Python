# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: component_information_server/component_information_server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?component_information_server/component_information_server.proto\x12\'mavsdk.rpc.component_information_server\x1a\x14mavsdk_options.proto\"\xc7\x01\n\nFloatParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x11short_description\x18\x02 \x01(\t\x12\x18\n\x10long_description\x18\x03 \x01(\t\x12\x0c\n\x04unit\x18\x04 \x01(\t\x12\x16\n\x0e\x64\x65\x63imal_places\x18\x05 \x01(\x05\x12\x13\n\x0bstart_value\x18\x06 \x01(\x02\x12\x15\n\rdefault_value\x18\x07 \x01(\x02\x12\x11\n\tmin_value\x18\x08 \x01(\x02\x12\x11\n\tmax_value\x18\t \x01(\x02\"^\n\x18ProvideFloatParamRequest\x12\x42\n\x05param\x18\x01 \x01(\x0b\x32\x33.mavsdk.rpc.component_information_server.FloatParam\"\x93\x01\n\x19ProvideFloatParamResponse\x12v\n#component_information_server_result\x18\x01 \x01(\x0b\x32I.mavsdk.rpc.component_information_server.ComponentInformationServerResult\"/\n\x10\x46loatParamUpdate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"\x1c\n\x1aSubscribeFloatParamRequest\"e\n\x12\x46loatParamResponse\x12O\n\x0cparam_update\x18\x01 \x01(\x0b\x32\x39.mavsdk.rpc.component_information_server.FloatParamUpdate\"\xea\x02\n ComponentInformationServerResult\x12`\n\x06result\x18\x01 \x01(\x0e\x32P.mavsdk.rpc.component_information_server.ComponentInformationServerResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xcf\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x1a\n\x16RESULT_DUPLICATE_PARAM\x10\x02\x12$\n RESULT_INVALID_PARAM_START_VALUE\x10\x03\x12&\n\"RESULT_INVALID_PARAM_DEFAULT_VALUE\x10\x04\x12\x1d\n\x19RESULT_INVALID_PARAM_NAME\x10\x05\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x06\x32\xe8\x02\n!ComponentInformationServerService\x12\xa0\x01\n\x11ProvideFloatParam\x12\x41.mavsdk.rpc.component_information_server.ProvideFloatParamRequest\x1a\x42.mavsdk.rpc.component_information_server.ProvideFloatParamResponse\"\x04\x80\xb5\x18\x01\x12\x9f\x01\n\x13SubscribeFloatParam\x12\x43.mavsdk.rpc.component_information_server.SubscribeFloatParamRequest\x1a;.mavsdk.rpc.component_information_server.FloatParamResponse\"\x04\x80\xb5\x18\x00\x30\x01\x42I\n&io.mavsdk.component_information_serverB\x1f\x43omponentInformationServerProtob\x06proto3')



_FLOATPARAM = DESCRIPTOR.message_types_by_name['FloatParam']
_PROVIDEFLOATPARAMREQUEST = DESCRIPTOR.message_types_by_name['ProvideFloatParamRequest']
_PROVIDEFLOATPARAMRESPONSE = DESCRIPTOR.message_types_by_name['ProvideFloatParamResponse']
_FLOATPARAMUPDATE = DESCRIPTOR.message_types_by_name['FloatParamUpdate']
_SUBSCRIBEFLOATPARAMREQUEST = DESCRIPTOR.message_types_by_name['SubscribeFloatParamRequest']
_FLOATPARAMRESPONSE = DESCRIPTOR.message_types_by_name['FloatParamResponse']
_COMPONENTINFORMATIONSERVERRESULT = DESCRIPTOR.message_types_by_name['ComponentInformationServerResult']
_COMPONENTINFORMATIONSERVERRESULT_RESULT = _COMPONENTINFORMATIONSERVERRESULT.enum_types_by_name['Result']
FloatParam = _reflection.GeneratedProtocolMessageType('FloatParam', (_message.Message,), {
  'DESCRIPTOR' : _FLOATPARAM,
  '__module__' : 'component_information_server.component_information_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information_server.FloatParam)
  })
_sym_db.RegisterMessage(FloatParam)

ProvideFloatParamRequest = _reflection.GeneratedProtocolMessageType('ProvideFloatParamRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEFLOATPARAMREQUEST,
  '__module__' : 'component_information_server.component_information_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information_server.ProvideFloatParamRequest)
  })
_sym_db.RegisterMessage(ProvideFloatParamRequest)

ProvideFloatParamResponse = _reflection.GeneratedProtocolMessageType('ProvideFloatParamResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEFLOATPARAMRESPONSE,
  '__module__' : 'component_information_server.component_information_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information_server.ProvideFloatParamResponse)
  })
_sym_db.RegisterMessage(ProvideFloatParamResponse)

FloatParamUpdate = _reflection.GeneratedProtocolMessageType('FloatParamUpdate', (_message.Message,), {
  'DESCRIPTOR' : _FLOATPARAMUPDATE,
  '__module__' : 'component_information_server.component_information_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information_server.FloatParamUpdate)
  })
_sym_db.RegisterMessage(FloatParamUpdate)

SubscribeFloatParamRequest = _reflection.GeneratedProtocolMessageType('SubscribeFloatParamRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEFLOATPARAMREQUEST,
  '__module__' : 'component_information_server.component_information_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information_server.SubscribeFloatParamRequest)
  })
_sym_db.RegisterMessage(SubscribeFloatParamRequest)

FloatParamResponse = _reflection.GeneratedProtocolMessageType('FloatParamResponse', (_message.Message,), {
  'DESCRIPTOR' : _FLOATPARAMRESPONSE,
  '__module__' : 'component_information_server.component_information_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information_server.FloatParamResponse)
  })
_sym_db.RegisterMessage(FloatParamResponse)

ComponentInformationServerResult = _reflection.GeneratedProtocolMessageType('ComponentInformationServerResult', (_message.Message,), {
  'DESCRIPTOR' : _COMPONENTINFORMATIONSERVERRESULT,
  '__module__' : 'component_information_server.component_information_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information_server.ComponentInformationServerResult)
  })
_sym_db.RegisterMessage(ComponentInformationServerResult)

_COMPONENTINFORMATIONSERVERSERVICE = DESCRIPTOR.services_by_name['ComponentInformationServerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&io.mavsdk.component_information_serverB\037ComponentInformationServerProto'
  _COMPONENTINFORMATIONSERVERSERVICE.methods_by_name['ProvideFloatParam']._options = None
  _COMPONENTINFORMATIONSERVERSERVICE.methods_by_name['ProvideFloatParam']._serialized_options = b'\200\265\030\001'
  _COMPONENTINFORMATIONSERVERSERVICE.methods_by_name['SubscribeFloatParam']._options = None
  _COMPONENTINFORMATIONSERVERSERVICE.methods_by_name['SubscribeFloatParam']._serialized_options = b'\200\265\030\000'
  _FLOATPARAM._serialized_start=131
  _FLOATPARAM._serialized_end=330
  _PROVIDEFLOATPARAMREQUEST._serialized_start=332
  _PROVIDEFLOATPARAMREQUEST._serialized_end=426
  _PROVIDEFLOATPARAMRESPONSE._serialized_start=429
  _PROVIDEFLOATPARAMRESPONSE._serialized_end=576
  _FLOATPARAMUPDATE._serialized_start=578
  _FLOATPARAMUPDATE._serialized_end=625
  _SUBSCRIBEFLOATPARAMREQUEST._serialized_start=627
  _SUBSCRIBEFLOATPARAMREQUEST._serialized_end=655
  _FLOATPARAMRESPONSE._serialized_start=657
  _FLOATPARAMRESPONSE._serialized_end=758
  _COMPONENTINFORMATIONSERVERRESULT._serialized_start=761
  _COMPONENTINFORMATIONSERVERRESULT._serialized_end=1123
  _COMPONENTINFORMATIONSERVERRESULT_RESULT._serialized_start=916
  _COMPONENTINFORMATIONSERVERRESULT_RESULT._serialized_end=1123
  _COMPONENTINFORMATIONSERVERSERVICE._serialized_start=1126
  _COMPONENTINFORMATIONSERVERSERVICE._serialized_end=1486
# @@protoc_insertion_point(module_scope)
