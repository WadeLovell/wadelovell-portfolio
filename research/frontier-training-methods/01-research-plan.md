# Research Plan: Identifying Unexplored Methods for Training Frontier Models

**Author:** B. Wade Lovell
**Prepared:** September 5, 2026
**Evidence window:** December 31, 2024 through September 5, 2026
**Companion documents:** `02-research-report.md` (findings), `references.md` (sources with review status), `search-log.md` (audit trail)

## 1. Thesis

An unexplored training method is a method that carries peer-reviewed evidence at academic scale and appears in no frontier training recipe. That definition turns novelty into a measurable property of two registers. The first register records what peer-reviewed and submitted research has validated, at what scale, and with what gain. The second register records what frontier technical reports disclose about their own recipes. The gap between the registers is the deliverable. The usual rival, a method-first survey, catalogues academic proposals and leaves the frontier side unmapped, so it mistakes "recently proposed" for "unexplored." The register method corrects that error by treating frontier technical reports as primary evidence of adoption and by grading each academic method on the largest scale at which anyone has tested it.

## 2. Scope

Four training paths define the study. Each path takes a starting checkpoint and a class of interventions.

| Path | Starting point | Interventions in scope | Reference models |
|---|---|---|---|
| 1. From scratch | Random initialization | Architecture, optimizer, parameterization, data, objective, precision, schedule, mid-training | Kimi K3 (2.8T MoE, July 2026), GLM-5 (744B MoE, February 2026) |
| 2. From or through distilled models | A teacher's outputs, logits, or hidden states | On-policy distillation, reasoning-trace distillation, multi-teacher merging, distilled checkpoints as bases for further training | GLM-5.2's on-policy distillation merge of more than ten expert models; Kimi K3 where its report discloses distillation |
| 3. From leading open-weights models | A released base checkpoint | Continued pretraining, architecture conversion, upcycling, growth, merging, long-context extension, reinforcement learning on the base | GLM-5.2 (June 2026), Kimi K3 (weights July 27, 2026), DeepSeek-V4, Qwen3 family |
| 4. From existing frontier models | A frontier post-trained checkpoint | Reinforcement learning with verifiable rewards, policy-gradient variants, asynchronous and agentic RL, reward modelling, self-improvement, effort control, continual learning, alignment | GLM-5.3 (same base as GLM-5.2, gains from post-training alone), Kimi K3 post-training, frontier system cards |

A frontier model is a model that a technical report places in the top open or proprietary tier on at least one of the coding, agentic, or reasoning suites during the window. A frontier recipe is the training pipeline that a technical report or model card discloses for such a model.

## 3. Grades of "unexplored"

Each gap receives one of four grades. The grade states the evidence that exists and the evidence that is missing.

- **G1, proposed and untested at scale.** Peer-reviewed evidence exists below 10B parameters or 1T tokens. No report at or above that scale exists.
- **G2, validated at scale and absent from frontier recipes.** Evidence exists at or above 10B parameters or 1T tokens from an academic group or a mid-tier lab. Every frontier report in the register omits the method.
- **G3, named open problem.** A limitations section, a future-work section, or a survey states the question as open. No method with evidence exists.
- **G4, untested combination.** Two adopted methods interact in a way that no report evaluates.

A method earns a grade only after the frontier register confirms absence. Absence in a report is weaker evidence than presence, since labs withhold detail. Section 9 states how the plan handles that asymmetry.

## 4. Evidence tiers

The user's standard is academic rigor, with peer-reviewed research first and submitted research second. Four tiers implement that standard.

- **Tier A, peer-reviewed and published.** Main tracks of NeurIPS 2025, ICML 2025 and 2026, ICLR 2025 and 2026, ACL, EMNLP, NAACL, COLING, COLM 2025 and 2026, AISTATS; journals including TMLR, JMLR, the Nature and Science families, IEEE and ACM transactions, and Wiley titles. Evidence: a proceedings URL, an ACL Anthology URL, an OpenReview "Published" venue line, a DOI, or an arXiv comments line naming the acceptance.
- **Tier B, submitted and under review.** An arXiv comments line reading "under review" or "submitted to," an OpenReview submission with visible reviews, or a NeurIPS 2026 submission. NeurIPS 2026 notifications arrive September 24, 2026, so every NeurIPS 2026 submission holds Tier B on the execution date. ICLR 2027 submissions close September 25, 2026, so none is public.
- **Tier C, industrial technical report or model card.** Primary evidence of frontier adoption. Tier C sources populate the frontier register and never substitute for Tier A or B evidence of a method's validity.
- **Tier D, preprint with no review signal.** Retained only when it is the primary statement of a method that matters to a path, and labelled as such in every citation.

Every claim in the report carries a tier. A finding that rests on Tier C or D evidence alone says so in the sentence that states it.

