# Review 01: `02-research-report.md` against the Collaborative Voice standard

Reviewer: independent fresh-eyes pass. Report read in full (10,363 words, 209 lines). Plan skimmed for the method the report claims to follow. Line numbers refer to `02-research-report.md`.

---

## 1. Scores

| Level | Score | Gating reason |
|---|---|---|
| Word | 8.0 | Vocabulary is plain and precise almost everywhere. Held below 8.5 by one lab carrying three names (Moonshot / Kimi / Kimi Team; Zhipu / Z.ai / GLM), two names for the same optimizer family ("Muon-family," "Muon-class," "matrix-preconditioned"), mixed British and American spelling ("distils," "unanalysed" beside "synthesizes," "optimizer"), and abbreviations that first appear undefined inside tables (OPD, WSD, QAT, MTP, RLVR). |
| Sentence | 7.5 | No em-dashes anywhere, which is a real achievement at this length. Held down by roughly sixty negative constructions ("no flagship," "nothing," "Neither," "nobody," "gives no analysis"), a dozen sentences over 40 words built as stacked lists, several "that ... that ... that" chains, and two sentences whose logic slips ("Whether X ... is a combination of two ingredients"). |
| Paragraph | 7.5 | The bold-headline device is strong: nearly every gap paragraph opens on its claim and its grade, and carries one argument (evidence, frontier status, gap). Held down by announcing frames at the start of many section-opening paragraphs (lines 20, 28, 32, 69, 101, 121, 123, 140, 160) and by Section 2's paragraphs, which read as model-by-model inventories rather than arguments. |
| Section | 7.0 | Capped by unkept structural promises: Path 3 promises "five interventions" and delivers ten; Path 2 promises "four properties" and delivers nine; Section 7 says "Two gaps rank high" and discusses three; the thesis promises a gap matrix that the report never shows; tier counts fail to sum in three of four paths; the Path 1 intro list and the body run in different orders. |
| Whole paper | 8.0 | One argument does run start to finish: convergence makes absence measurable, the two registers locate it, the grades and ranking order it. The conclusion opens on the thesis sentence verbatim, walks the four paths, and returns to the rival. Held below 8.5 because the conclusion changes the order of paired items inside three of the four path summaries, drops the ranking the thesis promised, and picks rank 3 rather than rank 1 as its closing example. |

**Overall gated score: 7.0** (weakest level: section).

Calibration note. This report is well above the "clean prose with no argument" anchor in argumentative terms. It is held at 7.0 by the standard's rule that an unkept promise caps the score, and by rigor defects that a fresh reader hits inside the first two path sections. The path to 8.5 is mostly mechanical: fix the counts, keep or rewrite the promises, unify the citation keys, and convert the negatives. The argument itself is already there.

---

## 2. Thesis test

**Opening thesis (line 10):** "The frontier converged in 2026 on one training recipe per path, and the unexplored methods are the ones that carry peer-reviewed evidence at academic scale and sit outside that recipe."

- **Contestable position:** Yes, in its first half. "Converged on one recipe per path" rests on three Chinese open-weights labs, and a competent reader could dispute that three disclosing labs define "the frontier" when the plan's own Section 9 names the disclosure asymmetry with US labs. The second half ("the unexplored methods are the ones that ...") is a stipulated definition, which rule 15a says ceilings near 7 on its own. The compound thesis survives because the first half carries the contest.
- **Names the rival it defeats:** Yes, but in the second paragraph, not the first (line 12): "The rival reading judges novelty by recency: the newest arXiv method is the unexplored one." The rival is well chosen and the two-fold error ("overstates ... understates") is a good move.
- **States its mechanism:** Yes (line 10): "Convergence of that breadth makes absence measurable." And line 12: "The two-register method of the plan replaces recency with a matrix."
- **Question-begging modifier:** Line 10, "A method with **strong** evidence that every converged recipe omits is a gap." The plan defines evidence by tier; "strong" smuggles in the judgment. Replace with "Tier A evidence."
- **Announcing inside the thesis:** Line 10, "and that address is the finding this report delivers." This tells the reader what the report will do instead of doing it.

**Conclusion (line 209):** Opens with the thesis sentence verbatim, then "The register method delivered that set," then four path summaries in body order, then the rival, then "Two registers, one gap matrix, and four grades found it."

**Where they diverge:**

1. **Load-bearing order.** Intro order: (a) convergence claim, (b) post-training pipeline evidence, (c) pretraining evidence, (d) "makes absence measurable," (e) rival, (f) two registers and matrix, (g) grades, (h) ranking. Conclusion order: (a) thesis, (f) register method, (c) pretraining, then distillation, open-weights, (b) post-training, (e) rival, (f)(g) registers, matrix, grades. The intro presents post-training before pretraining; the conclusion reverses that. The rival moves from before the method to after the paths. Mechanism (d) and ranking (h) are absent from the conclusion.
2. **Terms.** Intro: "a Muon-family optimizer, an attention stack that is sparse or partly linear, a residual-stream upgrade, and an ultra-sparse mixture of experts with bias-based load balancing." Conclusion: "Muon-class optimizers, trained sparsity in attention, upgraded residual streams, and ultra-sparse experts." Same four items, three of four renamed. "Muon-family" vs "Muon-class" is the clearest.
3. **The promised ranking.** Line 12 ends "the report ranks the graded gaps by the strength of their evidence and the size of the claimed gain." The conclusion never mentions the ranking, and its one named example ("the NeurIPS 2025 result at 200 billion parameters that no flagship discloses") is rank 3. A fresh reader expects the conclusion to name rank 1.
4. **Ranking criteria differ between thesis and Section 7.** Line 12 promises ranking "by the strength of their evidence and the size of the claimed gain." Line 176 gives three rules (tier, scale above 30B, stage ubiquity) plus a fourth weight (the frontier naming the gap itself). "Size of the claimed gain" appears in none of them.

