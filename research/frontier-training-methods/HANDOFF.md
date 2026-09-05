# Handoff: Unexplored Frontier-Model Training Methods

**Prepared:** September 5, 2026, 22:20 UTC. **Revised:** September 5, 2026, after the follow-up verification pass.
**Branch:** `claude/frontier-model-training-research-siwsgv`, restarted from `main` after pull request #1 merged
**Pull requests:** https://github.com/WadeLovell/wadelovell-portfolio/pull/1 (merged) and https://github.com/WadeLovell/wadelovell-portfolio/pull/2 (merged, removed `working/`)
**Head commit at handoff:** `111e4d3` plus this handoff commit

## 1. State of the work

The research program is complete and pushed. Five deliverables sit in `research/frontier-training-methods/`:

| File | Words | Status |
|---|---|---|
| `01-research-plan.md` | 2,200 | Final. Two-register method, four paths, grades G1 to G4, tiers A to D, protocol, threats |
| `02-research-report.md` | 11,800 | Final after one independent review pass (first-draft gated score 7.0; every flagged item applied) |
| `references.md` | 12,200 | 316 unique verified sources (110 A, 21 B, 57 C, 125 D) plus 41 register-only Tier C sources |
| `search-log.md` | 6,900 | Every query, channel, count, and coverage limit |
| `README.md` | 190 | Index and scale of the run |

A follow-up pass verified the five items that carried `verified: no` and applied the two corrections they forced. Foreign Sparse Attention proved to be an ICML 2025 ES-FoMo III workshop poster, so it moved from Tier B to Tier D under the plan's main-track rule, its row left the adoption matrix (38 rows to 37), and its G1 gap left the Path 3 list (ten interventions to nine). The CoT-Pass@K poster gained its authors and now reads as Wen et al., 2026, ICLR. The ranked table of 20 stands unchanged. `search-log.md` records the pass under "Follow-up verification pass."

The evidence base that produced the report (four sweep registers, the frontier recipe register, the shared protocol, the independent review, the orchestrator's anchor facts, the merged reference set, and the two build scripts) was committed as `working/` in pull request #1 and removed from `main` immediately after the merge at the author's request. It remains recoverable from the merge commit of pull request #1 (`git show 8ef9540^2:research/frontier-training-methods/working/`).

## 2. What a new session needs to know

**Thesis and method.** The frontier converged in 2026 on one recipe per path, so absence became measurable. A gap is a method with Tier A or B evidence whose every cell in the adoption matrix reads absent, undisclosed, or rejected. Grades: G1 proposed and untested at scale; G2 validated at scale and absent from frontier recipes; G3 named open problem; G4 untested combination. Tiers: A peer-reviewed main track or journal; B under review; C technical report or model card; D preprint or post with no review signal. Workshop papers count as D. A gap graded on undisclosed cells alone is provisional.

**Top-ranked gaps.** Rank 1: parameterization-correct hyperparameter transfer for Muon-family optimizers (NeurIPS 2025, two papers) versus the RMS-matching heuristic at 0.7T to 2.8T parameters. Rank 2: autonomous environment and verifier generation, named by GLM-5.3 as its next step. Rank 3: expert pruning validated on a trillion-parameter checkpoint (ICLR 2026) while every flagship ships unpruned. The full ranked table of 20 is Section 7 of the report.

**One correction already made.** The frontier register surfaced sliding-window checkpoint merging in Nemotron 3 Super's pretraining (arXiv 2604.12374, Section 2.5). Checkpoint merging moved from rank 3 to rank 14 and from G2 to G3. The search log records it.

**Environment facts that shaped the run.** The session's egress policy blocked direct access to arxiv.org, export.arxiv.org, openreview.net, api.semanticscholar.org, api.openalex.org, huggingface.co, and scholar.google.com. arXiv abstract and HTML pages were reachable through the Exa fetch tool. OpenReview was reachable only through domain-filtered web-search snippets. Scholar Gateway indexes Wiley journals and returned nothing on-path. A new session in the same environment will hit the same limits; a session with open egress could enumerate OpenReview and the arXiv API directly and tighten the Tier B statuses.

**Voice standard.** All prose follows the Collaborative Voice standard (`collaborative-voice` skill): short declarative sentences, affirmative construction, no em-dashes, arguments lead and citations follow, one thesis with a parallel conclusion. The report passed mechanical checks for em-dashes (zero), banned negatives (only inside direct quotations), and citation-key collisions (none) at handoff.

## 3. Open items, in priority order

1. **Tier B re-grade on September 24, 2026.** NeurIPS 2026 notifications land that day. Twenty Tier B items may move to A or D: the entropy-mechanism paper (2505.22617), pass@k training (2508.10751), PRIME (2502.01456), RLPR (2506.18254), Dr. GRPO (2503.20783), DeepSeek-GRM (2504.02495), Invisible Leash (2507.14843), and the others listed under Tier B in `references.md`. The ranking in Section 7 may shift if the entropy-mechanism, pass@k, or implicit-process-reward items publish. A scheduled trigger fires that morning with the full brief.
2. **ICLR 2027 submissions** open on OpenReview after the September 25, 2026 deadline. A follow-up sweep after that date would extend the window. A scheduled trigger fires on September 26.
3. **One source stays unverified.** The Quantile Balancing blog (`kexue.fm/archives/11619`) failed to crawl on the execution date and again on the follow-up pass, so it holds `verified: no`. Every other source in `references.md` is verified against a primary page.
4. **Two facts stay undisclosed at the source.** Kimi K3's pretraining token count appears nowhere in its report, confirmed twice. Apple Foundation Models 2026 and xAI Grok 5 do not exist as of the execution date.
5. **Residual voice items from the review** that were judged acceptable rather than fixed: bold-headline gap paragraphs lead with the claim by design; Section 2 reads model by model because it is register content; a handful of sentences remain over 30 words where the evidence demands it.

Closed since the first handoff: the pull request watch (both pull requests merged), the four unverified sweep items and Foreign Sparse Attention (all verified), and the portfolio link (`portfolio.html` now carries an Open Research section linking to this directory).

## 4. How to resume

```
git fetch origin main
git checkout main
```

Read, in order: `README.md`, `01-research-plan.md` Sections 1, 3, 4, and 6, then `02-research-report.md` Sections 1, 2.3, and 7. The path sections and `references.md` are lookup material. To regenerate `references.md` or `search-log.md`, or to re-run a sweep from the shared protocol, restore the evidence base from the pull request #1 merge commit as described in Section 1.

## 5. Decisions taken without asking, for your review

- Scope: research artifacts only, no change to the site pages.
- Register columns: six disclosing model families (Kimi K3; DeepSeek-V4; GLM-5, 5.2, 5.3; Nemotron 3; Qwen3 and 3.5; MiniMax M1 to M2.7). Proprietary system cards were omitted from the matrix because they disclose evaluations rather than algorithms, and the report says so.
- A fifth matrix cell value, "rejected," was added to the plan after Kimi K3 and GLM-5 each reported a tested-and-dropped method.
- Workshop papers were assigned Tier D under the plan's main-track rule; the report labels them "ICML workshop" where cited.
- The `working/` directory was committed in pull request #1 so the evidence base survives the ephemeral container, then removed from `main` at the author's request.
- The portfolio card was placed in its own "Open Research" section rather than the products grid, because that grid's stated thesis is products built on the CRI foundation. The card links to the GitHub-rendered directory, which renders the Markdown that a static host would serve as plain text.
