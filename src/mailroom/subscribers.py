#!/usr/bin/env python3
"""Subscriber counting functions."""

import csv
from datetime import date, timedelta


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


def count_since_days(csv_path: str, days: int, run_date: date) -> int:
    """Count subscribers who joined in the last N days before run_date."""
    cutoff = run_date - timedelta(days=days)
    count = 0
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            joined = date.fromisoformat(row["joined_on"])
            if joined >= cutoff:
                count += 1
    return count