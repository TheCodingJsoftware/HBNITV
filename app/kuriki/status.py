from dataclasses import dataclass
from enum import Enum

class StateType(str, Enum):
    new = "new"
    maintained = "maintained"

@dataclass(frozen=True)
class Status:
    state: StateType

    def to_dict(self) -> str:
        return self.state