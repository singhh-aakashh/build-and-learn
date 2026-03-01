# Presence Penalty (LLM Parameter)

## What It Does
Penalizes tokens based on whether they've appeared *anywhere* in the output so far. Encourages new topics.

## Behavior
| Value | Effect |
|-------|--------|
| **0** | No penalty |
| **Positive (0.5–1.0)** | Encourages new topics and themes |
| **Negative** | Can keep model stuck on same topic |

## When to Use
- **Positive:** When you want more topic diversity, avoid staying too narrow
- **0:** Default, no change

## Takeaway
Presence penalty = "Encourage tokens that haven't appeared yet." Good for topic diversity. (Different from frequency: presence = "have you appeared?" vs frequency = "how often?")