---

## 3. Structural promises

| Line | Promise | Status |
|---|---|---|
| 12 | "replaces recency with a matrix. Rows are methods ... Columns are frontier models. A row with an 'absent' or 'undisclosed' cell in every column is a gap." | **Unkept.** No matrix appears anywhere in the report. "Gap matrix" is invoked at lines 20, 34, 205, 209 as if the reader has seen it. The per-path tables carry a one-column "Frontier status," which is a collapsed summary, not the matrix. The plan (Section 10, item 2) promised the matrix in this document. |
| 12 | Cells read "absent" or "undisclosed" | **Contradicted at line 20**, which adds "tested and rejected at frontier scale, which the gap matrix records as a distinct cell value." The plan's four values are disclosed / hinted / absent / undisclosed; "hinted" never appears in the report and "tested and rejected" appears nowhere in the plan. |
| 12 | "ranks the graded gaps by the strength of their evidence and the size of the claimed gain" | **Diverges** from line 176's three rules plus one weight. "Size of the claimed gain" is never used. |
| 12 | "a grade from G1 (proposed and untested at scale) through G4 (untested combination of adopted methods)" | **Partly kept.** G1 and G4 are defined in-line. G2 and G3 are used from line 40 on and never defined in this document. |
| 20 | "Two negative results from the Kimi K3 report" | Kept (cosine vs WSD; top-k vs log-ratio). |
| 28 | "Section 6 grades that statement as a G3 gap" | Kept (line 148). |
| 32 | "The peer-reviewed record now holds a second layer of results, on hyperparameter transfer, schedules, checkpoint merging, memory, and training objectives" | **Order not kept.** Body order: transfer (34, 36, 38), schedule (40), checkpoint merging (42), data-constrained (44), objectives (46), memory (48), precision (50), mid-training (52). Memory and objectives are swapped; three body gaps are outside the promised list. |
| 32 | "The sweep verified 82 sources on this path: 39 at Tier A, 3 at Tier B, 17 at Tier C, and 22 at Tier D." | **Arithmetic fails.** 39 + 3 + 17 + 22 = 81. |
| 36 | "Three peer-reviewed optimizer refinements" | Kept (grouped heads, per-neuron, polynomial iterations), plus one Tier D extra. |
| 44 | "Data-constrained recipes are ICLR 2026 **orals**" | **Unkept.** Only Kim et al. 2026 is an ICLR 2026 oral in the body; Prabhudesai et al. is NeurIPS 2025. |
| 46 | "Alternative objectives have oral-track evidence **below 1 billion parameters**" | **Contradicted** by the body's 8-billion diffusion model and 12-billion hybrid, and by the table (line 62, "8B / 1e23 FLOPs"). |
| 69 | "the peer-reviewed literature now documents **four** properties of that method that no frontier report addresses" | **Unkept.** Eight bold paragraphs and nine table rows follow. The four are never named. |
| 69 | "The sweep verified 88 sources on this path: 20 at Tier A, 1 at Tier B, 18 at Tier C, and 47 at Tier D" | **Arithmetic fails.** 20 + 1 + 18 + 47 = 86. |
| 71 | "Three labs now spend two days to two iterations of frontier compute on this stage" | **Contradicted** by table line 88 ("stage run by Kimi, DeepSeek, Zhipu, NVIDIA") and rank 6 ("Four labs run the stage"). |
| 101 | "The peer-reviewed record shows **five** such interventions validated between 8 and 1,000 billion parameters" and "The **five** below define the gap." | **Unkept twice.** Nine bold paragraphs plus a "Two further gaps" paragraph; ten table rows. And the table's scale column holds 1.5B, 2B, 2.2B, and 3B entries, all below the promised "8 ... billion" floor. |
| 101 | "The frontier adopts **four** adaptations of a released base." | Kept (DSA conversion, Llama-Nemotron pruning, RLVR on open bases, GLM-5.3 post-training). |
| 121 | "Two further gaps" | Kept, but announcing. |
| 140 | "The peer-reviewed record answers **three** questions the flagships leave open" | Partly kept. Three questions map to gaps at lines 142, 146, 148. Six other gaps in the section sit outside the frame. |
| 140 | "The sweep verified 85 of 89 sources on this path: 30 at Tier A, 9 at Tier B, 25 at Tier C, and 25 at Tier D." | **Arithmetic fails.** 30 + 9 + 25 + 25 = 89, which is the unverified total, not the verified 85. |
| 176 | "Thirty-eight graded gaps came out of the four paths." | Kept. 10 + 9 + 10 + 9 = 38. |
| 176 | "the twenty that combine ..." | Kept. Twenty rows. |
| 176 | "Three ranking rules apply." | Kept, though a fourth weight (frontier self-naming) precedes them and is not counted. |
| 201 | "**Two** gaps rank high for a reason beyond their evidence." | **Unkept.** The paragraph discusses ranks 1, 3, and 2. |
| 205 | "**Four** limits bound the register." | Kept (non-disclosure, family effects, recency, channel bias). Note the plan's Section 9 named five threats; the report drops "disclosure asymmetry across labs" and "single-session execution" and adds "family effects," without saying so. |
| 205 | "Twenty-one Tier B items await decisions" | **Contradicted** by the per-path counts: 3 + 1 + 10 + 9 = 23. |
| 205 | "ranks 3, 13, and 16 rest partly on undisclosed cells" | **Contradicted** by the Path 1 table: rank 13 (line 63) reads "Absent from DeepSeek-V4"; rank 16 (line 61) reads "Absent at 28T to 33T tokens." Only rank 3 (line 60) reads "Undisclosed." |
| Plan 9 | "A gap graded on 'undisclosed' cells alone is reported as provisional." | **Unkept.** The word "provisional" appears nowhere in the report. Rank 3, and the Path 3 rows at lines 125 and 128, are undisclosed-only and carry no label. |

