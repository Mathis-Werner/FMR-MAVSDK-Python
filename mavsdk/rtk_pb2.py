# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rtk/rtk.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rrtk/rtk.proto\x12\x0emavsdk.rpc.rtk\x1a\x14mavsdk_options.proto\"\x1f\n\x08RtcmData\x12\x13\n\x0b\x64\x61ta_base64\x18\x01 \x01(\t\"B\n\x13SendRtcmDataRequest\x12+\n\trtcm_data\x18\x01 \x01(\x0b\x32\x18.mavsdk.rpc.rtk.RtcmData\"E\n\x14SendRtcmDataResponse\x12-\n\nrtk_result\x18\x01 \x01(\x0b\x32\x19.mavsdk.rpc.rtk.RtkResult\"\xcb\x01\n\tRtkResult\x12\x30\n\x06result\x18\x01 \x01(\x0e\x32 .mavsdk.rpc.rtk.RtkResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"x\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x13\n\x0fRESULT_TOO_LONG\x10\x02\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x05\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x06\x32m\n\nRtkService\x12_\n\x0cSendRtcmData\x12#.mavsdk.rpc.rtk.SendRtcmDataRequest\x1a$.mavsdk.rpc.rtk.SendRtcmDataResponse\"\x04\x80\xb5\x18\x01\x42\x19\n\rio.mavsdk.rtkB\x08RtkProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rtk.rtk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\rio.mavsdk.rtkB\010RtkProto'
  _globals['_RTKSERVICE'].methods_by_name['SendRtcmData']._loaded_options = None
  _globals['_RTKSERVICE'].methods_by_name['SendRtcmData']._serialized_options = b'\200\265\030\001'
  _globals['_RTCMDATA']._serialized_start=55
  _globals['_RTCMDATA']._serialized_end=86
  _globals['_SENDRTCMDATAREQUEST']._serialized_start=88
  _globals['_SENDRTCMDATAREQUEST']._serialized_end=154
  _globals['_SENDRTCMDATARESPONSE']._serialized_start=156
  _globals['_SENDRTCMDATARESPONSE']._serialized_end=225
  _globals['_RTKRESULT']._serialized_start=228
  _globals['_RTKRESULT']._serialized_end=431
  _globals['_RTKRESULT_RESULT']._serialized_start=311
  _globals['_RTKRESULT_RESULT']._serialized_end=431
  _globals['_RTKSERVICE']._serialized_start=433
  _globals['_RTKSERVICE']._serialized_end=542
# @@protoc_insertion_point(module_scope)
