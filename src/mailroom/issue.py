#!/usr/bin/env python3
"""Issue data structure and parsing."""

from dataclasses import dataclass
from typing import List


@dataclass
class Issue:
    """Parsed newsletter issue."""
    subject: str
    preview: str
    body: str
    links: List[str]


def parse_issue(issue_text: str) -> Issue:
    """Parse issue text into Issue object."""
    lines = issue_text.splitlines()

    subject = ""
    preview = ""
    body_lines = []

    state = "headers"
    for line in lines:
        if state == "headers":
            if line.startswith("Subject:"):
                # Don't strip - preserve empty/whitespace for validation
                subject = line[len("Subject:"):]
            elif line.startswith("Preview:"):
                preview = line[len("Preview:"):].strip()
            elif line.strip() == "":
                state = "body"
            else:
                body_lines.append(line)
        else:
            body_lines.append(line)

    body = "\n".join(body_lines).strip()

    # Extract links from body
    import re
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', body)
    link_urls = [url for _, url in links]

    return Issue(
        subject=subject,
        preview=preview,
        body=body,
        links=link_urls
    )