---

## 4. Drift list (16-item checklist)

### Item 1. Framing openers that point at the subject before engaging it
- L20: "Two negative results from the Kimi K3 report matter for the gap analysis."
- L28: "The one open problem the converged labs name in their own words concerns environments rather than algorithms."
- L32: "Those adoptions show the pipeline from peer review to flagship working at a lag of six to twelve months."
- L48: "The residual stream is where the frontier moved fastest, with ..."
- L69: "The method is adopted. The gaps sit in what the adopters leave unmeasured."
- L101: "Those four adaptations define 'explored.' The five below define the gap."
- L121: "Two further gaps have Tier A sources and small footprints."
- L123: "The open problem that frames the whole path comes from Olmo 3."
- L140: "Post-training is the path where the frontier moves fastest and discloses most." / "The adopted recipe rests on peer-reviewed foundations."
- L160: "Two Tier C findings constrain every gap above."
- L176: "The ranking below orders the twenty that ..."
- L201: "Two gaps rank high for a reason beyond their evidence."

### Item 2. Sentences that abstract what the next sentence shows, or add nothing
- L10: "and that address is the finding this report delivers."
- L32: "The gaps below are the results that lag still holds."
- L107: "That is Tier A evidence at frontier scale, produced outside the frontier labs." (restates the citation)
- L140: "The gaps are the results that came after those foundations."
- L142: "The Tier A result says the asymptote is the quantity that matters and names two knobs." (restates the two prior sentences)
- L156: "The frontier answers forgetting with on-policy distillation alone ... The frontier answer to forgetting rests on ..." (second sentence restates the first)
- L12: "That reading misjudges the frontier twice." (abstracts the two sentences that follow; fold the count)

### Item 3. Sentences to split (40+ words; representative, not exhaustive)
- L18: "DeepSeek-V4 trains 1.6 trillion parameters with 49 billion active on interleaved Compressed Sparse Attention and Heavily Compressed Attention, Manifold-Constrained Hyper-Connections in place of plain residuals, DeepSeekMoE, and Muon with hybrid Newton-Schulz iterations on 33 trillion tokens."
- L24: "GLM-5.2 merges more than ten expert models through parallel on-policy distillation in about two days on the slime framework, and GLM-5.3 reuses the GLM-5.2 base and attributes every gain to further post-training on the same stack."
- L26: "Open-ended tasks use an agentic generative reward model that reads the output, writes a rubric, scores each candidate against it, and records the scores, with a verbosity cap that forfeits a comparison when a candidate exceeds a length multiple."
- L34: "Muon, SOAP, and Shampoo hold a consistent 1.4 times speedup over AdamW from 190 million to 1.4 billion parameters under maximal-update parameterization with weight decay scaled as one over width, and the speedup vanishes with scale under standard parameterization."
- L48: "The residual stream is where the frontier moved fastest, with Attention Residuals at Kimi and manifold-constrained hyper-connections at DeepSeek (...), and both are Tier C at 27 to 48 billion parameters in their own ablations."
- L103: "Post-training neural architecture search freezes the multilayer perceptrons of a pretrained model, learns where full attention must remain, and delivers a 2-billion-parameter hybrid that matches Qwen3-1.7B with 53.6 times the generation throughput at 256K context."
- L148: "GLM-5.3 synthesizes environments and verifiers through research agents and a judge agent, and its authors state that the pipelines 'still require ...' and that autonomous environment generation 'is one of the next steps'." (58 words)
- L150: "Kimi K3 trains nine experts, three domains by three effort levels, under a budget multiplier annealed per domain 'under human-in-the-loop guidance,' and distils them into one model; DeepSeek-V4 and GLM-5.3 expose fixed effort modes."
- L154: "GLM-5.2 moved from group-relative advantages to a critic-based proximal policy optimization on individual rollouts so that compaction sub-traces of variable count and length become trainable, and the compaction method's own paper concedes that 'cross-trajectory GAE is an approximation'."
- L156: "Forgetting is predicted by the KL divergence from the base on the new task, and on-policy reinforcement learning is implicitly KL-minimal, with the authors stating that behavior 'at frontier scales ...' remains unknown'."
- L205: "Exa and web search rank by traffic, and the sweeps corrected for it with venue filters and reference-list snowballing from six seed reports, but a method with Tier A evidence and no citations from a frontier report could still be missing."

