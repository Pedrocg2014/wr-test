# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssl_gc_referee_message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ssl_gc_game_event_pb2 as ssl__gc__game__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cssl_gc_referee_message.proto\x1a\x17ssl_gc_game_event.proto\"\xd9\r\n\x07Referee\x12\x19\n\x11source_identifier\x18\x12 \x01(\t\x12-\n\nmatch_type\x18\x13 \x01(\x0e\x32\n.MatchType:\rUNKNOWN_MATCH\x12\x18\n\x10packet_timestamp\x18\x01 \x02(\x04\x12\x1d\n\x05stage\x18\x02 \x02(\x0e\x32\x0e.Referee.Stage\x12\x17\n\x0fstage_time_left\x18\x03 \x01(\x11\x12!\n\x07\x63ommand\x18\x04 \x02(\x0e\x32\x10.Referee.Command\x12\x17\n\x0f\x63ommand_counter\x18\x05 \x02(\r\x12\x19\n\x11\x63ommand_timestamp\x18\x06 \x02(\x04\x12!\n\x06yellow\x18\x07 \x02(\x0b\x32\x11.Referee.TeamInfo\x12\x1f\n\x04\x62lue\x18\x08 \x02(\x0b\x32\x11.Referee.TeamInfo\x12+\n\x13\x64\x65signated_position\x18\t \x01(\x0b\x32\x0e.Referee.Point\x12\"\n\x1a\x62lue_team_on_positive_half\x18\n \x01(\x08\x12&\n\x0cnext_command\x18\x0c \x01(\x0e\x32\x10.Referee.Command\x12\x1f\n\x0bgame_events\x18\x10 \x03(\x0b\x32\n.GameEvent\x12\x35\n\x14game_event_proposals\x18\x11 \x03(\x0b\x32\x17.GameEventProposalGroup\x12%\n\x1d\x63urrent_action_time_remaining\x18\x0f \x01(\x05\x1a\x80\x03\n\x08TeamInfo\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05score\x18\x02 \x02(\r\x12\x11\n\tred_cards\x18\x03 \x02(\r\x12\x1d\n\x11yellow_card_times\x18\x04 \x03(\rB\x02\x10\x01\x12\x14\n\x0cyellow_cards\x18\x05 \x02(\r\x12\x10\n\x08timeouts\x18\x06 \x02(\r\x12\x14\n\x0ctimeout_time\x18\x07 \x02(\r\x12\x12\n\ngoalkeeper\x18\x08 \x02(\r\x12\x14\n\x0c\x66oul_counter\x18\t \x01(\r\x12\x1f\n\x17\x62\x61ll_placement_failures\x18\n \x01(\r\x12\x16\n\x0e\x63\x61n_place_ball\x18\x0c \x01(\x08\x12\x18\n\x10max_allowed_bots\x18\r \x01(\r\x12\x1f\n\x17\x62ot_substitution_intent\x18\x0e \x01(\x08\x12\'\n\x1f\x62\x61ll_placement_failures_reached\x18\x0f \x01(\x08\x12 \n\x18\x62ot_substitution_allowed\x18\x10 \x01(\x08\x1a\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\"\xd1\x02\n\x05Stage\x12\x19\n\x15NORMAL_FIRST_HALF_PRE\x10\x00\x12\x15\n\x11NORMAL_FIRST_HALF\x10\x01\x12\x14\n\x10NORMAL_HALF_TIME\x10\x02\x12\x1a\n\x16NORMAL_SECOND_HALF_PRE\x10\x03\x12\x16\n\x12NORMAL_SECOND_HALF\x10\x04\x12\x14\n\x10\x45XTRA_TIME_BREAK\x10\x05\x12\x18\n\x14\x45XTRA_FIRST_HALF_PRE\x10\x06\x12\x14\n\x10\x45XTRA_FIRST_HALF\x10\x07\x12\x13\n\x0f\x45XTRA_HALF_TIME\x10\x08\x12\x19\n\x15\x45XTRA_SECOND_HALF_PRE\x10\t\x12\x15\n\x11\x45XTRA_SECOND_HALF\x10\n\x12\x1a\n\x16PENALTY_SHOOTOUT_BREAK\x10\x0b\x12\x14\n\x10PENALTY_SHOOTOUT\x10\x0c\x12\r\n\tPOST_GAME\x10\r\"\x96\x03\n\x07\x43ommand\x12\x08\n\x04HALT\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\x10\n\x0cNORMAL_START\x10\x02\x12\x0f\n\x0b\x46ORCE_START\x10\x03\x12\x1a\n\x16PREPARE_KICKOFF_YELLOW\x10\x04\x12\x18\n\x14PREPARE_KICKOFF_BLUE\x10\x05\x12\x1a\n\x16PREPARE_PENALTY_YELLOW\x10\x06\x12\x18\n\x14PREPARE_PENALTY_BLUE\x10\x07\x12\x16\n\x12\x44IRECT_FREE_YELLOW\x10\x08\x12\x14\n\x10\x44IRECT_FREE_BLUE\x10\t\x12\x1c\n\x14INDIRECT_FREE_YELLOW\x10\n\x1a\x02\x08\x01\x12\x1a\n\x12INDIRECT_FREE_BLUE\x10\x0b\x1a\x02\x08\x01\x12\x12\n\x0eTIMEOUT_YELLOW\x10\x0c\x12\x10\n\x0cTIMEOUT_BLUE\x10\r\x12\x13\n\x0bGOAL_YELLOW\x10\x0e\x1a\x02\x08\x01\x12\x11\n\tGOAL_BLUE\x10\x0f\x1a\x02\x08\x01\x12\x19\n\x15\x42\x41LL_PLACEMENT_YELLOW\x10\x10\x12\x17\n\x13\x42\x41LL_PLACEMENT_BLUE\x10\x11J\x04\x08\x0b\x10\x0cJ\x04\x08\r\x10\x0eJ\x04\x08\x0e\x10\x0f\"J\n\x16GameEventProposalGroup\x12\x1e\n\ngame_event\x18\x01 \x03(\x0b\x32\n.GameEvent\x12\x10\n\x08\x61\x63\x63\x65pted\x18\x02 \x01(\x08*T\n\tMatchType\x12\x11\n\rUNKNOWN_MATCH\x10\x00\x12\x0f\n\x0bGROUP_PHASE\x10\x01\x12\x15\n\x11\x45LIMINATION_PHASE\x10\x02\x12\x0c\n\x08\x46RIENDLY\x10\x03\x42\x36Z4github.com/RoboCup-SSL/ssl-go-tools/internal/referee')

