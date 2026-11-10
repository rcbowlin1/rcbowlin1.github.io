---
title: "Loop Engineering: Loops on Loops"
date: 2026-11-10
category: Thinking
track: Work
featured: true
description: "Loop engineering is a growing idea in AI, and it comes down to building the feedback that lets a system improve itself so people can step back."
---

Loop engineering is showing up more and more in AI, and under the jargon it's the oldest trick in engineering: test, learn, refine. What's new is you can build that cycle into the software, so it improves without a person turning every crank.

Build the feedback in well and the team's job shifts, from checking every output to validating a sample and writing the rule that closes the gap. Fewer errors, faster, and no human stuck in the middle (more on that in [Get the human out of the loop](/posts/human-in-the-loop-design-smell/)). These loops already have names. Here are the four that stand out to me.

**The evaluation loop.** Run against known answers, measure what's wrong, turn each miss into a check, run again. It's what an eval is, and it's the loop that improves all the others. I built one in [AI Evals](/posts/ai-evals/).

<figure class="diagram"><img src="/img/loop-evaluation.svg" alt="The evaluation loop: run the system, find what's wrong, write a new check, then run again, with every pass getting a little better." /></figure>

**Routing.** Read the input first, then send it to whatever handles it best: retrieval for a look-up, code for a count. One approach rarely does everything well. See [Where RAG stops and Code starts](/work/where-rag-stops/).

<figure class="diagram"><img src="/img/loop-routing.svg" alt="Routing: a question goes to a router that classifies it, sending look-ups to retrieval and counts and totals to code." /></figure>

**Reflection.** The system checks its own output, retries on a failure, and escalates after a few tries instead of shipping something broken. Speed without recklessness.

<figure class="diagram"><img src="/img/loop-reflection.svg" alt="Reflection: produce a draft, check whether it passes, ship it on a pass, retry on a fail, and escalate to a human after a few tries." /></figure>

**Human-in-the-loop.** A person validates results and writes the rules that teach the system. The better the other loops get, the less they have to see.

<figure class="diagram"><img src="/img/loop-human.svg" alt="Human in the loop: the system surfaces exceptions to a person, who writes new rules that feed back in, and who sees fewer exceptions every pass." /></figure>

**Loops on loops.** Routing and reflection run on every task. The evaluation loop runs around them, slowly making each pass better. The human sits on the edge with less to do each cycle.

<figure class="diagram"><img src="/img/loop-nested.svg" alt="Loops on loops: each task is routed and reflected on in the moment, inside an evaluation loop that improves the system over time, with a human on the outer edge validating and writing rules." /></figure>

No single loop is right for every job. High-stakes and low-volume keeps the human close. High-volume and low-risk leans on routing and reflection. Which loops you build, and where the human sits, are design calls, and they are some of the most important early conversations between a PM and engineering. The loops are the product.
