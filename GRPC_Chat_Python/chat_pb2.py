# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"7\n\x0b\x43hatMessage\x12\x17\n\x0fsender_username\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"e\n\x15\x43hatMessageFromServer\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1d\n\x07message\x18\x02 \x01(\x0b\x32\x0c.ChatMessage2J\n\x0b\x43hatService\x12;\n\x0fSendChatMessage\x12\x0c.ChatMessage\x1a\x16.ChatMessageFromServer(\x01\x30\x01\x42\x10\n\x0ema.enset.stubsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016ma.enset.stubs'
  _CHATMESSAGE._serialized_start=47
  _CHATMESSAGE._serialized_end=102
  _CHATMESSAGEFROMSERVER._serialized_start=104
  _CHATMESSAGEFROMSERVER._serialized_end=205
  _CHATSERVICE._serialized_start=207
  _CHATSERVICE._serialized_end=281
# @@protoc_insertion_point(module_scope)
