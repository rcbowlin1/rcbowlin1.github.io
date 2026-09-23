---
title: "Agent vs. Code… who ya gonna call?"
date: 2026-09-22
category: Thinking
track: Work
description: "When to reach for an AI agent and when to just write the code — and why the deciding factor isn't the one everyone argues about."
---

I'm not sold that an agent is the end-all, be-all.

In a world where the headlines are about companies blowing through their AI budgets, I keep coming back to the trade-off between the two: when is an agent actually worth it, and when should I just write the code?

I wanted a real answer to that. And it dawned on me that I've got the world's knowledge sitting at my fingertips — so I asked the question. Here's the gist of what came back:

---

**Start with one question: can you write down the steps in advance?**

If yes, write the code. Deterministic code is cheaper, it's auditable, it runs the same way every time, and when it breaks you can see exactly where. An agent doing that same job is slower, pricier, and non-deterministic — you're paying a premium to make a solved problem *less* reliable. A lot of "agentic workflow" excitement is really just that: paying by the token to reinvent a function call.

If *no* — if the inputs are genuinely open-ended and you can't map the branches ahead of time — then an agent earns its place. Its figure-it-out-at-runtime behavior is the actual value. The non-determinism isn't the benefit; it's the price you pay to handle inputs you couldn't anticipate.

So the real job of an agent isn't automating repeatable work — code wins there on every axis. **It's turning not-yet-repeatable work into repeatable work.** Two ways that shows up:

1. **Agent as path-finder.** Let it explore and find the path once, then harden that path into plain code. The finished system contains zero agent — it did its job by working itself out of one.
2. **Agent as translator.** Keep it at the messy edge, normalizing unpredictable input into the clean structure your pipeline expects, and let deterministic code own everything downstream. One rule: the agent can shape the *form* of the data, never the *substance*. Validation stays deterministic — an agent that decides substance can invent something plausible and wrong, and no downstream check will catch it.

---

That tracked with what I'd already learned the hard way, automating a big chunk of my own job. The agent found the path. Then I mostly deleted it.

So here's my rule of thumb: default to code, and make an agent prove the input space is too wild to enumerate. Novelty isn't proof. I'm still figuring out exactly where the line sits — but starting from "what can I just write down?" hasn't steered me wrong yet.
