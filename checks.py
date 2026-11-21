#!/usr/bin/env python3
"""Checks for subscriber count - written before the code."""

from mailroom import count_subscribers, count_by_group

subscribers = count_subscribers("data/subscribers.csv")
assert subscribers == 24, f"Expected 24 total, got {subscribers}"

groups = count_by_group("data/subscribers.csv")
assert groups["tea-curious"] == 8, f"Expected 8 tea-curious, got {groups['tea-curious']}"
assert groups["gift-buyers"] == 8, f"Expected 8 gift-buyers, got {groups['gift-buyers']}"
assert groups["daily-drinkers"] == 8, f"Expected 8 daily-drinkers, got {groups['daily-drinkers']}"

print("All checks passed!")