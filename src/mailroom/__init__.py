#!/usr/bin/env python3
"""Mailroom - Kettlebird Tea's Steep Club newsletter tool."""

import csv
import sys
from pathlib import Path


def count_subscribers(csv_path: str) -> int:
    """Count total subscribers in CSV file."""
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return sum(1 for _ in reader)


def count_by_group(csv_path: str) -> dict[str, int]:
    """Count subscribers by group."""
    counts: dict[str, int] = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            group = row["group"]
            counts[group] = counts.get(group, 0) + 1
    return counts


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: mailroom.py <command>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "subscribers":
        csv_path = "data/subscribers.csv"
        total = count_subscribers(csv_path)
        groups = count_by_group(csv_path)

        print(f"Total: {total}")
        for group, count in sorted(groups.items()):
            print(f"{group}: {count}")
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()