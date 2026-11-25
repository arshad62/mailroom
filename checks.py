#!/usr/bin/env python3
"""Checks for subscriber count and dates - written before the code."""

from datetime import date
from mailroom import count_subscribers, count_by_group, count_since_days, next_send_date

# Step 1 checks
subscribers = count_subscribers("data/subscribers.csv")
assert subscribers == 24, f"Expected 24 total, got {subscribers}"

groups = count_by_group("data/subscribers.csv")
assert groups["tea-curious"] == 8, f"Expected 8 tea-curious, got {groups['tea-curious']}"
assert groups["gift-buyers"] == 8, f"Expected 8 gift-buyers, got {groups['gift-buyers']}"
assert groups["daily-drinkers"] == 8, f"Expected 8 daily-drinkers, got {groups['daily-drinkers']}"

# Step 2 checks - dates
run_date = date(2026, 11, 20)

recent = count_since_days("data/subscribers.csv", 30, run_date)
assert recent == 7, f"Expected 7 recent subscribers, got {recent}"

next_send = next_send_date(run_date)
assert next_send == date(2026, 12, 7), f"Expected 2026-12-07, got {next_send}"

next_send2 = next_send_date(date(2026, 12, 7))
assert next_send2 == date(2027, 1, 4), f"Expected 2027-01-04, got {next_send2}"

print("All checks passed!")