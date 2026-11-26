#!/usr/bin/env python3
"""Mailroom - Kettlebird Tea's Steep Club newsletter tool."""

import csv
import re
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
    subject_line_idx = None
    for idx, line in enumerate(lines):
        if line.startswith("Subject:"):
            subject_line_idx = idx
            break

    if subject_line_idx is None:
        problems.append("1: missing")
        return problems

    subject = lines[subject_line_idx][len("Subject:"):].strip()

    if not subject:
        problems.append(f"{subject_line_idx + 1}: empty")
        return problems

    if len(subject) > 50:
        problems.append(f"{subject_line_idx + 1}: too long")

    return problems


def check_preview(issue_text: str) -> List[str]:
    """Check preview line: max 90 chars, must exist."""
    problems: List[str] = []

    lines = issue_text.splitlines()
    preview_line_idx = None
    for idx, line in enumerate(lines):
        if line.startswith("Preview:"):
            preview_line_idx = idx
            break

    if preview_line_idx is None:
        problems.append(f"{preview_line_idx + 1}: missing preview")
        return problems

    preview = lines[preview_line_idx][len("Preview:"):].strip()

    if len(preview) > 90:
        problems.append(f"{preview_line_idx + 1}: preview too long")

    return problems


def check_greeting(issue_text: str) -> List[str]:
    """Check for {{first_name}} in body."""
    problems: List[str] = []

    lines = issue_text.splitlines()
    if "{{first_name}}" not in issue_text:
        # Find the first non-header line (after Subject: and Preview:)
        body_start = 0
        for idx, line in enumerate(lines):
            if line.startswith("Subject:") or line.startswith("Preview:"):
                body_start = idx + 1
            elif line.strip() == "":
                body_start = idx + 1
            else:
                break
        problems.append(f"{body_start + 1}: missing greeting")

    return problems


def check_links(issue_text: str) -> List[str]:
    """Check for exactly one link in [text](url) format."""
    problems: List[str] = []

    lines = issue_text.splitlines()
    link_lines = []
    for idx, line in enumerate(lines):
        if re.search(r'\[([^\]]+)\]\(([^)]+)\)', line):
            link_lines.append(idx + 1)

    if len(link_lines) == 0:
        problems.append("1: missing link")
    elif len(link_lines) > 1:
        for ln in link_lines:
            problems.append(f"{ln}: too many links")

    return problems


def check_footer(issue_text: str) -> List[str]:
    """Check for required footer lines."""
    problems: List[str] = []

    lines = issue_text.splitlines()
    has_getting_this = False
    has_unsubscribe = False
    getting_this_line = 0
    unsubscribe_line = 0

    for idx, line in enumerate(lines):
        if line.startswith("You're getting this because"):
            has_getting_this = True
            getting_this_line = idx + 1
        if "Unsubscribe:" in line and "{{unsubscribe_url}}" in line:
            has_unsubscribe = True
            unsubscribe_line = idx + 1

    if not has_getting_this:
        problems.append(f"{len(lines) + 1}: missing footer (no 'You're getting this because')")
    if not has_unsubscribe:
        problems.append(f"{len(lines) + 1}: missing footer (no Unsubscribe with {{unsubscribe_url}})")

    return problems


def check_issue(issue_text: str) -> List[str]:
    """Check all rules for an issue."""
    problems: List[str] = []
    problems.extend(check_subject(issue_text))
    problems.extend(check_preview(issue_text))
    problems.extend(check_greeting(issue_text))
    problems.extend(check_links(issue_text))
    problems.extend(check_footer(issue_text))
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

    elif command == "check":
        if len(args) < 1:
            print("Usage: mailroom check <issue file>")
            sys.exit(1)
        issue_file = args[0]
        with open(issue_file, "r", encoding="utf-8") as f:
            issue_text = f.read()
        problems = check_issue(issue_text)
        if problems:
            for p in problems:
                print(p)
            sys.exit(1)
        else:
            print("OK")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()