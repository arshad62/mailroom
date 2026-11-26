#!/usr/bin/env python3
"""Mailroom - Kettlebird Tea's Steep Club newsletter tool."""

import csv
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import List


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


def next_send_date(run_date: date) -> date:
    """Return the first Monday of the month after run_date."""
    # First day of the next month
    if run_date.month == 12:
        first_of_next = date(run_date.year + 1, 1, 1)
    else:
        first_of_next = date(run_date.year, run_date.month + 1, 1)

    # Find first Monday (weekday 0 = Monday)
    days_ahead = (0 - first_of_next.weekday()) % 7
    return first_of_next + timedelta(days=days_ahead)


def check_subject(issue_text: str) -> List[str]:
    """Check subject line: max 50 chars, not empty, must exist."""
    problems: List[str] = []

    lines = issue_text.splitlines()
    subject_line = None
    for line in lines:
        if line.startswith("Subject:"):
            subject_line = line
            break

    if subject_line is None:
        problems.append("missing")
        return problems

    subject = subject_line[len("Subject:"):].strip()

    if not subject:
        problems.append("empty")
        return problems

    if len(subject) > 50:
        problems.append("too long")

    return problems


def parse_run_date(arg: str | None) -> date:
    """Parse run date from command line, default to today."""
    if arg:
        return date.fromisoformat(arg)
    return date.today()


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: mailroom <command> [options]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    # Parse common options
    run_date = date.today()
    since_days = None

    i = 0
    while i < len(args):
        if args[i] == "--run-date" and i + 1 < len(args):
            run_date = date.fromisoformat(args[i + 1])
            i += 2
        elif args[i] == "--since-days" and i + 1 < len(args):
            since_days = int(args[i + 1])
            i += 2
        else:
            i += 1

    if command == "subscribers":
        csv_path = "data/subscribers.csv"

        if since_days is not None:
            recent = count_since_days(csv_path, since_days, run_date)
            print(f"Joined in last {since_days} days: {recent}")
        else:
            total = count_subscribers(csv_path)
            groups = count_by_group(csv_path)

            print(f"Total: {total}")
            for group, count in sorted(groups.items()):
                print(f"{group}: {count}")

    elif command == "next-send":
        send_date = next_send_date(run_date)
        print(send_date.isoformat())

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()