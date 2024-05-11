from __future__ import annotations

from typing import NamedTuple, TypeAlias

from .protos.wire_format_pb2 import WifiCredentialsMetadata


class FileResult(NamedTuple):
    name: str
    path: str
    size: int


class TextResult(NamedTuple):
    text: str


class WifiResult(NamedTuple):
    ssid: str
    password: str
    security_type: WifiCredentialsMetadata.SecurityType


Result: TypeAlias = FileResult | TextResult | WifiResult
