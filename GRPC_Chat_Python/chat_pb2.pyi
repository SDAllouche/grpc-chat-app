from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatMessage(_message.Message):
    __slots__ = ["message", "sender_username"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    message: str
    sender_username: str
    def __init__(self, sender_username: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class ChatMessageFromServer(_message.Message):
    __slots__ = ["message", "timestamp"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    message: ChatMessage
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[_Union[ChatMessage, _Mapping]] = ...) -> None: ...
