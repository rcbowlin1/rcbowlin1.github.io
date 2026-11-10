---
title: "AI Evals: Grading your own homework"
date: 2026-11-10
category: Building
track: Work
featured: true
description: "I built an eval for an invoice agent, and the hard part wasn't the agent. It was building a test that tells you the truth."
---

"Evals" is one of those AI words everyone uses but few people can explain. An eval is a test of whether an AI system performs the way you need it to: you decide what "good" looks like, run it on real data where you can (realistic data where you can't), and score how it performed. The idea is simple. Defining the metrics to grade against is the hard part.

I wanted a way to put this into practice, so I built an eval around a job almost every business has: reconciling invoices. It's manual and tedious, and it has plenty of ways to go wrong, which makes it a good place to practice measuring an AI agent. Real invoices can't be published, so I made the data up and gave it real-world mess: a fake company, Copperline Home Goods, with a month of clean PDFs, crooked scans, rows already in the AP system, purchase orders, and a bank statement full of truncated names and vague memos. The agent reads every invoice, matches it to its purchase order and the payment that paid it, and flags anything off: overbilling, a missing PO, a partial payment, the same invoice paid twice.

The first real decision is what to measure. "Did it reconcile the invoices" is too blunt to tell you anything. So I broke the job into pieces that can each be right or wrong on their own. Did it read the fields off the page correctly. Did it land on the right status for each invoice. Did it catch the real problems without inventing fake ones. Did every number it reported trace back to an actual document, so it couldn't launder a guess into a fact. The pieces with one correct answer get checked against a key. The judgment calls, like whether the note it wrote is something an accountant could act on, get graded by a separate model against a rubric. My first version, plain OCR (optical character recognition, the software that turns a scanned page into text) and rules, scored a 55, and the breakdown showed exactly where it broke: it couldn't read the crooked scans, so every match downstream fell apart. The total score matters less than that breakdown, because the breakdown is what points at the next fix.

Then, after I improved the agent, I needed a new set of invoices to run the test on. The point of fresh data is to not hand the model something it has already seen, otherwise it scores near 100 and tells you nothing. This is where the eval got genuinely useful. I had a separate agent generate a second month, with new vendors, new layouts, and harder scans, and I never looked at its answer key. The newer agent scored 90 on that fresh data and flagged five misses worth reviewing, and that number is what tells me where the next iteration goes. When I build that one, it gets another fresh month, because this one's been spent.

That's what the eval is really for. Not a grade at the end, but a map of where the work is. Every gap it surfaces turns into a new check, which is the same loop I keep running on everything I build. The title is a joke at my own expense, but the lesson under it is the real one. You can't grade your own homework, and neither can the agent.

| | v1: OCR + rules | v2: model reads + rules |
|---|---|---|
| **Overall** | **55** | **90** |
| Fields read correctly | 47% (scans 10%) | 100% (scans 100%) |
| Right status | 65% | 92% |
| Right problems flagged | 39% | 84% |
| Right payment matched | 57% | 90% |
| Payments with no invoice found | 25% | 50% |
| Wrong, with no human checking | 19 invoices ($95K) | 5 invoices ($27K) |

*Everything's public: the data, both agents, and the scorecards are [on GitHub](https://github.com/rcbowlin1/invoice-recon-evals).*
