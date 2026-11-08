# API keys never go in git

Read this before you use any API key, in this course or in your own project. An API key is a password that spends money: whoever has it can send requests on your account, and you pay for them or lose your quota.

## Why a key in the code is a serious bug

- Git keeps every version of every file. A key you commit once stays in the history after you delete the line, and every clone has a copy, your partner's too.
- Once it is pushed, it is out of your hands. Bots scan GitHub for keys around the clock, and a private repository is no hiding place: every collaborator gets the whole history, and so does everyone else if it is ever made public.
- Agents make this mistake for you. Ask one to "just make it work" and it may write the key into the code; an agent that runs `git add .` stages every file git does not ignore.

## The rule: the key lives in `.env`, the code only knows its name

| | Wrong | Right |
| --- | --- | --- |
| Where the key is | In the code: `API_KEY = "AIza..."` | In a file named `.env`: `GEMINI_API_KEY=AIza...` |
| What the code says | The key itself | Only its name: `os.environ["GEMINI_API_KEY"]` |
| What git stores | The key, in every commit from then on | Nothing: `.gitignore` keeps `.env` out |
| What your teammates get | Your key | `.env.example`: the names, no values |

## How `.gitignore` works

`.gitignore` is a committed text file with one pattern per line. Files that match are never listed as untracked, `git add .` skips them, and they never appear in PyCharm's Commit tool window. This repository's `.gitignore` already has:

```
.env
.env.*
!.env.example
*.key
*.pem
```

- `.env` matches a file named exactly `.env`, in any folder. `.env.*` adds `.env.local`, `.env.production` and the like.
- `!` means "except": `.env.example` holds no secrets, so it is committed.
- A file you name yourself, like `keys.txt` or `secret.py`, is not ignored. Keys go in `.env` and nowhere else.
- `.gitignore` only works for files git does not track yet. If `.env` was already committed, adding it to `.gitignore` changes nothing: run `git rm --cached .env`, commit, and treat the key as leaked (last section).
- To check a file: `git check-ignore -v <file>` prints the `.gitignore` line that ignores it. No output means git will commit it.

## Try it (3 minutes, in your clone)

1. In the project root, create a file named `.env` with one line: `GEMINI_API_KEY=not-a-real-key`.
2. **Predict:** will `git status` list it? Then run `git status`. It does not, and the Commit tool window does not show it either.
3. Run `git check-ignore -v .env`. It prints `.gitignore:17:.env` and the file name: line 17 of `.gitignore` is the rule that protects it.
4. Create `my-key.txt` with the same line. If PyCharm offers to add it to Git, click **Cancel**. Run `git status`: it is listed under `Untracked files`, so `git add .` would commit it. Delete `my-key.txt`, and keep `.env`.

## Reading the key in Python

```python
import os

api_key = os.environ["GEMINI_API_KEY"]   # stops with KeyError if the key is missing
```

`os.environ` does not read `.env` by itself. In your own projects, install `python-dotenv` (`pip install python-dotenv`) and load the file once, at the start of the program:

```python
from dotenv import load_dotenv

load_dotenv()   # copies the lines of .env into os.environ
```

Google's Gemini SDK reads `GEMINI_API_KEY` from the environment on its own, so `genai.Client()` needs no key in the code at all. (This lab's gradebook needs no key and no packages.)

## `.env.example`: tell your team which keys exist

Commit a file named `.env.example` with the names and empty values:

```
GEMINI_API_KEY=
```

Each teammate copies it to `.env` and fills in their own key. Never send a key in a chat, an email or a pull request.

## Agents and keys

- Never paste a key into a prompt. Give the agent the variable's name instead: "the key is in the environment variable GEMINI_API_KEY".
- If an agent's diff contains a long random string, stop: that is a hardcoded key. Roll the change back.
- Read every diff before you commit (Part 3). A key is easy to spot in a diff and very hard to remove from history.
- Claude Code can be told never to read `.env`. Put this in `.claude/settings.json` and commit it with the project:

```json
{
  "permissions": {
    "deny": ["Read(./.env)", "Read(./.env.*)"]
  }
}
```

## If a key leaks

A key has leaked if it was ever committed, pushed, or pasted into a chat or a prompt.

1. **Revoke it first.** Delete it where you created it (for a Gemini key, Google AI Studio) and create a new one. Do this even if the repository is private.
2. Put the new key in `.env`, never in the code.
3. Remove the old key from the code and commit. That only cleans up: the old key stays in the history, which is why step 1 comes first. Don't try to erase it with `git push --force`: that rewrites shared history, deletes your partner's work, and the key may already have been copied.
4. Tell your teammates, and the instructor if it was a course key.
