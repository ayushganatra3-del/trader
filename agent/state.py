"""Durable state: one JSON document plus append-only logs, written atomically."""
from __future__ import annotations

import contextlib
import fcntl
import json
import os
import tempfile
from pathlib import Path

STATE_VERSION = 1


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


class StateStore:
    def __init__(self, folder: str | os.PathLike):
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=True)
        self.path = self.folder / "state.json"

    def load(self) -> dict | None:
        if not self.path.exists():
            return None
        state = json.loads(self.path.read_text(encoding="utf-8"))
        if state.get("version") != STATE_VERSION:
            raise ValueError(f"Unsupported state version {state.get('version')}")
        return state

    def save(self, state: dict) -> None:
        atomic_write(self.path, json.dumps(state, indent=1, allow_nan=False, default=str) + "\n")

    def append(self, name: str, rows: list[dict]) -> None:
        if not rows:
            return
        with (self.folder / name).open("a", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, allow_nan=False, default=str, separators=(",", ":")) + "\n")

    def read_jsonl(self, name: str, tail: int | None = None) -> list[dict]:
        path = self.folder / name
        if not path.exists():
            return []
        lines = path.read_text(encoding="utf-8").splitlines()
        if tail:
            lines = lines[-tail:]
        return [json.loads(line) for line in lines if line.strip()]

    @contextlib.contextmanager
    def lock(self):
        with (self.folder / ".agent.lock").open("a+") as handle:
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as error:
                raise RuntimeError("Another agent process is using this state folder") from error
            try:
                yield
            finally:
                fcntl.flock(handle, fcntl.LOCK_UN)
