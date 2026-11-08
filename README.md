# ai-git-lab

A tiny Python gradebook for practising git, PyCharm and AI coding agents together, in pairs. It has bugs on purpose: right now it fails the whole class.

- **Before class:** do [SETUP.md](SETUP.md) at home (about 20 minutes).
- **In class:** Part 0 below, then [tasks/README.md](tasks/README.md).
- **Before you use any API key:** [tasks/secrets.md](tasks/secrets.md). Keys never go in code or in git.

## Part 0: your pair repository (15 minutes)

By the end of Part 0, both partners have a clone of the same GitHub repository open in PyCharm.

### Partner A

1. On the template repository's page (this page, if you are reading it on GitHub), click **Use this template**, then **Create a new repository**. Owner: you. Name: `ai-git-lab`. Private. Click the green create button at the bottom of the form.
2. In your new repository: **Settings → Collaborators → Add people**. Enter your partner's GitHub username and send the invitation.

### Partner B

3. Accept the invitation from your email, from github.com/notifications, or at `https://github.com/<A's username>/ai-git-lab/invitations`.

### Both partners

4. In PyCharm: **Git → Clone** (on the Welcome screen: **Clone Repository**). Choose **GitHub** on the left, select `<A's username>/ai-git-lab`, and click **Clone**. Trust and open the project.
5. If PyCharm asks for a Python interpreter, create a virtual environment with any Python 3.10 or newer. There is nothing to install.
6. **Predict:** the tests say the final grade is broken. What will the report show? Write it down, then open PyCharm's terminal (Alt+F12 · Option+F12) and run:

```
python -m unittest
python -m gradebook report data/course.csv
```

Expected: `Ran 13 tests` and `FAILED (failures=4)`. The report fails all eight students, with final grades between 16 and 33.

**Checkpoint.** Both partners see the same 4 failures.

**No partner today?** Clone your repository twice, into folders `ai-git-lab-A` and `ai-git-lab-B`, open each in its own PyCharm window, and play both roles.

Next: open [tasks/README.md](tasks/README.md).

## Run it

Python 3.10 or newer, nothing to install. On macOS, type `python3` instead of `python`.

```
python -m unittest -v
python -m gradebook report data/course.csv
python -m gradebook stats data/course.csv
```

## What is where

| Path | What it holds |
| --- | --- |
| `SETUP.md` | Before-class setup |
| `tasks/README.md` | Start here in class: the plan, your cards, the rules |
| `tasks/git-basics.md` | The git ideas and commands from the opening slides |
| `tasks/cheatsheet.md` | The PyCharm action, git command and AI prompt for every step |
| `tasks/secrets.md` | API keys, `.env` and `.gitignore`: read before you use any key |
| `tasks/part1-A.md` … `tasks/part4.md` | One card per partner per part |
| `tasks/exit-ticket.md`, `tasks/bonus.md` | The exit ticket, and extras for fast pairs |
| `AGENTS.md` | Rules every coding agent follows in this repository |
| `gradebook/config.py` | Course policy: pass mark, letter bounds, weights |
| `gradebook/grades.py` | Final grade, letter, pass/fail |
| `gradebook/stats.py` | Mean and median |
| `gradebook/loader.py` | Reads the CSV file |
| `gradebook/cli.py` | The `report` and `stats` commands |
| `tests/` | Unit tests (`unittest`) |
| `data/course.csv` | Eight fictional students |
