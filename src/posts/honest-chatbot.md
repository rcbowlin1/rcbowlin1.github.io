---
title: "The chatbot I didn't build (and the dog I shipped instead)"
date: 2026-09-25
category: Building
track: Work
description: "Why I shipped a small, honest, curated assistant instead of a RAG chatbot over a thin corpus — data-readiness as a gate, graceful degradation, and knowing when not to build the fancy version."
---

There's a golden retriever in the corner of this site now. His name is Biscuit, and if you ask him about me he'll answer a handful of questions pretty well. He'll also, on purpose, admit when he doesn't know something.

That second part is the whole point.

The obvious move for someone who builds AI is to put an "ask my work" bot on the site — point a model at everything I've written, wire up retrieval, let people ask anything. It's a good demo. I wanted it.

Here's why I didn't build it: I've written a handful of posts. A retrieval bot over a thin corpus spends most of its time saying "I don't have information on that." And a chatbot that can't answer, sitting on the site of someone whose pitch is *AI judgment*, isn't a neutral miss. It becomes the counter-argument. The demo undercuts the thing it's supposed to prove.

So I shipped the honest version instead. Biscuit is a curated set of answers to the questions people actually ask — what I do, what I've shipped, my take on agents, how to reach me — and a graceful "I'm still learning that one" for everything else. No model, no backend, no API key to run up a bill. It does a few things well and tells you plainly where it stops.

This is the same call I make in real systems, just smaller. Use the simplest thing that solves the problem. Add the complicated, autonomous version only when it earns its keep — and "it would be a cool demo" isn't it earning its keep. Data-readiness is a gate you're allowed to fail. Right now the corpus isn't deep enough to ground a good retrieval bot, so building one would mean shipping something that bluffs. I'd rather ship something that's honest about its edges.

The other half of the point is graceful degradation. The failure mode of a confident bot is that it makes something up. The failure mode of Biscuit is that he says "ask Ryan." One of those costs me credibility; the other doesn't. When you can't guarantee the fancy version won't embarrass you, the boring version that fails safe is the better product.

None of this is permanent. Biscuit is the version that's right for the amount I've written *today*. As the site fills up, he graduates — same corner, same dog, a real retrieval model underneath, and hopefully fewer "ask Ryan"s. I'm building toward it. I'm just not pretending I'm already there.

Honesty turned out to be the feature. A dog that knows its limits beats a bot that fakes it — and if you're going to be limited, you might as well be a golden retriever about it.

Go poke him, bottom right. He'll tell you what he knows.