## 5. Sources and channels

The execution environment reaches scholarly sources through three working channels and blocks four.

| Channel | Reach | Use |
|---|---|---|
| Exa semantic search and fetch | arXiv abstract and HTML pages, NeurIPS and PMLR proceedings, ACL Anthology, lab blogs, GitHub | Candidate discovery, full-text mining of reference lists, verification of every arXiv item |
| Web search with domain filters | openreview.net, arxiv.org, proceedings.neurips.cc, proceedings.mlr.press, aclanthology.org, colmweb.org, jmlr.org, nature.com | Venue sweeps and acceptance-status confirmation |
| Scholar Gateway | Full text of Wiley journals | Peer-reviewed journal coverage |
| Blocked | Direct arXiv API, OpenReview API, Semantic Scholar API, OpenAlex, Hugging Face | Recorded in the search log as a coverage limit |

The blocked channels remove programmatic enumeration of venues. The plan compensates with domain-filtered venue sweeps, with snowballing from the reference lists of frontier reports, and with verification of every item against its primary page.

## 6. Search protocol

The protocol runs seven steps. Steps 1 through 4 run once per path, in parallel across the four paths.

1. **Seed terms.** Each path starts from a list of method families (Appendix A). Each family yields at least two semantic queries phrased as full descriptions of the ideal paper.
2. **Venue sweeps.** Each family runs once against OpenReview, once against arXiv, and once against the proceedings sites, with the domain filter set.
3. **Snowballing.** Backward: the reference lists of Kimi K3 (arXiv 2607.24653), GLM-5 (arXiv 2602.15763), IndexCache (arXiv 2603.12201), DeepSeek-R1 (Nature, 2025), DAPO (arXiv 2503.14476), and "Muon is Scalable for LLM Training" (arXiv 2502.16982) supply the 2025 and 2026 methods that frontier authors themselves cite. Forward: the foundational papers of each family (Muon, GRPO, DeepSeek Sparse Attention, generalized knowledge distillation) supply their 2025 and 2026 successors.
4. **Verification.** Every candidate is confirmed against its arXiv abstract page, proceedings page, or journal page before it enters the register. The record carries the identifier, title, first author, affiliation, first and latest version dates, tier, quoted tier evidence, venue, one-sentence method, largest scale tested, headline claim, path relevance, and known frontier adoption. An identifier never enters the register from memory.
5. **Frontier register.** Section 7 lists the models and fields. Every non-empty cell carries a quoted phrase and a source URL.
6. **Gap matrix.** Rows are methods with Tier A or B evidence. Columns are frontier models. Cells read "disclosed," "hinted," "absent," or "undisclosed." A method with an "absent" or "undisclosed" cell in every frontier column is a gap candidate.
7. **Grading and write-up.** Each gap candidate receives a grade from Section 3, a statement of the strongest evidence for the method, a statement of the largest scale tested, and a statement of the reason the report judges it unexplored.

## 7. Frontier register

The register covers every open-weights and proprietary model in the window whose report discloses training detail. Open-weights entries: Kimi K2, K2 Thinking, K2.5, and K3; DeepSeek-V3.1, V3.2-Exp, V3.2, V4, and R1; GLM-4.5, 4.7, 5, 5.1, 5.2, and 5.3; the Qwen3 family; MiniMax M1 through M3; Llama 4; gpt-oss; Gemma 3, 3n, and later; Mistral Large 3 and Magistral; Nemotron 3; OLMo 3; SmolLM3; Apertus; LongCat-Flash; Ling 2.0; Step-3; MiMo; Hunyuan; Seed-OSS; Granite 4; Falcon H1; Phi-4 reasoning; Apple Foundation Models. Proprietary entries rest on system cards and release posts: OpenAI o3, GPT-5, 5.5, and 5.6; Anthropic Claude 4.x, Opus 4.7 and 4.8, and Fable 5; Google Gemini 2.5, 3, and Diffusion; xAI Grok 4 and 5.

Fields per model: release date; total and active parameters; architecture family; attention variant; routing and balancing; position encoding; multi-token prediction; optimizer; pretraining tokens; precision and quantization-aware training; context-extension curriculum; mid-training stage; distillation use and teacher; SFT description; RL algorithms named; reward sources; asynchronous or off-policy design; agentic environment scale; reasoning-effort control; model or expert merging; cross-stage distillation; disclosed ablations; explicit non-disclosures; peer-reviewed version.

## 8. Screening criteria

A candidate enters the register when it meets four conditions. Its first public date falls inside the window. It changes how a language model of at least 1B parameters is trained, or it supplies theory with language-model experiments. Its primary source is reachable. It reports a measurable effect or a stated open problem.

