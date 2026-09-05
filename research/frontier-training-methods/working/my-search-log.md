# Orchestrator search log (queries run directly, not by sweep agents)

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