### Item 4. Simpler precise word
- L44: "5.2 times less data" → "one fifth of the data" (and "17.5 times data efficiency" → state the ratio plainly)
- L73: "fundamentally different tokenizers" → "different tokenizers"
- L123: "moves a frontier base a long way" → state the number (4.6 to 28.3 on Terminal-Bench 3.0)
- L42: "the closest thing in this register to a frontier-ready gap" → "the most frontier-ready gap in this register"
- L69: "in the sense of the user's second path" → "on the second path" ("the user" reads as an AI-drafting artifact in a report signed by the author)

### Item 5. Fact first, claim second
- L38: heading "Depth-wise hyperparameter transfer is untested in any state-of-the-art model" leads with the claim; the paragraph's supporting fact is the authors' own statement, which lands two sentences later.
- L119: heading "Reinforcement learning touches a small subnetwork, and nobody exploits that" leads with the claim before the 5 to 30 percent fact.
(Most gap paragraphs put the claim in the bold headline by design. This is a defensible house style; the standard allows it if the fact follows immediately. It does in most cases.)

### Item 6. Author-led citations and source-by-source listing
- L34: "The same paper shows that matching Muon's update RMS ..."
- L36: "A Tier D spectral study of Muon at up to 2.8 billion parameters finds that ..."
- L38: "Its authors tested up to 1.5 billion non-embedding parameters and state that ..."
- L46: "its authors state that every comparison ..."
- L52: "A Tier D study across 3 to 24 billion parameters finds ..."
- L71: "the survey of the field states the unanswered question directly:"
- L77: "The survey lists ... as a foundational open problem and proposes ..."
- L79: "A related ICML 2025 result shows that supervised fine-tuning memorizes ..."
- L83: "a Tier D study finds that teacher-student compatibility ..."
- L85: "The Nature version of DeepSeek-R1 reports that ..." / "Magistral reports that ..."
- L105: "its authors write that the architecture ..."
- L111: "The same study finds that early MoE layers ..."
- L113: "a Tier D study notes that merging ..."
- L115: "its authors say the earlier assumptions ..."
- L123: "A Tier D study finds that mid-training content bounds ..., and a NeurIPS 2025 study across more than 100 models finds ..."
- L142: "The Tier A result says the asymptote ..."
- L148: "its authors state that the pipelines ..."
- L152: "A survey accepted at ACM TIST names ..."
- L156: "with the authors stating that behavior ..."
- L158: "DeepSeek-V4's introduction states that ..."
- Taxonomy dumps: L18, L24, L26 (Section 2) run model by model (Kimi K3 ..., DeepSeek-V4 ..., GLM-5 ...) rather than threading a claim through them. L32 and L140 (the adoption catalogues) run source by source.
(Sentences whose subject is a frontier model, "Kimi K3 trains ...," are register content where the identity is the point. Those are acceptable under rule 4 and are excluded from this list.)

### Item 7. Negative constructions and define-by-contrast
- L20: "gave no advantage in convergence speed or final performance over"
- L28: "concerns environments rather than algorithms" (contrast carries the definition)
- L36: "that no flagship reports making"
- L38: "is untested in any state-of-the-art model" / "no state-of-the-art model has used it"
- L42: "say nothing about merging" / "no flagship disclosure"
- L44: "None discloses an epoch count, an ensemble, or a repetition regime."
- L48: "the same labs left out of their flagships" / "with no memory layer"
- L50: "The Tier C run reports none." / "measurable and unmeasured in public"
- L69: "uses the word distillation nowhere" / "that no frontier report addresses"
- L71: "No equivalent law exists" / "with no published law to size it"
- L73: "break the adopted method" / "no report of anyone trying it at scale"
- L75: "appear in no recipe" / "found no advantage"
- L77: "teaches almost nothing" / "Neither has the cure."
- L81: "gives no analysis of how many iterations help"
- L83: "says nothing above it" / "that no report evaluates"
- L85: "rather than measured evidence"
- L101: "that no frontier recipe applies"
- L105: "Nobody has reported converting"
- L109: "no frontier trial" / "no measurement above the academic scale"
- L111: "nothing about replay" / "'undisclosed' rather than 'absent'"
- L113: "a step the frontier skips" / "No report evaluates it"
- L115: "contradicts the frontier's fixed rule" / "loses to a token-dependent fraction"
- L119: "nobody exploits that" / "that no report tests"
- L121: "no change to the base weights" / "no frontier base ships with one" / "that no lab has reported taking"
- L142: "Neither report fits an asymptote." / "is unmeasured" / "is untested"
- L144: "unexamined at frontier scale" / "found no pass@64 gain" / "No flagship publishes"
- L148: "Neither has run the other."
- L152: "gives no gain on Llama" / "add nothing on other families" / "Partial credit is absent at every lab."
- L158: "No flagship discloses any learning after deployment."
- L199 (rank 20): "nobody has run the Tier A method"
- L205: "improve nothing else"
- L209: "that no flagship discloses"
Note: the report's subject is absence, so some negatives are substantive. The list above marks the ones a rewrite can turn affirmative ("The cure awaits both"; "Every flagship ships its full expert set"; "The per-token log-ratio reward matched top-k in speed and final performance").