A candidate stays out when it changes inference alone, prompting alone, or evaluation alone; when it applies a model to a downstream domain; or when it reports results below 1B parameters with no scaling argument. Baseline papers from before the window enter only as labelled baselines.

## 9. Threats to validity and their controls

**Non-disclosure.** Frontier labs omit detail, so absence from a report is weak evidence of non-adoption. Control: the gap matrix separates "absent" (the report describes the relevant stage and omits the method) from "undisclosed" (the report says nothing about the stage). A gap graded on "undisclosed" cells alone is reported as provisional.

**Recency.** NeurIPS 2026 decisions and COLM 2026 and EMNLP 2026 camera-ready lists are pending on the execution date. Control: Tier B labels, with the decision dates stated, so the reader can re-grade after September 24, 2026.

**Channel bias.** Semantic and web search rank by popularity, which favors work from large labs. Control: domain-filtered venue sweeps and reference-list snowballing, which surface work by citation rather than by traffic.

**Disclosure asymmetry across labs.** Chinese open-weights labs disclose recipes in detail; United States labs disclose less. The adoption matrix therefore over-represents the former. Control: the report names this asymmetry wherever it affects a grade.

**Single-session execution.** The sweep ran on one date with one set of tools. Control: the search log records every query, channel, and count, so a later run can measure drift.

## 10. Deliverables

1. `01-research-plan.md`: this document.
2. `02-research-report.md`: the findings, organized as one argument across the four paths, with the gap matrix and graded gaps.
3. `references.md`: every source with identifier, tier, tier evidence, and venue.
4. `search-log.md`: every query, channel, hit count, and verification outcome, plus the coverage limits.

## 11. Execution order

Steps 1 through 4 ran in parallel across the four paths on September 5, 2026, alongside the frontier register. The gap matrix and grading followed. The report, references, and log closed the run. The conclusion of the report returns to the thesis: the unexplored methods are the ones with peer-reviewed evidence and no frontier adoption, and the two registers make that set explicit.

## Appendix A. Seed method families by path

**Path 1, from scratch.** Optimizers (Muon and Per-Head Muon, Shampoo and SOAP, PSGD, Dion, MARS, AdEMAMix, cautious updates, spectral steepest descent, Newton-Schulz scaling); hyperparameter transfer (muP, CompleteP, u-muP, depth transfer, telescoping sweeps); schedules and batch scaling (warmup-stable-decay, critical batch size, weight-decay scaling); scaling laws (MoE sparsity, data-constrained, precision-aware, hybrid attention); architecture (Kimi Delta Attention, Gated DeltaNet, Mamba-3, RWKV-7, Lightning Attention, NSA, MoBA, DeepSeek Sparse Attention, IndexShare, Attention Residuals, hyper-connections, memory layers, latent MoE, aux-loss-free and Quantile Balancing, multi-token prediction, NoPE, looped and recurrent-depth transformers, mixture of depths); objectives and data (reinforcement pretraining, diffusion language models, energy-based objectives, synthetic and rephrased corpora, data-mixing laws, curricula, quantization-aware pretraining, checkpoint averaging).

**Path 2, distillation.** On-policy distillation and its variants (cross-stage, entropy-aware, dual, self-distillation, weak-to-strong); objectives (reverse KL, JSD, concrete score matching, speculative distillation, cross-tokenizer logit distillation, feature distillation, MoE-to-dense); reasoning-trace distillation (R1 distills, s1, LIMO, OpenThoughts, distillation scaling laws, teacher hacking); frontier distillation routes (Gemma from Gemini, Llama 4 codistillation, Minitron, Qwen3 strong-to-weak, Phi-4, Apple); distilled bases for further training; theory (sample complexity, dense-reward interpretation, teacher selection).

**Path 3, open-weights bases.** Continued and mid-training recipes; architecture conversion (dense-to-sparse attention, softmax-to-linear or hybrid conversion, post-hoc multi-token prediction, memory layers); growth and upcycling (sparse and drop upcycling, expert expansion, depth up-scaling, width growth); merging (task arithmetic successors, evolutionary merging, merging RL checkpoints); pruning plus distillation; long-context extension; RL on open bases at scale; tokenizer transplantation, quantization-aware continued training, low-rank continued training.

**Path 4, post-training.** RL with verifiable rewards and policy-gradient variants (GRPO, DAPO, Dr. GRPO, GSPO, GMPO, CISPO, VAPO, BAPO, critic-based PPO for compacted trajectories, ProRL); entropy and exploration; RL scaling laws; asynchronous and agentic RL (AReaL, slime, staleness correction, train-inference mismatch correction, persistent sandboxes, multi-turn credit assignment); reward signals (generative reward models, rubrics, process rewards, verifier-free rewards); self-improvement and self-play; effort control and test-time training; continual learning under post-training; alignment methods that double as capability methods; frontier disclosures.
