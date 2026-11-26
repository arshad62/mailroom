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

## Step 6 - Check other rules + check command

### Expected Test Cases (5 cases)
1. issues/issue-01.md → []
2. Preview 91 chars → ["preview too long"]
3. No {{first_name}} in body → ["missing greeting"]
4. Two links → ["too many links"]
5. No footer and no greeting → ["missing greeting", "missing footer"]

### New command
- `uv run mailroom check <issue file>` prints problems (one per line) and exits 1, or prints OK and exits 0

## Step 7 - Emoji length judgment

### Prediction
- Python len(): 21 (counts codepoints: 👍 = U+1F44D, 🏽 = U+1F3FD, space, 18 text chars)
- Reader sees: ~20 visual characters (1 emoji cluster + 19 text chars)
- Two ways to count: codepoints (len()) vs grapheme clusters (visual)

### Modify: Greeting format decision
- Decision: Require exactly `{{first_name}}` (lowercase, underscore, no spaces)
- Alternatives like `{{firstName}}`, `{{first name}}`, `{{FIRST_NAME}}` are NOT accepted
- Added test to verify this