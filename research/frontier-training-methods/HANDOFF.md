# Handoff: Unexplored Frontier-Model Training Methods

**Prepared:** September 5, 2026, 22:20 UTC. **Revised:** September 25, 2026, 15:30 UTC, written for a restart in a desktop session.
**Branch:** `claude/frontier-model-training-research-siwsgv`, restarted from `main` after pull request #4 merged
**Head commit:** `9b9c999` plus this handoff commit
**Open pull request:** https://github.com/WadeLovell/wadelovell-portfolio/pull/5 (open, mergeable, awaiting the author's word)
**Merged pull requests:** #1, #2, #3, #4

## 0. Restarting in a desktop session

Read this section first. Sections 1 through 6 carry the research program itself.

**Why the move helps.** Every cloud session for this program has run behind an egress proxy that returns 403 on arxiv.org, export.arxiv.org, openreview.net, neurips.cc, iclr.cc, api.semanticscholar.org, api.openalex.org, huggingface.co, and scholar.google.com. Exa fetch and web search reached those pages second-hand, and that constraint shaped several judgment calls in the log. A desktop session on an ordinary home network reaches all of them directly. The single largest payoff is OpenReview: a desktop session can query the API at `api2.openreview.net/notes?content.venueid=NeurIPS.cc/2026/Conference` and settle the open Tier B items in one pass.

**First four commands, one at a time.**

```
git clone https://github.com/WadeLovell/wadelovell-portfolio.git
```

```
cd wadelovell-portfolio && git fetch origin claude/frontier-model-training-research-siwsgv
```

```
git checkout claude/frontier-model-training-research-siwsgv
```

```
git log --oneline -3 && ls research/frontier-training-methods/
```

The third command should land you on `9b9c999` or later. Pull request #5 sits on this branch, so any new work either goes into that pull request or waits for it to merge.

**Read in this order.** `README.md`, then this file, then `01-research-plan.md` Sections 1, 3, 4, and 6, then `02-research-report.md` Sections 1, 2.3, and 7. Treat the path sections and `references.md` as lookup material. `search-log.md` carries every pass in date order, including the two errors described in Section 3 below.

**Load the voice standard.** All prose in this program follows the Collaborative Voice standard. In a desktop session, invoke the `collaborative-voice` skill before drafting or editing any of these files, and the `voice-pass` skill for a full review cycle.

**One scheduled job still fires in the cloud.** Trigger `trig_01MNjUMKLGQDgLgQvrASMatD`, an ICLR 2027 submission sweep, runs once on September 26, 2026 at 15:00 UTC in a fresh cloud session with web search alone. It will branch from `main` and may open its own pull request. Coordinate with it or disable it from the Routines list before starting parallel work on the same files. Every other trigger for this program has fired and disabled itself.

**What a desktop session should do first, in priority order.**

1. Settle the NeurIPS 2026 half of the re-grade through the OpenReview API. Section 3, item 1.
2. Re-verify the one source that has failed to crawl twice. Section 3, item 3.
3. Map every citation key in `02-research-report.md` to its row in `references.md`. Section 3, item 2, and the reason it matters.

## 1. State of the work

The research program is complete and pushed. Six deliverables sit in `research/frontier-training-methods/`:

| File | Size | Status |
|---|---|---|
| `01-research-plan.md` | 2,200 words | Final. Two-register method, four paths, grades G1 to G4, tiers A to D, protocol, threats |
| `02-research-report.md` | 11,800 words | Final after one independent review pass, then three re-grade passes |
| `references.md` | 355 rows | 316 unique verified sources (115 A, 14 B, 57 C, 127 D, plus 3 labeled baselines) |
| `search-log.md` | five passes | Every query, channel, count, coverage limit, and correction |
| `README.md` | 190 words | Index and scale of the run |
| `03-condensed-report.docx` | 2,373 words | Six to seven pages, US Letter, built with docx-js |

