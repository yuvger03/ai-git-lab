# ai-git-lab

A tiny Python gradebook for practising git, PyCharm and AI coding agents together. It has bugs on purpose: right now it fails the whole class.

## Run it

Python 3.10 or newer. Nothing to install.

```
python -m unittest -v
python -m gradebook report data/course.csv
python -m gradebook stats data/course.csv
```

On macOS you may need `python3` instead of `python`.

## What is where

| Path | What it holds |
| --- | --- |
| `gradebook/config.py` | Course policy: pass mark, letter bounds, weights |
| `gradebook/grades.py` | Final grade, letter, pass/fail |
| `gradebook/stats.py` | Mean and median |
| `gradebook/loader.py` | Reads the CSV file |
| `gradebook/cli.py` | The `report` and `stats` commands |
| `tests/` | Unit tests (`unittest`) |
| `data/course.csv` | Eight fictional students |
| `tasks/` | One task card per partner per part of the lab |
| `AGENTS.md` | Rules every coding agent follows in this repository |

## The lab

Follow the lab sheet from your instructor. Partner A and Partner B each open their own card in `tasks/` for each part.
