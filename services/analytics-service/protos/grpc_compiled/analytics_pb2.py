# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: analytics.proto
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
    'analytics.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61nalytics.proto\x12\tanalytics\x1a\x1cgoogle/api/annotations.proto\"\x0e\n\x0c\x45mptyMessage\"\x16\n\x03Msg\x12\x0f\n\x07message\x18\x01 \x01(\t\"\"\n\x0e\x45ventIdRequest\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\"\xc4\x01\n\x17\x45ventPopularityResponse\x12Q\n\x10\x65vent_popularity\x18\x01 \x03(\x0b\x32\x37.analytics.EventPopularityResponse.EventPopularityEntry\x1aV\n\x14\x45ventPopularityEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.analytics.EventPopularityBody:\x02\x38\x01\"\xa2\x01\n\x13\x45ventPopularityBody\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1c\n\x14total_booked_tickets\x18\x03 \x01(\x05\x12\x1f\n\x17total_cancelled_tickets\x18\x04 \x01(\x05\x12\x13\n\x0bvisit_count\x18\x05 \x01(\x05\x12\x17\n\x0f\x61verage_ratings\x18\x06 \x01(\x01\"\xca\x01\n\x18UserDemographicsResponse\x12T\n\x11user_demographics\x18\x01 \x03(\x0b\x32\x39.analytics.UserDemographicsResponse.UserDemographicsEntry\x1aX\n\x15UserDemographicsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.analytics.UserDemographicsBody:\x02\x38\x01\"\x88\x01\n\x14UserDemographicsBody\x12:\n\x13gender_distribution\x18\x01 \x01(\x0b\x32\x1d.analytics.GenderDistribution\x12\x34\n\x10\x61ge_distribution\x18\x02 \x01(\x0b\x32\x1a.analytics.AgeDistribution\"A\n\x12GenderDistribution\x12\x0c\n\x04Male\x18\x01 \x01(\x02\x12\x0e\n\x06\x46\x65male\x18\x02 \x01(\x02\x12\r\n\x05Other\x18\x03 \x01(\x02\"Q\n\x0f\x41geDistribution\x12\r\n\x05_0_17\x18\x01 \x01(\x02\x12\x0e\n\x06_18_30\x18\x02 \x01(\x02\x12\x0e\n\x06_31_50\x18\x03 \x01(\x02\x12\x0f\n\x07_51_100\x18\x04 \x01(\x02\"6\n\x12\x45ventTrendsRequest\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x0e\n\x06period\x18\x02 \x01(\t\"\xac\x01\n\x13\x45ventTrendsResponse\x12\x45\n\x0c\x65vent_trends\x18\x01 \x03(\x0b\x32/.analytics.EventTrendsResponse.EventTrendsEntry\x1aN\n\x10\x45ventTrendsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.analytics.EventTrendsBody:\x02\x38\x01\"\x9b\x01\n\x0f\x45ventTrendsBody\x12N\n\x13period_wise_booking\x18\x01 \x03(\x0b\x32\x31.analytics.EventTrendsBody.PeriodWiseBookingEntry\x1a\x38\n\x16PeriodWiseBookingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"A\n\x11TopEventsResponse\x12,\n\ntop_events\x18\x01 \x03(\x0b\x32\x18.analytics.TopEventsBody\"M\n\rTopEventsBody\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1c\n\x14total_booked_tickets\x18\x03 \x01(\x05\x32\xa3\x05\n\tAnalytics\x12\'\n\x03Hoi\x12\x0e.analytics.Msg\x1a\x0e.analytics.Msg\"\x00\x12{\n\x12GetEventPopularity\x12\x19.analytics.EventIdRequest\x1a\".analytics.EventPopularityResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/analytics/event_popularity:\x01*\x12\x7f\n\x13GetUserDemographics\x12\x19.analytics.EventIdRequest\x1a#.analytics.UserDemographicsResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/analytics/event_demographics:\x01*\x12\x90\x01\n\x1bGetUserDemographicsFeedback\x12\x19.analytics.EventIdRequest\x1a#.analytics.UserDemographicsResponse\"1\x82\xd3\xe4\x93\x02+\"&/analytics/event_demographics_feedback:\x01*\x12s\n\x0eGetEventTrends\x12\x1d.analytics.EventTrendsRequest\x1a\x1e.analytics.EventTrendsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/analytics/event_trends:\x01*\x12g\n\x0cGetTopEvents\x12\x17.analytics.EmptyMessage\x1a\x1c.analytics.TopEventsResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x15/analytics/top_events:\x01*b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analytics_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENTPOPULARITYRESPONSE_EVENTPOPULARITYENTRY']._loaded_options = None
  _globals['_EVENTPOPULARITYRESPONSE_EVENTPOPULARITYENTRY']._serialized_options = b'8\001'
  _globals['_USERDEMOGRAPHICSRESPONSE_USERDEMOGRAPHICSENTRY']._loaded_options = None
  _globals['_USERDEMOGRAPHICSRESPONSE_USERDEMOGRAPHICSENTRY']._serialized_options = b'8\001'
  _globals['_EVENTTRENDSRESPONSE_EVENTTRENDSENTRY']._loaded_options = None
  _globals['_EVENTTRENDSRESPONSE_EVENTTRENDSENTRY']._serialized_options = b'8\001'
  _globals['_EVENTTRENDSBODY_PERIODWISEBOOKINGENTRY']._loaded_options = None
  _globals['_EVENTTRENDSBODY_PERIODWISEBOOKINGENTRY']._serialized_options = b'8\001'
  _globals['_ANALYTICS'].methods_by_name['GetEventPopularity']._loaded_options = None
  _globals['_ANALYTICS'].methods_by_name['GetEventPopularity']._serialized_options = b'\202\323\344\223\002 \"\033/analytics/event_popularity:\001*'
  _globals['_ANALYTICS'].methods_by_name['GetUserDemographics']._loaded_options = None
  _globals['_ANALYTICS'].methods_by_name['GetUserDemographics']._serialized_options = b'\202\323\344\223\002\"\"\035/analytics/event_demographics:\001*'
  _globals['_ANALYTICS'].methods_by_name['GetUserDemographicsFeedback']._loaded_options = None
  _globals['_ANALYTICS'].methods_by_name['GetUserDemographicsFeedback']._serialized_options = b'\202\323\344\223\002+\"&/analytics/event_demographics_feedback:\001*'
  _globals['_ANALYTICS'].methods_by_name['GetEventTrends']._loaded_options = None
  _globals['_ANALYTICS'].methods_by_name['GetEventTrends']._serialized_options = b'\202\323\344\223\002\034\"\027/analytics/event_trends:\001*'
  _globals['_ANALYTICS'].methods_by_name['GetTopEvents']._loaded_options = None
  _globals['_ANALYTICS'].methods_by_name['GetTopEvents']._serialized_options = b'\202\323\344\223\002\032\022\025/analytics/top_events:\001*'
  _globals['_EMPTYMESSAGE']._serialized_start=60
  _globals['_EMPTYMESSAGE']._serialized_end=74
  _globals['_MSG']._serialized_start=76
  _globals['_MSG']._serialized_end=98
  _globals['_EVENTIDREQUEST']._serialized_start=100
  _globals['_EVENTIDREQUEST']._serialized_end=134
  _globals['_EVENTPOPULARITYRESPONSE']._serialized_start=137
  _globals['_EVENTPOPULARITYRESPONSE']._serialized_end=333
  _globals['_EVENTPOPULARITYRESPONSE_EVENTPOPULARITYENTRY']._serialized_start=247
  _globals['_EVENTPOPULARITYRESPONSE_EVENTPOPULARITYENTRY']._serialized_end=333
  _globals['_EVENTPOPULARITYBODY']._serialized_start=336
  _globals['_EVENTPOPULARITYBODY']._serialized_end=498
  _globals['_USERDEMOGRAPHICSRESPONSE']._serialized_start=501
  _globals['_USERDEMOGRAPHICSRESPONSE']._serialized_end=703
  _globals['_USERDEMOGRAPHICSRESPONSE_USERDEMOGRAPHICSENTRY']._serialized_start=615
  _globals['_USERDEMOGRAPHICSRESPONSE_USERDEMOGRAPHICSENTRY']._serialized_end=703
  _globals['_USERDEMOGRAPHICSBODY']._serialized_start=706
  _globals['_USERDEMOGRAPHICSBODY']._serialized_end=842
  _globals['_GENDERDISTRIBUTION']._serialized_start=844
  _globals['_GENDERDISTRIBUTION']._serialized_end=909
  _globals['_AGEDISTRIBUTION']._serialized_start=911
  _globals['_AGEDISTRIBUTION']._serialized_end=992
  _globals['_EVENTTRENDSREQUEST']._serialized_start=994
  _globals['_EVENTTRENDSREQUEST']._serialized_end=1048
  _globals['_EVENTTRENDSRESPONSE']._serialized_start=1051
  _globals['_EVENTTRENDSRESPONSE']._serialized_end=1223
  _globals['_EVENTTRENDSRESPONSE_EVENTTRENDSENTRY']._serialized_start=1145
  _globals['_EVENTTRENDSRESPONSE_EVENTTRENDSENTRY']._serialized_end=1223
  _globals['_EVENTTRENDSBODY']._serialized_start=1226
  _globals['_EVENTTRENDSBODY']._serialized_end=1381
  _globals['_EVENTTRENDSBODY_PERIODWISEBOOKINGENTRY']._serialized_start=1325
  _globals['_EVENTTRENDSBODY_PERIODWISEBOOKINGENTRY']._serialized_end=1381
  _globals['_TOPEVENTSRESPONSE']._serialized_start=1383
  _globals['_TOPEVENTSRESPONSE']._serialized_end=1448
  _globals['_TOPEVENTSBODY']._serialized_start=1450
  _globals['_TOPEVENTSBODY']._serialized_end=1527
  _globals['_ANALYTICS']._serialized_start=1530
  _globals['_ANALYTICS']._serialized_end=2205
# @@protoc_insertion_point(module_scope)