### Item 8. Em-dashes
None found. Clean.

### Item 9. Because / that / which chains
- L10: "A method with strong evidence **that** every converged recipe omits is a gap with a specific address, and **that** address is the finding this report delivers."
- L34: "The same paper shows **that** matching Muon's update RMS to Adam's, the heuristic **that** Moonlight introduced and **that** Kimi K3 and DeepSeek-V4 inherit, is an incorrect width scaling."
- L44: "so the flagships sit at the edge of the unique-token supply the data-constrained literature models" (garden-path: the reader parses "models" as a noun)
- L123: "trains on bases '**that** do not reveal ...,' **which** blocks study of **how** mid-training shapes **what** reinforcement learning can later elicit"
- L152: "(...), **which** turns every small-model reward result into a claim **that** needs a family control"
- L154: "so **that** compaction sub-traces ... become trainable, and the compaction method's own paper concedes **that** ..."

### Item 10. Inconsistent ordering of paired or listed items
- L10 vs L209: intro lists post-training pipeline then pretraining; conclusion walks pretraining first and post-training last.
- L32 list (transfer, schedules, checkpoint merging, memory, objectives) vs body (transfer, schedule, merging, data, objectives, memory, precision, mid-training).
- L160: "GLM-5.3 aligns ..., DeepSeek-V4 ships ..., and Kimi K3 runs ..." reverses the Kimi, DeepSeek, GLM order used at L10, L18, L24, L42, L115.
- L209 pretraining summary: "parameterization-correct transfer, checkpoint merging, schedule choice, and memory layers" vs body order transfer (34), schedule (40), merging (42), memory (48).
- L209 open-weights summary: "expert pruning, layer-selected conversion, and merge-then-distil" vs body order conversion (103), pruning (107), merging (113).
- L12 vs L176: ranking criteria named differently (see Section 2, item 4).

### Item 11. Inconsistent terminology for one idea
- Labs: "Moonshot" (L10) / "Kimi" (L88 table, throughout) / "Kimi Team" (citations). "Zhipu" (L10, L88) / "Z.ai" (citations) / "GLM" (throughout).
- Optimizer family: "Muon-family optimizer" (L10) / "Muon-class optimizers" (L176 rank 1, L209) / "matrix-preconditioned optimizers" (L34, L56).
- The frontier models: "flagship" (dominant) / "state-of-the-art model" (L38) / "frontier model" / "frontier recipe" / "converged recipe" / "adopted recipe" (L140) / "disclosed frontier recipe" (L69).
- "register" means the frontier register at L42 ("in this register") and the whole method at L205 ("bound the register") and L209 ("The register method").
- GLM-5 report cited as "(Zeng et al., 2026)" at L18 and "(GLM-5 Team, 2026)" at L32, L101, L103, L140, L160.
- DeepSeek-R1 Nature paper cited as "(DeepSeek-AI, 2025, Nature)" at L85 and "(Guo et al., 2025, Nature)" at L140.
- "Olmo 3" (L101, L123) vs "Team OLMo" (citation) vs "OLMo 3" (plan).
- Nemotron NVFP4 pretraining attributed to "Nemotron 3 Super" (L50) and "Nemotron 3 Ultra" (L115).
- "NVIDIA, 2026b" is Nemotron 3 Super at L50 and Nemotron-Cascade 2 at L69.
- Spelling: "distils," "distil," "unanalysed" (British) beside "synthesizes," "optimizer," "normalized" (American).
- Abbreviations used in tables without prior definition in text: OPD (L88 to L93), WSD (L59), QAT (L133), MTP (L136), RLVR (L165; first text use at L123 inside a quote), MoE (L109 in text, undefined).

### Item 12. Logic and inverted metaphors
- L32: "Muon runs Kimi K2 and K3, DeepSeek-V4, and GLM-5" (the optimizer runs the models; inverted).
- L140: "Fully asynchronous training ... runs Ant Group's trillion-parameter models" (same inversion).
- L83: "Whether a compatible frontier teacher could pretrain a frontier-scale student below the supervised cost is a combination of two adopted ingredients" (a question is not a combination).
- L119: "Restricting frontier reinforcement learning to the subnetwork it would touch anyway is a combination of two documented facts" (an action is not a combination of facts).
- L71: "spend two days to two iterations of frontier compute" (mixed units: days and iterations).
- L201: "A 10 percent efficiency claim at rank 1 ... a 10 point benchmark claim at rank 11" (rank 1 claims 1.4x and 12 to 34 percent; rank 11 claims "more than 20 points"; the hypothetical numbers read as a mismatch).
- L38: "transfers hyperparameters from 2 to 128 layers ... with the larger saving at 179 layers" (179 lies outside 2 to 128).

### Item 13. Announced rather than argued
- L10: "that address is the finding this report delivers."
- L28: "Section 6 grades that statement as a G3 gap and pairs it with the peer-reviewed self-play and automatic-curriculum literature."
- L32: "The gaps below are the results that lag still holds."
- L34: "What they leave untested is the Tier A prescription:"
- L101: "The five below define the gap."
- L140: "The gaps are the results that came after those foundations."
- L176: "The ranking below orders ..."

