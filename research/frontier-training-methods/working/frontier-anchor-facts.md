# Frontier anchor facts verified by the orchestrator from primary sources (Tier C)

## Kimi K3 (arXiv 2607.24653; blog 2026-07-14; weights 2026-07-27)
- 2.8T total / 104B active MoE; 93 layers; 69 KDA + 24 Gated MLA; 896 routed experts, 16 active, 2 shared; Stable LatentMoE; SiTU-GLU; Quantile Balancing (QB) for load balance; Attention Residuals; NoPE (per alphaXiv summary; verify in text); MoonViT-V2 vision encoder; 1 MTP layer.
- Optimizer: Per-Head Muon (Newton-Schulz per attention head) + weight clipping from K2; cosine schedule with 1% warmup; weight decay 0.1.
- Scaling law: ~2.5x scaling efficiency over K2; retuned batch size, LR, tokens-per-parameter, model shape. NEGATIVE RESULT: "Our scaling-law study consistently favors cosine decay over Warmup Stable Decay (WSD)... Under their respective optimal hyperparameter settings, cosine decay consistently achieves a lower final loss than WSD."
- Context curriculum: 8K to 64K during pre-training; 256K to 1M during cooldown (four stages).
- Post-training: SFT (trajectories synthesized by prior domain-specialized Kimi models, verified, human-in-the-loop; XTML template) -> RL producing 9 experts (3 domains x 3 effort levels) -> Multi-Teacher On-Policy Distillation (MOPD) into one model. OPD reward = clip(sg(log pi_teacher/pi_student), -Rmax, Rmax) per token. NEGATIVE RESULT: "we also experimented with more fine-grained top-k distillation objectives, we observed no clear advantage in either convergence speed or final performance."
- RL algorithm: partial rollouts (pause at fraction lambda), extreme off-policy tolerated via "per-token regularization" constraining updates to a localized neighborhood; policy optimization "follows the algorithm in Kimi K2.5".
- Reasoning effort RL: per-problem token budget b0(x) from cold-start model; reward overridden to -1 when T(y) > tau * b0(x); tau annealed per domain with human-in-the-loop guidance.
- Agentic Generative Reward Model: tournament-style binary comparisons; mandatory protocol (read output, generate rubric, score, scorepad); verbosity control via sigma * l0.
- QAT: MXFP4 expert weights / MXFP8 activations "throughout the entire post-training stage, covering both SFT and RL... rollout and training share the same quantization scheme, eliminating the train-inference mismatch."
- Draft model: MTP layer fine-tuned into EAGLE-3-style draft with LK loss (negative log acceptance rate).
- Environments: unified white-box RL environment (composable harness modules; instantiates Kimi Code, Claude Code, Codex, OpenClaw, Hermes); knowledge-graph-guided task synthesis (self-evolving DAG expanded by agents); verifiable agentic problems; kernel tasks; mock personal-assistant apps; Autonomous Execution Tasks (verify-in-the-loop); web dev tasks with deterministic checks + internal RM.
- Infra: co-located RL, external KV cache pool in CPU DRAM, auto-throttling scheduler, gradient-buffer reuse for reference model; microVM sandbox (AgentENV per alphaXiv summary) with pause/resume/snapshot; MoonEP balanced expert parallelism.
- Conclusion states no open problems.

## DeepSeek-V4 (arXiv 2606.19348; released 2026-04-24)
- V4-Pro 1.6T/49B; V4-Flash 284B/13B; 1M context; 32-33T pretraining tokens.
- Architecture: hybrid Compressed Sparse Attention (CSA: 4x KV compression + DSA top-k via lightning indexer) and Heavily Compressed Attention (HCA: 128x compression, dense); Manifold-Constrained Hyper-Connections (mHC, Xie et al. 2026; Sinkhorn-Knopp projection onto Birkhoff polytope); DeepSeekMoE; MTP unchanged from V3.
- Optimizer: Muon "for the majority of modules" with hybrid Newton-Schulz; AdamW for embeddings, head, mHC biases/gates, RMSNorm; hybrid ZeRO for Muon.
- Precision: FP4 QAT for MoE expert weights and indexer QK path during post-training; batch-invariant deterministic kernels for bitwise train/inference reproducibility.
- Post-training (model card): "two-stage paradigm: independent cultivation of domain-specific experts (through SFT and RL with GRPO), followed by unified model consolidation via on-policy distillation."
- Three effort modes (Non-think, Think High, Think Max). DSec sandbox platform (function calls, containers, microVMs, VMs; hundreds of thousands of concurrent sandboxes; preemption-safe trajectory replay).

## GLM-5 (arXiv 2602.15763; 2026-02-12) and GLM-5.2 (blog 2026-06-16) and GLM-5.3 (blog 2026-08-14)
- GLM-5: 744B/40B MoE; 28.5T tokens; DSA introduced by continued pretraining from the MLA base after mid-training (1000-step warm-up + 20B-token sparse adaptation, versus 943.7B tokens for DeepSeek-V3.2); context 4K->32K (1T)->128K (500B)->200K (50B); post-training SFT -> Reasoning RL -> Agentic RL -> General RL with On-Policy Cross-Stage Distillation to prevent forgetting; slime asynchronous RL; Muon (per "Spectral Scaling Laws of Muon": "Kimi-K2, GLM-5, and DeepSeek-V4 were all trained with Muon"; verify in GLM-5 report).
- GLM-5.2: IndexShare (one indexer per 4 DSA layers; 2.9x fewer per-token FLOPs at 1M; trained from mid-training at 128K); MTP with IndexShare + KVShare + rejection sampling + end-to-end TV loss (+20% acceptance length); critic-based PPO on individual rollouts with compaction sub-traces and token-level loss (replacing group-relative optimization); anti-hack module (rule filter + LLM intent judge, online blocking with dummy results); parallel OPD merging ">ten expert models" in ~2 days; effort levels High/Max.
- GLM-5.3: "same base model as GLM-5.2, every gain comes from post-training"; "SAO with compaction" (RL method name introduced in 5.2); environment synthesis pipeline with synthesized verifiers (oracle, no-op, unsolved-state checks); top-k and full-vocabulary OPD; R3-style train-rollout consistency (logprob diff 1e-7); multi-teacher OPD with dynamic teacher switching; 2.3x RL throughput; emergent cyber capability from post-training scale. OPEN PROBLEM (quoted): "These pipelines still require a meaningful amount of human-in-the-loop work; making environment generation and verification more autonomous is one of the next steps."

## Convergent 2026 frontier post-training recipe (three independent labs)
SFT cold start -> domain/effort-level RL experts -> on-policy distillation consolidation into one model: Kimi K3 (MOPD), DeepSeek-V4 (experts via SFT+GRPO then OPD), GLM-5.2/5.3 (parallel OPD merge of >10 experts). This makes "OPD as consolidation" ADOPTED, and variants (top-k OPD) TESTED with null result at Kimi.

## Convergent 2026 pretraining recipe
Muon-family optimizer (Kimi K2/K3, DeepSeek-V4, GLM-5 per third-party statement), sparse or hybrid-linear attention trained from scratch or via short continued pretraining (KDA hybrid; CSA/HCA; DSA/IndexShare), residual-stream upgrades (Attention Residuals; mHC), ultra-sparse MoE with bias-based balancing (QB; aux-loss-free), MTP head kept for speculative decoding, FP4/MXFP4 QAT in post-training, 1M context via late-stage curriculum, cosine schedule at Kimi (WSD rejected).
