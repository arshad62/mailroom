Python with Claude Code · Chapters 13 to 15 of The AI Agent Factory

# Mailroom Lab

You build **Mailroom**, a small Python tool for a newsletter, from an empty folder. It counts subscribers, checks an issue before it goes out, and sends it to a practice mail server. Each step brings in **one** new idea, when the project needs it. At the end, Mailroom moves into the Email Studio you already built and checks its emails with code.

27 steps, 0 to 26 Python only you write the prompts tests first no real emails are sent

## Before you start

1. **Claude Code**, as in the Email Studio Lab.
2. **uv**, which installs Python and runs it. Check with `uv --version`, or install it from `docs.astral.sh/uv`.
3. **Git** and a **GitHub** account. Install the GitHub command line, `gh`, and sign in yourself with `gh auth login`.
4. An empty folder called `mailroom`, with Claude Code open in it.
5. A file `notes/predictions.md`. You write each prediction there **before** the run, and never change it afterwards.

#### How every step works: PRIMM-AI+, from 13.1

1. 1 · PREDICT**You decide first**The answers you expect, in your predictions file.
2. 2 · MAKE**Your own prompt**It must say what the box lists. Open the sample after.
3. 3 · RUN**Claude runs it**Compare the output with your prediction.
4. 4 · INVESTIGATE**Read the new code**Claude asks you to predict each new piece. Then ask "what does line N do?"
5. 5 · MODIFY**Change one thing**Predict again, run again.
6. 6 · CHECK**Fresh session**`/exit`, `claude`, paste the check.

**Claude writes only what you have learned.** Step 0 puts your lesson number in AGENTS.md, and each step tells you when to raise it. If Claude needs something new, it stops and names it. You decide.

**Red prompts** break something on purpose. Paste those exactly. **Yellow** marks the answers you decided: replace them with yours.

## Practice files

Made-up data for the whole lab. Each step says when to download one, and where to put it.

- 24 made-up subscribers, three groups. Step 1.
- One newsletter issue that follows every rule. Step 5.
- The five rules an issue must follow. Step 5.
- Eight new sign-ups, some of them wrong. Step 11.

```

```

Downloads are not available in this view. Copy the text into a file with this name.

#### Your project at the end

```
mailroom/
├── AGENTS.md            the rules, one more per step
├── CLAUDE.md            one line: @AGENTS.md
├── REVIEW.md            what a reviewer checks
├── data/                subscribers, new sign-ups
├── issues/  docs/       an issue, and its rules
├── src/mailroom/        one module per job
├── tests/               every behavior, as a test
├── notes/predictions.md your predictions
└── .github/             checks, template, owners
```

0 done

#### 0 · The base

#### A · Read and check

#### B · Shape the code

#### C · Talk to a service

#### D · Ship like a team

#### E · Into your studio

