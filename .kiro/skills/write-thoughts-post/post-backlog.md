# Thoughts — post backlog

Living queue of post ideas for the Thoughts section. Pair with `SKILL.md`
(the how-to). Move an item to **Shipped** once it's pushed. Keep titles playful;
keep theses sharp (one line each).

Overlap between the agent-themed posts is fine and intentional — the whole field
is "agents this, agents that," so multiple angles on the same beast is the point.
We'll add a short framing note about the series when there are enough of them.

---

## Shipped
- **Agent vs. Code… who ya gonna call?** — `Thinking · Work` — `agent-vs-code.md`
  Thesis: default to code; an agent only earns its place when the input space
  can't be enumerated in advance. The agent's real job is turning
  not-yet-repeatable work into repeatable work.

## Queued (the agent series)
- **Art Vandelay, (Agent) Architect** — `Thinking · Work`
  Thesis: *"You don't build an agent; you build the box it's allowed to move in."*
  Good agent architecture is mostly constraint, not intelligence — tool design,
  decomposition into focused sub-agents, memory/context boundaries, guardrails
  (agent shapes the *form*, deterministic checks own the *substance*).
  Answers: you've decided you need an agent — now how do you build it well?

- **Graph Engineering for Workflows (is it the future… for now?)** — `Thinking · Work`
  Thesis: *"An agent is just a graph you refused to draw."* Explicit workflow
  graphs (LangGraph / Step Functions / Temporal-style) are today's best practice
  for the deterministic-core / adaptive-edge system — the graph *is* the
  enumeration. "The future, for now": a pragmatic bridge, not the destination.

- **You down with MCP? Yeah, you know me!** — `Learning · Work`  *(highest leverage — Anthropic-native)*
  Thesis: MCP is the boring plumbing that makes agents useful — a standardized,
  typed contract at the messy boundary (the "USB-C for AI tools"). The value is
  standardization, not intelligence; it's the clean interface layer the
  form-not-substance rule lives on. Measured take, not cheerleading: name the
  open questions (adoption/network effects, tool security & prompt injection).
  Write from real use — I've wired up a bunch of MCP servers.

## Queued (Play)
- **Hot Springs, Arkansas: mobsters, bathhouses & a lot of lake** — `Learning · Play`
  The unlikely mix — historic mob history, spring-training baseball, wellness/bathhouse
  culture, and the surrounding lakes. A "you'd never guess this town" piece.
- **Why is Scottsdale so known for golf?** — `Learning · Play`
  The curiosity explainer: climate, land, the desert-course boom, the economics of a golf town.
- **Fun things to do in the Bay Area** — `Learning · Play`
  A transplant's running list — off the clock, opinionated, low-tourist.
- **The bond market… who cares? (who's asking?)** — `Thinking · Play`
  Plain-English take on why the bond market quietly runs everything and who's actually watching it.

## Queued (Work — energy / domain)
- **Power Purchase Agreements… where'd they go?** — `Thinking · Work`
  Draws on the decarbonization/renewables background: what PPAs are, why they boomed,
  and where the market/attention actually went. Genericize any confidential specifics.

## Queued (Work — AI, novel angles)
- **You have a non-determinism budget** — `Building · Work`
  Thesis: non-determinism (and token spend) is a resource you *allocate*, like latency or
  memory — not a free good. Where to spend it, where to refuse. Extends Agent vs. Code.
- **Human-in-the-loop is a design smell** — `Thinking · Work`
  Contrarian: HITL is often a band-aid for a system you didn't bound. Put the human on the
  *edge* (structure/approve), not in the critical path. Ties to "push ambiguity to the edge."
- **The deletion metric** — `Building · Work`
  Thesis: measure an AI project by how much of it you got to *delete* afterward. The agent
  that works itself out of a job. Direct sequel to the close of Agent vs. Code.
- **Can agents run an entire small business? News at 6.** — `Thinking · Work`
  The honest stress-test of the "agents do everything" hype: which parts of running a real
  small business could an agent actually own end-to-end, and where a human or a deterministic
  system is still load-bearing. (Can lean on real SMB analysis — genericize any specifics.)

## Queued (Work — Product management)
- **The doc is the thinking, not the memo** — `Thinking · Work`
  Amazon narrative/6-pager culture: writing isn't how you communicate the decision, it's how
  you *find the flaw* in it. From lived experience writing 6-pagers and PR/FAQs.
- **Feasibility is a PM skill, not an engineering handoff** — `Thinking · Work`
  A PM who can assess technical feasibility changes the conversation — when to probe vs. trust
  engineering. (Doubles as evidence for the PMT tech bar.)
- **Prioritization is subtraction** — `Thinking · Work`
  The hard part of a roadmap isn't picking what to build; it's defending what you won't —
  operational excellence and the discipline of "no."
- **PM + AI: the fundamentals still win** — `Thinking · Work`
  Thesis: PMing AI is more than "you're an expert in [field], build me [product]." Working
  backwards from the customer and defining + ruthlessly prioritizing requirements *before* you
  prompt is still P0. The model lowers the cost of building, not the cost of knowing what to build.

---

## Cadence
One post per session: I draft from the thesis, you react, we ship. Reorder freely;
MCP can jump the line since it's the strongest Anthropic signal.

**This week — ~10 min/day**
- **Tue 9/22** — ✅ Agent vs. Code (shipped)
- **Wed 9/23** — Art Vandelay, Agent Architect
- **Thu 9/24** — Graph Engineering for Workflows
- **Fri 9/25** — You down with MCP?
- **Next up** — a Play post (Hot Springs or Scottsdale reads easiest first)

**Scaling rule:** once ~50 posts are published, drop to every-other-day (or a
lighter weekly cadence) — the point by then is quality and range, not volume.
