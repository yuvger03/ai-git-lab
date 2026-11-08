# Git basics

The ten ideas from the opening slides, in the same order. Come back here whenever a word or a command is unclear.

## 1. Why version control?

| Without git | With git |
| --- | --- |
| `report_final_v2_REALLY_final.py` | One folder, every version kept |
| "Who broke this, and when?" | Every change has an author, a time and a reason |
| Zip files emailed to your partner | Partners work in parallel, then merge |
| One bad edit and yesterday's version is gone | Any change can be undone |

When an AI agent edits your files, this stops being optional.

## 2. Nine words

| Word | Meaning |
| --- | --- |
| Repository (repo) | A project folder plus its full history of changes |
| Commit | A saved snapshot of the project, with an author and a message |
| Branch | A named line of commits; `main` is the shared one |
| Clone | Your full local copy of a repo, history included |
| Remote, `origin` | The copy on a server, here GitHub. Git calls it `origin` |
| Fork | Your own GitHub copy of someone else's repo |
| Merge | Joining two lines of commits into one |
| Conflict | Both sides changed the same lines; a human decides |
| Pull request | A request, on GitHub, to merge your branch after review |

Remote, fork and pull request are GitHub ideas. The rest is git itself, on your laptop.

## 3. A commit is a snapshot with a parent

```
a1f3c09 <-- 7d2e4b1 <-- 3f1c2ab <-- e58d6a0 <-- main <-- HEAD
Starter     Fix final   Raise pass  Add --top N
code        grade       mark to 60  to the report
```

- A commit stores the whole project as it was, plus who, when and why.
- Its ID, like `3f1c2ab`, is a hash of all that: change anything and the ID changes.
- Each commit points to its parent, so history is a chain you can walk back.
- A branch name such as `main` points at the newest commit; `HEAD` marks where you are.

## 4. The life of one change

| Step | Command | `git status` then says | In PyCharm |
| --- | --- | --- | --- |
| 1. Edit | You, or the agent, change `grades.py` | `Changes not staged for commit` | A coloured bar in the gutter |
| 2. Stage | `git add gradebook/grades.py` | `Changes to be committed` | Tick the file in the Commit dialog |
| 3. Commit | `git commit -m "Fix final grade weighting"` | `Your branch is ahead of 'origin/main' by 1 commit.` | Ctrl+K · Cmd+K |
| 4. Push | `git push` | `Your branch is up to date with 'origin/main'.` | Ctrl+Shift+K · Cmd+Shift+K |

A commit is saved on your laptop only: nobody sees it until you push. PyCharm's Commit dialog stages and commits in one go, so ticking a file is `git add`.

## 5. A branch is a movable label

```
            o---o   <-- feature/top-n  <-- HEAD
           /
  o---o---o         <-- main
```

| Command | What happens |
| --- | --- |
| `git switch -c feature/top-n` | A new label at the current commit; `HEAD` moves onto it |
| `git commit`, twice | The label you are on moves forward with each commit; `main` stays where it was |
| `git switch main` | `HEAD` moves back to `main`, and your files change to main's version |

A branch costs nothing: it is just a name that points at a commit.

## 6. A merge ends in one of three ways

| Case | When | What git does |
| --- | --- | --- |
| Fast-forward | Only one side has new commits | Moves the label forward; no new commit |
| Merge commit | Both sides have new commits, on different lines | Joins them in a commit with two parents |
| Conflict | Both sides changed the same lines | Stops; you choose, then you commit the merge |

Git merges lines, not files: two people can edit the same file and still merge cleanly. `git merge <branch>` joins that branch into the one you are on; `git pull` does the same with GitHub's copy. You will meet all three cases today.

## 7. Your laptop and GitHub

```
  YOUR LAPTOP                                    GITHUB
  +----------------------+                       +------------+
  |  origin/main   <-----+------ git fetch ------+            |
  |       |              |                       |    main    |
  |   git merge          |                       |            |
  |       v              |                       |            |
  |  main   -------------+------ git push  ----->+            |
  +----------------------+                       +------------+
```

- `git clone` copies the whole repo to your laptop, once, at the start.
- `origin/main` is your laptop's picture of GitHub's `main`, as you last saw it.
- `git fetch` downloads new commits into `origin/main` and changes none of your files.
- `git merge origin/main` brings them into your `main`. That is the step that changes your files.
- `git pull` is `git fetch`, then `git merge`. That is why a pull can stop with a conflict.
- `git push` sends your new commits to GitHub's `main`.

## 8. Clone, fork or template?

| Kind of copy | Clone | Fork | Template |
| --- | --- | --- | --- |
| Where it lives | Your laptop | GitHub, your account | GitHub, your account |
| History | All of it | All of it | Fresh: one commit |
| Still linked? | Yes, as `origin` | Yes: pull requests can go back | No |
| Use it when | You work on a repo | You can't push, but want to help | You want a clean starter |
| Today | Both partners clone | Not used | A makes the pair's repo |

Your final project: one shared repo with your teammates as collaborators, and everyone clones it. Forks are for projects you cannot push to. Clone is a git command; fork and template are buttons on GitHub.

## 9. The commands, and where they work

| Command | What it does | Talks to GitHub? |
| --- | --- | --- |
| `git status` | What changed? What's staged? | No |
| `git add <file>` | Stage a change for the next commit | No |
| `git commit -m "..."` | Save a snapshot with a message | No |
| `git switch -c <name>` | Create a branch and move to it | No |
| `git merge <branch>` | Join that branch into the one you are on | No |
| `git clone <url>` | Copy a repo, history and all | Yes |
| `git push` | Send your commits to GitHub | Yes |
| `git fetch` | Download only; your files stay as they are | Yes |
| `git pull` | `git fetch`, then `git merge` | Yes |

Fork and pull request are buttons on GitHub, not git commands. In class you click most of these in PyCharm; [cheatsheet.md](cheatsheet.md) gives the PyCharm action for each.

## 10. Quick check, with your partner

Agree on your answers first, then check them at the bottom of this page.

1. Which four commands talk to GitHub?
2. You ran `git fetch`. Did any of your files change?
3. Complete it: `git pull` = ? + ?
4. Where does a fork live? And a clone?

&nbsp;

&nbsp;

&nbsp;

**Answers.** 1: `clone`, `push`, `fetch`, `pull`. 2: No; only `origin/main` moved. 3: `git fetch` + `git merge`. 4: A fork lives on GitHub, in your account; a clone lives on your laptop.
