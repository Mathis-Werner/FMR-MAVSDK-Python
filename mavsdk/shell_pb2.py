# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: shell/shell.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'shell/shell.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11shell/shell.proto\x12\x10mavsdk.rpc.shell\x1a\x14mavsdk_options.proto\"\x1e\n\x0bSendRequest\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\"C\n\x0cSendResponse\x12\x33\n\x0cshell_result\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.shell.ShellResult\"\x19\n\x17SubscribeReceiveRequest\"\x1f\n\x0fReceiveResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\xe6\x01\n\x0bShellResult\x12\x34\n\x06result\x18\x01 \x01(\x0e\x32$.mavsdk.rpc.shell.ShellResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x8c\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x16\n\x12RESULT_NO_RESPONSE\x10\x04\x12\x0f\n\x0bRESULT_BUSY\x10\x05\x32\xc5\x01\n\x0cShellService\x12K\n\x04Send\x12\x1d.mavsdk.rpc.shell.SendRequest\x1a\x1e.mavsdk.rpc.shell.SendResponse\"\x04\x80\xb5\x18\x01\x12h\n\x10SubscribeReceive\x12).mavsdk.rpc.shell.SubscribeReceiveRequest\x1a!.mavsdk.rpc.shell.ReceiveResponse\"\x04\x80\xb5\x18\x00\x30\x01\x42\x1d\n\x0fio.mavsdk.shellB\nShellProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'shell.shell_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017io.mavsdk.shellB\nShellProto'
  _globals['_SHELLSERVICE'].methods_by_name['Send']._loaded_options = None
  _globals['_SHELLSERVICE'].methods_by_name['Send']._serialized_options = b'\200\265\030\001'
  _globals['_SHELLSERVICE'].methods_by_name['SubscribeReceive']._loaded_options = None
  _globals['_SHELLSERVICE'].methods_by_name['SubscribeReceive']._serialized_options = b'\200\265\030\000'
  _globals['_SENDREQUEST']._serialized_start=61
  _globals['_SENDREQUEST']._serialized_end=91
  _globals['_SENDRESPONSE']._serialized_start=93
  _globals['_SENDRESPONSE']._serialized_end=160
  _globals['_SUBSCRIBERECEIVEREQUEST']._serialized_start=162
  _globals['_SUBSCRIBERECEIVEREQUEST']._serialized_end=187
  _globals['_RECEIVERESPONSE']._serialized_start=189
  _globals['_RECEIVERESPONSE']._serialized_end=220
  _globals['_SHELLRESULT']._serialized_start=223
  _globals['_SHELLRESULT']._serialized_end=453
  _globals['_SHELLRESULT_RESULT']._serialized_start=313
  _globals['_SHELLRESULT_RESULT']._serialized_end=453
  _globals['_SHELLSERVICE']._serialized_start=456
  _globals['_SHELLSERVICE']._serialized_end=653
# @@protoc_insertion_point(module_scope)