The evidence base that produced the report (four sweep registers, the frontier recipe register, the shared protocol, the independent review, the orchestrator's anchor facts, the merged reference set, and the two build scripts) was committed as `working/` in pull request #1 and removed from `main` immediately after the merge at the author's request. It remains recoverable: `git show 8ef9540^2:research/frontier-training-methods/working/`.

`portfolio.html` carries an Open Research section linking to this directory on GitHub.

## 2. What a new session needs to know

**Thesis and method.** The frontier converged in 2026 on one recipe per path, so absence became measurable. A gap is a method with Tier A or B evidence whose every cell in the adoption matrix reads absent, undisclosed, or rejected. Grades: G1 proposed and untested at scale; G2 validated at scale and absent from frontier recipes; G3 named open problem; G4 untested combination. Tiers: A peer-reviewed main track or journal; B under review; C technical report or model card; D preprint or post with no review signal.

**Workshop papers are Tier D.** That single rule has caught three separate misfilings: Foreign Sparse Attention (ICML 2025 ES-FoMo III), Truncated Importance Sampling, and an ICML 2025 AI for Math hit for Dr. GRPO that would have masked its real COLM 2025 publication. Check both the workshop and the main track on every acceptance.

**The venue index is the discriminator, and the OpenReview forum line is not.** An OpenReview forum venue line read through a search tool renders identically for an accepted ICLR 2026 poster and a declined submission. Acceptance is confirmed on `iclr.cc/virtual`, `proceedings.iclr.cc`, `icml.cc/virtual`, or `neurips.cc/virtual`. The September 17 pass searched `proceedings.iclr.cc` alone and nearly produced a false negative; the venue audit that followed found REAP and LLM-JEPA on `iclr.cc/virtual` with no proceedings hit. Query both indexes.

**Top-ranked gaps.** Rank 1: parameterization-correct hyperparameter transfer for Muon-family optimizers (NeurIPS 2025, two papers) against the RMS-matching heuristic at 0.7T to 2.8T parameters. Rank 2: autonomous environment and verifier generation, named by GLM-5.3 as its next step. Rank 3: expert pruning validated on a trillion-parameter checkpoint (ICLR 2026) while every flagship ships unpruned. The full ranked table of 20 is Section 7 of the report.

**Editing `references.md` safely.** Rows are pipe-delimited and split into ten fields: index 1 id, 2 first author, 3 date, 4 title, 5 venue, 6 evidence, 7 paths, 8 verified. Edit by field index in Python, never by regex across columns. A regex written as `(?:[^|]*\|){4}` consumed one field too few and overwrote the venue column on four Tier A rows.

```python
f = lines[idx].split('|')
f[6] = ' ' + evidence + ' '
lines[idx] = '|'.join(f)
```

After any edit, count malformed rows (any row whose split yields other than ten fields) and confirm zero, then confirm the stated tier counts still sum to 313 in-window sources.

**Coupled numbers.** A tier change ripples into: the count header in `references.md`, the scale line in `README.md`, the four per-path tally sentences in `02-research-report.md` Section 2.3, any inline tier label in the report's prose, and the evidence column of the ranked table in Section 7. Section 2.3 prose cites matrix row numbers, so removing a matrix row forces a renumber. The matrix stands at 37 rows and the ranked table at 20.

**Voice standard.** Short declarative sentences, affirmative construction, no em-dashes, arguments lead and citations follow, one thesis with a parallel conclusion. All six Markdown files carry zero em-dashes as of this handoff. Verify with `grep -c $'\xe2\x80\x94' *.md`, which should report zero for each file.

## 3. Open items, in priority order

1. **NeurIPS 2026 re-check.** Nine Tier B items await an accepted-paper index. At 15:00 UTC on September 25, three hours after notifications closed at 11:59 UTC, `nips.cc/virtual/2026/papers.html` loaded and listed nothing, and the OpenReview group rendered a JavaScript shell. The six items ICLR 2026 declined are PRIME (2502.01456), DeepSeek-GRM (2504.02495), RLPR (2506.18254), Invisible Leash (2507.14843), pass@k training (2508.10751), and hybrid architectures (2510.04800). Three more carry a stale review signal: the entropy mechanism (2505.22617), OpT-DeUS (2508.08011), and optimizer benchmarking (2509.01440). The ranking in Section 7 may shift if the entropy-mechanism, pass@k, or implicit-process-reward items publish. **A desktop session should query the OpenReview API directly rather than waiting on the conference virtual site.** A scraped list of roughly 7,000 NeurIPS 2026 titles has circulated since early September from a `dev.neurips.cc` export; its own posters report it mixes accepted, rejected and withdrawn papers, it carries no venue authority, and this program has declined to use it.

2. **Citation keys and reference rows do not cross-check by string search.** On September 17 a pass moved Truncated Importance Sampling to Tier D and stated the report never cites it. The report does cite it, in Section 6, under the key "Yao et al., 2025." The check had searched for the title, for "TIS", and for the author string "Yao, F". The structural claim survived, because the citation sits in narrative prose outside the matrix, the graded gaps and the ranked table, so only the inline tier label was wrong and it now reads Tier D. Build a key-to-row map before the next re-grade.

3. **One source stays unverified.** The Quantile Balancing blog (`kexue.fm/archives/11619`) failed to crawl on the execution date and again on the follow-up pass, so it holds `verified: no`. Every other source in `references.md` is verified against a primary page. A desktop session on an open network should reach it.

4. **ICLR 2027 submissions** open on OpenReview after the September 25, 2026 deadline. The scheduled sweep described in Section 0 fires September 26.

5. **Two facts stay undisclosed at the source.** Kimi K3's pretraining token count appears nowhere in its report, confirmed twice. Apple Foundation Models 2026 and xAI Grok 5 do not exist as of the execution date.

6. **Residual voice items from the review**, judged acceptable rather than fixed: bold-headline gap paragraphs lead with the claim by design; Section 2 reads model by model because it is register content; a handful of sentences remain over 30 words where the evidence demands it.

**Closed since the first handoff:** pull requests #1 through #4 merged; the five unverified sweep items verified; the portfolio card added; the condensed Word report built and indexed; a full venue-column audit across all 355 rows, after which no workshop paper remains at Tier A or B; and four items moved to Tier A on September 25 (Dr. GRPO at COLM 2025, MergeBench at NeurIPS 2025 Datasets and Benchmarks, GPTailor and Compute-Optimal QAT at ICLR 2026).

## 4. Pass history in `search-log.md`

| Pass | Date | Outcome |
|---|---|---|
| Original sweep log | September 5 | Four paths, the frontier register, every query and count |
| Follow-up verification | September 5 | Five unverified items resolved; Foreign Sparse Attention to Tier D; matrix 38 to 37 |
| Partial Tier B re-grade | September 17 | UltraLong to Tier A; Truncated Importance Sampling to Tier D; one false claim, corrected September 25 |
| Venue-column audit | September 17 | All 355 rows checked for tier-versus-venue contradictions; four Tier A rows confirmed against venue pages |
| Tier B re-grade | September 25 | Four items to Tier A; NeurIPS 2026 half left open with the evidence recorded |

## 5. Decisions taken without asking, for your review

- Scope: research artifacts only, plus the one portfolio card the author approved.
- Register columns: six disclosing model families (Kimi K3; DeepSeek-V4; GLM-5, 5.2, 5.3; Nemotron 3; Qwen3 and 3.5; MiniMax M1 to M2.7). Proprietary system cards were omitted from the matrix because they disclose evaluations rather than algorithms, and the report says so.
- A fifth matrix cell value, "rejected," was added to the plan after Kimi K3 and GLM-5 each reported a tested-and-dropped method.
- Workshop papers were assigned Tier D under the plan's main-track rule; the report labels them "ICML workshop" where cited.
- The `working/` directory was committed in pull request #1 so the evidence base survives the ephemeral container, then removed from `main` at the author's request.
- The portfolio card was placed in its own "Open Research" section rather than the products grid, because that grid's stated thesis is products built on the CRI foundation. The card links to the GitHub-rendered directory, which renders the Markdown that a static host would serve as plain text.
- The condensed report was validated against the OOXML schema rather than rendered visually, because LibreOffice and `pdftoppm` are both unavailable in the cloud container. A desktop session can open the `.docx` and confirm the page count directly.

## 6. Environment facts worth carrying forward

The cloud container is ephemeral and reclaimed after inactivity, so anything worth keeping is committed and pushed. Outbound HTTPS runs through an agent proxy whose 403 list is given in Section 0. Exa fetch and web search worked throughout. Scholar Gateway indexes Wiley journals and returned nothing on-path. A desktop session lifts all of it.