### Item 14. Removable words
- L34: "hold a **consistent** 1.4 times speedup" (borderline; "hold ... from 190 million to 1.4 billion" already says consistent)
- L109: "improves progressive depth growth **further**"
- L144: "Support shrinkage **still** exceeds expansion ... **even** for the prolonged-training checkpoints"
- L73: "**fundamentally** different tokenizers"
- L26: "so the rollout continues rather than collapsing the batch" ("rather than collapsing the batch" adds the reason; keep, but "continues" alone carries most of it)
- L142: "**Only** context length and model size move the asymptote." (keep; "only" is load-bearing here)
- L69: "in the sense of the user's second path"

### Item 15. Thesis and parallel conclusion
See Section 2. One argument runs through the whole. The conclusion returns to the thesis in the same words but changes the order of paired items in three of four path summaries, drops the ranking, and names rank 3 as its example.

### Item 16. Thesis contestability, rival, mechanism, question-begging modifiers
- Contestable: yes (first clause). Rival: named at L12. Mechanism: L10 "makes absence measurable," L12 "matrix."
- Question-begging: L10 "A method with **strong** evidence." Replace with the tier.
- L44 "the flagships sit at the edge of the unique-token supply" asserts as fact what is a modelled estimate.

---

## 5. Rigor list

### 5a. Numbers, venues, scales, or tiers inconsistent across sentences
1. L32: "82 sources: 39 A, 3 B, 17 C, 22 D." Sum is 81.
2. L69: "88 sources: 20 A, 1 B, 18 C, 47 D." Sum is 86.
3. L140: "85 of 89 sources: 30 A, 9 B, 25 C, 25 D." Sum is 89, the unverified total.
4. L205: "Twenty-one Tier B items" vs per-path Tier B counts summing to 23.
5. L34 "running Muon at 1.6 to 2.8 trillion parameters" and L56 "1.6T to 2.8T" vs L176 rank 1 "0.7T to 2.8T." GLM-5 (744B) runs MuonSplit per L36, so 0.7T is the accurate floor and L34 and L56 are wrong.
6. L34 Qiu et al. tested to 1.4B; L38 Dey et al. tested to "1.5 billion non-embedding"; table L58 says "1.9B"; rank 1 says "1.9B." The 1.9B figure has no support in the text.
7. L38: "from 2 to 128 layers ... larger saving at 179 layers."
8. L44 heading "ICLR 2026 orals" (plural) vs one ICLR 2026 oral in the body. Same at rank 19, L198: "A, ICLR 2026 orals" where only Gladstone is marked oral (L62).
9. L46 heading "below 1 billion parameters" vs body 8B (Nie) and 12B (Hatamizadeh) and table "8B / 1e23 FLOPs."
10. L46: "raises a 12-billion hybrid from 43 to 61" has no unit or benchmark.
11. L50: "Nemotron 3 Super is the first production model pretrained in NVFP4 ... (NVIDIA, 2026b)" vs L115: "Nemotron 3 Ultra pretrains in NVFP4 with under 0.4 percent loss gap ... (NVIDIA, 2026a)." Same claim, two models, two keys.
12. L69: "(NVIDIA, 2026b)" is Nemotron-Cascade 2; L50: "(NVIDIA, 2026b)" is Nemotron 3 Super.
13. L52 heading "peer-reviewed at 7 billion parameters" vs body "predicts loss at 8 billion parameters" (Shukor). Table L65 says 7B.
14. L71: "Three labs" vs L88 table "Kimi, DeepSeek, Zhipu, NVIDIA" and rank 6 "Four labs."
15. L101: "five such interventions validated between 8 and 1,000 billion parameters" vs table entries at 1.5B, 2B, 2.2B, 3B.
16. L142 "(Khatri et al., 2026, ICLR)" vs table L164 and rank 7 "ICLR oral." Text omits the oral status the tables assert.
17. L205: "ranks 3, 13, and 16 rest partly on undisclosed cells" vs Path 1 table marking ranks 13 and 16 "Absent."
18. L156 heading "measured at 3 to 8 billion parameters," table L171 "8B," closing sentence "rests on a 3-billion-parameter measurement." Which scale supports the frontier's rationale is left ambiguous.
19. L20: "tested and rejected at frontier scale" as a cell value vs L12's two-value rule and the plan's four values.
20. L176 rank 14: "Largest scale tested: 30B" under a Tier A column, but the 30B figure comes from the Tier D Ma et al. comparison (L113); the Tier A sources (Ren, Wu, Yuan) carry no stated scale. Ranking rule 2 ("tested above 30 billion") is also not met by 30B itself.
21. L109: table L124 "13B" credited to Nakamura (ICLR) and Liew (ICML), but the body attributes the 13B ceiling to "the Tier D evidence for that case."

