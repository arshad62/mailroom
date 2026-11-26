#!/usr/bin/env python3
"""Tests for subscriber counting functions."""

from datetime import date
from mailroom import count_subscribers, count_by_group, count_since_days, next_send_date, check_subject, check_issue


def test_count_subscribers():
    """Test total subscriber count."""
    subscribers = count_subscribers("data/subscribers.csv")
    assert subscribers == 24, f"Expected 24 total, got {subscribers}"


def test_count_by_group_tea_curious():
    """Test tea-curious group count."""
    groups = count_by_group("data/subscribers.csv")
    assert groups["tea-curious"] == 8, f"Expected 8 tea-curious, got {groups['tea-curious']}"


def test_count_by_group_gift_buyers():
    """Test gift-buyers group count."""
    groups = count_by_group("data/subscribers.csv")
    assert groups["gift-buyers"] == 8, f"Expected 8 gift-buyers, got {groups['gift-buyers']}"


def test_count_by_group_daily_drinkers():
    """Test daily-drinkers group count."""
    groups = count_by_group("data/subscribers.csv")
    assert groups["daily-drinkers"] == 8, f"Expected 8 daily-drinkers, got {groups['daily-drinkers']}"


def test_count_since_days_30():
    """Test subscribers who joined in last 30 days."""
    run_date = date(2026, 11, 20)
    recent = count_since_days("data/subscribers.csv", 30, run_date)
    assert recent == 7, f"Expected 7 recent subscribers, got {recent}"


def test_next_send_date_from_nov_20():
    """Test next send date from 2026-11-20."""
    run_date = date(2026, 11, 20)
    next_send = next_send_date(run_date)
    assert next_send == date(2026, 12, 7), f"Expected 2026-12-07, got {next_send}"


def test_next_send_date_from_dec_7():
    """Test next send date from 2026-12-07 (should be first Monday of Jan)."""
    run_date = date(2026, 12, 7)
    next_send = next_send_date(run_date)
    assert next_send == date(2027, 1, 4), f"Expected 2027-01-04, got {next_send}"


# Step 5: check_subject tests
def test_check_subject_normal():
    """Normal subject under 50 chars."""
    issue = "Subject: The Steep Club opens Monday\n\nBody"
    assert check_subject(issue) == []


def test_check_subject_exactly_50():
    """Subject exactly 50 chars is OK."""
    issue = "Subject: Your Steep Club box ships on Monday with new teas.\n\nBody"
    assert check_subject(issue) == []


def test_check_subject_51_chars():
    """Subject 51 chars is too long."""
    issue = "Subject: Your Steep Club box ships on Monday with fresh teas\n\nBody"
    problems = check_subject(issue)
    assert len(problems) == 1
    assert "too long" in problems[0]


def test_check_subject_empty():
    """Empty subject is a problem."""
    issue = "Subject: \n\nBody"
    problems = check_subject(issue)
    assert len(problems) == 1
    assert "empty" in problems[0]


def test_check_subject_only_spaces():
    """Subject with only spaces is empty."""
    issue = "Subject:    \n\nBody"
    problems = check_subject(issue)
    assert len(problems) == 1
    assert "empty" in problems[0]


def test_check_subject_missing():
    """Missing Subject line is a problem."""
    issue = "No subject here\n\nBody"
    problems = check_subject(issue)
    assert len(problems) == 1
    assert "missing" in problems[0]


# Step 6: check_issue tests
def test_check_issue_valid():
    """issue-01.md passes all checks."""
    with open("issues/issue-01.md", "r") as f:
        issue = f.read()
    assert check_issue(issue) == []


def test_check_issue_preview_too_long():
    """Preview over 90 chars fails."""
    issue = """Subject: Test
Preview: """ + "x" * 91 + """

Hi {{first_name}},
[Link](https://example.com)

You're getting this because...
Unsubscribe: {{unsubscribe_url}}"""
    problems = check_issue(issue)
    assert any("preview" in p.lower() for p in problems)


def test_check_issue_missing_greeting():
    """Missing {{first_name}} fails."""
    issue = """Subject: Test
Preview: Short preview

Hi there,
[Link](https://example.com)

You're getting this because...
Unsubscribe: {{unsubscribe_url}}"""
    problems = check_issue(issue)
    assert any("greeting" in p.lower() or "first_name" in p.lower() for p in problems)


def test_check_issue_two_links():
    """Two links fails."""
    issue = """Subject: Test
Preview: Short preview

Hi {{first_name}},
[Link 1](https://example.com)
[Link 2](http://another.com)

You're getting this because...
Unsubscribe: {{unsubscribe_url}}"""
    problems = check_issue(issue)
    assert any("link" in p.lower() for p in problems)


def test_check_issue_missing_footer_and_greeting():
    """Missing footer and greeting gives two problems."""
    issue = """Subject: Test
Preview: Short preview

Hi there,
[Link](https://example.com)"""
    problems = check_issue(issue)
    assert len(problems) >= 2
    assert any("greeting" in p.lower() or "first_name" in p.lower() for p in problems)
    assert any("footer" in p.lower() or "unsubscribe" in p.lower() for p in problems)


# Step 7: Emoji length test
def test_check_subject_emoji():
    """Emoji subject counts as Python len() (codepoints)."""
    # 👍🏽 is 2 codepoints (U+1F44D + U+1F3FD)
    subject = "👍🏽 Thanks for joining"
    assert len(subject) == 21  # Python counts codepoints
    issue = f"Subject: {subject}\n\nBody"
    problems = check_subject(issue)
    assert problems == []  # 21 <= 50, so OK