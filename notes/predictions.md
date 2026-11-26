# Predictions

## Step 0 - The Base

### Newsletter Name
Kettlebird Tea's Steep Club

### Audience
Tea enthusiasts who want curated loose-leaf teas delivered monthly

### Expected Project Structure
- Python project with uv and Python 3.12+
- AGENTS.md with project rules
- CLAUDE.md that imports AGENTS.md
- Git repository
- Public GitHub repository called "mailroom"

## Step 1 - Count Subscribers

### Expected Results
- Total subscribers: 24
- tea-curious: 8
- gift-buyers: 8
- daily-drinkers: 8

## Step 2 - Dates

### Expected Results (run date: 2026-11-20)
- Subscribers in last 30 days: 7 (includes 2026-10-21)
- Next send (first Monday of next month): 2026-12-07
- Send after that (run date 2026-12-07): 2027-01-04

## Step 3 - The 30th of February

### Prediction
- Mailroom will crash with ValueError: day is out of range for month
- Last line of error: `ValueError: day is out of range for month`
- Function named in error: `count_since_days` (line 35 in mailroom/__init__.py)
- The error does not say which row it was

### Modify: Column renamed to "joined"
- Error: `KeyError: 'joined_on'` at line 35 in count_since_days
- The code expects column "joined_on" but CSV has "joined"

## Step 4 - Tests first (pytest)

### Prediction
- 7 tests total (one per behavior from checks.py)
- Tests named for what they check
- checks.py deleted

## Step 5 - check_subject

### Expected Test Cases (6 cases)
1. "The Steep Club opens Monday" → []
2. "Your Steep Club box ships on Monday with new teas." (50 chars) → []
3. "Your Steep Club box ships on Monday with fresh teas" (51 chars) → ["too long"]
4. "" (empty) → ["empty"]
5. "   " (only spaces) → ["empty"]
6. (no Subject line) → ["missing"]