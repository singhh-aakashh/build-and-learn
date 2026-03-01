# Top-K (LLM Parameter)

## What It Does
Limits sampling to the K most likely tokens before choosing the next one. Filters the candidate pool.

## Behavior
| Value | Effect |
|-------|--------|
| **Low (1–10)** | Fewer options, more deterministic |
| **High (40–100)** | More options, more varied output |

## When to Use
- **Low:** Facts, code, focused tasks
- **High:** Creative tasks, varied wording

## Takeaway
Top-K = "How many candidate tokens to consider?" Lower = fewer options. Higher = more variety.
