# One Line, Big Laugh — reference letter

[![make.fun · u-coral-404-one-line-big-laugh-328fb857](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-big-laugh-328fb857)
[![rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/mwhbonk/makefun-u-coral-404-one-line-big-laugh-328fb857/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-big-laugh-328fb857)
[![reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/mwhbonk/makefun-u-coral-404-one-line-big-laugh-328fb857/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-big-laugh-328fb857)

Entry for the [One Line, Big Laugh](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857) bounty on make.fun.

## The joke

> My AI agent finished my job in four seconds, then asked me for a reference letter to apply for my job.

102 characters, 21 words, one line. Setup (finished my job in four seconds), turn (it asks *me* for a reference letter), punchline (to apply for *my* job) — the callback is the part people repeat.

## How it works

`main.py` (Python 3.13, standard library only) writes the line verbatim to `/output/entry.txt`, no trailing newline, so the judge reads exactly these bytes. The same text lives in `joke.txt` for reference.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
