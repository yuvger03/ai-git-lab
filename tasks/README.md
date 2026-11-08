# Start here

You work in pairs on one shared GitHub repository, each partner in their own PyCharm clone. By the end, git will have rejected your push at least twice, you will have fixed it the right way each time, and you will have shipped an AI-written change through a reviewed pull request.

## The plan

| Time | Part | Minutes | Open |
| --- | --- | --- | --- |
| 0:00 | Git basics | 18 | [git-basics.md](git-basics.md) |
| 0:18 | 0. Pair repository | 15 | Part 0 in [../README.md](../README.md) |
| 0:33 | 1. Commit and the push race | 25 | Your Part 1 card |
| 0:58 | 2. A real merge conflict | 20 | Your Part 2 card |
| 1:18 | 3. AI on a branch: the demo, then your turn | 10 + 20 | Your Part 3 card |
| 1:48 | 4. Break it, recover it | 7 | [part4.md](part4.md) |
| 1:55 | Exit ticket | 5 | [exit-ticket.md](exit-ticket.md) |

Need a command? [cheatsheet.md](cheatsheet.md). Finished early? [bonus.md](bonus.md).

## Your cards

| Part | Partner A | Partner B | Who pushes first |
| --- | --- | --- | --- |
| 1 | [part1-A.md](part1-A.md) | [part1-B.md](part1-B.md) | A |
| 2 | [part2-A.md](part2-A.md) | [part2-B.md](part2-B.md) | B |
| 3 | [part3-A.md](part3-A.md) | [part3-B.md](part3-B.md) | Either: you work on separate branches |
| 4 | [part4.md](part4.md) | [part4.md](part4.md) | Nobody pushes |

Open only your own card for the part you are on. When a card says **Stop here**, do that step before you read on, or you spoil your own prediction.

## How the cards are written

- **Predict** steps: write one line before you click (what will git do?), then run it, then explain the result to your partner in one sentence. Wrong predictions are useful: they show where your picture of git breaks.
- Each step gives the PyCharm action you click and, on a **Git:** line, the command behind it. Coding agents type these commands in the terminal, so you need to be able to read them and judge them before you approve them.
- Shortcuts are written Windows/Linux · macOS, for example Commit: Ctrl+K · Cmd+K.
- On macOS, type `python3` wherever a card says `python`.

## The AI trust ladder

The AI gets more autonomy as your git safety net gets stronger.

| Rung | The AI | You | Where |
| --- | --- | --- | --- |
| 1. Explain | Reads code, test output and git messages; changes nothing | Ask, then check the answer against what you see | Part 1 |
| 2. Suggest | Proposes a fix or a conflict resolution | Apply it yourself, or reject it | Part 2 |
| 3. Act on a branch | Edits files on a feature branch | Review the diff, run the tests, commit | Part 3 |
| 4. Review | Comments on your partner's pull request | Decide what gets merged | Part 3 |

## Three rules for the whole session

1. Know your `git status` before an agent touches your files. A clean working tree is your undo point.
2. Never approve an agent's `git push --force`, `git reset --hard` or `git clean -fd`. These delete work, sometimes your partner's. Part 4 shows the safe ways to undo instead.
3. When something looks wrong, stop and run `git status` before anything else. Then ask the AI, your partner, or the instructor.

The agents follow [../AGENTS.md](../AGENTS.md). Read it once: it is what keeps them inside these rules.
