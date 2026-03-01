# Build and Learn — Agentic AI

> A structured, project-driven path from LLM basics to production-grade agentic systems.
> Designed for experienced web developers who are new to AI/ML.

**Your starting point:** Comfortable with Python, REST APIs, databases, auth, async programming, deployment.
**Already completed:** First LLM API call (Gemini) — `llm-sandbox/01-first-api-call/`

**Time commitment:** ~10–14 hrs/week (1–2 hrs weekdays + 4–5 hrs weekends)

---

## Progress

- [x] Phase 1 — First API call (`llm-sandbox/01-first-api-call/`)
- [ ] Phase 1 — Multi-provider CLI tool
- [ ] Phase 1 — Prompt engineering workbench
- [ ] Phase 2 — Tool use & function calling
- [ ] Phase 2 — RAG assistant
- [ ] Phase 3 — Research agent (LangGraph)
- [ ] Phase 3 — Coding assistant with memory
- [ ] Phase 4 — Multi-agent dev team
- [ ] Phase 4 — Multi-agent support system
- [ ] Phase 5 — Production RAG platform
- [ ] Phase 5 — Deployable agent SaaS

---

## What Is Agentic AI?

Before diving in, understand the spectrum:

| Level | What It Is | Example |
|-------|-----------|---------|
| **Basic LLM** | Single prompt → single response | ChatGPT conversation |
| **LLM + Tools** | LLM decides to call functions/APIs | "What's the weather?" → calls weather API → responds |
| **Single Agent** | LLM with memory, planning, and tool access that pursues a goal across multiple steps | Research assistant that searches, reads, summarizes |
| **Multi-Agent** | Multiple specialized agents collaborating | PM agent delegates to coder agent and reviewer agent |

**Agentic AI** = LLMs that *act autonomously* — they plan, use tools, remember context, handle errors, and achieve goals over multiple steps rather than just responding to a single prompt.

### Key Concepts You'll Learn

- **Agents**: Autonomous LLM-powered entities that reason and act in loops
- **Tools/Function Calling**: External capabilities an agent can invoke (APIs, databases, code execution)
- **Memory**: Short-term (conversation context) and long-term (vector stores, persistent state)
- **Planning**: Task decomposition, chain-of-thought, ReAct (Reason + Act) patterns
- **Orchestration**: Controlling agent flow — sequential, parallel, hierarchical
- **RAG**: Retrieval-Augmented Generation — grounding LLM responses in your own data
- **Evaluation**: Measuring agent quality, reliability, and safety

---

## Phase 1: LLM Foundations + Prompt Engineering + API Mastery

**Duration:** 2–3 weeks | **Goal:** Become fluent in calling LLMs programmatically, understand tokenization, models, and write effective prompts.

### What to Learn

- How LLMs work at a high level (transformers, tokens, context windows, temperature, top-p)
- API patterns across providers: OpenAI, Anthropic (Claude), Google (Gemini)
- Prompt engineering: system prompts, few-shot learning, chain-of-thought, output formatting
- Structured output: getting JSON responses reliably
- Streaming responses
- Cost awareness: token counting, model selection tradeoffs (cost vs quality vs speed)

### Project 1.1 — Multi-Provider LLM CLI Tool

**Folder:** `llm-sandbox/02-llm-cli-tool/`  
**Goal:** Build a CLI tool that sends prompts to OpenAI, Anthropic, and Gemini, supporting streaming, conversation history, and structured JSON output.

**What you'll build:** CLI with `typer`, `--stream` flag, conversation history in JSON, `--json-schema` for structured output, provider comparison.

**Tech:** `openai`, `anthropic`, `google-genai`, `typer`, `rich`

### Project 1.2 — Prompt Engineering Workbench

**Folder:** `llm-sandbox/03-prompt-workbench/`  
**Goal:** Web UI to test and compare prompts across models side by side.

**What you'll build:** FastAPI backend, A/B prompt comparison UI, prompt templates with variables, token/latency/cost display, SQLite for history.

