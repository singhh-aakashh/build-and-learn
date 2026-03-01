# Top-P / Nucleus Sampling (LLM Parameter)

## What It Does
Keeps tokens until cumulative probability reaches P, then samples only from that set. Dynamic cutoff.

## Behavior
| Value | Effect |
|-------|--------|
| **Low (0.3–0.5)** | Fewer tokens considered, more focused |
| **High (0.9–1.0)** | More tokens considered, more diverse |

## When to Use
- **Low:** Deterministic, focused outputs
- **High:** Creative, varied outputs

## Takeaway
Top-P = "Use tokens until we've covered P% of probability mass." Often use temperature *or* top_p, not both.
