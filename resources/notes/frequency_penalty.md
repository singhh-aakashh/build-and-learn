# Frequency Penalty (LLM Parameter)

## What It Does
Penalizes tokens based on how often they've already appeared in the output. Reduces repetition.

## Behavior
| Value | Effect |
|-------|--------|
| **0** | No penalty |
| **Positive (0.5–1.0)** | Reduces repetition of same words/phrases |
| **Negative** | Can increase repetition |

## When to Use
- **Positive:** When model repeats words or phrases (lists, long answers)
- **0:** Default, no change

## Takeaway
Frequency penalty = "Discourage tokens that have already been used often." Good for reducing verbatim repetition.
