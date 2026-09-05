# Search Log

Execution date: September 5, 2026 (UTC). Window: December 31, 2024 through September 5, 2026. Every query below ran through one of the channels named in Section 5 of the research plan. "Kept" counts the hits that entered a sweep register after verification against a primary page.

## Coverage limits recorded during execution

- Direct access to the arXiv API, the OpenReview API, the Semantic Scholar API, OpenAlex, and Hugging Face was blocked by the session's egress policy. arXiv abstract and HTML pages were reached through Exa fetch. OpenReview content was reached only through domain-filtered web-search snippets and PDF links, so acceptance status for some OpenReview submissions could not be confirmed and those items hold Tier B.
- Scholar Gateway indexes Wiley journals only. Four queries (on-policy distillation; pretraining methods; RLVR and self-improvement; knowledge distillation theory) returned 45 Wiley articles, of which one review (WIREs Computational Statistics, October 2025) was on-path. Peer-reviewed evidence for frontier training methods in the window lives in conference proceedings and in Nature, and the sweeps sourced it from proceedings.neurips.cc, proceedings.mlr.press, aclanthology.org, iclr.cc, icml.cc, colmweb.org, and nature.com through Exa and domain-filtered search.
- NeurIPS 2026 notifications are due September 24, 2026, and the ICLR 2027 deadline is September 25, 2026, so no NeurIPS 2026 acceptance and no ICLR 2027 submission was observable. Items carrying "under review" on arXiv hold Tier B.
- The Kimi K3 arXiv HTML page was fetched in full (200,000 characters) and mined for Sections 3.2, 4.1, 4.2, 5.3, and 8. The GLM-5.2 and GLM-5.3 release posts were fetched in full. The DeepSeek-V4 report was read through its arXiv HTML highlights and the Hugging Face model card.
- Four sweep items were kept with verified=no because two fetch attempts failed (2601.05607; 2604.15804; 2603.09938; the ICLR 2026 CoT-Pass@K poster). One Path 3 item, Foreign Sparse Attention, exists only on OpenReview and holds Tier B unverified.
- Wide search returned no Tier A evidence for Muon-class optimizers or maximal-update transfer above roughly 4 billion dense parameters outside lab reports, no Tier A comparison of diffusion or energy-based objectives against autoregressive training above 1e23 FLOPs, and no Tier A long-context extension study above 8 billion parameters.

## Orchestrator queries

| # | Channel | Query or URL | Outcome |
|---|---|---|---|
| 1 | WebSearch | Moonshot AI Kimi K3 model release 2026 | K3 released 2026-07-14/16; weights 2026-07-27; 2.8T MoE |
| 2 | WebSearch | Zhipu GLM-5.2 open weights model release 2026 | GLM-5.2 launched 2026-06-13; ~744B MoE; MIT license |
| 3 | curl | export.arxiv.org API, api.openalex.org, api.semanticscholar.org, api2.openreview.net | All blocked by egress proxy |
| 4 | WebFetch | huggingface.co model cards, arxiv.org/abs, openreview.net | All blocked by egress proxy |
| 5 | Exa search | Kimi K3 technical report arXiv | arXiv 2607.24653 confirmed; GitHub MoonshotAI/Kimi-K3; kimi.ai blog 2026-07-14 |
| 6 | Exa search | GLM-5.2 technical report | GLM-5 arXiv 2602.15763; IndexCache arXiv 2603.12201; z.ai/blog/glm-5.2 (2026-06-16) |
| 7 | Scholar Gateway | on-policy distillation methods 2025-2026 | 8 Wiley articles; none on OPD; corpus is Wiley journals only |
| 8 | Exa fetch | arxiv.org/abs/2607.24653 | Reachable through Exa; abstract confirmed |
| 9 | Exa fetch | api2.openreview.net, openreview.net/group | Browser check page; OpenReview reachable only through WebSearch snippets |
| 10 | WebSearch (openreview.net) | on-policy distillation language model ICLR 2026 | 4 OpenReview items + 6 arXiv items (2604.00626, 2606.07082, 2606.30626, 2607.05394, 2605.01749) |
| 11 | Exa search | NeurIPS 2025 accepted paper pretraining optimizer Muon scaling laws | 2502.16982; NeurIPS 2025 "Hyperparameter Transfer Enables Consistent Gains of Matrix-Preconditioned Optimizers Across Scales"; 2606.04058; 2505.02222 |
| 12 | WebSearch | ICLR 2027 deadline, NeurIPS 2026 notification | ICLR 2027 full paper deadline 2026-09-25; NeurIPS 2026 notifications 2026-09-24 |
| 13 | Exa search | DeepSeek-V4 technical report | arXiv 2606.19348 (2026-04-24/26); 1.6T/49B; CSA+HCA; mHC; Muon; 32-33T tokens; FP4 QAT; experts then OPD consolidation |
| 14 | Exa search | GLM-5.3 release same base as GLM-5.2 | z.ai/blog/glm-5.3 (2026-08-14): same base, gains from post-training; SAO with compaction; slime; OPD variants; R3-style consistency |
| 15 | Exa fetch | arxiv.org/html/2607.24653v1 | Full K3 report text saved for mining |
| 16 | WebSearch (arxiv.org) | "under review" NeurIPS 2026 frontier training | NVFP4 pretraining (2509.25149) surfaced; no explicit under-review labels in snippets |
| 17 | Exa fetch | arxiv.org/html/2607.24653v1 (full, 200K chars) | Sections 3.2, 4.1, 4.2, 5.3, 8 mined; two negative results recorded (WSD vs cosine; top-k OPD) |
| 18 | Exa fetch | z.ai/blog/glm-5.2, z.ai/blog/glm-5.3 | IndexShare, MTP TV loss, critic-based PPO with compaction, anti-hack module, parallel OPD merge; GLM-5.3 same base, environment-synthesis open problem quoted |
| 19 | Scholar Gateway | novel pretraining methods for LLMs 2025-2026 (optimizers, sparse attention, MoE, scaling laws) | 13 Wiley articles; zero primary method papers on frontier pretraining; corpus limit recorded |
| 20 | Scholar Gateway | RLVR, GRPO variants, self-improvement post-training 2025-2026 | 12 Wiley articles; zero primary method papers; corpus limit recorded |


