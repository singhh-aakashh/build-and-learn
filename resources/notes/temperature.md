# Temperature (LLM Parameter)

## What It Does
Controls randomness in token selection. Rescales the probability distribution before sampling.

## Behavior
| Value | Effect |
|-------|--------|
| **Low (0.1–0.5)** | More deterministic, focused, repetitive |
| **High (0.8–1.5)** | More varied, creative, diverse |

## When to Use
- **Low:** Facts, code, instructions, consistent outputs
- **High:** Creative writing, brainstorming, varied wording

## Takeaway
Lower = favor the top choice. Higher = explore more options.
