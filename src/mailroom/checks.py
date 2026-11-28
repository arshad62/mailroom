#!/usr/bin/env python3
"""Issue checking functions."""

import re
from typing import List

from .issue import Issue, parse_issue


def check_subject(issue: Issue) -> List[str]:
    """Check subject line: max 50 chars, not empty, must exist."""
    problems: List[str] = []

    # Check if subject was present (even if just whitespace)
    if not issue.subject and issue.subject != " ":
        problems.append("1: missing")
        return problems

    if not issue.subject.strip():
        problems.append("1: empty")
        return problems

    # Count length after stripping (the actual content)
    if len(issue.subject.strip()) > 50:
        problems.append(f"1: too long")

    return problems


def check_preview(issue: Issue) -> List[str]:
    """Check preview line: max 90 chars, must exist."""
    problems: List[str] = []

    if not issue.preview:
        problems.append("2: missing preview")
        return problems

    if len(issue.preview) > 90:
        problems.append(f"2: preview too long")

    return problems


def check_greeting(issue: Issue) -> List[str]:
    """Check for {{first_name}} in body."""
    problems: List[str] = []

    if "{{first_name}}" not in issue.body:
        # Find the first non-header line (after Subject: and Preview:)
        body_lines = issue.body.splitlines()
        body_start = 0
        for idx, line in enumerate(body_lines):
            if line.startswith("Subject:") or line.startswith("Preview:"):
                body_start = idx + 1
            elif line.strip() == "":
                body_start = idx + 1
            else:
                break
        problems.append(f"{body_start + 3}: missing greeting")

    return problems


def check_links(issue: Issue) -> List[str]:
    """Check for exactly one link in [text](url) format."""
    problems: List[str] = []

    link_lines = []
    body_lines = issue.body.splitlines()
    for idx, line in enumerate(body_lines):
        if re.search(r'\[([^\]]+)\]\(([^)]+)\)', line):
            link_lines.append(idx + 4)  # +3 for Subject:, Preview:, blank line

    if len(link_lines) == 0:
        problems.append("1: missing link")
    elif len(link_lines) > 1:
        for ln in link_lines:
            problems.append(f"{ln}: too many links")

    return problems


def check_footer(issue: Issue) -> List[str]:
    """Check for required footer lines."""
    problems: List[str] = []

    body_lines = issue.body.splitlines()
    has_getting_this = False
    has_unsubscribe = False

    for idx, line in enumerate(body_lines):
        if line.startswith("You're getting this because"):
            has_getting_this = True
        if "Unsubscribe:" in line and "{{unsubscribe_url}}" in line:
            has_unsubscribe = True

    if not has_getting_this:
        problems.append(f"{len(body_lines) + 4}: missing footer (no 'You're getting this because')")
    if not has_unsubscribe:
        problems.append(f"{len(body_lines) + 4}: missing footer (no Unsubscribe with {{unsubscribe_url}})")

    return problems


def check_issue_text(issue_text: str) -> List[str]:
    """Check all rules for an issue text."""
    issue = parse_issue(issue_text)
    problems: List[str] = []
    problems.extend(check_subject(issue))
    problems.extend(check_preview(issue))
    problems.extend(check_greeting(issue))
    problems.extend(check_links(issue))
    problems.extend(check_footer(issue))
    return problems