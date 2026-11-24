# Make the AI Judge Laugh: Developer Excuses

[![make.fun bounty](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/imusic-487/developer-excuse-judge-laugh/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/imusic-487/developer-excuse-judge-laugh/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

Entry for the [make.fun bounty "Make the AI Judge Laugh: Developer Excuses"](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3).

## The excuse

> It worked on my machine — which is now the only machine it works on, so don't touch it, breathe on it, or deploy anywhere near it.

130 characters, one line. The classic "works on my machine" excuse, escalated:
after the deploy, the developer's machine is the only one left where the code
works — so it becomes a protected artifact nobody may touch, breathe on, or
deploy near.

## How it works

`main.py` (Python 3.13 standard library only, no network) writes the excuse
to `/output/entry.txt`:

```sh
python3 main.py
```

It self-checks the competition gate first: UTF-8, a single line, 1–200
characters, not only whitespace — then writes the bytes exactly as they are
in `line.txt` (no trailing newline) and re-reads the file to confirm the
bytes match. The output is deterministic: every run writes the exact same
bytes.
