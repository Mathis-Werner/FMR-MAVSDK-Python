# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mocap/mocap.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11mocap/mocap.proto\x12\x10mavsdk.rpc.mocap\x1a\x14mavsdk_options.proto\"n\n SetVisionPositionEstimateRequest\x12J\n\x18vision_position_estimate\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mocap.VisionPositionEstimate\"X\n!SetVisionPositionEstimateResponse\x12\x33\n\x0cmocap_result\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.mocap.MocapResult\"k\n\x1fSetAttitudePositionMocapRequest\x12H\n\x17\x61ttitude_position_mocap\x18\x01 \x01(\x0b\x32\'.mavsdk.rpc.mocap.AttitudePositionMocap\"W\n SetAttitudePositionMocapResponse\x12\x33\n\x0cmocap_result\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.mocap.MocapResult\"B\n\x12SetOdometryRequest\x12,\n\x08odometry\x18\x01 \x01(\x0b\x32\x1a.mavsdk.rpc.mocap.Odometry\"J\n\x13SetOdometryResponse\x12\x33\n\x0cmocap_result\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.mocap.MocapResult\"5\n\x0cPositionBody\x12\x0b\n\x03x_m\x18\x01 \x01(\x02\x12\x0b\n\x03y_m\x18\x02 \x01(\x02\x12\x0b\n\x03z_m\x18\x03 \x01(\x02\"A\n\tAngleBody\x12\x10\n\x08roll_rad\x18\x01 \x01(\x02\x12\x11\n\tpitch_rad\x18\x02 \x01(\x02\x12\x0f\n\x07yaw_rad\x18\x03 \x01(\x02\"8\n\tSpeedBody\x12\r\n\x05x_m_s\x18\x01 \x01(\x02\x12\r\n\x05y_m_s\x18\x02 \x01(\x02\x12\r\n\x05z_m_s\x18\x03 \x01(\x02\"Q\n\x13\x41ngularVelocityBody\x12\x12\n\nroll_rad_s\x18\x01 \x01(\x02\x12\x13\n\x0bpitch_rad_s\x18\x02 \x01(\x02\x12\x11\n\tyaw_rad_s\x18\x03 \x01(\x02\"\'\n\nCovariance\x12\x19\n\x11\x63ovariance_matrix\x18\x01 \x03(\x02\"8\n\nQuaternion\x12\t\n\x01w\x18\x01 \x01(\x02\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\t\n\x01z\x18\x04 \x01(\x02\"\xca\x01\n\x16VisionPositionEstimate\x12\x11\n\ttime_usec\x18\x01 \x01(\x04\x12\x35\n\rposition_body\x18\x02 \x01(\x0b\x32\x1e.mavsdk.rpc.mocap.PositionBody\x12/\n\nangle_body\x18\x03 \x01(\x0b\x32\x1b.mavsdk.rpc.mocap.AngleBody\x12\x35\n\x0fpose_covariance\x18\x04 \x01(\x0b\x32\x1c.mavsdk.rpc.mocap.Covariance\"\xc1\x01\n\x15\x41ttitudePositionMocap\x12\x11\n\ttime_usec\x18\x01 \x01(\x04\x12\'\n\x01q\x18\x02 \x01(\x0b\x32\x1c.mavsdk.rpc.mocap.Quaternion\x12\x35\n\rposition_body\x18\x03 \x01(\x0b\x32\x1e.mavsdk.rpc.mocap.PositionBody\x12\x35\n\x0fpose_covariance\x18\x04 \x01(\x0b\x32\x1c.mavsdk.rpc.mocap.Covariance\"\xdb\x03\n\x08Odometry\x12\x11\n\ttime_usec\x18\x01 \x01(\x04\x12\x35\n\x08\x66rame_id\x18\x02 \x01(\x0e\x32#.mavsdk.rpc.mocap.Odometry.MavFrame\x12\x35\n\rposition_body\x18\x03 \x01(\x0b\x32\x1e.mavsdk.rpc.mocap.PositionBody\x12\'\n\x01q\x18\x04 \x01(\x0b\x32\x1c.mavsdk.rpc.mocap.Quaternion\x12/\n\nspeed_body\x18\x05 \x01(\x0b\x32\x1b.mavsdk.rpc.mocap.SpeedBody\x12\x44\n\x15\x61ngular_velocity_body\x18\x06 \x01(\x0b\x32%.mavsdk.rpc.mocap.AngularVelocityBody\x12\x35\n\x0fpose_covariance\x18\x07 \x01(\x0b\x32\x1c.mavsdk.rpc.mocap.Covariance\x12\x39\n\x13velocity_covariance\x18\x08 \x01(\x0b\x32\x1c.mavsdk.rpc.mocap.Covariance\"<\n\x08MavFrame\x12\x17\n\x13MAV_FRAME_MOCAP_NED\x10\x00\x12\x17\n\x13MAV_FRAME_LOCAL_FRD\x10\x01\"\xf6\x01\n\x0bMocapResult\x12\x34\n\x06result\x18\x01 \x01(\x0e\x32$.mavsdk.rpc.mocap.MocapResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x9c\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x1f\n\x1bRESULT_INVALID_REQUEST_DATA\x10\x04\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x05\x32\x87\x03\n\x0cMocapService\x12\x8a\x01\n\x19SetVisionPositionEstimate\x12\x32.mavsdk.rpc.mocap.SetVisionPositionEstimateRequest\x1a\x33.mavsdk.rpc.mocap.SetVisionPositionEstimateResponse\"\x04\x80\xb5\x18\x01\x12\x87\x01\n\x18SetAttitudePositionMocap\x12\x31.mavsdk.rpc.mocap.SetAttitudePositionMocapRequest\x1a\x32.mavsdk.rpc.mocap.SetAttitudePositionMocapResponse\"\x04\x80\xb5\x18\x01\x12`\n\x0bSetOdometry\x12$.mavsdk.rpc.mocap.SetOdometryRequest\x1a%.mavsdk.rpc.mocap.SetOdometryResponse\"\x04\x80\xb5\x18\x01\x42\x1d\n\x0fio.mavsdk.mocapB\nMocapProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mocap.mocap_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017io.mavsdk.mocapB\nMocapProto'
  _globals['_MOCAPSERVICE'].methods_by_name['SetVisionPositionEstimate']._loaded_options = None
  _globals['_MOCAPSERVICE'].methods_by_name['SetVisionPositionEstimate']._serialized_options = b'\200\265\030\001'
  _globals['_MOCAPSERVICE'].methods_by_name['SetAttitudePositionMocap']._loaded_options = None
  _globals['_MOCAPSERVICE'].methods_by_name['SetAttitudePositionMocap']._serialized_options = b'\200\265\030\001'
  _globals['_MOCAPSERVICE'].methods_by_name['SetOdometry']._loaded_options = None
  _globals['_MOCAPSERVICE'].methods_by_name['SetOdometry']._serialized_options = b'\200\265\030\001'
  _globals['_SETVISIONPOSITIONESTIMATEREQUEST']._serialized_start=61
  _globals['_SETVISIONPOSITIONESTIMATEREQUEST']._serialized_end=171
  _globals['_SETVISIONPOSITIONESTIMATERESPONSE']._serialized_start=173
  _globals['_SETVISIONPOSITIONESTIMATERESPONSE']._serialized_end=261
  _globals['_SETATTITUDEPOSITIONMOCAPREQUEST']._serialized_start=263
  _globals['_SETATTITUDEPOSITIONMOCAPREQUEST']._serialized_end=370
  _globals['_SETATTITUDEPOSITIONMOCAPRESPONSE']._serialized_start=372
  _globals['_SETATTITUDEPOSITIONMOCAPRESPONSE']._serialized_end=459
  _globals['_SETODOMETRYREQUEST']._serialized_start=461
  _globals['_SETODOMETRYREQUEST']._serialized_end=527
  _globals['_SETODOMETRYRESPONSE']._serialized_start=529
  _globals['_SETODOMETRYRESPONSE']._serialized_end=603
  _globals['_POSITIONBODY']._serialized_start=605
  _globals['_POSITIONBODY']._serialized_end=658
  _globals['_ANGLEBODY']._serialized_start=660
  _globals['_ANGLEBODY']._serialized_end=725
  _globals['_SPEEDBODY']._serialized_start=727
  _globals['_SPEEDBODY']._serialized_end=783
  _globals['_ANGULARVELOCITYBODY']._serialized_start=785
  _globals['_ANGULARVELOCITYBODY']._serialized_end=866
  _globals['_COVARIANCE']._serialized_start=868
  _globals['_COVARIANCE']._serialized_end=907
  _globals['_QUATERNION']._serialized_start=909
  _globals['_QUATERNION']._serialized_end=965
  _globals['_VISIONPOSITIONESTIMATE']._serialized_start=968
  _globals['_VISIONPOSITIONESTIMATE']._serialized_end=1170
  _globals['_ATTITUDEPOSITIONMOCAP']._serialized_start=1173
  _globals['_ATTITUDEPOSITIONMOCAP']._serialized_end=1366
  _globals['_ODOMETRY']._serialized_start=1369
  _globals['_ODOMETRY']._serialized_end=1844
  _globals['_ODOMETRY_MAVFRAME']._serialized_start=1784
  _globals['_ODOMETRY_MAVFRAME']._serialized_end=1844
  _globals['_MOCAPRESULT']._serialized_start=1847
  _globals['_MOCAPRESULT']._serialized_end=2093
  _globals['_MOCAPRESULT_RESULT']._serialized_start=1937
  _globals['_MOCAPRESULT_RESULT']._serialized_end=2093
  _globals['_MOCAPSERVICE']._serialized_start=2096
  _globals['_MOCAPSERVICE']._serialized_end=2487
# @@protoc_insertion_point(module_scope)