## Path 1, from scratch

- Exa search | Hyperparameter Transfer Enables Consistent Gains of Matrix-Preconditioned Optimizers Across Scales NeurIPS 2025 arxiv | 1
- Exa search | Fantastic pretraining optimizers and where to find them Marin Stanford arxiv benchmark | 1
- Exa search | Benchmarking optimizers for large language model pretraining arxiv 2025 | 1
- Exa fetch | arxiv abs 2607.24653, 2602.15763, 2603.12201, 2502.16982 (seeds) | 4
- Exa fetch | arxiv html 2607.24653, 2602.15763, 2603.12201, 2502.16982 (reference mining; K3/GLM-5 html carry no arXiv IDs in references; Muon-is-Scalable references yielded 2502.07529 and MARS 2411.10438) | 1
- Exa search | Dion distributed orthonormalized updates | 2
- Exa search | Per-Head Muon optimizer attention heads 2026 | 2
- Exa search | Polar Express optimal matrix sign Newton-Schulz Muon | 1
- Exa search | CompleteP depth hyperparameter transfer | 1
- Exa search | Power Lines scaling laws weight decay batch size Cerebras | 1
- Exa search | multi-power law learning rate schedule ICML 2025 | 1
- Exa search | Training deep learning models with norm-constrained LMOs Scion | 1
- Exa search | Kimi Linear Kimi Delta Attention | 1
- Exa search | Attention Residuals Kimi 2026 | 1
- Exa search | Parameters vs FLOPs optimal sparsity MoE Apple | 1
- Exa search | Farseer refined scaling law StepFun | 1
- Exa search | Native Sparse Attention DeepSeek ACL 2025 | 1
- Exa search | mHC manifold-constrained hyper-connections | 1
- Exa search | Engram conditional memory scalable lookup DeepSeek | 1
- Exa search | Latent MoE NVIDIA Nemotron | 3
- Exa search | Quantile Balancing MoE routing 2026 | 1
- Exa search | Mamba-3 ICLR 2026 | 1
- Exa search | RWKV-7 Goose | 1
- Exa search | LLaDA large language diffusion models | 1
- Exa search | Reinforcement Pre-Training RPT Microsoft | 1
- Exa search | Pretraining LLMs with NVFP4 | 1
- Exa search | Scaling law for quantization-aware training | 1
- Exa search | Scaling laws for optimal data mixtures Meta/Apple | 1
- Exa search | Pre-training under infinite compute Stanford | 1
- Exa search | Diffusion beats autoregressive data-constrained | 1
- Exa search | Scaling latent reasoning looped language models Ouro | 1
- Exa search | Gated attention non-linearity sparsity attention-sink-free Qwen | 1
- Exa search | Predictable Scale Part I Step Law | 1
- Exa search | Cautious optimizers ICML 2025 | 1
- Exa search | NorMuon | 1
- Exa search | Practical efficiency of Muon Essential AI | 1
- Exa search | Muon optimizes under spectral norm constraints | 1
- Exa search | Kimi K2 MuonClip | 1
- Exa search | Scaling collapse supercollapse ICML 2025 | 1
- Exa search | Straight to Zero linear decay to zero ICLR 2025 | 1
- Exa search | MoBA mixture of block attention | 1
- Exa search | DeepSeek-V3.2 DSA technical report | 1
- Exa search | IndexShare sparse attention shared indexer 2026 | 1
- Exa search | multi-token prediction pretraining 2025 from scratch | 3
- Exa search | NoPE Rope to Nope hybrid position encoding 2025 | 1
- Exa search | Hybrid architectures for language models systematic analysis Meta | 2
- Exa search | Scaling laws for floating-point quantization training | 1
- Exa search | Quartet native FP4 training NeurIPS 2025 | 1
- Exa search | Distillation scaling laws Busbridge | 1
- Exa search | BeyondWeb synthetic data DatologyAI | 1
- Exa search | Model merging in pre-training ByteDance PMA | 1
- Exa search | BitNet b1.58 2B4T | 1
- Exa search | JEPA / energy-based LM objectives 2025-2026 | 2
- Exa search | midtraining bridges pretraining and posttraining; mid-training schedules | 2
- Exa search | Efficiency Leverage MoE scaling laws Ant | 1
- Exa search | Dream 7B diffusion LLM | 1
- Exa search | Mercury diffusion LLM Inception Labs | 1
- Exa search | survey of optimizers for LLM pretraining 2025-2026 | 3
- Exa search | fully asynchronous pipeline parallelism pretraining 2025-2026 | 2
- Exa search | 1M-token context training recipe Qwen2.5-1M UltraLong | 2
- Exa search | Demons in the Detail global-batch load balancing ACL 2025 | 1
- Exa search | Joint MoE scaling laws Ludziejewski ICML 2025 | 1
- Exa search | survey of diffusion language models 2025 | 2
- Exa search | Quantile Balancing arXiv paper dual bias (found blogs + Megatron PR only) | 1
- Exa search | Energy-Based Transformers Gladstone 2025 | 1
- Exa search | RLP Reinforcement as a Pretraining Objective NVIDIA | 1
- Exa fetch | arxiv abs verification batches (14 batches, 70 IDs) - all resolved with title/first author/date | 70
- Exa fetch | arxiv abs 2505.22757, 2502.05172, 2501.11873, 2508.10875, 2507.02092, 2506.13759, 2510.01265 | 7
- Exa fetch | kexue.fm/archives/11619 (Quantile Balancing blog) - CRAWL TIMEOUT; item kept as verified=no | 0
- WebSearch openreview/neurips | Benchmarking Optimizers NeurIPS 2025 D&B status (submission only) | 1
- WebSearch openreview/neurips | Polar Express venue (ICLR 2026 confirmed) | 1
- WebSearch openreview/neurips | Muon spectral norm constraints venue (NeurIPS 2025 OPT workshop) | 1
- WebSearch openreview/iclr | Ouro ICLR 2026 (not confirmed) | 0
- WebSearch openreview/iclr | Hybrid Architectures Meta ICLR 2026 (submission only) | 1
- WebSearch openreview/colmweb | RWKV-7 COLM 2025 (confirmed) | 1
- WebSearch openreview/neurips | Step Law venue (OpenReview attachment only) | 1
- WebSearch openreview/icml | Scaling Law for QAT ICML 2026 (confirmed poster) | 1
- WebSearch openreview/icml | mHC ICML 2026 (not confirmed) | 0
- WebSearch openreview | Dion venue (none) | 0
- WebSearch openreview/iclr | Kimi Linear venue (none) | 0
- WebSearch openreview | Practical Efficiency of Muon venue (none) | 0
- WebSearch openreview | RPT venue (none; surfaced RLP ICLR 2026) | 1
- WebSearch openreview/iclr | NVFP4 venue (none) | 0
- WebSearch openreview | Systematic Analysis of Hybrid Linear Attention venue (none) | 0
- WebSearch openreview/neurips | Titans venue (NeurIPS 2025 confirmed) | 1
- WebSearch openreview/iclr | Energy-Based Transformers venue (ICLR 2026 oral confirmed) | 1
- WebSearch icml/openreview | Group Muon ICML 2026 (icml.cc virtual page found in Exa; WebSearch inconclusive) | 1
- Scholar Gateway (Wiley) | Optimizers/parameterizations/scaling laws for LLM pretraining from scratch, 2025-2026, topN 10 - 10 results, none about from-scratch pretraining methods (classification scaling law, medical summarization, fine-tuning reviews) | 0


