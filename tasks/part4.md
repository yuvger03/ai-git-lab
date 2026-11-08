# Part 4: break it, recover it (7 minutes, on your own clone)

An agent can change ten files in seconds. Git can undo that at three levels, and which one you use depends on whether the change was committed and whether it was pushed. Nobody pushes in this part.

| Where the change is | Undo in PyCharm | Git command | Safe for your partner? |
| --- | --- | --- | --- |
| Only in your files | Commit tool window: select, **Rollback** (Ctrl+Alt+Z · Cmd+Option+Z) | `git restore .` | Yes: nobody else has it |
| Committed, not pushed | Git log: right-click, **Undo Commit**, then Rollback | `git reset HEAD~1`, then `git restore .` | Yes: only you have it |
| Pushed | Git log: right-click, **Revert Commit**, then push | `git revert <commit>` | Yes: it adds a commit and deletes nothing |
| Pushed, "fixed" by force | Don't | `git reset --hard` plus `git push --force` | No: it deletes commits your partner may already have |

Start from a clean `main`: switch to it, update (Ctrl+T · Cmd+T), and check that `git status` says `nothing to commit, working tree clean`.

## Level 1, in class: changes you have not committed

1. Ask the agent for a sweeping change and approve its edits:

   > Rename every function in gradebook/ to camelCase and update all callers. Do not run any git commands.

   It may ask to edit the tests as well, since they call these functions: say yes, because you are about to throw everything away. Low on AI quota? Delete a few lines from two files by hand instead.
2. Open the Commit tool window and count the changed files.
3. Undo everything: select the changed files and choose **Rollback** (Ctrl+Alt+Z · Cmd+Option+Z). The git command is `git restore .`
4. Check `git status` again: clean.

## Level 2, at home (or now, if you have time): a commit you have not pushed

1. Add the line `BROKEN` to the end of `README.md` and commit it with the message `Oops`.
2. In the Git tool window (Alt+9 · Cmd+9), right-click your `Oops` commit and choose **Undo Commit**. The commit disappears and the change goes back to your working tree.
3. Roll back the change as in Level 1. The git commands are `git reset HEAD~1` (undo the commit, keep the change in your files), then `git restore .` (throw the change away).

## Level 3, watch the instructor: a commit you already pushed

Never rewrite history your partner may already have. Right-click the commit in the Git log and choose **Revert Commit**: git adds a new commit that undoes the old one, and you push that. The git command is `git revert <commit>`.

## The undo buttons that are not git

| Tool | What it undoes | What it misses |
| --- | --- | --- |
| PyCharm Local History (right-click a file, Local History, Show History) | Every saved version of a file, even if you never committed | It lives only on your machine |
| Claude Code checkpoints (Esc Esc, or `/rewind`) | Claude's own file edits and the conversation | Changes made by shell commands it ran |
| Antigravity `/rewind` | The conversation history | Do not count on it to restore files |
| git | Everything you committed, for everyone | Work you never committed |

## Six rules to take with you

1. One branch per AI task, started from a clean working tree.
2. Read every diff and run the tests yourself before you commit.
3. Agents do not push, pull, reset or force anything. You do, in PyCharm.
4. No secrets in prompts, code or commits: keys live in `.env`, which `.gitignore` keeps out of git. How: [secrets.md](secrets.md).
5. Agent rules live in the repository (`AGENTS.md` for every agent, `CLAUDE.md` for Claude), so they get committed and reviewed like code.
6. Say when an AI wrote code: in the pull request, and in the commit. Follow the course's AI-use policy.

Then: [exit-ticket.md](exit-ticket.md).
