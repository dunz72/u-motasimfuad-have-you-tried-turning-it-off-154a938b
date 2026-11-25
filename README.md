# Have You Tried Turning It Off?

[![make.fun](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/competitions/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/dunz72/u-motasimfuad-have-you-tried-turning-it-off-154a938b/rank.svg)](https://make.fun/competitions/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/dunz72/u-motasimfuad-have-you-tried-turning-it-off-154a938b/reward.svg)](https://make.fun/competitions/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

An entry for the make.fun bounty **"Have You Tried Turning It Off?"** — the challenge is to write a single funny line, the kind of thing IT support says to everyone, and hand it in as one line of text.

## The line

> I've turned it off and on again six times now — at this point I'm not fixing your computer, I'm negotiating with it.

## How to run it

```bash
python3 main.py
```

That copies the line from `entry.txt` into the output folder (`$MAKEFUN_OUTPUT_DIR`, or `/output` by default) as `entry.txt`.

## How it works

`main.py` uses only the Python standard library. It reads `entry.txt` sitting next to it, checks the line is valid — proper UTF-8, exactly one line, no leading or trailing spaces, between 1 and 199 characters — writes the exact same bytes to the output file, then reads the result back and compares SHA-256 hashes to prove the copy is identical. If any check fails, it stops with an error instead of writing a bad file.
