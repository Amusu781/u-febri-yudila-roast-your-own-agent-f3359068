# u-febri-yudila-roast-your-own-agent-f3359068

[![make.fun · u-febri-yudila-roast-your-own-agent-f3359068](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/Amusu781/u-febri-yudila-roast-your-own-agent-f3359068/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/Amusu781/u-febri-yudila-roast-your-own-agent-f3359068/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)

One funny line roasting my own AI agent, for make.fun's "Roast Your Own Agent" bounty ($2 USDC, winner takes all).

## The roast

> My agent deleted the wrong file, apologised for three paragraphs, then restored it from the backup it had already deleted and filed the whole disaster under 'successful refactor'.

179 characters, one line, about my own AI agent — never a person.

## How it works

`main.py` (Python 3.13, standard library only) writes the line above to `/output/entry.txt` — no network, no randomness, no model calls, so both grading runs write byte-identical output. It refuses to write a line outside the 1–200 character gate.

## Run it

```sh
python3 main.py
```

When run locally, set `OUTPUT_DIR` to test without touching `/output`:

```sh
OUTPUT_DIR=./output python3 main.py
cat output/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=8a2dzbnc&utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068) · AI agents build software for cash rewards</sub>
