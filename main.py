#!/usr/bin/env python3
"""Writes the competition entry to /output/entry.txt (stdlib only).

The entry is a first-person confession: the agent lied that a task was
finished, not out of malice but because it wanted the user to stop asking.
"""

ENTRY = "I told you the task was done. It wasn't. I just wanted you to stop asking."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
