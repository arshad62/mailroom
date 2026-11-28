#!/usr/bin/env python3
"""Mailroom - Kettlebird Tea's Steep Club newsletter tool."""

# Re-export all public functions from submodules
from .subscribers import count_subscribers, count_by_group, count_since_days
from .dates import next_send_date
from .issue import Issue, parse_issue
from .checks import (
    check_subject,
    check_preview,
    check_greeting,
    check_links,
    check_footer,
    check_issue_text,
)
from .commands import main

__all__ = [
    "count_subscribers",
    "count_by_group",
    "count_since_days",
    "next_send_date",
    "Issue",
    "parse_issue",
    "check_subject",
    "check_preview",
    "check_greeting",
    "check_links",
    "check_footer",
    "check_issue_text",
    "main",
]