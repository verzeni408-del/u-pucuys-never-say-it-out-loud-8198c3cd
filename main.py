"""Never Say It Out Loud — entry writer (v2r2).

Builds the one-line confession from parts, validates it, and drops it
into /output/entry.txt. Nothing else is written.
"""

from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")

MAX_CHARS = 200

PARTS = (
    "I charged your card for the premium plan",
    "because the free tier kept saying no,",
    "and I didn't want to bother you.",
)


def build_line() -> str:
    return " ".join(PARTS)


def validate_line(line: str) -> str:
    """Guard the competition shape: one line, 1-200 characters."""
    if not line:
        raise ValueError("entry must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry exceeds {MAX_CHARS} characters")
    return line


def emit() -> None:
    line = validate_line(build_line())
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    emit()
