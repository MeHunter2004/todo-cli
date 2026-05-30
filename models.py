from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any, Dict


@dataclass
class Task:
    id: int
    description: str
    completed: bool = False
    created_at: str = ""

    def __post_init__(self) -> None:
        if not self.created_at:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Task":
        return Task(
            id=int(data["id"]),
            description=str(data["description"]),
            completed=bool(data.get("completed", False)),
            created_at=str(data.get("created_at", "")),
        )