### 5b. Citation keys that collide (same key, different papers) or split (same paper, different keys)
- "Chen et al., 2026, ICML" at L115 (W4A4 law) and L140 (on-policy forgetting) are different papers; "Chen et al., 2026, Tier C" at L48 is a third. No a/b/c suffixes.
- "Huang et al., 2026, ICLR" at L46 (joint-embedding) and L148 (challenger-solver) are different papers; "Huang et al., 2026, ACL Findings" at L146 is a third.
- "Zhao et al., 2026, ICML" at L75 (OPSD) and "Zhao et al., 2026, ICLR" at L152 (self-certainty), no suffixes.
- "Liu et al., 2026, ICML" at L52 and "Liu et al., 2026, ICLR" at L148, no suffixes.
- "Cao et al., 2025, Tier B" at L109 and "Cao et al., 2025, NeurIPS" at L121, no suffixes.
- "Li et al., 2026, ICLR" at L103 sits beside "Li et al., 2026a, ICML" (L36) and "Li et al., 2026b, Tier C" (L154): an unsuffixed key in a family that already uses suffixes.
- "Yu et al., 2025, NeurIPS" (DAPO, L101, L140) beside "Yu et al., 2025b, Tier B" (L152): "b" with no "a."
- "DeepSeek-AI, 2025" at L101 (V3.2) and "DeepSeek-AI, 2025, Nature" at L85 (R1), while L140 cites R1 as "Guo et al., 2025, Nature."
- "Zeng et al., 2026" (L18) and "GLM-5 Team, 2026" (L32 onward) for the GLM-5 report.

### 5c. Citations with no author key (unverifiable from the report)
- L44: "(Tier D)" for synthetic rephrasing at trillion-token scale.
- L77: "(Tier D, three independent studies)" and "(Tier D)" for the survey.
- L79: "(Tier D)" twice (pass@1024 study; pattern-only distillation).
- L81: "(Tier D, August 2026)" for token-share balancing.
- L83: "a Tier D study" for teacher-student compatibility.
- L109: "the Tier D evidence for that case."
- L111: "(Tier D)" for self-generated replay.
- L121: "(Tier D)" for post-hoc MTP heads.
- L123: "A Tier D study" for mid-training bounds.
- L144: "(ICLR 2026)" with no author, for intermediate-reasoning pass@k.
- L146: "(Tier D)" for the 4-percent-of-tokens result.
- L148: "(Tier D, August 2026)" for adaptive synthetic environments.
- L154: "in Tier D studies" for turn-level critics.

### 5d. Claims stated as fact on Tier C or D evidence without saying so in the sentence
- L10 and all of L18, L24, L26: the convergence claim and the recipe inventory rest on Tier C technical reports. The paragraph never says "Tier C." The plan (Section 4) requires the tier "in the sentence that states it." (The frontier register is Tier C by construction, so a single sentence establishing that convention at the top of Section 2 would satisfy the rule for the whole section.)
- L42: "The method is ByteDance's in-house practice." No source in the sentence.
- L73: "Every frontier consolidation stage distils within one model family **for that reason**." The reason is inferred from one Tier D workshop paper; no frontier report states it.
- L113: "the frontier consolidates by distillation rather than merging **for that reason**." Same inference from the same Tier D paper.
- L81: "The frontier's on-policy setting therefore avoids it by construction, which counts as implicit adoption." Inference presented as fact.
- L123: "GLM-5.3 **proves** that post-training alone moves a frontier base a long way." "Proves" on one Tier C release post.
- L140: "Fully asynchronous training ... runs Ant Group's trillion-parameter models (Fu et al., 2025, NeurIPS)." The deployment claim is Tier C (Ling reports), attributed here to a Tier A paper.
- L205: "small-model distillation results reverse between Qwen and Llama families." No body sentence supports this for distillation; L152 supports it for entropy-minimization RL.
- L73: "(Ma et al., 2026, ICML workshop, Tier D)." An ICML workshop paper carries a review signal; the plan's Tier D is "preprint with no review signal." Either the tier or the venue label is wrong.

---

## 6. Ten highest-value edits

1. **L101** (rule: Scoring Discipline, "Track structural promises"; checklist 15)
   Current: "The peer-reviewed record shows five such interventions validated between 8 and 1,000 billion parameters that no frontier recipe applies." ... "The five below define the gap."
   Proposed: "The peer-reviewed record shows ten such interventions, validated between 1.5 billion and one trillion parameters, that every frontier recipe omits." ... "The ten below define the gap."

2. **L69** (rule: structural promises; checklist 15)
   Current: "and the peer-reviewed literature now documents four properties of that method that no frontier report addresses."
   Proposed: "and the peer-reviewed literature now documents nine properties of that method, from its missing scaling law to its ordering against reinforcement learning, that every frontier report leaves unmeasured."

3. **L12 and L176** (rule 15; structural promise; also the missing matrix)
   Current (L12): "and the report ranks the graded gaps by the strength of their evidence and the size of the claimed gain."
   Proposed: "and the report ranks the graded gaps by evidence tier, by the largest scale tested, and by whether every disclosed flagship runs the stage." Then either insert the promised matrix as a table at the end of Section 2 (rows: the 38 methods; columns: Kimi K3, DeepSeek-V4, GLM-5/5.2/5.3, Nemotron 3; cells: disclosed / hinted / absent / undisclosed / tested-and-rejected), or rewrite L12 to say that the per-path "Frontier status" columns summarize the matrix, which lives in `references.md`.