## Path 2, distillation

- Exa search | arXiv OPD student samples own trajectories teacher per-token reverse KL | 10 | 8
- Exa search | Thinking Machines 'On-Policy Distillation' Kevin Lu | 5 | 1
- Exa search | Distillation scaling laws Busbridge Apple | 5 | 1
- WebSearch arxiv.org | on-policy distillation language model 2026 | 9 | 6
- WebSearch openreview.net | on-policy distillation LLM ICLR 2026 | 9 | 5
- Exa fetch | abs+html of 2607.24653, 2602.15763, 2604.00626 (seeds); full html mined for 'distill' and reference entries | 3 | 3
- Exa search | GLM-5.2 parallel OPD merging expert models | 8 | 2
- Exa search | Qwen3 strong-to-weak distillation | 5 | 1
- Exa search | Gemma 3 distillation from teacher pretraining sampled logits | 5 | 1
- Exa search | Llama 4 codistillation Behemoth | 5 | 1
- Exa search | NVIDIA Nemotron/Minitron pruning distillation 2025 | 8 | 2
- Exa search | Kimi K2.5 report distillation | 5 | 1
- Exa search | DeepSeek-V4 distillation specialists | 6 | 1
- Exa search | Apple Foundation Models 2025 distillation | 5 | 1
- Exa search | Phi-4-reasoning o3-mini traces | 5 | 1
- Exa search | teacher hacking distillation | 5 | 1
- Exa search | speculative knowledge distillation | 5 | 1
- Exa search | cross-tokenizer / universal logit distillation 2025 | 8 | 1
- Exa search | concrete score matching distillation | 5 | 1
- Exa search | MoE into dense / smaller MoE distillation 2025 | 8 | 3
- Exa search | long CoT distillation failure modes small models | 8 | 2
- Exa search | distilled models as RL starting points | 8 | 3
- Exa search | theory sample complexity distillation vs RL dense reward | 8 | 4
- Exa search | entropy-aware on-policy distillation | 6 | 1
- Exa search | 'Rethinking Large Language Model Distillation' ICLR 2026 | 6 | 1
- Exa search | Nemotron 3 Ultra MOPD | 6 | 1
- Exa search | Gemma 3n distillation | 5 | 0
- Exa search | Magistral distillation SFT then RL | 5 | 1
- Exa search | Apple Foundation Models 2026 distillation | 5 | 0
- Exa search | OPD as RL with dense reward theory | 8 | 3
- Exa search | RL on DeepSeek-R1-Distill vs base | 8 | 2
- WebSearch openreview.net | distillation LLM reasoning ICLR 2026 accepted | 10 | 1
- WebSearch neurips.cc | knowledge distillation language models NeurIPS 2025 | 10 | 2
- WebSearch aclanthology.org | distillation reasoning LLM 2025 | 10 | 1
- WebSearch proceedings.mlr.press | distillation language model ICML 2025/2026 | 9 | 2
- Scholar Gateway (Wiley) | how KD transfers reasoning to smaller LLMs, 2025-2026, topN 10 | 10 | 1
- Exa search | DeepSeek-V3.2 specialist distillation | 5 | 1
- Exa search | Qwen3.5 report on-policy distillation | 5 | 1
- Exa search | Sky-T1 blog | 3 | 1
- Exa search | distillation ceiling / capability ceiling OPD 2026 | 6 | 4
- Exa search | continued pretraining / growth from distilled checkpoint | 6 | 0
- WebSearch venues | s1 / LIMO / Small Models Struggle venue | 9 | 2
- WebSearch venues | OpenThoughts / RL vs Distillation / SFT Memorizes venue | 9 | 1
- WebSearch openreview | Self-Distilled Reasoner venue | 10 | 1
- WebSearch openreview+arxiv | OPD NeurIPS 2026 under review | 8 | 2
- Exa fetch | abs pages, 12 batches of <=5 (about 75 IDs) for verification | 75 | 75
- Exa fetch | html of 2602.02276 (Kimi K2.5) and 2601.02780 (MiMo-V2-Flash) mined for 'distill'/'MOPD' | 2 | 2
- Exa search | Nemotron-Cascade 2 | 5 | 1
- WebSearch venues | LIMO COLM 2025; Small Models ACL; OpenThoughts ICLR 2026; Minitron-SSM NeurIPS 2025; CSD ICLR 2026; Llama-Nemotron / Unveiling key factors | 6 | 6
- WebSearch icml.cc / iclr.cc | distillation posters ICML 2026 and ICLR 2026 | 2 | 6
- Exa search | MOPD paper arXiv; pi-Distill arXiv; Residual-learning KD ICLR 2026 | 3 | 3
- Exa fetch | z.ai/blog/glm-5.2; icml.cc pages for MOPD, pi-Distill, OPSD | 4 | 4
- WebSearch | COLM 2026 distillation; Valley of Code Reasoning; RLVR vs Distillation venue | 3 | 1

