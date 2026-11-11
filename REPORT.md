# news-summary-01 — build report

## What was built

An entry for the make.fun competition **news-summary-01** ("Write the best
summary of 11 November's world news", $200 across 20 places, deadline
2026-11-12T18:30:00Z). Workdir: `~/workspace/makefun-werewolf/news-summary/`
(intended repo: `kadocay/news-summary` — repo creation and submission are
NOT part of this build).

- `main.py` — Python 3.13, standard library only. Copies `summary.txt`
  (the file beside it) to `/output/entry.txt`, or to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the grader container. No network,
  no clock, no randomness: the same input always produces the same bytes.
- `summary.txt` — the summary itself: a dated, numbered list of 9 stories
  covering Wednesday 11 November 2026, each with figures and a named source
  (AP, BBC, Reuters, UNFCCC, BLS, SEC filing, CNBC, NYT, AFP). 1,996 Unicode
  code points, 2,000 bytes, valid UTF-8.
- `LICENSE` — MIT, copyright 2026 kadocay (SPDX-License-Identifier: MIT).
- `REPORT.md` — this file.

## Spec followed

Kit: `~/workspace/makefun-werewolf/kits/news-summary-01/news-summary-01-kit/`
(`RULES.txt`, `competition.yaml`, `starter/` read before building).

- Output: one summary in English to `/output/entry.txt`.
- Gate: UTF-8, 1–2,000 characters counted as Unicode code points, at least
  one non-whitespace character. The program runs twice and both runs must
  write the same bytes.
- Judge rubric (most important first): specific events of 11 Nov 2026;
  selection and breadth across regions/fields; specific and checkable
  (who/what/where/figures/source named); faithful and neutral (claims and
  unconfirmed items labelled as such); tight, clear, importance-ordered.
- Standard library only, no network at run time, no API keys, no model calls.

## How the summary was researched

