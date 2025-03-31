from _typeshed import Incomplete
from typing import Any

from .segment import Segment

MUTATION_UNSUPPORTED_MESSAGE: str

class FacadeSegment(Segment):
    initializing: Any
    def __init__(self, name, entityid, traceid, sampled) -> None: ...
    def close(self, end_time: Incomplete | None = None) -> None: ...
    def put_http_meta(self, key, value) -> None: ...
    def put_annotation(self, key, value) -> None: ...
    def put_metadata(self, key, value, namespace: str = "default") -> None: ...
    def set_aws(self, aws_meta) -> None: ...
    def set_user(self, user) -> None: ...
    def add_throttle_flag(self) -> None: ...
    def add_fault_flag(self) -> None: ...
    def add_error_flag(self) -> None: ...
    def add_exception(self, exception, stack, remote: bool = False) -> None: ...
    def apply_status_code(self, status_code) -> None: ...
    def serialize(self) -> None: ...
    def ready_to_send(self): ...
    def increment(self) -> None: ...
    def decrement_ref_counter(self) -> None: ...
