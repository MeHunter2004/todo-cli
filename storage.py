import json
from json import JSONDecodeError
from pathlib import Path
from typing import List

from models import Task

DATA_FILE = Path("data") / "tasks.json"


def load_tasks() -> List[Task]:
    DATA_FILE.parent.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")
        return []

    try:
        raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        if not isinstance(raw, list):
            return []
        return [Task.from_dict(item) for item in raw]
    except (JSONDecodeError, OSError, TypeError, ValueError):
        return []


def save_tasks(tasks: List[Task]) -> None:
    DATA_FILE.parent.mkdir(exist_ok=True)
    payload = [t.to_dict() for t in tasks]
    DATA_FILE.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