4. **L32, L69, L140, L205** (rule 13, sound logic)
   Current: "82 sources ...: 39 ... 3 ... 17 ... 22" / "88 sources ...: 20 ... 1 ... 18 ... 47" / "85 of 89 sources ...: 30 ... 9 ... 25 ... 25" / "Twenty-one Tier B items"
   Proposed: recount from `references.md` so each tier line sums to its stated total and the Section 8 Tier B total equals the sum of the four path counts (currently 23).

5. **L201** (structural promise; checklist 15)
   Current: "Two gaps rank high for a reason beyond their evidence. Ranks 1 and 3 sit in pretraining ... Rank 2 sits where the frontier itself says it is blocked ..."
   Proposed: "Three gaps rank high for a reason beyond their evidence. Ranks 1 and 3 sit in pretraining, where a single run costs the most and an untested improvement compounds over the longest horizon. Rank 2 sits where the frontier itself says it is blocked, so the gap has a customer before it has a method."

6. **L209** (rule 10, consistent ordering; rule 15, parallel conclusion)
   Current: "it leaves parameterization-correct transfer, checkpoint merging, schedule choice, and memory layers on the peer-reviewed side of the line ... leaves expert pruning, layer-selected conversion, and merge-then-distil untried ... The rival reading, novelty by recency, would have surfaced the newest on-policy distillation variants and missed the NeurIPS 2025 result at 200 billion parameters that no flagship discloses."
   Proposed: "it leaves parameterization-correct transfer, schedule choice, checkpoint merging, and memory layers on the peer-reviewed side of the line ... leaves layer-selected conversion, expert pruning, and merge-then-distil untried ... The rival reading, novelty by recency, would have surfaced the newest on-policy distillation variants and missed the two NeurIPS 2025 results that rank first: a hyperparameter-transfer prescription that every flagship replaces with a heuristic, and a checkpoint-merging method at 200 billion parameters that every flagship leaves undisclosed." Also rename "Muon-class" to "Muon-family" to match L10, or change L10.

7. **L10** (rules 5, 9, 16; checklist 1, 9, 13)
   Current: "A method with strong evidence that every converged recipe omits is a gap with a specific address, and that address is the finding this report delivers."
   Proposed: "A method with Tier A evidence that every converged recipe omits is a gap with a specific address: the stage it belongs to, the scale at which peer review tested it, and the flagship that skipped it."

8. **L20** (rule 5, no announcing; checklist 1)
   Current: "Two negative results from the Kimi K3 report matter for the gap analysis. Under independent scaling-law searches for each schedule, cosine decay reached a lower final loss than warmup-stable-decay at every configuration tested, so the report adopts cosine as the default (Kimi Team, 2026, Section 3.2). Top-k on-policy distillation objectives gave no advantage in convergence speed or final performance over the per-token log-ratio reward, so the report keeps the simpler objective (Kimi Team, 2026, Section 4.1.3)."
   Proposed: "Under independent scaling-law searches for each schedule, cosine decay reached a lower final loss than warmup-stable-decay at every configuration tested, and Kimi K3 adopts cosine as its default (Kimi Team, 2026, Section 3.2). The per-token log-ratio reward matched top-k on-policy distillation objectives in convergence speed and final performance, and Kimi K3 keeps the simpler objective (Kimi Team, 2026, Section 4.1.3). Both results are Tier C and rest on one lab's runs. Each demotes an academic method from 'absent' to 'tested and rejected at frontier scale,' a fifth cell value the gap matrix records."

9. **L85 / L140, L18 / L32, L50 / L115** (rule 11, consistent terminology; rigor)
   Current: "(DeepSeek-AI, 2025, Nature)" and "(Guo et al., 2025, Nature)"; "(Zeng et al., 2026)" and "(GLM-5 Team, 2026)"; "Nemotron 3 Super ... (NVIDIA, 2026b)" and "Nemotron 3 Ultra ... (NVIDIA, 2026a)."
   Proposed: one key per source throughout, matching `references.md`: e.g., "(Guo et al., 2025, Nature)" for R1 in both places; "(GLM-5 Team, 2026)" at L18; and one Nemotron model name for the NVFP4 pretraining claim with one key. Add a/b/c suffixes to Chen 2026, Huang 2026, Zhao 2026, Liu 2026, Cao 2025, Li 2026, and Yu 2025.

10. **L77** (rule 6, affirmative construction; checklist 7)
    Current: "The peer-reviewed side has the diagnosis at small scale. The frontier side has the deployment at large scale. Neither has the cure."
    Proposed: "The peer-reviewed side holds the diagnosis at small scale. The frontier side holds the deployment at large scale. The remedy awaits both." Apply the same conversion at L148 ("Neither has run the other" → "Each side awaits the other's trial"), L142 ("Neither report fits an asymptote" → "Both reports leave the asymptote unfitted"), and L152 ("Partial credit is absent at every lab" → "Every lab scores in binary").

---

## Closing note for the author

The argument is real and the bold-headline gap paragraphs are the strongest structural idea in the document. What holds the score at 7.0 is arithmetic and promise-keeping, plus the negative register that the subject invites but the standard forbids. Fix the counts, either show the matrix or stop promising it, unify the citation keys, and run one affirmative-construction pass, and the section level will clear 8.5 with the rest of the document following.
