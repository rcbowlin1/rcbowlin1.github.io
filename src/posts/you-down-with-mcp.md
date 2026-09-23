---
title: "You down with MCP? Yeah, you know me!"
date: 2026-09-23
category: Thinking
track: Work
description: "What MCP is, why it quietly won, and the part that actually matters — the registry as a mechanism, and the open standard pulling us toward a consumer-agent world."
---

Quick catch-up for anyone who hasn't gone down this particular rabbit hole. (Already sold and just want to build one? I made a tiny MCP you can download — [grab it here](/work/build-your-own-mcp/).)

MCP — the Model Context Protocol — is an open standard Anthropic released in late 2024 to fix a boring, expensive problem: every AI-to-tool connection used to be a custom integration. N tools times M assistants equals a mess. MCP defines one universal interface — think HTTP for browsers, or the standard plug shape behind every wall — so any AI can talk to any tool without a bespoke connector.

Boring on purpose. And it won. Within a year, OpenAI, Google, Microsoft, and AWS had all adopted it, and Anthropic handed it to the Linux Foundation. A protocol your competitors adopt *and* you give away is the definition of a standard. So "will MCP win?" is settled. The interesting questions are downstream.

Here's the one I keep coming back to, and it isn't the protocol — it's the registry.

Once you have a standard interface, you get a catalog of tools that all speak it. And once you have a catalog, the way you work changes. I don't go hunting for the right script or API anymore. I go to the registry and describe the job — "here's what I'm trying to do" — and it hands me back a tool that does it. Finding capability went from a scavenger hunt to a lookup. Large companies are standing these registries up internally now, and learning to manage one well is quietly becoming a real skill.

Which is where an old Amazon line keeps rattling around my head: good intentions don't work; mechanisms do. "Everyone should use the right tools" is a good intention — and good intentions decay the second someone's in a hurry. A registry is a mechanism. It has an owner. It's inspectable. It routes you to the right thing instead of trusting you to remember it exists. That's the difference between *hoping* your org gets leverage from AI and *building the thing* that delivers it by default.

But — and this is the part the breathless takes skip — a mechanism is only as good as its governance. An ungoverned pile of MCP servers isn't leverage, it's a liability: over-broad tool permissions, prompt injection riding in through tool outputs, six half-maintained tools that do the same job, nobody sure which one is safe. "Manage them correctly" is carrying the whole promise. Get the governance right and you get the good version — ripple effects, where a well-built mechanism in one corner quietly upgrades how the whole org works. Get it wrong and you've just built a very efficient way to make a mess.

Now zoom out from the org to the consumer, because this is where it gets interesting.

Standardize how agents reach tools, and apps stop being screens *you* open and start being things an agent *operates* on your behalf.

Picture it: you're mid-game in your favorite chess app and a notification lands — your opponent just moved. You don't open anything. You just say, "Hey Siri, queen to h5 — checkmate," and it plays the move. Game won, from the lock screen, without ever opening the app. This is silly, but you get the idea — and I think it's the future, coming fast.

You can already see two philosophies competing. Apple's App Intents is the walled version — a proprietary framework that lets *Apple's* assistant act inside your app. MCP is the open version — any assistant, any vendor, no permission slip. And the tell is that even Apple, patron saint of the walled garden, adopted MCP in Xcode so outside agents like Claude could drive its tools directly. When interop actually matters, the open standard wins the seams between ecosystems.

That shift — from "my app has an assistant" to "any assistant can use my app" — is exactly what a lot of companies are now hiring forward-deployed AI PMs to navigate. Someone has to decide which capabilities you expose, to which agents, walled or open, and how you don't get owned in the process. It's the same mechanism as the internal registry, just pointed outward.

So — am I down with MCP? Yeah. Not because the protocol is exciting; it's deliberately not. I'm down with it because it's the boring plumbing that makes the interesting stuff possible: registries that turn intent into tools, mechanisms that beat good intentions, and a consumer world inching toward agents that just *do the thing*. The standard is settled. The craft — governing it, and deciding what to plug in — is where the next few years actually happen.