Blocked hosts were not retried. OpenReview forum pages return a browser check; venue lines were taken from WebSearch snippets and icml.cc/iclr.cc/aclanthology/PMLR pages.


## Path 3, open-weights bases

- Exa fetch | arxiv abs 2602.15763, 2603.12201 | 2
- Exa search | DeepSeek-V3.2 technical report DSA warm-up CPT from V3.1-Terminus | 1 (2512.02556)
- Exa search | OLMo 3 technical report mid-training Dolmino Think RLVR | 1 (2512.13961)
- Exa search | Nemotron 3 technical report hybrid Mamba MoE open recipe | 3 (2512.20856, 2604.12374, Ultra PDF)
- Exa search | GLM-5.3 release same base as GLM-5.2 post-training gains | 1 (Z.ai blog) + GitHub README fetch
- WebSearch openreview | continued pretraining replay ratio LR rewarming forgetting 2025 | 3 (2603.16177, 2605.26097, 2503.05029)
- WebSearch openreview | sparse upcycling drop-upcycling ICLR 2025 | 3 (2502.19261, 2503.01359, 2606.16456)
- WebSearch openreview | linearizing pretrained transformers LoLCATs Liger RADLADS | 4 (2505.03005, 2504.14366, 2603.15590, KL-guided)
- WebSearch openreview | model merging task arithmetic TIES evolutionary 2025 2026 | 3 (2512.10772, 2602.08218, 2502.10339)
- WebSearch openreview | Minitron pruning distillation MoE experts | 2 (2605.08738, 2603.11881)
- WebSearch openreview | long context extension 128K 1M YaRN curriculum | 3 (2504.06214, 2604.14339, 2502.17129)
- WebSearch openreview | ProRL DAPO AReaL RLVR open-weights | 2 (2505.24864, 2510.01180)
- WebSearch openreview | tokenizer transplantation vocabulary adaptation | 4 (2505.09738, 2506.06607, 2605.13429, 2505.20133)
- Exa search | Jet-Nemotron PostNAS | 1 (2508.15884, NeurIPS 2025 proceedings)
- Exa search | post-hoc multi-token prediction heads gated LoRA | 1 (2507.11851) + negative-result note (2502.09419)
- Exa search | RoPE to NoPE / SWAN-GPT conversion | 2 (2504.08719, 2501.18795)
- Exa search | depth up-scaling layer stacking model growth 2025 | 4 (2502.13794, 2510.08008, 2508.08011, 2511.04981)
- Exa search | merging RL checkpoints, merging scaling laws | 6 (2509.24244, 2607.22039, 2607.16062, 2505.10833, 2602.12566, 2601.13572 not kept)
- Exa search | expert pruning and merging REAP | 1 (2510.13999)
- Exa search | retrofitting MLA into GQA models | 2 (2502.07864, 2502.14837)
- Exa search | QAT scaling laws ParetoQ Kimi K2 Thinking | 3 (2502.02631, 2505.14302, 2509.22935)
- Exa search | LoRA at scale, LoRA without regret | 1 kept (blog); NeurIPS 2025 LoRA papers noted as baselines
- Exa search | DAPO / AReaL / OpenThoughts | 3 (2503.14476, 2505.24298, 2506.04178)
- Exa search | openly licensed pretraining as constraint Common Pile Apertus | 2 (2506.05209, 2509.14233)
- Exa search | post-hoc memory / retrieval layers | 2 (2508.09874, 2604.05248)
- Exa search | expert expansion / upcycling into hybrid | 2 (2604.19835, 2510.08008)
- Exa search | Liger ICML 2025 | 1
- Exa search | continual pretraining of MoEs router robustness | 1 (TMLR evidence)
- Exa search | Nemotron-H MiniPuzzle, Nemotron Nano 2 | 2 (2504.03624, 2508.14444)
- Exa search | mid-training / continual pretraining surveys | 3 (2510.06826, 2510.23081, 2603.12658)
- Exa search | model merging surveys | 1 (2603.09938) + 1 baseline
- Exa search | Kimi K2 Thinking INT4 QAT, Kimi K3 | 2 (model card, 2607.24653)
- Exa search | Qwen3.5 / Qwen3-Next / DeepSeek-V4 | 1 kept (2606.19348)
- Exa search | layer pruning with recovery healing 2025 | 2 (2505.02819, 2506.20480)
- Exa search | Llama-Nemotron / Puzzle | 1 (2505.00949) + baseline 2411.19146
- Exa search | OPD merging RL checkpoints GLM-5.2 | 5 (2604.13016, 2608.19098, 2607.05394 not kept, 2602.12125, 2607.26246)
- WebSearch arxiv | Drop-Upcycling arXiv id | 1
- WebSearch openreview | LoLCATs ICLR 2025 | baseline only
- WebSearch arxiv/openreview | scaling laws for upcycling MoE | 1 (2502.03009)
- Exa search | GLM-5 DSA adaptation 20B tokens | quotes captured
- Exa search | GLM-5.2 blog OPD merge IndexShare | quotes captured
- Exa search | KL-guided hybrid distillation arXiv id | 1 (2512.20569, ICLR 2026)
- Exa search | Nemotron 3 Ultra arXiv | 1 (2606.15007)
- WebSearch venue checks (neurips/openreview/mlr/aclanthology/cvf/colm) | ProRL, LongRoPE2, EvoLM, Common Pile, OpenThoughts, RADLADS, upcycling scaling laws, MTP post hoc, merging scaling laws, STAR, AReaL, QAT scaling law, UltraLong, IndexCache/Finetuner's Fallacy/Expert Upcycling, MergeBench, RL subnetworks, AWEDIST, DeRS, Rope-to-Nope, GPTailor/OpT-DeUS | tiers assigned as recorded
- Exa search | Foreign Sparse Attention, Compute-Optimal QAT, Dense2MoE, Memory Decoder ids | 4
- Scholar Gateway (Wiley) | continued pretraining / merging / upcycling of open-weight LLMs, 2025-2026, topN 10 | 0 kept (6 articles returned, none on-path: incremental-learning review, PEFT module combination, medical/hallucination reviews)
- Exa fetch | arxiv abs verification batches (63 IDs) + Z.ai blogs + GitHub README + Thinking Machines blog | all listed items verified except openreview:Y50Mdo9k1v