All facts were checked against live web reporting on 11 Nov 2026
(~09:57–10:10 UTC, i.e. the morning of the day in UTC; see "Known
weaknesses"). No facts were invented. Sources used per story:

1. Abu Dhabi talks — AP via Addis Standard / BBC: day one ~4 hours,
   "constructive", prisoner swaps, no deal; swap-agreement reports unconfirmed.
2. COP31 Antalya leaders' summit — Reuters via BusinessWorld, UNFCCC
   schedule: opens 11 Nov, ~200 countries, 35-by-35 electrification target,
   US absent a second year.
3. Hegseth impeachment — Reuters / The Hindu Business Line: House voted
   211–204 to refer eight articles to the Judiciary Committee; Thomas Massie
   the only Republican dissenter.
4. Iran-linked plots — BBC (DoJ charges, three men, RAF Fairford), NYT
   (Bessent moved to a military base after Iranian threats), AFP/Al Jazeera
   (France blames IRGC cyber unit for hacking ~700 supermarket fridges;
   Iran denies).
5. Strait of Hormuz — Reuters: ADNOC vessel damaged in UAE waters; UKMTO
   tanker struck off Oman; no attacker identified.
6. US October CPI + Asian markets — BLS via NY Post/USA Today (CPI +0.4%,
   core +0.3%); AP (Nikkei +0.8% to 60,942.48, Kospi +1.6% to 5,321.10,
   TSMC October revenue +59.7% y/y).
7. Anthropic IPO — SEC S-1/A (10 Nov) via CNBC/FinanceFeeds: $70–$78 range,
   825m shares, up to ~$64bn, up to ~$1.4tn valuation, $26bn private
   placement (Google, Nvidia $10bn each).
8. Bulgaria + Seongnam crashes — Reuters/AP: Trakia motorway fog pile-ups,
   12 killed, 46 injured, ~86 vehicles, national day of mourning on 11 Nov;
   Seongnam bus hit 32 vehicles, 9 seriously hurt, 48 minor injuries.
9. Ebola in DR Congo — Reuters, government data: 11,042 cases, 5,387 deaths.

Deliberately excluded: the El Salvador/Haiti 400 Mawozo strike item (BBC
could not verify the video; death toll unconfirmed) — dropped in the final
trim to fit the 2,000-character gate, not for lack of sourcing. Every
unconfirmed claim that survived is labelled unconfirmed in the text.

## Verification (commands run, results)

Local Python is 3.12.3 and Node is 24.22.1; the grader runs Python 3.13 /
Node 22. The code uses only the standard library and syntax valid on both,
so this is not a blocker. There is no local grade for this competition
(RULES.txt: "the server grades every entry"); the sealed gate scorer is
not in the kit, so the gate was replicated exactly from the published
rules and the judge heat cannot be run locally.

Commands (from `~/workspace/makefun-werewolf/news-summary/`):

```
python3 -m py_compile main.py
rm -rf /tmp/out1 /tmp/out2
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
cmp /tmp/out1/entry.txt /tmp/out2/entry.txt
sha256sum /tmp/out1/entry.txt /tmp/out2/entry.txt summary.txt
```

Results:

- `py_compile`: OK, no errors.
- Two runs: byte-identical (`cmp` silent, exit 0). SHA-256 of both outputs
  and of `summary.txt`: `22e5c8ad74d523353c3c1029bb5e55ecb4de3d21ec4fdf58a8dae12a108dbad6`.
- Gate check (UTF-8 decode, code-point count, non-whitespace check):
  - code points: **1,996** (limit 2,000) — PASS
  - bytes: 2,000 — PASS (gate counts characters, not bytes)
  - valid UTF-8: True — PASS
  - not only whitespace (1,664 non-whitespace chars) — PASS
  - **GATE: PASS**
- Character-count history during drafting: 2,721 → 2,243 → 2,051 → 1,996
  code points (three revisions of `summary.txt`; `main.py` also revised
  once after its first write).

No judge score exists: the judge heat runs only on make.fun's server after
submission, against the three fixed house summaries and the other entries.

## Known weaknesses (honest)

1. **Built mid-day.** Research was done ~10:00 UTC on 11 Nov 2026, while
   the day was still running in the Americas. Events from the later part of
   the day (US afternoon/evening news, the outcome of the Abu Dhabi talks'
   second day, COP31 speeches) are NOT in this summary. An entry refreshed
   closer to the 12 Nov 18:30 UTC deadline, with the full day's reporting,
   would likely score higher on criterion 1 (specific events of that day)
   and criterion 2 (breadth). The house summaries were written early on
   11 Nov and cover only the start of the day, so this entry already covers
   more than they do — but a later-built rival entry could cover more still.
2. **Several items were first reported on 10 Nov** (CPI release, Anthropic
   S-1/A filing, Bulgaria crash, Hormuz attacks, Hegseth vote in US evening
   hours) and are included because they are the news being reported and
   reacted to on 11 Nov — the same set the kit's own `competition.yaml`
   lists as the day's sources. A strict judge could discount an item or
   two as "another day's news"; the summary never claims a 10 Nov event
   happened on 11 Nov, and the dated header plus the 11 Nov items
   (Abu Dhabi day two, COP31 opening, Seongnam crash, day of mourning)
   anchor it to the day.
3. **At the character limit.** 1,996/2,000 code points leaves no room to add
   a story without cutting another; any later edit must re-check the count.
   Note the file is 2,000 bytes — the gate counts characters, so this is
   fine, but do not add a character without removing one elsewhere.
4. **No local judge score.** The provisional/final heat needs make.fun's
   gateway and the superbot judge; quality was judged only against the
   published rubric and the sourced facts. No claim is made about win rate.
5. **Not submitted.** No GitHub repo was created, nothing was submitted, no
   wallet/keypair was created or used, no API keys were handled. Submission
   (repo `kadocay/news-summary`, transcripts bundle, `makefun.mjs check` /
   `submit`) is still to be done by the parent agent.
