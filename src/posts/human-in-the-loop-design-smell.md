---
title: "Get the human out of the loop (my AI came up with this one…)"
date: 2026-11-10
category: Thinking
track: Work
description: "An AI automation project at work kept raising the same question at every handoff, and it changed how I think about where a human actually belongs."
---

I'm working on an AI automation project at work right now. The process behind it is a slog: teams coordinating with suppliers around the world to gather and validate data, then feeding it through models to produce an output that gets sent to third-party verifiers for certification. A lot of steps, a lot of hands, a lot of waiting on someone else's time zone.

As we design the agent flow and the tooling around it, the same question surfaces at every handoff. Does a human need to be in the loop here, or not? We care about getting the validation metrics right, that part isn't optional. But we also didn't want a person to become the bottleneck at the next step. Nobody should have to click "Approve" on an email that lands at 1am Pacific because it's 5pm in China. That question sent me back to an article I'd read on how to think about humans in the loop versus on it.

It's worth being precise about the two. A human in the loop approves each outcome before the work moves on, sitting inside the execution path. A human on the loop lets the system run inside set limits and watches it, handling the exceptions and keeping a hand on the switch. Elementum has [a clear writeup](https://www.elementum.ai/blog/human-in-the-loop-vs-human-on-the-loop) of the difference, and the test they land on is reversibility: can this decision be undone. Irreversible, expensive calls want a human in the path. Cheap, high-volume ones don't.

Here's what I keep coming back to as more of the work moves to agents. If a person has to sign off on every step, the person is the bottleneck. You've built something that can run around the clock and then capped it at the speed of one tired human clicking approve between meetings. That isn't oversight, it's a traffic jam with good intentions, and it's the quiet way an automation project fails to deliver what it promised.

So we've started treating "human in the loop" as something to design down, not a box to check for comfort. Where the flow routes a case to a person, that isn't the finished design, it's a measurement of where the system is still weak. Each of those cases is one to study, turn into a validation check or a rule, and then stop routing. The set that needs a human should shrink with every pass. The calls that can't be undone, a bad number sent on to a verifier, we keep a person on. The rest, we design them out of.

That's the shift I think the next few years ask for. Not more humans in more loops to feel safe, and not fewer because we got careless, but humans placed deliberately in the few loops that genuinely need them, watching the many that don't. When you design an AI workflow, the rule I'd start with is simple: don't make the human the bottleneck. Keep them where a wrong answer is expensive and hard to undo, and get them out of the way everywhere else. The point was never to get a human to stop checking. It was to make the list of things they have to check shorter every time, so the one that lands at 1am can wait until morning without holding up the world.
