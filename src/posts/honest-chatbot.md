---
title: "The chatbot I didn't build (and the dog I shipped instead)"
date: 2026-09-25
category: Building
track: Work
description: "This site is my sandbox for learning and deploying AI. Here's how a debate with my AI about a RAG tool turned into a curated FAQ helper — and why it's a golden retriever named Sam."
---

The whole point of this site is to be a sandbox — somewhere I actually learn and deploy AI instead of just reading about it. And the way I usually get there is by arguing with my AI. I float an idea, it pushes back, I push back, and somewhere in the back-and-forth the real design shakes out.

Here's a recent one.

I wanted an "ask about me" tool on the site — something a visitor could actually use to get a straight answer without digging through every page. The obvious build is a RAG system: point a model at everything I've written, let it retrieve the relevant bits, and have it answer in plain language. Genuinely cool, and exactly the kind of thing I want to be building.

Then the debate started poking holes, fast. One: I've written a handful of posts so far — there isn't much to retrieve yet, so a model would spend most of its time saying "I don't know." Two: a live model answering every passing visitor is real API spend, month after month, for something that today wouldn't have much to say. Paying to look thin isn't a great trade.

So we talked it through and landed somewhere I like a lot better for right now. Skip the live model. Write the answers myself — the questions people actually ask: what I do, what I've built, my take on agents, how to reach me — and let the tool match your question to the closest one and hand it over. Anything it doesn't have, it says so and points you to me. The whole thing runs in your browser. No server, no model, no bill. It does a few things well and is honest about the rest.

That's the same instinct I bring to real systems: use the simplest thing that solves the problem, and save the heavy, expensive version for when it's actually earned. Right now, it hasn't. When the site fills up and there's enough to retrieve, this little helper graduates into the real thing.

Which left me with a feature whose whole job is to sniff out the right answer from what's on hand. Say "retrieval" and "sniff out the answer" enough times and the mascot names itself. What retrieves better than a retriever? I happen to be partial to one in particular — a golden named Sam.

So that's who's waiting in the corner. Say hi. He knows what he knows, he'll admit what he doesn't, and one day he'll be a lot smarter. Good boy.
