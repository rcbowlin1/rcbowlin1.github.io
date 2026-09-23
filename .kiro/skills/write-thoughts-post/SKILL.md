---
name: write-thoughts-post
description: >-
  Write and publish a post in the "Thoughts" section of rcbowlin1.github.io
  (Ryan Bowlin's personal site). Use when Ryan wants to draft, shape, or ship a
  new Thoughts entry. Covers the front-matter schema (title, date, category,
  track, description), the house voice and structure, the confidentiality
  guardrails, and the exact Eleventy publish mechanics. The worked example is
  src/posts/agent-vs-code.md.
---

# Write a Thoughts post

Ryan's Thoughts section is framed as **"a collection of thoughts and debates
between me and AI."** Posts are short, first-person, and honest. Each one is an
instance of this repeatable process — the skill is the SOP, the post is the run.

## 1. Front-matter schema (every post carries all five)

```yaml
---
title: "The post title"          # punchy; a song/movie riff is on-brand
date: 2026-09-22                  # publish date, YYYY-MM-DD (see the date rule)
category: Thinking                # one of exactly three — see below
track: Work                       # Work | Play  (the binary filter)
description: "One sentence."      # ALSO powers the link-preview (OG) card — never skip it
---
```

- **category** — exactly three, and they describe *what kind of post it is*, not the subject:
  - **Building** — making something (a tool, a pipeline, a project)
  - **Thinking** — a POV or framework (strategy, how you reason)
  - **Learning** — exploring something new
- **track** — `Work` or `Play`. This is the only thing the Thoughts filter keys on, so it must be exactly one of those two strings (capitalized).
- **description** — one plain sentence. It's the meta description AND the OG/Twitter card text when the post URL is shared. A missing/empty description means a blank preview, so it is required, not optional.

## 2. Voice (non-negotiable — this is what makes it read like Ryan, not an AI)

- First person, conversational, direct. Plain language. Show, don't tell.
- **Calibrated confidence, not hedging.** State what you've actually done as fact; save "still figuring out" for the close. Never open with a hedge. (This is the same call we made on the site headline — don't undersell earned claims, don't overclaim either.)
- No listicle padding, no buzzword hype ("revolutionary," "game-changing," "unlock"). If a sentence could open a LinkedIn thought-leader post, cut it.
- A little wry is good. Titles riff on songs/movies — e.g. *"Agent vs. Code… who ya gonna call?"* (Ghostbusters), *"You down with MCP? Yeah, you know me!"* (Naughty by Nature). The title does the winking; keep the body clean rather than forcing the pun.
- **Short and sweet.** Target ~350–500 words. If it's running long, the thesis probably isn't sharp yet.

## 3. Structure (a flexible skeleton, not a template to fill blindly)

1. **Hook** — a claim or a tension, in 1–2 sentences. No throat-clearing.
2. **The stakes** — why it matters / what people get wrong.
3. **The argument** — the core idea. The meat.
4. **A grounding example** — one concrete instance (genericized — see guardrails).
5. **The reframe** — the sharper way to see it; the takeaway.
6. *(optional)* **What I'm still figuring out** — an honest close. On-brand, not obligatory.

**The "conversation with AI" device works well and fits the section framing:** pose the question in Ryan's voice, then "I've got the world's knowledge at my fingertips — so I asked. Here's the gist of what came back:", present the framework (bracket it with `---` horizontal rules), then return to Ryan's voice to validate/extend it with lived experience. When you use this device, the **close must stake Ryan's own claim** so the post still shows his judgment, not just the model's answer.

## 4. Guardrails (hard rules)

- **Confidentiality.** Never expose confidential Amazon / program specifics (codenames, unreleased products, internal metrics, org detail). Genericize: "a big chunk of my own job," "an internal reporting workflow." When in doubt, abstract it or ask Ryan for the exact line.
- **Trace claims to source; never invent.** Facts, numbers, and quotes must be real. If something can't be substantiated, cut it or mark it as opinion.
- **Don't merge the two axes.** A post's `category` (kind) and `track` (Work/Play) are independent; don't collapse them.

## 5. Publish mechanics (Eleventy — this exact site)

The plumbing is already built. Publishing a post is: **write the file → preview → commit → push → verify.**

1. **Create** `src/posts/<slug>.md` with the front matter above. `src/posts/posts.json` auto-applies `layout: post.njk` and `tags: posts`, so the post is automatically added to `collections.posts`.
2. **It auto-appears** on `/thoughts/` (newest-first, with the Work/Play filter and date-sort toggle) and renders at `/posts/<slug>/`. The post page shows `date · category · track`. No manual list editing.
3. **Date rule (avoid the off-by-one).** Front-matter `date: YYYY-MM-DD` is parsed as UTC midnight. Both display (`readableDate`) and the sort key (`isoDate`) are pinned to `timeZone: "UTC"` in `eleventy.config.js`, so the site shows the exact calendar date you typed. Don't "fix" a date by shifting it a day — keep the filters UTC.
4. **Preview locally.** Dev server: `npm run serve` → http://localhost:8080/posts/<slug>/ and /thoughts/. (Editing `eleventy.config.js` restarts the server; a plain post edit hot-reloads.)
5. **Verify before claiming done** (can't see the rendered page, so check with curl):
   ```bash
   curl -s http://localhost:8080/posts/<slug>/ | grep -Eo '<title>[^<]*</title>|<meta name="description"[^>]*>|post-meta">[^<]*'
   curl -s http://localhost:8080/thoughts/ | grep -Eo 'href="/posts/[^"]*"|post-meta">[^<]*'
   ```
   Confirm the title, the description (feeds the preview card), and that the date reads correctly.
6. **Ship.** `git add -A && git commit -q -m "Add Thoughts post: <title>" && git push`. GitHub Actions builds in ~1 min. Optionally confirm live: `curl -s https://rcbowlin1.github.io/posts/<slug>/ | grep -Eo '<title>[^<]*</title>'`.

## 6. Worked example

`src/posts/agent-vs-code.md` — *"Agent vs. Code… who ya gonna call?"* (Thinking · Work). Uses the ask-the-AI device, brackets the framework with `---` rules, closes in Ryan's voice with a genericized ("automating a big chunk of my own job") lived example. Read it before drafting a new one.
