---
title: "Red pill or blue pill… or green or yellow?"
date: 2026-09-23
category: Thinking
track: Work
description: "AI persona agents can now simulate millions of customers to test a product before you build it. What that unlocks for startups — and the catch."
---

You know the scene: one pill wakes you up, the other sends you back to sleep. Red or blue, pick one.

The more useful question for anyone building a product isn't which pill *you'd* take — it's which one your *customers* would. And a new paper out of a Harvard/MIT-led team (with a sprawling author list) makes a real run at letting you ask a few million of them before you've built anything.

It's called MatrAIx, and the pitch is simple: human testing is slow, expensive, and hard to scale, so simulate it. They built ~8.3 billion "persona" records across 1,290 attributes, released a filtered set of about a million (roughly 600k grounded in real human profiles, 400k synthetic), and dropped them into four environments — a survey, a chatbot, a website, and an app — where these simulated people actually use your product and react. The feedback isn't a thumbs-up; it's texture: someone hesitating after a price hike, deciding whether to stick with an AI assistant after it flubs a task, running out of patience when things lag.

Here's why I can't stop thinking about it — specifically for small, scrappy teams.

If you're a startup, the hardest, most expensive part of the early game is finding out you built the wrong thing. This is a way to run the beta *before* the build — to pressure-test a flow, a price, an onboarding, a message against thousands of varied "customers" and watch where they bail. That's the loop that gets you from 0 to your first 100 real users without torching your runway guessing. Run it well and it's part of what carries you to 10,000 and beyond.

The red-pill / blue-pill bit is the joke. The real move is testing the *green* pill and the *yellow* one too — which framing, which price, which color, tested across a simulated crowd before a single real person sees it. A/B/n testing where the "n" is your imagination and the cost is API tokens, not months.

Where I think this actually goes: the released personas are a *generic* population. The version that matters is the one a company trains on its **own** data — its real customers, its real behavior, not a stand-in. A simulated customer base that mirrors *your* actual one. That's the piece I think takes a company from 10k users to a million, because you're no longer testing against humanity in the abstract — you're testing against *your* market.

If you want to poke at it, the on-ramp is short but not free:

- **Get an API key from a frontier model provider** — the paper ran its agents on Claude and GPT. The personas are live model calls, so you're billed per token; budget it like compute, not a free survey tool.
- **Define who you're simulating and what you're testing** — a segment, a flow, a price change — and what "good" looks like *before* you run it.
- **Run it, read the signal, iterate** — then validate the winner against real humans before you bet anything real on it.

That last step is the whole ballgame, and it's where I'll be the wet blanket. Simulated customers are a fast signal, not the truth. The paper's own validation had personas behaving as declared about 91.5% of the time — genuinely impressive, and also *not* a green light to ship on vibes. Moving fast on a wrong signal is still just efficient waste. So use this to kill bad ideas cheaply and sharpen good ones — then go find out what actual people do.

Still. Being able to ask a million customers what they think before you've written a line of code? That's a wild place to be building from.
