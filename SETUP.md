# Before class: setup (about 20 minutes)

Do this at home. If any check fails, message the instructor before class: there is no time for installs during the lab.

## 1. Accounts

- A free GitHub account. Write down your username; your partner needs it.
- A personal Google account (a gmail.com address) for Gemini. Antigravity is not available to users under 18, and university or work Google accounts work only if their administrator has enabled it.

## 2. Install

- **PyCharm 2026.2.1 or newer.** Check with Help → About.
- **Git.** Windows: Git for Windows, default options. macOS: run `git --version` in Terminal and accept the offer to install the command line tools. Linux: your package manager.
- **Python 3.10 or newer.**
- **The Antigravity CLI**, Gemini's coding agent ([quickstart](https://antigravity.google/docs/getting-started)):
  - macOS or Linux: `curl -fsSL https://antigravity.google/cli/install.sh | bash`
  - Windows PowerShell: `irm https://antigravity.google/cli/install.ps1 | iex`
  - Then open a new terminal and run `agy --version`.

## 3. Tell git who you are

In any terminal, once:

```
git config --global user.name "Your Name"
git config --global user.email "the email of your GitHub account"
git config --global pull.rebase false
```

The last line makes `git pull` merge, which is what we practise in class. Without it, newer git versions stop with "Need to specify how to reconcile divergent branches".

## 4. Connect PyCharm to GitHub

Settings → Version Control → GitHub → **+** → **Log In via GitHub**, then approve in the browser.

## 5. Sign in to Antigravity

Run `agy` in a terminal, pick a colour scheme, and sign in with your personal Google account in the browser. Type `/usage` to see your quota, then close that terminal. The free plan has a weekly quota, so do not use it up before class.

## 6. Smoke test

Restart PyCharm, open its terminal (Alt+F12 · Option+F12) and run:

```
git --version
agy --version
python --version
```

On macOS, use `python3 --version`. Then open **Git → Clone** and choose **GitHub** on the left: you should see your repositories listed. Cancel.

Optional: Antigravity can also run inside PyCharm's AI Chat (Settings → Tools → AI Assistant → Agents, search for Antigravity, Install). The lab itself uses the terminal, which works the same on every machine.
