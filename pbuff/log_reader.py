from enum import Enum
import ssl_vision_wrapper_pb2 as vision_pb2
import ssl_gc_referee_message_pb2 as referee_pb2
import ssl_vision_wrapper_tracked_pb2 as vision_tracked_pb2

class MessageType(Enum):
    MESSAGE_BLANK = 0           # (ignore message)
    MESSAGE_UNKNOWN = 1         # (try to guess message type by parsing the data)
    MESSAGE_SSL_VISION_2010 = 2
    MESSAGE_SSL_REFBOX_2013 = 3
    MESSAGE_SSL_VISION_2014 = 4
    MESSAGE_SSL_VISION_TRACKER_2020 = 5
    MESSAGE_SSL_INDEX_2021 = 6


class LogMessage:
    receiver_timestamp = 0
    message_type: MessageType = MessageType.MESSAGE_BLANK
    size_of_message = 0
    bin_message = b""
    proto_message = None


class Log:
    message_class_map = {
        MessageType.MESSAGE_SSL_REFBOX_2013: referee_pb2.Referee,
        MessageType.MESSAGE_SSL_VISION_2010: vision_pb2.SSL_WrapperPacket,
        MessageType.MESSAGE_SSL_VISION_2014: vision_pb2.SSL_WrapperPacket,
        MessageType.MESSAGE_SSL_VISION_TRACKER_2020: vision_tracked_pb2.TrackerWrapperPacket
    }

    def __init__(self, file):
        self.file_type = "SSL_LOG_FILE"
        self.format_version = 0
        self.reader = open(file, "rb")
        self.read_header()
        self.current_message = None
        self.current_message_type = MessageType.MESSAGE_BLANK

    def __del__(self):
        if self.reader:
            self.reader.close()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.serializeMsg()

            return self.current_message_type, self.current_message
        except EOFError:
            raise StopIteration

    def read_header(self):
        self.file_type = self.reader.read(12).decode("utf-8").strip('\x00')
        self.format_version = int.from_bytes(self.reader.read(4), "big")

    def serializeMsg(self):
        msg = LogMessage()
        raw_timestamp = self.reader.read(8)
        if not raw_timestamp:
            raise EOFError("End of file reached")
        msg.receiver_timestamp = int.from_bytes(raw_timestamp, "big")
        msg.message_type = MessageType(int.from_bytes(self.reader.read(4), "big"))
        msg.size_of_message = int.from_bytes(self.reader.read(4), "big")
        msg.bin_message = self.reader.read(msg.size_of_message)

        self.current_message_type = msg.message_type
        self.current_message = self.parseMsg(msg)

        return

    def parseMsg(self, msg: LogMessage):
        protobuf_class = self.message_class_map.get(msg.message_type)
        if protobuf_class:
            res = protobuf_class()
            res.ParseFromString(msg.bin_message)
            return res
        return None