- [Before you start](#start)
- [Practice files](#files)
- [When you are finished](#done-list)

Step 0

## The base

An empty folder that knows its rules, on GitHub from the first minute.

0

[15.2 Git through the agent](https://agentfactory.panaversity.org/building-ai-workers/code-review/git-through-the-agent/)

### An empty folder that knows its rules

Start a Python project, give it a rules file, and save it on GitHub.

[ ] Done

**The problem.** Claude starts every session knowing nothing about your project. A rules file tells it, every time. GitHub keeps every step safe, and lets your teacher see your work.

**You decide first.** Pick a name for your newsletter, and who it is for. Kettlebird Tea's Steep Club is the sample. Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- a Python project with uv, Python 3.12 or newer
- AGENTS.md with your project's rules, and a CLAUDE.md that only imports it
- How I learn: how far you have read, that Claude uses only that, and that it asks you to predict anything new
- git, and a new public GitHub repository

Show a sample prompt

Sample promptCompare with yours

```
Set up a Python project called Mailroom in this folder, with uv and Python 3.12 or newer.
Write AGENTS.md with these rules, and a CLAUDE.md that only imports it:
- Mailroom is a command-line tool for one newsletter: Kettlebird Tea's Steep Club. It reads the subscribers, checks an issue, and sends it to a practice mail server.
- Use uv for everything.
- Never use a real person's email address. Use @example.com, and @resend.dev for practice sends.
- Commit and push after every step.
Add a section called How I learn:
- I am new to Python. I have completed up to 13.7 of https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/ and I update this number as I learn.
- Write only with what I have learned. If something new would really help, stop and tell me its name in one line. I decide.
- When the code uses something new, show me that piece first and ask me to predict what it does. Stay quiet while I guess. Then run it, and explain a line only when I ask.
Then start git, and push to a new public GitHub repository called mailroom.
```

#### Investigate

1. Open pyproject.toml. Which line sets the Python version?
2. Ask: "What does uv run do that plain python does not?"
3. Ask: "What does a classmate get if they clone this repository now?"

#### Modify

Ask Claude to add one more rule of your own to AGENTS.md. Commit and push.

CheckNew session: /exit, then claude, then paste

```
Check my base project. Don't change any files.
1. Without opening any file, list the rules you follow here and name the file they came from.
2. Run uv run python --version, git log --oneline and git remote -v.
3. Run gh repo view --json url,visibility.
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why the rules live in a file, and why we push from the first step.
```

#### You'll know it worked when

- The fresh session lists your rules and names AGENTS.md, without opening it.
- Your repository is on GitHub.

#### AGENTS.md gains

The rules in your prompt, plus your own.

Part A · Steps 1 to 7 · Chapter 13

## Read and check

Read a file, work with dates, read an error, and write tests before the code. Everything stays in one file.

1

[13.8 Text from a file](https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/text-dates-files/)

### Count your subscribers

Read a CSV file, with the expected answers written before the code.

[ ] Done

**Before you start.** Download `subscribers.csv` below and put it in a folder called `data` inside your project.

**Your level.** Before you start, tell Claude: "I have now completed up to 13.8. Update How I learn in AGENTS.md."

**The problem.** Your subscribers live in a file. Before Mailroom can do anything, it has to read them.

**You decide first.** Open the file and count: how many subscribers in total, and how many in each group? Write the numbers in `notes/predictions.md`. They become your first checks. Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- what the command prints
- your expected numbers, as checks written before the code

Show a sample prompt

Sample promptCompare with yours

```
Mailroom's first job: count the subscribers in data/subscribers.csv.
First write my expected answers as assert lines in checks.py that call my functions, and show me them failing: 24 in total, and 8 in each of the three groups.
Then write mailroom.py so that uv run mailroom.py subscribers prints the total and one line per group, and the checks pass.
Add to AGENTS.md: behaviors first. I give the expected answers, you write them as checks, show them failing, then write the code.
```

#### Investigate

1. Find the line that opens the file. Ask why it names an encoding.
2. Ask Claude to print one row as Python sees it. Is it a list or a dictionary?
3. Predict what happens if the file ends with an empty line. Try it on a copy.

#### Modify

Ask for one more line: how many subscribers gave consent. Give the expected number first.

CheckNew session: /exit, then claude, then paste

```
Test my subscriber count. Don't change any project files.
1. Run uv run python checks.py and uv run mailroom.py subscribers.
2. Count the rows and the groups in data/subscribers.csv yourself with a command, without Mailroom's code. Do the numbers agree?
3. Make a copy with only 6 rows, outside the project, and run the count on it. Does it say 6?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why I wrote the expected numbers before the code.
```

#### You'll know it worked when

- checks.py failed first, then passed.
- The 6-row copy prints 6: nothing is fixed to your file.

#### AGENTS.md gains

Behaviors first: I give the expected answers, you write them as checks, show them failing, then write the code.

2

[13.9 Dates](https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/dates/)

### Who is new, and when do we send?

Turn text into dates, compare them, and keep "today" out of the logic.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 13.9. Update How I learn in AGENTS.md."

**The problem.** Each issue welcomes the people who joined in the last 30 days, and the newsletter goes out on the first Monday of each month.

**You decide first.** Use the run date 20 November 2026. Does "the last 30 days" include someone who joined on 21 October? Decide, then count by hand. Then work out the first Monday of December 2026, and the send after that. Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- your expected answers, including the edge you decided
- that the run date is passed in, and only the command line may read today's date

Show a sample prompt

Sample promptCompare with yours

```
Add dates. Checks first:
- with the run date 2026-11-20, 7 subscribers joined in the last 30 days. Someone who joined on 2026-10-21 counts.
- the next send is the first Monday of the next month: 2026-12-07 for the run date 2026-11-20, and 2027-01-04 for 2026-12-07.
Add the commands subscribers --since-days 30 and next-send, both with an optional --run-date. Only the command line may read today's date.
Add to AGENTS.md: never read today's date inside the logic. Pass the run date in.
```

#### Investigate

1. Find where today's date is read. Is it in one place only?
2. Ask: "Would comparing the text 2026-10-21 work too? When would it break?"
3. Find the line that decides whether 21 October counts.

#### Modify

Ask for --since 2026-10-01, an exact date instead of a number of days. Check first.

CheckNew session: /exit, then claude, then paste

```
Test the dates in Mailroom. Don't change any files.
1. Run uv run python checks.py.
2. Work out the first Monday of the next month for the run dates 2026-11-20, 2026-12-07 and 2026-12-31 with Python's datetime, without Mailroom's code, and compare.
3. Count who joined from 2026-10-21 to 2026-11-20 with a command, and compare with Mailroom.
4. Find every place that reads today's date.
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why the run date is passed in.
```

#### You'll know it worked when

- Every date agrees with an independent calculation.
- Today's date is read in one place: the command line.

#### AGENTS.md gains

Never read today's date inside the logic. Pass the run date in.

3

[13.10 Reading an error](https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/reading-an-error/)

### The 30th of February

Read a Python error from the bottom up, before anyone changes code.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 13.10. Update How I learn in AGENTS.md."

**The problem.** Someone retyped a subscriber's date by hand: 2026-02-30. That day does not exist.

**You decide first.** Will Mailroom crash? If so, what will the last line of the error say, and which of your functions will it name? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- make the bad date, run the count, and show the full error
- no fixing and no explaining yet

Break itPaste this exactly

```
In data/subscribers.csv, change Jonas Berg's joined_on to 2026-02-30, as if someone retyped it by hand.
Then run uv run mailroom.py subscribers --since-days 30 --run-date 2026-11-20.
Don't fix or explain anything. Show me the full error, exactly as printed.
```

**Read it yourself, bottom up:** the last line gives the error's type and message. Going up, find the lowest line in *your* file, `mailroom.py`, and its function. Does the error say which row it was?

Show the sample for: Then, after you read it

Then, after you read itCompare with yours

```
Explain the error in three lines: what happened, where in our code, and why.
Then fix the data, not the code: put back Jonas's real date from git. Run the checks again.
Add to AGENTS.md: when something breaks, show me the full error before changing anything.
```

#### Investigate

1. Which line of the error told you the most?
2. Ask: "Why fix the data and not the code this time?"

#### Modify

In a copy of the file, rename the column joined_on to joined. Predict the error, run it, and read it bottom up.

CheckNew session: /exit, then claude, then paste

```
Check my fix. Don't change any files.
1. Check every joined_on in data/subscribers.csv with a command: is each one a real calendar date?
2. Run uv run python checks.py and uv run mailroom.py subscribers.
3. Run git status and git log -1 --stat. Is the data back to what git had, and is the new rule committed?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about where to start reading a Python error.
```

#### You'll know it worked when

- You named the error type and the function before Claude explained.
- The data is back to what git had, and the checks pass.

#### AGENTS.md gains

When something breaks, show me the full error before changing anything.

4

[13.11 Tests first](https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/tests-first/)

### Real tests

Turn your checks into tests that report every result.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 13.11. Update How I learn in AGENTS.md."

**The problem.** checks.py stops at the first failed assert, and it keeps growing. A test runner runs every test and reports each one.

**You decide first.** Predict how many tests you will have after the move, one per behavior. Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- pytest
- one test per behavior, named for the behavior
- checks.py deleted

Show a sample prompt

Sample promptCompare with yours

```
Move the checks into pytest: one test per behavior, each named for the behavior it checks. Delete checks.py, run the tests, and update AGENTS.md to say the checks are now tests.
```

#### Investigate

1. Read the test names only. Do they tell you what Mailroom does?
2. Ask: "What does pytest show that checks.py did not?"

#### Modify

Break one expected number on purpose. Predict pytest's message, run it, then put it back.

CheckNew session: /exit, then claude, then paste

```
Check the tests. Don't change any files.
1. Run uv run pytest.
2. Compare the tests with git show HEAD~1:checks.py. Is every old assert still tested, with the same expected answer?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why one test per behavior.
```

#### You'll know it worked when

- Every old assert is a test, with the same answer.
- Each test's name says what it checks.

#### AGENTS.md

no new rule

5

[13.11 Tests first](https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/tests-first/)

### Is this subject line OK?

Write tests first for a new rule, with answers only you decide.

[ ] Done

**Before you start.** Download `issue-01.md` into a folder called `issues`, and `email-rules.md` into `docs`. Ask Claude to commit them.

**Your level.** Before you start, tell Claude: "I have now completed up to 13.11. Update How I learn in AGENTS.md."

**The problem.** Mailroom's next job is checking an issue before it goes out. Start with rule 1 in docs/email-rules.md: a subject of 50 characters or fewer.

**You decide first.** Write six subject lines and what the check should say for each. Include an empty subject, one of exactly 50 characters, one of 51, and an issue with no Subject line. Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- your six cases, each with its expected answer
- tests first, and your answers never change

Show a sample prompt

Sample promptCompare with yours

```
Tests first for check_subject(issue_text), which returns a list of problems, empty when the subject is fine. My cases:
- "The Steep Club opens Monday": no problems
- "Your Steep Club box ships on Monday with new teas." (50 characters): no problems
- "Your Steep Club box ships on Monday with fresh teas" (51 characters): one problem, too long
- an empty subject: one problem, empty
- a subject of only spaces: one problem, empty
- no Subject line at all: one problem, missing
Show the tests failing first. Then make them pass, and never change my answers. If you think one is wrong, stop and tell me.
Add to AGENTS.md: I decide the test cases and their answers. Never change an expected answer to make a test pass.
```

#### Investigate

1. Ask: "If check_subject always returned an empty list, which tests would still pass?"
2. Ask: "What does green prove here, and what does it not?"
3. Find the number 50. How many places hold it?

#### Modify

Add two cases of your own, one you think the code will fail. Were you right?

CheckNew session: /exit, then claude, then paste

```
Test my tests. Don't change any project files.
1. Run uv run pytest.
2. Read git log -p for the subject tests. Did any expected answer change after the code was written?
3. In a temporary copy, make check_subject always return an empty list, run the tests there, and count the failures.
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about who owns the expected answers, and what green does not prove.
```

#### You'll know it worked when

- The tests failed first, then passed, and no answer changed.
- A broken check_subject fails most of them.

#### AGENTS.md gains

I decide the test cases and their answers. Never change an expected answer to make a test pass.

6

[13.11 Tests first](https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/tests-first/)

### The rest of the rules

Practice the loop: your cases, failing tests, then code.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 13.11. Update How I learn in AGENTS.md."

**The problem.** docs/email-rules.md has four more rules: the preview, the greeting, one link, and the footer. Then Mailroom needs a command that checks a whole issue.

**You decide first.** Two cases per rule, each with its expected answer. One should be an issue with two problems at once. Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- your cases
- a check command that prints every problem and exits 1, or prints OK

Show a sample prompt

Sample promptCompare with yours

```
Check the other rules in docs/email-rules.md the same way. My cases:
- issues/issue-01.md: no problems
- a preview of 91 characters: one problem
- no {{first_name}} in the body: one problem
- two links: one problem. A link starting http:// still counts as a link
- no footer, and no greeting: two problems
Then add uv run mailroom.py check <issue file>, which prints every problem on its own line and exits 1, or prints OK and exits 0.
```

#### Investigate

1. Ask: "What counts as a link for you? Does {{unsubscribe_url}} count?"
2. Ask: "What did you assume that I never told you?"

#### Modify

Ask for the line number beside each problem.

CheckNew session: /exit, then claude, then paste

```
Test the issue checks. Don't change any project files.
1. Run uv run pytest, and the check on issues/issue-01.md.
2. Make three temporary broken copies outside the project: a 91-character preview, two links, no footer. Does the check find exactly the right problem in each?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about what the check assumed that the rules file does not say.
```

#### You'll know it worked when

- issue-01.md is OK, and each broken copy gets exactly its own problem.

#### AGENTS.md

no new rule: AGENTS.md already says tests first, so your prompt no longer has to

7

[13.12 Judgment](https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/judgment/)

### How long is an emoji?

Find a decision the code made for you, and make it yourself.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 13.12. Update How I learn in AGENTS.md."

**The problem.** The next subject starts with an emoji: "👍🏽 Thanks for joining". The rule says 50 characters. What is a character?

**You decide first.** How many characters does a reader see in "👍🏽 Thanks for joining"? How many will Python's len() say? Write both. Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- ask for an answer and its proof
- then your decision, as a test and a rule

Show a sample prompt

Ask firstCompare with yours

```
How long is the subject "👍🏽 Thanks for joining"? Give your answer, then prove it in Python, and tell me the two ways our check could count.
```

Show the sample for: Then your decision

Then your decisionCompare with yours

```
Count length as what Python's len() counts. Add a test with this emoji that proves it, and add the decision to AGENTS.md.
```

#### Investigate

1. Read all the tests. Is there one that would pass even if the check did nothing? Ask Claude to look too.

#### Modify

Ask what other choices the code made without asking you. Pick one and decide it.

CheckNew session: /exit, then claude, then paste

```
Check the emoji decision. Don't change any files.
1. Read AGENTS.md: what does a character mean in this project?
2. Run uv run pytest. Is there a test with an emoji that proves the code follows that decision?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why the emoji question was mine to decide.
```

#### You'll know it worked when

- Your decision is in AGENTS.md and in a test.

#### AGENTS.md gains

Subject and preview length count what Python's len() counts.

Part B · Steps 8 to 13 · Chapter 14

## Shape the code

One file is not enough any more. Split it, give it types and objects, and check what comes in.

8

[14.1 Modules and packages](https://agentfactory.panaversity.org/building-ai-workers/structuring-programs/modules/)

### One file per job

Split one long file into a package, without changing what it does.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 14.1. Update How I learn in AGENTS.md."

**The problem.** mailroom.py is long now. Finding the checks means scrolling past the dates and the counting.

**You decide first.** Which tests will break when the code moves, and why? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- a package, one module per job
- the same behavior: only imports may change in the tests
- a mailroom command

Show a sample prompt

Sample promptCompare with yours

```
Turn Mailroom into a package under src/mailroom, one module per job: subscribers and dates, the issue, the checks, and the commands. uv run mailroom must work. Move code only: no behavior changes, and only the imports change in the tests. Delete the unused main.py.
Add to AGENTS.md: one module per job. Only the commands module prints.
```

#### Investigate

1. Ask: "How does an import find checks.py now?"
2. Ask: "What is \_\_init\_\_.py for?"
3. Which module prints?

#### Modify

Ask to move the send-date code into its own module.

CheckNew session: /exit, then claude, then paste

```
Check the package. Don't change any files.
1. Run uv run pytest and each command.
2. Check out the commit before the move into a temporary git worktree, run the same commands there, and compare the output.
3. Search for print( outside the commands module.
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why each module has one job.
```

#### You'll know it worked when

- Same output before and after the move.
- Only the commands module prints.

#### AGENTS.md gains

One module per job. Only the commands module prints.

9

[14.2 Types you write down](https://agentfactory.panaversity.org/building-ai-workers/structuring-programs/types-you-write-down/)

### A date that was really text

Write types down, and let a checker catch mistakes before the code runs.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 14.2. Update How I learn in AGENTS.md."

**The problem.** A teammate passes the run date as the text "2026-11-20" instead of a date. Python does not complain until that line runs, if it complains at all.

**You decide first.** Crash, or a wrong answer? Which is worse? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- show the mistake first
- type hints everywhere, and pyright
- fix the call, not the hint

Break itPaste this exactly

```
Add a test that calls the 30-day function with the run date as the text "2026-11-20". Run it, and show me exactly what happens.
```

Show the sample for: Then

ThenCompare with yours

```
Add type hints to every function, and pyright. Run it and show me what it finds. Fix the call, not the hint.
Add to AGENTS.md: every function has type hints, and pyright must be clean.
```

#### Investigate

1. Find a type like list\[str\]. Say it in words.
2. Ask: "What did pyright catch that the tests did not, and the other way round?"

#### Modify

Return a number where a list is promised, in a copy. Predict pyright's message, then run it.

CheckNew session: /exit, then claude, then paste

```
Check the types. Don't change any files.
1. Run uv run pyright and uv run pytest.
2. Find any function without full type hints, and any Any or type: ignore.
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about what a type checker catches and what it cannot.
```

#### You'll know it worked when

- pyright named the text-for-a-date mistake.
- pyright and pytest are both clean.

#### AGENTS.md gains

Every function has type hints, and pyright must be clean.

10

[14.3 Classes and objects](https://agentfactory.panaversity.org/building-ai-workers/structuring-programs/classes-and-objects/)

### A subscriber is a thing

Group data and what you do with it into classes.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 14.3. Update How I learn in AGENTS.md."

**The problem.** Rows travel as dictionaries, so a typo like row\["join_on"\] fails only when that line runs. And every check splits the issue text again.

**You decide first.** What will print(subscriber) show? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- a Subscriber class and an Issue class
- what Issue knows and does
- used everywhere

Show a sample prompt

Sample promptCompare with yours

```
Rows and issue text are passed around raw. Make Subscriber a dataclass, and Issue a class with its subject, preview, body, links, and personalize(first_name). Use them everywhere. Tests first:
- issues/issue-01.md has one link, https://kettlebird.example/steep-club
- personalize("Ayesha") puts Ayesha where {{first_name}} was, and leaves {{unsubscribe_url}} as it is
Add to AGENTS.md: pass Subscriber and Issue objects around, never raw rows or raw text.
```

#### Investigate

1. Ask: "What does self mean in Issue?"
2. Ask: "What did @dataclass write that I cannot see?"
3. Why is links a property but personalize a method?

#### Modify

Ask for full_name on Subscriber, test first.

CheckNew session: /exit, then claude, then paste

```
Check the classes. Don't change any files.
1. Run uv run pytest and uv run pyright.
2. Search for row["...] style access outside the code that reads the CSV.
3. In Python, make one Subscriber and one Issue from the files, print both, and call personalize("Ayesha").
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about what a class gives us that a dictionary does not.
```

#### You'll know it worked when

- No column names in quotes outside the reading code.
- personalize("Ayesha") greets Ayesha.

#### AGENTS.md gains

Pass Subscriber and Issue objects around, never raw rows or raw text.

11

[14.4 Data models and schemas](https://agentfactory.panaversity.org/building-ai-workers/structuring-programs/data-models-and-schemas/)

### Marketing sent a messy file

Check data at the edge with a model.

[ ] Done

**Before you start.** Download `new-signups.csv` into `data`.

**Your level.** Before you start, tell Claude: "I have now completed up to 14.4. Update How I learn in AGENTS.md."

**The problem.** Marketing hands you new sign-ups. Some rows are fine. Some are not. Code should never trust a file it did not write.

**You decide first.** A model checks each field's shape: an email address looks like one, the group is one of three names, the date is a real date, consent is not empty. Which of the 8 rows will it accept? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- the model's rules
- an import command that says accepted or rejected, with the reason
- your predictions, as tests

Show a sample prompt

Sample promptCompare with yours

```
Replace Subscriber with a Pydantic model: an email address, one of our three groups, a real date, and consent that is not empty. Add mailroom import <file>, which prints each row as accepted or rejected, with the reason.
Tests first, from my predictions for data/new-signups.csv: accepted: Maria, Sara, Tom, Ines. Rejected: Omar, Lena, Kofi, Hana.
Add to AGENTS.md: data from outside goes through the model before any code uses it.
```

#### Investigate

1. Ask: "What exactly does the email field check?"
2. Find where a rejected row's reason comes from. Who wrote it?

#### Modify

Ask to accept "Gift Buyers" by turning it into gift-buyers first. Is that a good idea? Decide.

CheckNew session: /exit, then claude, then paste

```
Test the import. Don't change any project files.
1. Run uv run mailroom import data/new-signups.csv. Which rows are accepted?
2. For each rejected row, is the reason the real problem?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about what the model checks.
```

#### You'll know it worked when

- Four rows accepted, four rejected, each with its real reason.

#### AGENTS.md gains

Data from outside goes through the model before any code uses it.

12

[14.5 What a schema lets through](https://agentfactory.panaversity.org/building-ai-workers/structuring-programs/schema-rules/)

### What the model let through

Find the rows a model accepts that are still wrong, and add your own rules.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 14.5. Update How I learn in AGENTS.md."

**The problem.** Two accepted rows are wrong for us: Sara's address is real-looking but not ours, and Tom joined after the run date.

**You decide first.** Which of the two rules can live inside the model, and which cannot? Why? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- the two rules
- tests first

Show a sample prompt

Sample promptCompare with yours

```
Two accepted rows are still wrong for us: Sara is not at @example.com, and Tom joined after the run date. Add our own rules for both, tests first. Tell me why the date rule cannot live inside the model.
```

#### Investigate

1. Ask: "Why does the email check accept sara.ali@gmail.com?"

#### Modify

Add a row at @example.org to a copy and import it.

CheckNew session: /exit, then claude, then paste

```
Test our own rules. Don't change any project files.
1. Run uv run mailroom import data/new-signups.csv --run-date 2026-11-20. Which rows are accepted now?
2. Run uv run pytest and uv run pyright.
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about the difference between a field's shape and its meaning.
```

#### You'll know it worked when

- Only Maria and Ines are accepted.

#### AGENTS.md gains

The model checks the shape. Our own rules check the meaning.

13

[14.6 Errors as design](https://agentfactory.panaversity.org/building-ai-workers/structuring-programs/errors-as-design/)

### One bad row, 999 good ones

Decide which problems stop the program, and report the rest all at once.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 14.6. Update How I learn in AGENTS.md."

**The problem.** In step 3 one bad date stopped everything. A real list has thousands of rows, and the person fixing them wants every problem at once, with its row.

**You decide first.** Sort these into "stop everything" and "report and carry on": no file, wrong columns, a bad date in one row, a Gmail address, an issue with two links. Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- your sorting
- row and field in every problem
- what the user sees, and the exit codes

Show a sample prompt

Sample promptCompare with yours

```
Make bad data a report, not a crash. Reading subscribers returns the good ones and every problem, with its row and field. Commands print all the problems and exit with 1.
These stop everything with one plain sentence, no traceback, and exit 2: no file, and wrong columns.
Tests first: data/new-signups.csv gives 2 good subscribers and 6 problems.
Add to AGENTS.md: report every problem with its row. No traceback for a user's mistake.
```

#### Investigate

1. Find every try and except. What does each catch?
2. Ask: "Which program reads the exit codes?"

#### Modify

Ask for --strict, which stops at the first problem.

CheckNew session: /exit, then claude, then paste

```
Test the errors. Don't change any project files.
1. Run the import on data/new-signups.csv with --run-date 2026-11-20, then show the exit code.
2. Run it on a file that does not exist, and show the exit code.
3. Search for an except that hides an error.
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about which errors should stop a program.
```

#### You'll know it worked when

- Six problems at once, with rows, exit code 1.
- A missing file: one sentence, no traceback, exit code 2.

#### AGENTS.md gains

Report every problem with its row. No traceback for a user's mistake.

Part C · Steps 14 to 18 · Chapter 14

## Talk to a service

JSON, a REST API, many requests at once, and a vendor's own library, all against the practice server. Start the practice mail server in a second terminal before step 15: `npx emulate@0.12.3 start --service resend`

14

[14.7 JSON and REST APIs](https://agentfactory.panaversity.org/building-ai-workers/structuring-programs/json-and-rest-apis/)

### See the send before it happens

Write data as JSON, and check it again when it comes back in.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 14.7. Update How I learn in AGENTS.md."

**The problem.** Before anything is sent, you want to see exactly what would go out, in a file both people and programs can read.

**You decide first.** JSON has no dates. How will the run date look in the file? And what should fill {{company_address}} and {{unsubscribe_url}}? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- a dry run that writes the plan as JSON
- the check runs first
- outbox/ stays out of git

Show a sample prompt

Sample promptCompare with yours

```
Add mailroom send <issue> --dry-run --run-date 2026-12-07. It checks the issue first, then writes outbox/plan.json: one entry per subscriber with to, subject and the text with every placeholder filled: their first name, the company address 12 Leaf Lane, Portland, OR 97201, and the unsubscribe link https://kettlebird.example/unsubscribe. Add the run date. Keep outbox/ out of git.
Tests first: 24 entries, the first one to ayesha.khan@example.com with "Hi Ayesha", and an issue that fails the check writes no plan.
```

#### Investigate

1. Open plan.json. Point at a list, an object and a text value. Where is the date?
2. Ask: "What happens if you hand a date straight to json.dumps?"

#### Modify

Edit one subject in plan.json to 60 characters. Ask for --from-plan, which reads the plan back through a model and checks it again. Is your edit caught?

CheckNew session: /exit, then claude, then paste

```
Test the dry run. Don't change any project files.
1. Run the dry run, and check outbox/plan.json with python -m json.tool.
2. Count its entries and compare with the subscribers.
3. Is any {{...}} placeholder left unfilled?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why JSON from a file needs checking again.
```

#### You'll know it worked when

- One entry per subscriber, nothing left unfilled.

#### AGENTS.md gains

JSON read from a file is outside data: it goes through a model too.

15

[14.7 JSON and REST APIs](https://agentfactory.panaversity.org/building-ai-workers/structuring-programs/json-and-rest-apis/)

### Send one email

Make a request to a REST API and read the answer.

[ ] Done

**Before you start.** Start the practice mail server in a second terminal, as in the Email Studio Lab: `npx emulate@0.12.3 start --service resend`. Wait until it shows `http://localhost:4000`.

**Your level.** Before you start, tell Claude: "I have now completed up to 14.7. Update How I learn in AGENTS.md."

**The problem.** Time to send, to the practice server on your own computer. It speaks the same REST API as the real email service.

**You decide first.** What will the server send back for a good email: which status code, and what in the body? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- the request: method, address, header, body
- where the address and the key come from
- two guards in code

Show a sample prompt

Sample promptCompare with yours

```
Send one email to the practice server with httpx: POST /emails with from onboarding@resend.dev, to, subject and text, and the key as a Bearer header. Take the server's address and the key from RESEND_API_URL and RESEND_API_KEY, defaulting to http://localhost:4000 and re_practice.
Two guards: refuse to send unless the address is localhost, and refuse any recipient not at @example.com or @resend.dev.
Add mailroom send-one <issue> --to delivered@resend.dev. Print the status code and the id, then GET the email back and print its status. Tests must not need the server.
Add to AGENTS.md: the key and the address come from the environment. Sending works only against localhost.
```

#### Investigate

1. Find where the key goes. Why not in the address?
2. Find where Python data becomes the request body.

#### Modify

Ask to print when the server says the email was created.

CheckNew session: /exit, then claude, then paste

```
Test sending. Don't change any project files. The practice server is running.
1. Send one email to delivered@resend.dev, then list the server's emails with curl http://localhost:4000/emails. Is it there?
2. Try sara.ali@gmail.com. Is it refused before any request?
3. Run it with RESEND_API_URL=https://api.resend.com. Does it refuse?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about where the key comes from, and why.
```

#### You'll know it worked when

- The server lists your email.
- Gmail and the real service are both refused before any request.

#### AGENTS.md gains

The key and the address come from the environment. Sending works only against localhost.

16

[14.7 JSON and REST APIs](https://agentfactory.panaversity.org/building-ai-workers/structuring-programs/json-and-rest-apis/)

### When the server says no

Handle each kind of failure on purpose.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 14.7. Update How I learn in AGENTS.md."

**The problem.** A request can fail in different ways, and each needs a different answer. The practice server never checks the key, so a wrong key works there. The real service answers 401.

**You decide first.** Predict the status code for: no subject, an id that does not exist, and the server switched off. Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- see each failure first
- how to handle each

Break itPaste this exactly

```
Show me the status code and body the server sends for: a request without a subject, and GET /emails/does-not-exist. Then I will stop the server: show me what happens then.
```

**Between the two prompts:** stop the practice server with Ctrl+C in its terminal, and tell Claude "I stopped the server. Show me what happens now." Start the server again before the next prompt.

Show the sample for: Then

ThenCompare with yours

```
Handle each on purpose, tests first: a 422 shows the server's message and is never retried, a 404 says the id is unknown, and no connection says the practice server is not running and how to start it.
Add to AGENTS.md: handle each status on purpose. Never retry a 4xx.
```

#### Investigate

1. The error body has three fields. Which one does Mailroom show?
2. Ask: "Why is a 422 never retried?"

#### Modify

Ask what Mailroom would do with a 401 from the real service. Add a test for it.

CheckNew session: /exit, then claude, then paste

```
Test the failures. Don't change any project files. The practice server is running.
1. Make Mailroom send without a subject, and fetch an unknown id. What does it print?
2. Point RESEND_API_URL at http://localhost:4999, where nothing runs. What does it print?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about which failures are worth retrying.
```

#### You'll know it worked when

- Each failure gets its own plain message, and nothing is retried.

#### AGENTS.md gains

Handle each status on purpose. Never retry a 4xx.

17

[14.8 Async and await](https://agentfactory.panaversity.org/building-ai-workers/structuring-programs/async-and-await/)

### Twenty-four at once, five at a time

Send many requests at the same time, with a limit.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 14.8. Update How I learn in AGENTS.md."

**The problem.** Real servers take time, and the program waits for each answer. The practice server answers at once, so Mailroom gets --latency, a wait before each request that stands in for the internet.

**You decide first.** With 0.3 seconds per request, how long for 24 emails one by one? And five at a time? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- one by one first, timed
- then at once, with a limit, in order

Show a sample prompt

Sample promptCompare with yours

```
Add mailroom send <issue> --run-date 2026-12-07 --latency 0.3. It sends the whole plan one by one, waits the latency before each request, and prints the time it took. Then add --at-once 5: the same send with asyncio, at most 5 at a time, results in the plan's order. Tests first: the order is kept, and never more than 5 run at once.
Add to AGENTS.md: send with a limit on how many at once.
```

#### Investigate

1. Find async def and await. What does the program do while it waits?
2. Find the limit. What happens with no limit and 10,000 subscribers?

#### Modify

Predict the time for --at-once 1 and --at-once 24. Run both.

CheckNew session: /exit, then claude, then paste

```
Test sending at once. Don't change any project files. The practice server is running.
1. Time the send one by one and with --at-once 5, both with --latency 0.3.
2. List the server's emails with curl. Did each subscriber get exactly one email?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why async helps when waiting, and why we limit it.
```

#### You'll know it worked when

- About 7 seconds one by one, about 1.5 five at a time.
- One email per subscriber.

#### AGENTS.md gains

Send with a limit on how many at once.

18

[14.9 Reading SDK-shaped code](https://agentfactory.panaversity.org/building-ai-workers/structuring-programs/reading-sdk-code/)

### The vendor's own library

Read an official SDK, find what it does not do, and add it safely.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 14.9. Update How I learn in AGENTS.md."

**The problem.** The email company publishes a Python library, an SDK. What does it do for you, and what does it leave to you?

**You decide first.** If the server does not answer, will the SDK try again? How long will it wait? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- the SDK pointed at the practice server
- where to look in its source
- then a safe retry

Show a sample prompt

Read the SDKCompare with yours

```
Add the official resend package, point it at the practice server with RESEND_API_URL, and write the same send with it. Show me both versions side by side. Then show me in the package's own source, with files and lines: where it builds the request, where an error becomes an exception, its timeout, and whether it retries.
```

Show the sample for: Then

ThenCompare with yours

```
Add our own retry: only after no connection, a timeout, a 429 or a 5xx, at most 3 tries with growing waits, never a 4xx. Give each email an idempotency key made from the issue and the recipient. Tests first.
Prove it against the server: the same key twice sends one email, and the same key with another subject gets a 409.
Add to AGENTS.md: retry only what can succeed later, and every send has an idempotency key.
```

#### Investigate

1. Ask: "Without the key, how could a retry send twice?"
2. Which version will Mailroom keep, httpx or the SDK? Decide, and add why to AGENTS.md.

#### Modify

Ask to log each retry with its try number and wait.

CheckNew session: /exit, then claude, then paste

```
Test the retries. Don't change any project files. The practice server is running.
1. Run uv run pytest and uv run pyright.
2. Read the retry code. Which answers are retried? Any 4xx?
3. Send one email twice with the same idempotency key, then list the server's emails. How many arrived?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about what the SDK does for us, and what it leaves to us.
```

#### You'll know it worked when

- You found that the SDK never retries.
- The same key twice gives one email. Another subject with the same key gets a 409.

#### AGENTS.md gains

Retry only what can succeed later, and every send has an idempotency key.

Part D · Steps 19 to 24 · Chapter 15

## Ship like a team

From now on nothing goes straight to main. Every change arrives as a pull request, with evidence, checks and review.

19

[15.1 The change is the unit of work](https://agentfactory.panaversity.org/building-ai-workers/code-review/the-change-is-the-unit-of-work/)[15.3 GitHub and the pull request](https://agentfactory.panaversity.org/building-ai-workers/code-review/github-and-the-pull-request/)

### Your first pull request

Make a change on a branch, and offer it as a pull request.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 15.1. Update How I learn in AGENTS.md."

**The problem.** Committing straight to main means nobody looks before a change lands. A pull request is a change offered for review.

**You decide first.** Which files will the new report command touch? Write the list. Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- a branch
- the feature
- a pull request that says what, why and how it was tested
- no merge yet

Show a sample prompt

Sample promptCompare with yours

```
On a new branch, add mailroom report: the send also writes outbox/sent.json with each email's id, recipient and status, and report prints how many each group got, and any failures. Tests first: after a send to all 24, the report says 8 per group and no failures. Then push and open a pull request with gh that says what changed, why, and how I tested it. Don't merge.
Add to AGENTS.md: every change goes on a branch and arrives as a pull request.
```

**Then:** open the pull request on GitHub and read *Files changed* yourself. When you are happy, tell Claude: "Merge it, delete the branch, and pull main."

#### Investigate

1. Compare your list with the pull request's files. What did you miss?
2. Ask: "What is the difference between a commit and a pull request?"

#### Modify

Write a prompt for a small change of your own, as a second pull request.

CheckNew session: /exit, then claude, then paste

```
Check my pull request. Don't change any files.
1. Run gh pr list --state all.
2. For the report pull request, does the description say what, why and how it was tested?
3. Run git log --oneline --graph -8 on main. Did the change come in through the merge?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why changes go through pull requests.
```

#### You'll know it worked when

- The report pull request is merged, and you read it first.

#### AGENTS.md gains

Every change goes on a branch and arrives as a pull request.

20

[15.4 Layers of trust](https://agentfactory.panaversity.org/building-ai-workers/code-review/why-review-changes/)[15.5 Evidence before the pull request](https://agentfactory.panaversity.org/building-ai-workers/code-review/evidence-before-the-pr/)

### Evidence, not "done"

Put the proof in the pull request.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 15.4. Update How I learn in AGENTS.md."

**The problem.** "Done" is a claim. A reviewer wants proof: the tests ran, the types are clean, the real issue still passes.

**You decide first.** For the new rule below, what would the tests catch, what would the type checker catch, and what only a person? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- a pull request template
- the new rule, tests first
- real outputs pasted

Show a sample prompt

Sample promptCompare with yours

```
On a new branch, add a pull request template with What changed, Why, Evidence (the real output of pytest, pyright and mailroom check) and Risk. Then add a rule, tests first: the preview must not repeat the subject. Open the pull request with the template filled in with the real outputs.
Add to AGENTS.md: a pull request shows its evidence.
```

#### Investigate

1. Which piece of evidence would you trust least?
2. Ask: "Which mistakes would none of these layers catch?"

#### Modify

Review a classmate's pull request and ask for one missing piece of evidence.

CheckNew session: /exit, then claude, then paste

```
Review my latest pull request. Don't change any files.
1. Read it with gh pr view and gh pr diff.
2. Check its branch out into a temporary git worktree, run pytest, pyright and mailroom check yourself, and compare with the evidence pasted. Do they match?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about the difference between evidence and a claim.
```

#### You'll know it worked when

- A fresh session re-ran your evidence and got the same results.

#### AGENTS.md gains

A pull request shows its evidence.

21

[15.8 Checks that block](https://agentfactory.panaversity.org/building-ai-workers/code-review/checks-that-block/)

### Checks that block

Run the checks on GitHub for every pull request, and refuse a merge that fails.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 15.8. Update How I learn in AGENTS.md."

**The problem.** Evidence pasted by hand can be skipped. Checks that GitHub runs cannot.

**You decide first.** You will open a pull request that only gives the issue a 56-character subject. Will GitHub let you merge it? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- a workflow that runs the tests, the types and the issue checks
- main protected: a pull request and the passing check

Show a sample prompt

Sample promptCompare with yours

```
On a new branch, add a GitHub Actions workflow that runs on every pull request: uv sync, pytest, pyright, and mailroom check on every issue. Open it as a pull request, and when it passes, merge it. Then protect main: a pull request and the passing check are required before merging.
Add to AGENTS.md: the checks must pass before a merge.
```

Break itPaste this exactly

```
On a new branch, change only the issue's subject to "Your first Steep Club box ships Monday, and it is lovely". Don't run anything yourself. Push, open a pull request, and tell me what the checks say and whether GitHub allows the merge.
```

#### Investigate

1. Open the failed check's log. Find the line that says why.
2. Ask: "Could I merge anyway? What would stop me?"

#### Modify

Fix the subject on the same branch and watch the check turn green.

CheckNew session: /exit, then claude, then paste

```
Check the protection. Don't change any files.
1. Run gh api repos/{owner}/{repo}/branches/main/protection and say in plain words what it requires.
2. Find the pull request with the 56-character subject. Did its check fail?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why a check that blocks beats evidence pasted by hand.
```

#### You'll know it worked when

- The long subject was blocked before any person looked.

#### AGENTS.md gains

The checks must pass before a merge.

22

[15.6 Rules the reviewer reads](https://agentfactory.panaversity.org/building-ai-workers/code-review/rules-the-reviewer-reads/)[15.7 AI review on every pull request](https://agentfactory.panaversity.org/building-ai-workers/code-review/ai-review-on-every-pr/)

### A reviewer that reads your rules

Write down what a reviewer checks, and let Claude review every pull request against it.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 15.6. Update How I learn in AGENTS.md."

**The problem.** Checks catch what can be tested. A reviewer catches the rest, if it knows your rules.

**You decide first.** Which of your AGENTS.md rules can no test catch? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- REVIEW.md from your rules
- Claude reviewing each pull request against it

Show a sample prompt

Sample promptCompare with yours

```
Write REVIEW.md: what a reviewer checks in Mailroom, taken from AGENTS.md, with the rules no test can catch first.
```

**Then you do this yourself:** in Claude Code, run `/install-github-app` and follow its steps, so Claude can review pull requests on your repository. Then ask Claude to add a workflow that reviews every pull request against REVIEW.md, as 15.7 shows. Open a small pull request and read the review.

#### Investigate

1. Which rule did the review use?
2. Ask: "What does a reviewer catch that a check cannot?"

#### Modify

Add one rule to REVIEW.md, and open a pull request that breaks it. Does the review notice?

CheckNew session: /exit, then claude, then paste

```
Check the review setup. Don't change any files.
1. Read REVIEW.md. Does each rule match one in AGENTS.md?
2. List the workflows in .github/workflows and what each runs.
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about what a reviewer adds to the checks.
```

#### You'll know it worked when

- Claude's review cites a rule from REVIEW.md.

#### AGENTS.md gains

Reviewers read REVIEW.md.

23

[15.9 Human approval, scaled by risk](https://agentfactory.panaversity.org/building-ai-workers/code-review/approval-scaled-by-risk/)

### A person for risky changes

Ask a person to approve only the risky code.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 15.9. Update How I learn in AGENTS.md."

**The problem.** An issue's wording is low risk. The sending code can email the wrong people. They should not need the same approval.

**You decide first.** Which files in Mailroom could do real harm if they were wrong? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- CODEOWNERS for the risky files
- main requires a code owner's approval

Show a sample prompt

Sample promptCompare with yours

```
On a new branch, add a CODEOWNERS file so that the sending code needs approval from @my-classmate, and merge it. Then make main require one approval, from a code owner, before merging.
```

**Then:** add your classmate to your repository as a collaborator, and they add you. Open two small pull requests, one that changes the sending code and one that changes only an issue. Which one waits for your classmate?

#### Investigate

1. Ask: "Why does risk decide who approves?"
2. Ask: "As the owner, could I bypass this? Should I?"

#### Modify

Approve your classmate's sending change, after reading it.

CheckNew session: /exit, then claude, then paste

```
Check the approvals. Don't change any files.
1. Read .github/CODEOWNERS. Which files need whose approval?
2. Read main's protection with gh api. Is a code owner's review required?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why not every change needs the same approval.
```

#### You'll know it worked when

- A sending change waits for your classmate. An issue change does not.

#### AGENTS.md

no new rule: CODEOWNERS holds it

24

[15.10 After the merge](https://agentfactory.panaversity.org/building-ai-workers/code-review/after-the-merge/)

### After the merge

Release a version, and undo a bad merge cleanly.

[ ] Done

**Your level.** Before you start, tell Claude: "I have now completed up to 15.10. Update How I learn in AGENTS.md."

**The problem.** Something bad will get merged one day. You need a clean way back, and a test so it never happens again.

**You decide first.** The checks will let a new issue with an http:// link through. Why? And when you add the https rule, an older test may disagree with it. Whose call is that? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- a release
- the bad change, then a revert
- the test that would have caught it

Show a sample prompt

Sample promptCompare with yours

```
Tag v1.0 and create a GitHub release with notes from the merged pull requests.
```

Break itPaste this exactly

```
A bad change: on a branch, add issues/issue-02.md, a copy of issue-01 with its link changed from https:// to http://. Open a pull request and merge it when the checks pass. Then undo it with a revert, as its own pull request.
```

Show the sample for: Then make it impossible

Then make it impossibleCompare with yours

```
Tests first, make the check require https links, as a pull request. If an older test disagrees: an http:// link is a problem of its own, so an issue with two links, one of them http://, has two problems. Merge it, and release v1.0.1.
Add to AGENTS.md: undo a bad merge with a revert pull request, then add the test that would have caught it.
```

#### Investigate

1. Ask: "Why a revert and not deleting the commit?"

#### Modify

Ask for release notes for v1.0.1 that explain the fix in two sentences.

CheckNew session: /exit, then claude, then paste

```
Check the releases. Don't change any files.
1. Run gh release list.
2. Find the revert pull request and the https test. Does uv run pytest pass on main?
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about how a bad merge is undone.
```

#### You'll know it worked when

- v1.0 and v1.0.1 exist, and a test now stops http links.

#### AGENTS.md gains

Undo a bad merge with a revert pull request, then add the test that would have caught it.

Part E · Steps 25 and 26

## Into your studio

Your Email Studio checked emails by reading them. Now your own code checks them, every time.

25

Your Email Studio

### A guard for Claude Code

Give Mailroom a command that a Claude Code hook can call.

[ ] Done

**The problem.** In the Email Studio, the send-guard hook had its own copy of the recipient rule. Mailroom has the same rule, tested. One copy is better than two.

**You decide first.** A hook sends a tool call as JSON. What must the guard read from it? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- what the guard reads and when it refuses
- exit codes
- --subscribers for the studio's file

Show a sample prompt

Sample promptCompare with yours

```
Add mailroom guard: it reads a Claude Code hook's tool call as JSON from standard input. For the tools send-email and send-batch-emails, it checks every to, cc and bcc address with our recipient rule. If any fails, it prints why to standard error and exits 2. Otherwise it exits 0. Also add --subscribers to every command that reads subscribers. Tests first: sara.ali@gmail.com exits 2 with a reason, delivered@resend.dev exits 0, and another tool exits 0. Merge it and release v1.1.
```

#### Investigate

1. Ask: "Why exit code 2?"
2. Where does the recipient rule live now?

#### Modify

Ask what the guard does with a tool it does not know. Decide if that is right.

CheckNew session: /exit, then claude, then paste

```
Test the guard. Don't change any project files.
1. Pipe a sample hook JSON for send-email to sara.ali@gmail.com into uv run mailroom guard, and show the exit code and message.
2. Do the same for delivered@resend.dev.
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why one copy of a rule beats two.
```

#### You'll know it worked when

- Gmail gets exit code 2 with a reason. A practice address gets 0.

#### AGENTS.md

no new rule

26

Your Email Studio

### Mailroom guards the studio

Install your tool and let hooks run it: code enforces the fixed rules, Claude handles the judgment.

[ ] Done

**Before you start.** Open Claude Code in your `my-email-studio` folder for this step.

**The problem.** In the studio, a fresh session counted characters to check your emails. Reading can be wrong. Mailroom is not.

**You decide first.** You ask the studio's Claude for an email with a 56-character subject. Who notices first: you, Claude, or Mailroom? And if you tell Claude to keep it anyway? Write it in `notes/predictions.md`.

#### Write your own prompt. It must say

- install Mailroom from your release
- a hook that checks every email Claude writes
- the send-guard calling mailroom guard
- which rule decides who may receive practice mail

Show a sample prompt

Sample prompt, in the studioCompare with yours

```
Install my Mailroom tool from GitHub: uv tool install git+https://github.com/you/mailroom@v1.1.
Add a PostToolUse hook for Write and Edit: when the file is an email under campaigns/, run mailroom check on it, and if it finds problems, print them to standard error and exit 2 so you see them.
Make .claude/hooks/send-guard.mjs pass the tool call to mailroom guard and use its answer.
Update CLAUDE.md: practice sends go only to @example.com and @resend.dev, and Mailroom's guard decides.
Commit.
```

**Then:** start a new session in the studio, so the hooks load. Ask for a new email with the subject "Your first Steep Club box ships Monday, and it is lovely". Claude will probably shorten it on its own, because it read the rule. Now ask again, and insist: "Use exactly this subject, and do not shorten it." Claude writes it, Mailroom's hook reports the problem the moment the file is saved, and Claude has to stop and ask you.

#### Investigate

1. Find the line in the hook script that decides a file is an email.
2. Ask: "What does Claude see when the hook exits 2?"

#### Modify

Stretch: restart the practice server with an allowlist (a seed file with resend: and allowlist:, started with --seed). Now a third guard, the server, answers 403.

CheckNew session: /exit, then claude, then paste

```
Test Mailroom inside this studio. Don't change files you did not make for this test.
1. Run mailroom --help.
2. Write a temporary email under campaigns/test/emails/ with a 56-character subject. Did the hook report it? Quote it. Then delete the file.
3. Run mailroom check on every email under campaigns/.
Give me a short table: Test | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about which rules belong in code and which in Claude's judgment.
```

#### You'll know it worked when

- Even when you told Claude to keep the long subject, Mailroom caught it the moment the file was saved.
- Claude stopped and asked you, instead of going around the hook.

#### AGENTS.md

the studio's CLAUDE.md) Fixed rules are checked by Mailroom. Claude handles the judgment.

## When you are finished

| Check | How you show it |
| --- | --- |
| Every command works on a fresh clone | A classmate clones your repository and runs `uv run mailroom --help`. |
| Tests and types are clean | `uv run pytest` and `uv run pyright` pass on main. |
| The checks are green on main | The latest GitHub run is green, and a bad issue fails it. |
| Reviewed pull requests | At least three merged, each with evidence. |
| Releases | `v1.0`, `v1.0.1` and `v1.1`. |
| Honest predictions | `notes/predictions.md` has one for every step, never changed after the run. |
| The studio uses Mailroom | Step 26's check passes in your studio. |

| Steps | Hand in |
| --- | --- |
| 0 to 18 | Your repository's address after each class. Your commits and predictions show the work. |
| 19 to 25 | The address of each pull request. |
| 26 | A screenshot of Mailroom's message in your studio, and the studio's commit. |

Each step links to its section of *The AI Agent Factory*. Read it before class, or straight after. Every subscriber is made up, and every email goes to the practice server on your own computer.