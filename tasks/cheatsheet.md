# Cheat sheet

Every action has three forms: the PyCharm action you click, the git command an agent would type, and the question worth asking the AI. Shortcuts are Windows/Linux · macOS.

| I want to | PyCharm | Git | Ask the AI |
| --- | --- | --- | --- |
| See what changed | Commit tool window (Alt+0 · Cmd+0), double-click a file | `git status`, `git diff` | "Summarize my uncommitted changes. Don't change files." |
| Commit | Ctrl+K · Cmd+K | `git add <file>`, `git commit -m "..."` | "Write a one-line commit message for these changes." |
| Push | Ctrl+Shift+K · Cmd+Shift+K | `git push` | Nothing: you push |
| Get my partner's work | Git → Update Project: Ctrl+T · Cmd+T, Merge | `git pull` (`git fetch` + `git merge`) | "Explain what this update brought in." |
| Understand a git error | Read the dialog first | `git status` | "Explain this message and the safest fix. Read-only commands only." |
| See history | Git tool window (Alt+9 · Cmd+9), Log tab | `git log --oneline --graph --all` | "Tell the story of this history." |
| Find who changed a line | Right-click the gutter, Annotate with Git Blame | `git blame <file>` | "Why did this line change? Use git log -p." |
| Start a branch | Branch name in the toolbar → New Branch | `git switch -c <name>` | Nothing: you branch |
| Switch branch | Branch name in the toolbar → the branch → Checkout | `git switch <name>` | Nothing: you switch |
| Resolve a conflict | Commit tool window → Merge Conflicts → Resolve → Merge | Edit the file, `git add`, `git commit` | "Explain both sides of this conflict. Don't edit." |
| Throw away uncommitted changes | Rollback: Ctrl+Alt+Z · Cmd+Option+Z | `git restore .` | Nothing: you decide |
| Undo a pushed commit | Git log → right-click → Revert Commit | `git revert <commit>` | Nothing: you decide |
| Open the terminal | Alt+F12 · Option+F12 | | |

## Agent controls

| Control | Antigravity CLI (Gemini) | Claude Code (instructor demo) |
| --- | --- | --- |
| Start in the project folder | `agy` | `claude` |
| Approve or reject a step | `y` or `n` | Pick an option in the prompt |
| Cycle modes | Shift+Tab: default, accept-edits, auto, plan | Shift+Tab: manual, accept edits, plan, auto |
| See its changes | `/diff` | Diffs open in PyCharm's diff viewer |
| Project rules file | `AGENTS.md` or `GEMINI.md` | `CLAUDE.md`; reads `AGENTS.md` when there is no `CLAUDE.md` |
| Undo inside a session | `/rewind` (the conversation only) | Esc Esc or `/rewind` (its own edits and the conversation) |
| One question, no session | `agy -p "..."` | `claude -p "..."` |
| Quota left | `/usage` | |

Stay in the default mode today: it asks before every edit and every command.