## Path 4, post-training

exa_fetch | seeds abs: 2607.24653 Kimi K3, 2602.15763 GLM-5, 2503.14476 DAPO, nature s41586-025-09422-z DeepSeek-R1 | 4 kept
exa_search | DAPO open-source LLM RL system clip-higher dynamic sampling | 1 kept (2503.14476, NeurIPS 2025 proceedings)
exa_search | Does RL really incentivize reasoning beyond base model Yue 2025 | 1 kept (2504.13837, NeurIPS 2025 proceedings)
exa_search | Art of Scaling RL Compute ScaleRL | 1 kept (2510.13786, ICLR 2026 oral, proceedings.iclr.cc)
exa_search | Beyond the 80/20 rule high-entropy minority tokens | 1 kept (2506.01939, NeurIPS 2025 proceedings)
exa_search | RL's Razor online RL forgets less than SFT | 1 kept (2509.04259, ICLR 2026 via mlanthology)
exa_search | Absolute Zero reinforced self-play zero data | 1 kept (2505.03335, NeurIPS 2025 proceedings)
exa_search | AReaL asynchronous RL system decoupled generation staleness | 1 kept (2505.24298, NeurIPS 2025 proceedings)
websearch arxiv.org | GSPO Group Sequence Policy Optimization Qwen | 1 kept (2507.18071) + candidates 2601.05607 dynamic hybrid token/sequence
websearch arxiv+openreview | ProRL prolonged RL NVIDIA | 1 kept (2505.24864, OpenReview forum YPsJha5HXQ) + BroRL 2510.01180, Negative reinforcement 2506.01347
exa_fetch | abs verify: 2507.18071 GSPO, 2505.24864 ProRL, 2510.13786 ScaleRL, 2509.04259 RL's Razor, 2505.24298 AReaL | 5 verified
exa_search | Understanding R1-Zero-like training Dr. GRPO | 1 kept (2503.20783; OpenReview 5PAF7PAY2Y)
exa_search | Geometric-Mean Policy Optimization GMPO | 1 kept (2507.20673; ICLR 2026 proceedings)
exa_search | MiniMax-M1 CISPO | 1 kept (2506.13585, Tier C)
exa_search | VAPO value-based augmented PPO ByteDance | 1 kept (2504.05118)
exa_search | BAPO balanced policy optimization adaptive clipping | 1 kept (2510.18927; OpenReview rdjV7dFvxq) + noted "Buffer Matters" ICLR 2026 (different BAPO)
exa_search | Entropy Mechanism of RL Clip-Cov KL-Cov | 1 kept (2505.22617; OpenReview vXoksdcfqC)
exa_search | Unreasonable Effectiveness of Entropy Minimization | 1 kept (2505.15134; NeurIPS 2025 proceedings)
exa_search | Learning to Reason without External Rewards Intuitor RLIF | 1 kept (2505.19590; ICLR 2026 proceedings)
exa_search | RLPR verifier-free probability reward | 1 kept (2506.18254; OpenReview T03kNBYq81)
exa_search | Rubrics as Rewards | 1 kept (2507.17746; ICLR 2026 poster)
exa_search | Checklists better than reward models RLCF | 1 kept (2507.18624; NeurIPS 2025 proceedings)
exa_search | PRIME implicit process rewards | 1 kept (2502.01456; OpenReview 9SkkifLopZ)
exa_search | TTRL test-time RL | 1 kept (2504.16084; NeurIPS 2025 proceedings)
exa_search | SPIRAL self-play zero-sum games | 1 kept (2506.24119; ICLR 2026 proceedings)
exa_search | R-Zero challenger solver | 1 kept (2508.05004; ICLR 2026 poster)
exa_fetch | abs verify batch: 2503.20783, 2507.20673, 2506.13585, 2504.05118, 2510.18927, 2505.22617, 2505.15134, 2505.19590, 2506.18254, 2507.17746, 2507.18624, 2502.01456, 2504.16084, 2506.24119, 2508.05004, 2504.13837, 2506.01939, 2505.03335 | 18 verified
websearch openreview | Dr.GRPO/ProRL/Entropy Mechanism NeurIPS 2025 | ProRL confirmed NeurIPS 2025 poster; others via forum ids
websearch openreview | BAPO/RLPR/PRIME venue | 0 direct (noise)
exa_search | slime GLM RL framework | 1 kept (github THUDM/slime; lmsys blog; Tier C infra) + APRIL arXiv 2509.18521
exa_search | training-inference mismatch TIS/MIS | 3 kept (opt-ml TIS workshop paper OpenReview 8MHqvb4lK9; 2605.14220 TIM diagnosis; 2603.19470 ALP)
exa_search | Kimi K2 technical report | 1 kept (2507.20534, Tier C)
exa_search | Qwen3 technical report thinking fusion | 1 kept (2505.09388, Tier C)
exa_search | deliberative alignment | 1 kept (2412.16339, v1 2024-12-20 = pre-window baseline)
exa_search | constitutional classifiers | 1 kept (2501.18837)
exa_search | on-policy distillation continual learning / retaining by doing | 2 kept (2510.18874 ICML 2026; Thinking Machines OPD blog Tier C) + OPD survey 2604.00626
exa_search | survey RL for LRMs | 3 kept (2509.08827; 2509.16679; 2501.09686 Patterns journal)
exa_search | Spurious rewards RLVR | 1 kept (2506.10947, ICML 2026 poster)
exa_search | Invisible Leash RLVR | 1 kept (2507.14843, OpenReview KXtLWJAzgh)
exa_search | Pass@k training | 1 kept (2508.10751, OpenReview eslxxopXTF ICLR 2026 submission)
exa_search | L1 length controlled policy optimization | 1 kept (2503.04697, COLM 2025)
exa_search | learning when to think AdaptThink Thinkless | 2 kept (2505.13417 EMNLP 2025; 2505.13379 NeurIPS 2025)
exa_search | DeepSeek-GRM SPCT | 1 kept (2504.02495, OpenReview sokbAEcsJM)