**Tech:** `fastapi`, `sqlite`, `jinja2` or React, provider SDKs

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Docs | Free |
| [OpenAI API Documentation](https://platform.openai.com/docs) | Docs | Free |
| [DeepLearning.AI — ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) | Course | Free |
| [Andrej Karpathy — "Intro to LLMs"](https://www.youtube.com/watch?v=zjkBMFhNj_g) | Video | Free |
| [Anthropic Claude API Docs](https://docs.anthropic.com/en/api/getting-started) | Docs | Free |
| [Google Gemini API Docs](https://ai.google.dev/docs) | Docs | Free |

### Common Mistakes

1. **Ignoring system prompts.** The system prompt is your most powerful lever — always use it.
2. **Not handling rate limits and errors.** Use retries with exponential backoff (`tenacity`).
3. **Overpaying for simple tasks.** Use cheaper models (GPT-4o-mini, Claude Haiku, Gemini Flash) for simple tasks.
4. **Prompt injection naivety.** Never trust user input directly in prompts.
5. **Ignoring token limits.** Always count tokens before sending.

---

## Phase 2: Tool Use, Function Calling, and RAG

**Duration:** 3–4 weeks | **Goal:** Make LLMs interact with the real world via tools and ground them with your own data using RAG.

### What to Learn

- Function calling / tool use (OpenAI, Claude, Gemini)
- The tool-use loop: LLM decides → execute → return → LLM continues
- RAG architecture: chunking → embedding → vector store → retrieval → generation
- Vector databases: ChromaDB, Pinecone, Weaviate, Qdrant
- Chunking strategies: fixed-size, recursive, semantic

### Project 2.1 — LLM-Powered Dev Toolkit with Tool Use

**Folder:** `llm-sandbox/04-dev-toolkit/`  
**Goal:** LLM assistant that can run shell commands, read/write files, search the web, and query a database.

**Tech:** `openai`, `anthropic`, `httpx`, `sqlite3`

### Project 2.2 — RAG-Powered Documentation Assistant

**Folder:** `llm-sandbox/05-rag-assistant/`  
**Goal:** Ingest docs, answer questions grounded in that content, with citations.

**Tech:** `chromadb`, `langchain`, `openai` or `anthropic`, `fastapi`

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling) | Docs | Free |
| [Anthropic Tool Use Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview) | Docs | Free |
| [DeepLearning.AI — Building Systems with the ChatGPT API](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/) | Course | Free |
| [ChromaDB Documentation](https://docs.trychroma.com/) | Docs | Free |
| [RAG paper](https://arxiv.org/abs/2005.11401) | Paper | Free |

### Common Mistakes

1. **Building RAG before understanding tool use.** Master tool use first.
2. **Bad chunking ruins retrieval.** Test multiple strategies.
3. **Not evaluating retrieval separately from generation.** Diagnose each.
4. **Embedding model mismatch.** Use the *same* model for indexing and querying.

---

## Phase 3: Single Agents with Memory and Planning

**Duration:** 3–4 weeks | **Goal:** Build autonomous agents that maintain state, reason about tasks, and execute multi-step plans.

### What to Learn

- Agent architectures: ReAct, Plan-and-Execute, Reflexion
- LangGraph (graph-based agent orchestration)
- Conversation memory: buffer, summary, vector-backed
- Planning patterns: task decomposition, self-reflection
- OpenAI Assistants API

### Project 3.1 — Research Agent with LangGraph

**Folder:** `llm-sandbox/06-research-agent/`  
**Goal:** Autonomous agent that searches the web, reads articles, takes notes, and produces a structured report.

**Tech:** `langgraph`, `langchain`, `tavily-python`, `beautifulsoup4`, `httpx`

### Project 3.2 — Personal Coding Assistant with Persistent Memory

**Folder:** `llm-sandbox/07-coding-assistant/`  
**Goal:** Assistant that remembers your codebase, preferences, and past conversations.

**Tech:** `openai` (Assistants API) or `anthropic`, `chromadb`, `sqlite3`, `tree-sitter`

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [LangGraph Documentation](https://langchain-ai.github.io/langgraph/) | Docs | Free |
| [DeepLearning.AI — AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) | Course | Free |
| [ReAct Paper](https://arxiv.org/abs/2210.03629) | Paper | Free |
| [Lilian Weng — "LLM Powered Autonomous Agents"](https://lilianweng.github.io/posts/2023-06-23-agent/) | Blog | Free |

### Common Mistakes

1. **Infinite loops.** Always set max iterations and cost limits.
2. **Giant context windows as "memory."** Use summarization + vector retrieval.
3. **Skipping error handling in tools.** Every tool needs graceful error messages.
4. **Ignoring cost.** Track token usage, cache when possible.

---

## Phase 4: Multi-Agent Systems and Orchestration

**Duration:** 3–4 weeks | **Goal:** Design systems where multiple specialized agents collaborate.

### What to Learn

- Multi-agent patterns: supervisor, hierarchical, peer-to-peer
- CrewAI, AutoGen / AG2
- Task delegation and handoff
- Human-in-the-loop patterns

### Project 4.1 — AI Software Team with CrewAI

**Folder:** `llm-sandbox/08-ai-dev-team/`  
**Goal:** PM, developer, reviewer, QA agents working together.

**Tech:** `crewai`, `langchain`, provider SDKs

### Project 4.2 — Multi-Agent Customer Support System

**Folder:** `llm-sandbox/09-support-system/`  
**Goal:** Router, FAQ, Technical, Escalation agents with shared state.

**Tech:** `langgraph`, `crewai` or `autogen`, `fastapi`, `chromadb`, `sqlite`

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [CrewAI Documentation](https://docs.crewai.com/) | Docs | Free |
| [AutoGen Documentation](https://microsoft.github.io/autogen/) | Docs | Free |
| [DeepLearning.AI — Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) | Course | Free |

### Common Mistakes

1. **Using multi-agent when a single agent suffices.** Use only when genuinely needed.
2. **Agents with overlapping responsibilities.** Each agent needs a clear, distinct role.
3. **Not testing agents in isolation first.** Get each working alone before combining.

---

## Phase 5: Production-Grade Agentic Applications

**Duration:** 3–4 weeks | **Goal:** Production-ready with observability, evaluation, safety, and deployment.

### What to Learn

- Observability: LangSmith, Langfuse
- Evaluation: custom evals, LLM-as-judge
- Guardrails, cost optimization, security
- Deployment: Docker, async task queues

### Project 5.1 — Production RAG Platform

**Folder:** `llm-sandbox/10-prod-rag-platform/`  
**Goal:** RAG assistant with tracing, evaluation, caching, CI/CD.

**Tech:** `fastapi`, `langfuse` or `langsmith`, `chromadb` or `qdrant`, `redis`, `docker`, `ragas`

### Project 5.2 — Deployable Multi-Agent SaaS App

**Folder:** `llm-sandbox/11-agent-saas/`  
**Goal:** Complete SaaS with auth, background jobs, WebSocket streaming, admin dashboard.

**Tech:** `fastapi`, `celery` or `arq`, `redis`, `postgresql`, `langgraph`, `langfuse`, `docker`

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [Langfuse Documentation](https://langfuse.com/docs) | Docs | Free |
| [RAGAS — RAG Evaluation](https://docs.ragas.io/) | Docs | Free |
| [Hamel Husain — "Your AI Product Needs Evals"](https://hamel.dev/blog/posts/evals/) | Blog | Free |
| [MCP Specification](https://modelcontextprotocol.io/) | Docs | Free |

### Common Mistakes

1. **No evaluation before deployment.** Build automated evals in CI.
2. **No observability.** Add tracing from day one.
3. **Synchronous agent execution.** Use background jobs + WebSocket streaming.
4. **Skipping guardrails.** Add input/output validation.

---

## Timeline Summary

| Phase | Focus | Duration | Cumulative |
|-------|-------|----------|------------|
| **Phase 1** | LLM APIs + Prompt Engineering | 2–3 weeks | 2–3 weeks |
| **Phase 2** | Tool Use + RAG | 3–4 weeks | 5–7 weeks |
| **Phase 3** | Single Agents + Memory | 3–4 weeks | 8–11 weeks |
| **Phase 4** | Multi-Agent Systems | 3–4 weeks | 11–15 weeks |
| **Phase 5** | Production + Deployment | 3–4 weeks | 14–19 weeks |

**Total: ~4–5 months** at 10–14 hrs/week.

---

## Project Directory Structure

```
build-and-learn/
├── llm-sandbox/
│   ├── 01-first-api-call/          ✅ Done
│   ├── 02-llm-cli-tool/           Phase 1
│   ├── 03-prompt-workbench/       Phase 1
│   ├── 04-dev-toolkit/            Phase 2
│   ├── 05-rag-assistant/          Phase 2
│   ├── 06-research-agent/         Phase 3
│   ├── 07-coding-assistant/       Phase 3
│   ├── 08-ai-dev-team/            Phase 4
│   ├── 09-support-system/         Phase 4
│   ├── 10-prod-rag-platform/      Phase 5
│   └── 11-agent-saas/             Phase 5
├── resources/
│   └── python/
│       └── ai-agents.pdf
└── README.md
```

---

## Framework Decision Guide

| Need | Use | Why |
|------|-----|-----|
| Quick single agent with tools | Raw API (OpenAI/Claude SDK) | Minimal abstraction |
| Complex agent with branching logic | **LangGraph** | Graph-based state machine |
| Role-based multi-agent team | **CrewAI** | Easy role/goal setup |
| Multi-agent conversations | **AutoGen / AG2** | Agent-to-agent dialogue |
| Managed agent with file handling | **OpenAI Assistants API** | Built-in threads, files |
| Document processing + RAG | **LangChain** | Loaders, splitters, retrievers |
| Production observability | **Langfuse** or **LangSmith** | Tracing, evaluation |

**Recommendation:** Raw API first (Phase 1–2) → LangGraph (Phase 3) → CrewAI (Phase 4) → Production tools (Phase 5).

---

## Recommended Channels & Blogs

| Channel/Blog | Why |
|-------------|-----|
| [AI Jason](https://www.youtube.com/@AIJasonZ) | Practical agent tutorials |
| [James Briggs](https://www.youtube.com/@jamesbriggs) | LangChain, RAG, vector DB |
| [Lilian Weng's Blog](https://lilianweng.github.io/) | Technical deep dives |
| [Simon Willison's Blog](https://simonwillison.net/) | LLM security, prompt engineering |
| [Hamel Husain's Blog](https://hamel.dev/) | Evals, AI engineering |
| [LangChain Blog](https://blog.langchain.dev/) | Framework updates |

---

## Key Papers

| Paper | Phase |
|-------|-------|
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | 1 |
| [RAG](https://arxiv.org/abs/2005.11401) | 2 |
| [ReAct](https://arxiv.org/abs/2210.03629) | 3 |
| [Toolformer](https://arxiv.org/abs/2302.04761) | 2 |
| [Generative Agents](https://arxiv.org/abs/2304.03442) | 4 |

---

## Tips for Success

1. **Build first, optimize later.** Get something working, then improve it.
2. **Read the raw API docs before using frameworks.** Understand function calling at the API level.
3. **Track your costs.** Set up billing alerts.
4. **Version your prompts.** Store them in files, treat changes like code.
5. **Join communities.** LangChain Discord, r/LocalLLaMA — the field moves fast.
6. **Don't chase every new framework.** Focus on fundamentals (tool use, memory, planning).
7. **Use Git religiously.** Every project, every experiment.
