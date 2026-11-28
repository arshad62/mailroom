#!/usr/bin/env python3
"""Date functions for Mailroom."""

from datetime import date, timedelta


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