_MATCHTYPE = DESCRIPTOR.enum_types_by_name['MatchType']
MatchType = enum_type_wrapper.EnumTypeWrapper(_MATCHTYPE)
UNKNOWN_MATCH = 0
GROUP_PHASE = 1
ELIMINATION_PHASE = 2
FRIENDLY = 3


_REFEREE = DESCRIPTOR.message_types_by_name['Referee']
_REFEREE_TEAMINFO = _REFEREE.nested_types_by_name['TeamInfo']
_REFEREE_POINT = _REFEREE.nested_types_by_name['Point']
_GAMEEVENTPROPOSALGROUP = DESCRIPTOR.message_types_by_name['GameEventProposalGroup']
_REFEREE_STAGE = _REFEREE.enum_types_by_name['Stage']
_REFEREE_COMMAND = _REFEREE.enum_types_by_name['Command']
Referee = _reflection.GeneratedProtocolMessageType('Referee', (_message.Message,), {

  'TeamInfo' : _reflection.GeneratedProtocolMessageType('TeamInfo', (_message.Message,), {
    'DESCRIPTOR' : _REFEREE_TEAMINFO,
    '__module__' : 'ssl_gc_referee_message_pb2'
    # @@protoc_insertion_point(class_scope:Referee.TeamInfo)
    })
  ,

  'Point' : _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
    'DESCRIPTOR' : _REFEREE_POINT,
    '__module__' : 'ssl_gc_referee_message_pb2'
    # @@protoc_insertion_point(class_scope:Referee.Point)
    })
  ,
  'DESCRIPTOR' : _REFEREE,
  '__module__' : 'ssl_gc_referee_message_pb2'
  # @@protoc_insertion_point(class_scope:Referee)
  })
_sym_db.RegisterMessage(Referee)
_sym_db.RegisterMessage(Referee.TeamInfo)
_sym_db.RegisterMessage(Referee.Point)

GameEventProposalGroup = _reflection.GeneratedProtocolMessageType('GameEventProposalGroup', (_message.Message,), {
  'DESCRIPTOR' : _GAMEEVENTPROPOSALGROUP,
  '__module__' : 'ssl_gc_referee_message_pb2'
  # @@protoc_insertion_point(class_scope:GameEventProposalGroup)
  })
_sym_db.RegisterMessage(GameEventProposalGroup)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4github.com/RoboCup-SSL/ssl-go-tools/internal/referee'
  _REFEREE_TEAMINFO.fields_by_name['yellow_card_times']._options = None
  _REFEREE_TEAMINFO.fields_by_name['yellow_card_times']._serialized_options = b'\020\001'
  _REFEREE_COMMAND.values_by_name["INDIRECT_FREE_YELLOW"]._options = None
  _REFEREE_COMMAND.values_by_name["INDIRECT_FREE_YELLOW"]._serialized_options = b'\010\001'
  _REFEREE_COMMAND.values_by_name["INDIRECT_FREE_BLUE"]._options = None
  _REFEREE_COMMAND.values_by_name["INDIRECT_FREE_BLUE"]._serialized_options = b'\010\001'
  _REFEREE_COMMAND.values_by_name["GOAL_YELLOW"]._options = None
  _REFEREE_COMMAND.values_by_name["GOAL_YELLOW"]._serialized_options = b'\010\001'
  _REFEREE_COMMAND.values_by_name["GOAL_BLUE"]._options = None
  _REFEREE_COMMAND.values_by_name["GOAL_BLUE"]._serialized_options = b'\010\001'
  _MATCHTYPE._serialized_start=1889
  _MATCHTYPE._serialized_end=1973
  _REFEREE._serialized_start=58
  _REFEREE._serialized_end=1811
  _REFEREE_TEAMINFO._serialized_start=629
  _REFEREE_TEAMINFO._serialized_end=1013
  _REFEREE_POINT._serialized_start=1015
  _REFEREE_POINT._serialized_end=1044
  _REFEREE_STAGE._serialized_start=1047
  _REFEREE_STAGE._serialized_end=1384
  _REFEREE_COMMAND._serialized_start=1387
  _REFEREE_COMMAND._serialized_end=1793
  _GAMEEVENTPROPOSALGROUP._serialized_start=1813
  _GAMEEVENTPROPOSALGROUP._serialized_end=1887
# @@protoc_insertion_point(module_scope)
