#!/usr/bin/env python3
"""Command-line interface for Mailroom."""

import sys
from datetime import date

from .subscribers import count_subscribers, count_by_group, count_since_days
from .dates import next_send_date
from .checks import check_issue_text


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
        problems = check_issue_text(issue_text)
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