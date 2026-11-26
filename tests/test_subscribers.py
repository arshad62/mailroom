#!/usr/bin/env python3
"""Tests for subscriber counting functions."""

from datetime import date
from mailroom import count_subscribers, count_by_group, count_since_days, next_send_date


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