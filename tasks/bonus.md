# Finished early?

## 1. The AI as git historian (rung 1)

> Using `git log --graph --oneline --all` and `git show`, tell the story of what happened in this repository today: who changed what, where the merges are, and which commit changed the pass mark. Do not change any files.

Compare its story with the graph in PyCharm's Git tool window (Alt+9 · Cmd+9). Did it get anything wrong?

## 2. An empty file crashes `stats`

Make a CSV that has only the header line. `python -m gradebook stats` on it crashes with `ZeroDivisionError`. On a new branch `fix/empty-file`, have the agent make `stats` print `No students in file` and exit with code 1, with a new test. Open a pull request.

## 3. Rebase instead of merge

Repeat the push race from Part 1 with two new small commits, but this time choose **Rebase** when PyCharm offers to update. Compare the Git log graph with the one from Part 1: where did the merge commit go?
