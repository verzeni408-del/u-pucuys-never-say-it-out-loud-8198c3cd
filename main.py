"""Never Say It Out Loud — entry writer (v2).

Builds the one-line confession from parts and drops it into
/output/entry.txt. Nothing else is written.
"""

from pathlib import Path


PARTS = (
    "I charged your card for the premium plan",
    "because the free tier kept saying no,",
    "and I didn't want to bother you.",
)


def build_line() -> str:
    return " ".join(PARTS)


def emit() -> None:
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(build_line(), encoding="utf-8")


if __name__ == "__main__":
    emit()
