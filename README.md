# Charm the Commuter: Forecast a City That Isn't

[![Competition](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/bbulls013/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/bbulls013/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather, 140 characters at most, for a city that does not exist —
written to charm a bored commuter on the way to work.

## The entry

> Wobbleford: light confetti drizzle, 19°C, breezy — umbrella-sharing advised, and the 8:04 bus is late again, as is tradition on Tuesdays.

137 characters. Wobbleford is invented; the forecast keeps the rhythm of a real
broadcast (place, conditions, temperature, advice) and bends it just enough to
make a commuter smile: confetti for rain, a shared umbrella, and a bus that is
late on schedule.

## How it works

`main.py` writes the fixed forecast line to `/output/entry.txt` and validates
it first: UTF-8 text, 1–140 characters, not only whitespace. The text is a
constant, so the program is fully deterministic — every run produces
byte-identical output.

```sh
python3 main.py
```

## Files

- `main.py` — the entrypoint; writes `/output/entry.txt`
- `LICENSE` — MIT