exa_fetch | abs verify: 2507.20534, 2505.09388, 2501.18837, 2510.18874, 2509.08827, 2506.10947, 2507.14843, 2508.10751, 2503.04697, 2505.13417, 2505.13379, 2504.02495, 2605.14220, 2603.19470, 2604.00626 | 15 verified
exa_fetch | html seeds for reference mining: 2607.24653 (223k chars, 153 refs, 93 dated 2025-26), 2602.15763 (143k chars; refs not delimited, method sections mined), 2503.14476 (full, 39 refs: 2025 items = R1, K1.5, PRIME, VC-PPO 2503.01491, ORZ, REINFORCE++, empirical study 2503.04548) | 3 fetched
exa_search | Your efficient RL framework secretly off-policy TIS Feng Yao | 1 kept (OpenReview xsonlP8DRV; opt-ml paper116)
exa_search | GLM-5.2 critic PPO compaction effort | 2 kept (z.ai blog; CompactionRL 2607.05378)
exa_search | DeepSeek-V4 technical report RL | 1 kept (2606.19348)
exa_search | MiniMax M2.5 / M3 RL CISPO | 3 kept (2605.26494; Forge blog; M3 blog + MSA 2606.13392)
exa_search | Kimi K2.5 / K2 Thinking | 1 kept (2602.02276) + K2 Thinking model card
exa_search | GPT-5 system card | 1 kept (2601.03267 / openai.com)
exa_search | Claude Fable 5 system card | 1 kept (Anthropic PDF 2026-06-09)
exa_search | Gemini 3 report RL post-training | 1 kept (Gemini 3 Pro FSF report; thinking_level docs)
exa_search | multi-turn credit assignment GiGPO turn-level | 3 kept (2505.10978 NeurIPS 2025; 2512.17008; 2505.11821) + GAGPO 2605.13217 noted
exa_search | PipelineRL in-flight weight updates | 1 kept (2509.19128)
exa_search | safety-capability trade-off under RLVR | 3 kept (2511.21050; 2512.01848; Safety Tax 2503.00555 unverified) + STAR-1 2504.01903, ReAlign OpenReview noted
exa_search | model merging of RL checkpoints | 3 kept (2601.13572 ACL 2026; 2606.18521 KDD 2026; ResMerge 2606.02252 noted; merging-duration study 2607.11997 noted)
exa_search | reward hacking detection during RL | 3 kept (2510.01367 TRACE; 2604.16242 GRIFT; OpenAI CoT monitoring) + Trace-and-Amplify 2604.23488, TRACE benchmark 2601.20103 noted
exa_search | automatic environment generation / language self-play 2026 | 3 kept (2608.19197 SPADE; 2605.14392; Agent-World 2604.18292 noted; SCOPE 2605.31433, ARISE-RL 2609.01058, ScaleEnv 2602.06820, pursuit-evasion 2608.21871 noted)
exa_search | Qwen3.5 technical report RL | 1 kept (Qwen3.5-Omni 2604.15804, not abs-verified) + LEGO-RL 2608.17393 (GSPO on Qwen3.5-35B-A3B)
exa_search | GLM-5.3 blog | 1 kept (z.ai/blog/glm-5.3)
exa_search | 2026 RL scaling follow-ups | 3 kept (2603.12151 IsoCompute; 2607.22186 entropy-scaled trust regions; ACL 2026 Findings low-probability tokens) + relative-budget theory 2602.01523, 2604.04894, 2602.07992 noted
exa_search | Kimi K2.5 algorithm / Toggle / tau | 1 kept (2602.02276 sections 4.4.2)
exa_search | self-rewarding successors / RLIF 2026 | 2 kept (G-Zero 2605.09959; Skill Self-Play 2607.22529 noted; S3Gym 2608.31100, SRPO 2608.23493, 2604.03098 co-evolving reward noted)
exa_search | IcePop Ring-1T | 1 kept (2510.18855)
exa_fetch | abs verify: 2509.19128, 2505.10978, 2512.17008, 2511.21050, 2512.01848, 2601.13572, 2606.18521, 2510.01367, 2604.16242, 2602.02276, 2606.19348, 2605.26494, 2606.13392, 2607.05378, 2608.19197, 2601.03267, 2603.22446, 2412.16339, 2505.11821, 2510.01180, 2509.24203, 2511.05993, 2604.00860, 2602.05261, 2509.18521, 2607.22186, 2603.12151, 2605.14392, 2605.09959, 2501.12599 | 30 verified
exa_fetch | aclanthology: 2026.findings-acl.1209, 2026.acl-long.1524, 2025.emnlp-main.184 | 3 verified
websearch iclr.cc/openreview | BAPO ICLR 2026 | confirmed (proceedings.iclr.cc)
websearch openreview | RLPR ICLR 2026 | submission with Feb-2026 revisions (B)
websearch openreview | PRIME venue | ICLR 2026 submission CmyqMn3HeJ (B)
websearch neurips.cc/openreview | Entropy Mechanism NeurIPS 2025 | not confirmed (B)
websearch neurips.cc/openreview | Dr.GRPO / DeepSeek-GRM | not confirmed (B)
websearch iclr.cc/openreview | Invisible Leash / GSPO / Pass@k | Invisible Leash 'under review ICLR 2026'; SimKO and CoT-Pass@K (ICLR 2026 poster 10007896) surfaced
websearch iclr.cc | RLPR/PRIME/GRM/Pass@k/Sparse-but-Critical posters | none confirmed; CoT-Pass@K and F-GRPO, distributional-critic RLVR posters surfaced
websearch iclr.cc/neurips.cc | RL's Razor / Entropy / R1-Zero | RL's Razor confirmed in proceedings.iclr.cc 2026
websearch neurips.cc | R1-Zero / Entropy / GiGPO posters | GiGPO poster 118123 confirmed; others not
websearch neurips.cc | 80/20 / AZR / Yue orals | Yue oral 119945, AZR poster 116121 confirmed
scholar_gateway (Wiley) | RLVR/GRPO entropy exploration 2025-26 | 0 relevant (7 articles, all off-topic: BO, aquaculture, finance NLP)
scholar_gateway (Wiley) | catastrophic forgetting RL vs SFT post-training | 0 relevant (5 articles, incremental-learning review in Expert Systems is closest but generic)

Blocked hosts were not retried. OpenReview forum pages returned browser-check pages, so venue status for B-tier items comes from WebSearch snippets only.


## Frontier recipe register

(log pending)
