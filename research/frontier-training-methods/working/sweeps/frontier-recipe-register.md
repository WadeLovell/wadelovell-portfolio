# Frontier Recipe Register (2024-12-31 → 2026-09-05)

Generated 2026-09-05 by the register sweep. Scope: what each frontier / leading open-weights model released in the window discloses about how it was trained. Every entry is **Tier C** (industrial tech report / model card / blog) unless a peer-reviewed version exists, in which case both are recorded. Quotes are verbatim from the cited source (single-quoted); `[S#]` pointers resolve in the Source key. Fields the sources do not address are marked undisclosed rather than guessed.

## Method notes

- **Verification rule**: a model is 'verified' only if its arXiv abs page, official blog / GitHub README, or system card was fetched (or, for huggingface-hosted cards blocked to direct fetch, corroborated by Exa search highlights of the card plus a secondary report). Unverifiable entries are kept with `verified: no` and blank fields.
- **Channels**: arXiv abs/html via Exa fetch (persisted to tool-result files, then indexed with a KWIC grep); official blogs/system cards via Exa search highlights and WebSearch; huggingface.co, openreview.net and z.ai were not directly fetchable.
- **Matrix cell semantics**: `D` disclosed = explicit statement in the cited source; `H` hinted = indirect / inherited from a parent model / stated only in secondary coverage; `A` absent = the source states an alternative or that the method is not used (e.g., AdamW ⇒ Muon absent; cosine ⇒ WSD absent; CISPO ⇒ GRPO absent; 'from scratch' ⇒ upcycling absent); `U` undisclosed = not addressed. Proprietary system cards default to `U`.
- **Family inheritance**: point releases that publish only a blog (GLM-4.7/5.1/5.2/5.3, K2 Thinking, M2.5, Qwen3.8, Hy3) inherit architecture fields from their parent report and are marked `H` unless the blog restates the item.

**Coverage**: 67 model entries; 65 verified; not verifiable: Apple Foundation Models 2026, xAI Grok 5.

## Source key

| Key | Source |
|---|---|
| S1 | Kimi K2 tech report, arXiv 2507.20534 (v1 2025-07-28) https://arxiv.org/abs/2507.20534 |
| S2 | Kimi K2 Thinking blog https://moonshotai.github.io/Kimi-K2/thinking ; HF card moonshotai/Kimi-K2-Thinking ; Medium 2025-11-10 |
| S3 | Kimi K2.5 tech report, arXiv 2602.02276 (v1 2026-02-02) https://arxiv.org/abs/2602.02276 ; GitHub MoonshotAI/Kimi-K2.5 ; TechCrunch 2026-01-27 |
| S4 | Kimi K3 tech report, arXiv 2607.24653 (v1 2026-07-27) https://arxiv.org/abs/2607.24653 ; blog https://www.kimi.com/blog/kimi-k3 ; GitHub moonshotai/Kimi-K3 |
| S5 | DeepSeek-V3.1 release note https://www.deepseek.com/en/news/deepseek-v3-1/ (2025-08-21); HF card deepseek-ai/DeepSeek-V3.1 |
| S6 | DeepSeek-V3.2-Exp GitHub https://github.com/deepseek-ai/deepseek-v3.2-exp (2025-09-29) |
| S7 | DeepSeek-V3.2 tech report, arXiv 2512.02556 (v1 2025-12-02) https://arxiv.org/abs/2512.02556 |
| S8 | DeepSeek-V4 tech report, arXiv 2606.19348 (arXiv page dated 2026-04-26) https://arxiv.org/abs/2606.19348 ; HF README deepseek-ai/DeepSeek-V4-Flash ; HF blog https://huggingface.co/blog/deepseekv4 (2026-04-24); HF transformers docs deepseek_v4 |
| S9 | DeepSeek-R1 arXiv 2501.12948 (v1 2025-01-22) https://arxiv.org/abs/2501.12948 ; Nature 645, 633-638 (2025-09-17) https://www.nature.com/articles/s41586-025-09422-z |
| S10 | GLM-4.5 tech report, arXiv 2508.06471 (v1 2025-08-08) https://arxiv.org/abs/2508.06471 ; blog https://z.ai/blog/glm-4.5 |
| S11 | GLM-4.7 blog https://z.ai/blog/glm-4.7 (2025-12-22); HF card zai-org/GLM-4.7 |
| S12 | GLM-5 tech report, arXiv 2602.15763 (v1 2026-02-17) https://arxiv.org/abs/2602.15763 ; blog https://z.ai/blog/glm-5 (2026-02-12); GitHub zai-org/GLM-5 |
| S13 | GLM-5.1 blog https://z.ai/blog/glm-5.1 (2026-04-07); docs.z.ai release notes; VentureBeat 2026-04-07 |
| S14 | GLM-5.2 blog https://z.ai/blog/glm-5.2 (2026-06-16); HF card zai-org/GLM-5.2; IndexShare arXiv 2603.12201 |
| S15 | GLM-5.3 blog https://z.ai/blog/glm-5.3 (2026-08-14); GitHub zai-org/GLM-5 README; SemiAnalysis InferenceX page |
| S16 | Qwen3 tech report, arXiv 2505.09388 (v1 2025-05-14) https://arxiv.org/abs/2505.09388 ; blog https://qwenlm.github.io/blog/qwen3/ (2025-04-29); GSPO arXiv 2507.18071 |
| S17 | Qwen3-Next blog (Alibaba Cloud community mirror, 2025-09-12) https://www.alibabacloud.com/blog/qwen3-next-towards-ultimate-training-%26-inference-efficiency_602580 ; HF card Qwen/Qwen3-Next-80B-A3B-Instruct |
| S18 | Qwen3.5 blog https://www.alibabacloud.com/blog/602894 (2026-02-16/17); HF README Qwen/Qwen3.5-397B-A17B; GitHub QwenLM/Qwen3.5; Qwen3.5-Omni report arXiv 2604.15804 |
| S19 | Qwen3.8-27B HF card https://huggingface.co/Qwen/Qwen3.8-27B (2026-08-14); GitHub QwenLM/Qwen3.8 |
| S20 | MiniMax-M1 tech report, arXiv 2506.13585 (v1 2025-06-16) https://arxiv.org/abs/2506.13585 |
| S21 | MiniMax-M2 blog https://www.minimax.io/blog/minimax-m2-en-1748600000 (2025-10-27); GitHub MiniMax-AI/MiniMax-M2; M2 series report arXiv 2605.26494 (v1 2026-05-26); Forge blog https://www.minimax.io/blog/forge-scalable-agent-rl-en-1779896141 |
| S22 | MiniMax-M2.5 blog https://www.minimax.io/blog/minimax-m25 (2026-02-12); GitHub MiniMax-AI/MiniMax-M2.5 |
| S23 | MiniMax-M3 blog https://www.minimax.io/blog/minimax-m3 (2026-06-01); GitHub MiniMax-AI/MiniMax-M3; MSA paper arXiv 2606.13392 (v1 2026-06-11) |
| S24 | Llama 4 blog https://ai.meta.com/blog/llama-4-multimodal-intelligence/ (2025-04-05); model card github.com/meta-llama/llama-models/.../llama4/MODEL_CARD.md; HF blog llama4-release |
| S25 | gpt-oss model card, arXiv 2508.10925 (2025-08-05) https://arxiv.org/abs/2508.10925 ; https://openai.com/index/introducing-gpt-oss/ |
| S26 | Gemma 3 tech report, arXiv 2503.19786 (v1 2025-03-25; release 2025-03-12) https://arxiv.org/abs/2503.19786 ; developers.googleblog.com/introducing-gemma3/ |
| S27 | Gemma 3n developer guide https://developers.googleblog.com/introducing-gemma-3n-developer-guide/ (2025-06-26); HF blog gemma3n |
| S28 | Gemma 4 tech report, arXiv 2607.02770 (v1 2026-07-02; release 2026-04-02) https://arxiv.org/abs/2607.02770 ; https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/ ; HF blog gemma4; ai.google.dev/gemma/docs/core |
| S29 | Mistral 3 announcement https://mistral.ai/news/mistral-3/ (2025-12-02); HF README Mistral-Large-3-675B-Instruct-2512; Mistral downstream-provider technical documentation |
| S30 | Magistral report, arXiv 2506.10910 (v1 2025-06-12) https://arxiv.org/abs/2506.10910 |
| S31 | Devstral 2 announcement https://mistral.ai/news/devstral-2-vibe-cli/ (2025-12-09) |
| S32 | Nemotron 3 white paper arXiv 2512.20856 (2025-12-24); Nemotron 3 Nano report arXiv 2512.20848 (2025-12-23) https://arxiv.org/abs/2512.20848 ; docs.nvidia.com/nemotron nano3 pretrain |
| S33 | Nemotron 3 Super report, arXiv 2604.12374 (v1 2026-04-14; release 2026-03-10) https://arxiv.org/abs/2604.12374 ; research.nvidia.com/labs/nemotron/Nemotron-3-Super/ |
| S34 | Nemotron 3 Ultra report, arXiv 2606.15007 (v1 2026-06-12; release ~2026-06-04) https://arxiv.org/abs/2606.15007 ; PDF research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf ; NeMo-RL docs nemotron-3-ultra |
| S35 | Olmo 3 report, arXiv 2512.13961 (v1 2025-12-15; release 2025-11-20) https://arxiv.org/abs/2512.13961 ; https://allenai.org/blog/olmo3 |
| S36 | SmolLM3 blog https://huggingface.co/blog/smollm3 (2025-07-08); HF card HuggingFaceTB/SmolLM3-3B |
| S37 | Apertus report, arXiv 2509.14233 (v1 2025-09-17) https://arxiv.org/abs/2509.14233 ; ACL 2026 long paper https://aclanthology.org/2026.acl-long.2172/ |
| S38 | LongCat-Flash tech report, arXiv 2509.01322 (v1 2025-09-01) https://arxiv.org/abs/2509.01322 |
| S39 | Ling 2.0 report 'Every Activation Boosted', arXiv 2510.22115 (v1 2025-10-25) https://arxiv.org/abs/2510.22115 ; HF card inclusionAI/Ling-1T |
| S40 | Ring-1T report 'Every Step Evolves', arXiv 2510.18855 (v1 2025-10-21) https://arxiv.org/abs/2510.18855 ; Ant Ling Medium post 2025-10-14 |
| S41 | Step-3 report, arXiv 2507.19427 (v1 2025-07-25) https://arxiv.org/abs/2507.19427 ; GitHub stepfun-ai/Step3 model card |
| S42 | MiMo-7B report, arXiv 2505.07608 (v1 2025-05-12) https://arxiv.org/abs/2505.07608 |
| S43 | MiMo-V2-Flash report, arXiv 2601.02780 (v1 2026-01-06; release 2025-12-16) https://arxiv.org/abs/2601.02780 ; GitHub XiaomiMiMo/MiMo-V2-Flash; mimo.xiaomi.com/mimo-v2-flash |
| S44 | Hunyuan-A13B GitHub https://github.com/Tencent-Hunyuan/Hunyuan-A13B (2025-06-27) and technical report linked there; Hy3 GitHub https://github.com/tencent-hunyuan/hy3 (2026-07-06); hy.tencent.com/research/hy3 |
| S45 | Seed-OSS GitHub https://github.com/ByteDance-Seed/seed-oss (2025-08-20); Seed blog 2025-08-21 |
| S46 | IBM Granite 4.0 announcement https://www.ibm.com/new/announcements/ibm-granite-4-0-hyper-efficient-high-performance-hybrid-models (2025-10-02); ibm.com/granite/docs/models/granite4-0 |
| S47 | Falcon-H1 report, arXiv 2507.22448 (v1 2025-07-30; release 2025-05-20) https://arxiv.org/abs/2507.22448 ; blog falcon-lm.github.io/blog/falcon-h1/ ; tiiuae.github.io/Falcon-H1/post_training_details/ |
| S48 | Grok 2.5 open-weights release: TechCrunch 2025-08-24 https://techcrunch.com/2025/08/24/elon-musk-says-xai-has-open-sourced-grok-2-5/ ; allaboutai.com summary of HF card (huggingface.co blocked for direct fetch) |
| S49 | Phi-4-reasoning report, arXiv 2504.21318 (v1 2025-04-30) https://arxiv.org/abs/2504.21318 |
| S50 | Apple Intelligence Foundation Language Models Tech Report 2025, arXiv 2507.13575 (v1 2025-07-17) https://arxiv.org/abs/2507.13575 |
| S51 | Arcee Trinity Large report, arXiv 2602.17004 (v1 2026-02-19; release 2026-01-27) https://arxiv.org/abs/2602.17004 ; https://www.arcee.ai/blog/trinity-large |
| S52 | OpenAI o3 and o4-mini system card https://openai.com/index/o3-o4-mini-system-card/ (2025-04-16) |
| S53 | GPT-5 system card https://openai.com/index/gpt-5-system-card/ (2025-08-07); arXiv 2601.03267 |
| S54 | GPT-5.5 system card https://deploymentsafety.openai.com/gpt-5-5 (2026-04-23) |
| S55 | GPT-5.6 system card https://deploymentsafety.openai.com/gpt-5-6 (2026-07-09) |
| S56 | Claude Opus 4 & Sonnet 4 system card https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47.pdf (2025-05-22); https://www.anthropic.com/news/claude-4 |
| S57 | Claude Opus 4.5 system card https://www.anthropic.com/claude-opus-4-5-system-card (2025-11-24) |
| S58 | Claude Opus 4.7 system card https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340.pdf (2026-04-16) |
| S59 | Claude Opus 4.8 system card https://www-cdn.anthropic.com/0f0c97ad20d8005706296bd92aa1c27c6b2f4f61.pdf (2026-05-28); https://www.anthropic.com/news/claude-opus-4-8 |
| S60 | Claude Fable 5 & Mythos 5 system card https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20&%20Claude%20Mythos%205%20System%20Card.pdf (2026-06-09); https://www.anthropic.com/system-cards ; platform.claude.com/docs/en/build-with-claude/effort |
| S61 | Gemini 2.5 tech report, arXiv 2507.06261 (v1 2025-07-07) https://arxiv.org/abs/2507.06261 ; Gemini 2.5 Deep Think model card |
| S62 | Gemini 3 Pro model card https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf (2025-11-18); https://blog.google/products-and-platforms/products/gemini/gemini-3/ |
| S63 | Gemini Diffusion https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-diffusion/ (2025-05-20); https://deepmind.google/models/gemini-diffusion/ |
| S64 | Grok 4 https://x.ai/news/grok-4 (2025-07-09); Grok 4 model card https://data.x.ai/2025-08-20-grok-4-model-card.pdf |
| S65 | Grok 4.6 model card https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf (2026-08-12); Grok 5 status: geotoolbox/felloai/buildbevy reports Aug 2026 (no xAI Grok 5 card exists) |
| S66 | MiMo-V2-Flash HF/GitHub statements (see S43) |

## Register

One block per model (all required fields; empty fields say undisclosed).

### Moonshot / DeepSeek / Zhipu

#### Kimi K2 (Instruct/Base)

| Field | Value |
|---|---|
| Model | Kimi K2 (Instruct/Base) |
| Lab | Moonshot AI |
| Release date | 2025-07-11 (weights); report v1 2025-07-28 [S1] |
| Total / active params | '32 billion activated parameters and 1 trillion total parameters' (1.04T; 384 experts, 8 active + 1 shared) [S1] |
| Architecture family | MoE (ultra-sparse): 'ultra-sparse MoE with multi-head latent attention (MLA) similar to DeepSeek-V3' [S1] |
| Attention variant | MLA, 64 heads: 'we cut the number of attention heads to 64, as opposed to 128 in DeepSeek-V3' [S1] |
| MoE routing / balancing | DeepSeek-V3-style routing; sparsity 48 chosen from 'sparsity scaling law'; balancing method not restated (follows V3) [S1] |
| Position encoding | RoPE within MLA ('q R(head-specific rotary)') [S1] |
| MTP | not stated in fetched sections; MTP absent from K2 architecture table (K3 table lists K2 'Number of MTP Layers: 1 layer') [S4] |
| Optimizer | MuonClip: 'We integrate Muon with weight decay, consistent RMS matching, and QK-Clip into a single optimizer' [S1] |
| Pre-training tokens | 'pre-trained on 15.5 trillion tokens with zero loss spike'; WSD schedule: 'first 10T tokens ... constant learning rate of 2e-4 ... followed by 5.5T tokens with a cosine decay' [S1] |
| Precision & QAT | not stated for K2 pre-training in fetched text; INT4 QAT introduced later for K2 Thinking [S2] |
| Context-extension curriculum | '400 billion tokens with a 4k sequence length, followed by an additional 60 billion tokens with a 32k sequence length. To extend the context window to 128k, we employed the YaRN method' [S1] |
| Mid-training stage? | annealing + 'long-context activation stage' described [S1] |
| Distillation (where, teacher) | no distillation stated; agentic data synthesized with LLM-judge filtering [S1] |
| SFT | 'We employ the Muon optimizer in our post-training'; SFT on synthesized agentic trajectories; critic bootstrapped in SFT [S1] |
| RL algorithms | K1.5-style policy-gradient with regularizer tau (no named GRPO); additions: 'Budget Control', 'PTX Loss', 'Temperature Decay' [S1] |
| Reward sources | 'combines verifiable rewards (RLVR) with a self-critique rubric reward mechanism' — core, prescriptive and human-annotated rubrics; critic refined with verifiable signals [S1] |
| Async / off-policy RL | 'Gym-like extensible framework'; asynchrony not described in fetched sections [S1] |
| Agentic RL environment scale | 'hundreds of domains containing thousands of tools ... hundreds of agents' (data synthesis); RL 'interactions with real and synthetic environments' [S1] |
| Reasoning-effort control | 'per-sample maximum token budget throughout RL training' (budget control) [S1] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'sparsity scaling law'; attention-head count ablation ('doubling the attention heads yields only modest improvements ... 0.5% to 1.2%'); rephrasing vs multi-epoch ablation (Table 1) [S1] |
| Explicitly undisclosed | data composition per domain quantities; RL compute; MoE balancing hyper-parameters; whether MTP used |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S1 |

#### Kimi K2 Thinking

| Field | Value |
|---|---|
| Model | Kimi K2 Thinking |
| Lab | Moonshot AI |
| Release date | 2025-11-06 [S2] |
| Total / active params | same K2 backbone (1T total / 32B active), 256K context [S2] |
| Architecture family | MoE (K2 backbone) [S2] |
| Attention variant | MLA (inherited from K2) [S2] |
| MoE routing / balancing | inherited from K2 [S2] |
| Position encoding | inherited from K2 [S2] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | n/a (post-trained from K2) [S2] |
| Precision & QAT | 'we adopt Quantization-Aware Training (QAT) during the post-training phase, applying INT4 weight-only quantization to the MoE components ... native INT4 inference with a roughly 2x generation speed improvement' [S2] |
| Context-extension curriculum | '256k context window' [S2] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | 'End-to-end trained to interleave chain-of-thought reasoning with function calls' [S2] |
| RL algorithms | 'Specific training methods and datasets' undisclosed (DeepLearning.AI summary); blog gives no algorithm name [S2] |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | 'can execute up to 200 – 300 sequential tool calls without human interference' [S2] |
| Reasoning-effort control | 'heavy' reasoning mode mentioned by third parties; no explicit control mechanism disclosed [S2] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | RL algorithm, reward design, data; only INT4 QAT and tool-call scaling are disclosed |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S2 |

#### Kimi K2.5

| Field | Value |
|---|---|
| Model | Kimi K2.5 |
| Lab | Moonshot AI |
| Release date | 2026-01-27 (weights); report v1 2026-02-02 [S3] |
| Total / active params | '1T total / 32B activated' (Kimi K2 LM + 400M MoonViT-3D) [S3] |
| Architecture family | MoE, native multimodal: 'MoonViT-3D ... an MLP projector, and the Kimi K2 MoE language model' [S3] |
| Attention variant | MLA (K2 backbone) [S3] |
| MoE routing / balancing | '384 experts with 8 activated per token (sparsity of 48)' [S3] |
| Position encoding | inherited from K2 [S3] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | 'Kimi K2 employs the token-efficient MuonClip optimizer' (inherited) [S3] |
| Pre-training tokens | 'continual pretraining on approximately 15 trillion mixed visual and text tokens atop Kimi-K2-Base' [S3] |
| Precision & QAT | 'adopts the same native int4 quantization method as Kimi-K2-Thinking' [S3] |
| Context-extension curriculum | 256K context; 'K2.5 mixes text and vision tokens with a constant ratio throughout the entire training process' [S3] |
| Mid-training stage? | continual pretraining stage on ~15T mixed tokens [S3] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | 'zero-vision SFT—text-only SFT alone activates visual reasoning and tool use' [S3] |
| RL algorithms | 'Parallel-Agent Reinforcement Learning (PARL)': 'sub-agents are frozen ... only the orchestrator is updated'; joint text-vision RL; K2-style policy optimization [S3] |
| Reward sources | 'verifiable rewards'; 'Generative Reward Model (GRM)' [S3] |
| Async / off-policy RL | 'our RL framework treats every agent task as an independent asynchronous coroutine' [S3] |
| Agentic RL environment scale | 'agent swarm of up to 100 sub-agents, executing parallel workflows across up to 1,500 coordinated steps' [S3] |
| Reasoning-effort control | 'instant and thinking modes' [S3] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | vision-injection timing/ratio ablation ('early fusion with lower ratios tends to yield better results') [S3] |
| Explicitly undisclosed | policy-optimization loss specifics; RL compute; data mixture |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S3 |

#### Kimi K3

| Field | Value |
|---|---|
| Model | Kimi K3 |
| Lab | Moonshot AI |
| Release date | 2026-07-16 (API); weights by 2026-07-27; report v1 2026-07-27 [S4] |
| Total / active params | '2.8T parameter Mixture-of-Experts model with 104 billion activated parameters' ; 93 layers, 896 experts, 16 active + 2 shared [S4] |
| Architecture family | hybrid linear attention + latent MoE: 'Hybrid Attention combines three Kimi Delta Attention (KDA) layers with one Gated MLA layer in each block' ; 'Stable LatentMoE' [S4] |
| Attention variant | '69 KDA + 24 Gated MLA'; 'Attention Residuals (AttnRes) allows each layer to selectively attend to representations from all preceding layers' [S4] |
| MoE routing / balancing | 'Quantile Balancing derives expert allocation directly from router-score quantiles, eliminating heuristic updates and a sensitive balancing hyperparameter' [S4] |
| Position encoding | KDA recurrence carries position; MLA layers rotary (Gated MLA) [S4] |
| MTP | 'Kimi K3 is pre-trained with a multi-token-prediction (MTP) layer that mirrors the structure of a backbone block' (fine-tuned into EAGLE-3-style draft) [S4] |
| Optimizer | 'Per-Head Muon extends Muon by optimizing attention heads independently'; 'together with the weight-clipping mechanism introduced in Kimi K2' [S4] |
| Pre-training tokens | count not located; 'scaling-law studies to retune ... tokens-per-parameter ratio (TPP)'; 'cosine learning rate schedule with a 1% linear warmup' [S4] |
| Precision & QAT | 'MXFP4 weights with MXFP8 activations'; 'quantization-aware training (QAT) from the SFT stage onward' [S4] |
| Context-extension curriculum | 'four-stage curriculum. The window grows from 8K to 64K tokens during pre-training, and from 256K to 1M tokens during the cooldown phase' [S4] |
| Mid-training stage? | cooldown phase with long-context stages [S4] |
| Distillation (where, teacher) | 'Domain- and effort-specialized policies are consolidated into a unified model through multi-teacher on-policy distillation' (MOPD) [S4] |
| SFT | 'initializing baseline agent capabilities via supervised fine-tuning (SFT)' [S4] |
| RL algorithms | RL with per-problem budget control (K2 lineage); 'nine expert models' (3 domains x low/high/max); MOPD reward 'clip(sg(log pi_teacher/pi_theta), -R_max, R_max)' [S4] |
| Reward sources | verifiable environments; per-token OPD rewards from teachers [S4] |
| Async / off-policy RL | 'co-located system combines partial rollouts'; 'million-token agentic RL with persistent rollout and sandbox states' [S4] |
| Agentic RL environment scale | 'hundreds or thousands of tool calls and millions of accumulated context tokens'; 'resumable sandboxes' [S4] |
| Reasoning-effort control | 'reasoning_effort ... low, high, max'; RL 'override the task reward with -1 for trajectories whose total token budget T(y) exceeds a scaled threshold' [S4] |
| Model / expert merging | no weight merging; consolidation via MOPD [S4] |
| Continual / cross-stage distillation | MOPD consolidation of RL experts (cross-expert, on-policy) [S4] |
| Ablations / scaling laws | 'cosine decay consistently achieves a lower final loss than WSD' under separately tuned hyper-parameters; ~2.5x scaling-efficiency gain over K2 [S4] |
| Explicitly undisclosed | pretraining token count and compute; RL objective beyond budget rule; data mixture sizes |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S4 |

#### DeepSeek-V3.1

| Field | Value |
|---|---|
| Model | DeepSeek-V3.1 |
| Lab | DeepSeek |
| Release date | 2025-08-21 [S5] |
| Total / active params | 671B total / 37B active (same structure as V3) [S5] |
| Architecture family | MoE (DeepSeek-V3 architecture) [S5] |
| Attention variant | MLA (inherited) [S5] |
| MoE routing / balancing | aux-loss-free bias ('mlp.gate.e_score_correction_bias') inherited from V3 [S5] |
| Position encoding | RoPE within MLA (inherited) [S5] |
| MTP | inherited from V3 [S5] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | '840B tokens continued pretraining for long context extension on top of V3' [S5] |
| Precision & QAT | 'trained using the UE8M0 FP8 scale data format on both model weights and activations' [S5] |
| Context-extension curriculum | '32K extension phase has been increased 10-fold to 630B tokens, while the 128K extension phase has been extended by 3.3x to 209B tokens' [S5] |
| Mid-training stage? | long-context continued pretraining described [S5] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | 'Post-training boosts tool use and multi-step agent tasks' [S5] |
| RL algorithms | undisclosed (not addressed in the cited sources) |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | 'Hybrid inference: Think & Non-Think — one model, two modes' via chat template [S5] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | post-training algorithm, rewards, data; no technical report |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S5 |

#### DeepSeek-V3.2-Exp

| Field | Value |
|---|---|
| Model | DeepSeek-V3.2-Exp |
| Lab | DeepSeek |
| Release date | 2025-09-29 [S6] |
| Total / active params | 685B (HF) / 37B active; same backbone as V3.1-Terminus [S6,S7] |
| Architecture family | MoE + trained sparse attention: 'introducing DeepSeek Sparse Attention—a sparse attention mechanism' [S6] |
| Attention variant | DSA on MLA: 'lightning indexer and a fine-grained token selection mechanism'; 'implement DSA based on the MQA mode of MLA' [S7] |
| MoE routing / balancing | inherited (V3) [S6] |
| Position encoding | RoPE (indexer uses non-interleaved RoPE layout) [S6] |
| MTP | inherited [S6] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | continued pretraining: dense warm-up 2.1B tokens + sparse stage 943.7B tokens [S7] |
| Precision & QAT | indexer 'can be implemented in FP8' [S7] |
| Context-extension curriculum | starts from 128K checkpoint [S7] |
| Mid-training stage? | DSA continued pre-training [S7] |
| Distillation (where, teacher) | 'specialist distillation and mixed RL training' [S7] |
| SFT | specialist SFT data [S7] |
| RL algorithms | GRPO (same pipeline as V3.2) [S7] |
| Reward sources | see V3.2 [S7] |
| Async / off-policy RL | see V3.2 [S7] |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | think/non-think modes [S6] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'deliberately aligned the training configurations of DeepSeek-V3.2-Exp with V3.1-Terminus' parity study [S6] |
| Explicitly undisclosed | training compute; hyper-parameters beyond DSA stage |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S6, S7 |

#### DeepSeek-V3.2 (and V3.2-Speciale)

| Field | Value |
|---|---|
| Model | DeepSeek-V3.2 (and V3.2-Speciale) |
| Lab | DeepSeek |
| Release date | 2025-12-01 (weights); report v1 2025-12-02 [S7] |
| Total / active params | 671B / 37B active (V3 backbone) [S7] |
| Architecture family | MoE + DSA: 'the only architectural modification of DeepSeek-V3.2 is the introduction of DeepSeek Sparse Attention (DSA) through continued training' [S7] |
| Attention variant | DSA: 'retrieves only the key-value entries corresponding to the top-k index scores' (k=2048) [S7] |
| MoE routing / balancing | inherited V3 aux-loss-free; RL 'Keep Routing' [S7] |
| Position encoding | RoPE in MLA [S7] |
| MTP | inherited [S7] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | DSA continued pre-training '15000 steps, with each step consisting of 480 sequences of 128K tokens, resulting in a total of 943.7B tokens' [S7] |
| Precision & QAT | lightning indexer 'can be implemented in FP8' [S7] |
| Context-extension curriculum | 'Starting from a base checkpoint of DeepSeek-V3.1-Terminus, whose context length has been extended to 128K' [S7] |
| Mid-training stage? | yes (DSA continued pre-training) [S7] |
| Distillation (where, teacher) | 'Specialist Distillation: For each task, we initially develop a specialized model'; distilled data then RL [S7] |
| SFT | SFT on distilled specialist data [S7] |
| RL algorithms | 'we still adopt Group Relative Policy Optimization (GRPO)'; 'Unbiased KL Estimate'; 'Off-Policy Sequence Masking'; 'Keep Routing'; 'Keep Sampling Mask' [S7] |
| Reward sources | 'rule-based outcome reward, length penalty, and language consistency reward. For general tasks, we employ a generative reward model where each prompt has its own rubrics' [S7] |
| Async / off-policy RL | 'we mask negative sequences that introduce significant policy divergence'; multi-minibatch off-policy updates [S7] |
| Agentic RL environment scale | 'Large-Scale Agentic Task Synthesis Pipeline'; search, coding, Jupyter, synthesized environments [S7] |
| Reasoning-effort control | think/non-think; Speciale = high-compute variant [S7] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | post-training compute >10% of pre-training (stated); parity evaluation vs V3.1-Terminus [S7] |
| Explicitly undisclosed | RL compute totals; hyper-parameters delta, beta |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S7 |

#### DeepSeek-V4 (Pro / Flash, preview)

| Field | Value |
|---|---|
| Model | DeepSeek-V4 (Pro / Flash, preview) |
| Lab | DeepSeek |
| Release date | 2026-04-24 (weights); arXiv 2606.19348 [S8] |
| Total / active params | 'DeepSeek-V4-Pro with 1.6T parameters (49B activated) and DeepSeek-V4-Flash with 284B parameters (13B activated)' [S8] |
| Architecture family | MoE + hybrid compressed/sparse attention + mHC residuals [S8] |
| Attention variant | 'hybrid attention mechanism combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA). CSA compresses the KV caches along the sequence dimension and then performs DeepSeek Sparse Attention (DSA)' [S8] |
| MoE routing / balancing | DeepSeekMoE; 'Hash-MoE bootstrap' first layers ('frozen tid2eid lookup'); scoring 'sqrtsoftplus' (HF config) [S8] |
| Position encoding | RoPE (rope_theta 10000; compressed branches 160000 with YaRN) [S8] |
| MTP | 'retain the DeepSeekMoE framework and Multi-Token Prediction (MTP) strategy' [S8] |
| Optimizer | 'we introduce the Muon optimizer to the training of DeepSeek-V4 series, leading to faster convergence and improved training stability' [S8] |
| Pre-training tokens | 'we train DeepSeek-V4-Flash on 32T tokens and DeepSeek-V4-Pro on 33T tokens' [S8] |
| Precision & QAT | 'the routed expert parameters utilize FP4 precision'; 'during the post-training stage, we incorporate FP4 quantization-aware training for MoE expert weights and the indexer QK path' [S8] |
| Context-extension curriculum | 'After pre-training, these two models can natively and efficiently support 1M-length contexts' [S8] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | 'unified model consolidation via on-policy distillation ... the unified model acts as the student learning to optimize the reverse KL loss with teacher models' [S8] |
| SFT | 'The base model first undergoes Supervised Fine-Tuning (SFT) on high-quality, domain-specific data' per expert [S8] |
| RL algorithms | 'Reinforcement Learning (RL) is applied using Group Relative Policy Optimization (GRPO)' per domain expert [S8] |
| Reward sources | 'reward models tailored to specific success criteria' [S8] |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | agent expert domain; details not fetched [S8] |
| Reasoning-effort control | 'three reasoning modes: Non-think, Think High, and Think Max' [S8] |
| Model / expert merging | no weight merging; OPD consolidation [S8] |
| Continual / cross-stage distillation | OPD consolidation of experts [S8] |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | training compute; balancing hyper-parameters; RL environments |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S8 |

#### DeepSeek-R1 / R1-Zero

| Field | Value |
|---|---|
| Model | DeepSeek-R1 / R1-Zero |
| Lab | DeepSeek |
| Release date | 2025-01-20 (weights); arXiv v1 2025-01-22; Nature 2025-09-17 [S9] |
| Total / active params | 671B / 37B active (DeepSeek-V3-Base) [S9] |
| Architecture family | MoE (V3 backbone) [S9] |
| Attention variant | MLA (V3) [S9] |
| MoE routing / balancing | inherited V3 [S9] |
| Position encoding | inherited [S9] |
| MTP | inherited [S9] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | n/a (post-trained from V3-Base) [S9] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | 128K [S9] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | 'six dense models (1.5B, 7B, 8B, 14B, 32B, 70B) distilled from DeepSeek-R1 based on Qwen and Llama' using 800k samples (SFT-style) [S9] |
| SFT | 'thousands of cold-start data'; second SFT via rejection sampling [S9] |
| RL algorithms | 'use Group Relative Policy Optimization (GRPO) as our RL framework' [S9] |
| Reward sources | 'rule-based reward system to compute accuracy and format rewards'; 'model-based rewards for general data'; 'language consistency reward' [S9] |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | distillation vs RL on Qwen-32B ('direct distillation from DeepSeek-R1 outperforms applying RL on it') [S9] |
| Explicitly undisclosed | RL infrastructure details (Supplementary); compute |
| Peer-reviewed venue | Nature 645, 633–638 (2025), peer reviewed ('Nature thanks Edward Beeching, Yarin Gal ...') [S9] |
| Evidence tier | A (Nature) + C (arXiv report) |
| Verified? | yes |
| Sources | S9 |

#### GLM-4.5 / GLM-4.5-Air

| Field | Value |
|---|---|
| Model | GLM-4.5 / GLM-4.5-Air |
| Lab | Zhipu AI / Z.ai |
| Release date | 2025-07-28 (weights); report v1 2025-08-08 [S10] |
| Total / active params | '355 billion total parameters with 32 billion active'; Air 106B/12B [S10] |
| Architecture family | MoE (deeper, narrower): 'we reduce the width ... and increase its height (number of layers)' [S10] |
| Attention variant | 'Grouped-Query Attention with partial RoPE ... 96 heads for a 5120 hidden dimension'; 'QK-Norm' [S10] |
| MoE routing / balancing | 'loss-free balance routing and sigmoid gates'; 'bias update rate to 0.001 for the first 15T tokens, and to 0.0 for the remaining'; 'auxiliary sequence-level balance loss with a 0.0001 weight' [S10] |
| Position encoding | partial RoPE; base 10,000 -> 1,000,000 at 32K [S10] |
| MTP | 'we add an MoE layer as the MTP (Multi-Token Prediction) layer'; 'MTP loss weight ... 0.3 ... to 0.1' [S10] |
| Optimizer | 'We employed the Muon optimizer for all parameters except word embedding, bias, and weights for RMSNorm' [S10] |
| Pre-training tokens | 23T (blog for GLM-5 comparison: 'increases pre-training data from 23T to 28.5T'); 'cosine decay schedule ... instead of warmup-stable-decay (WSD)' [S10,S12] |
| Precision & QAT | 'BF16 for training while leveraging FP8 for inference to accelerate the data generation phase' (RL rollouts) [S10] |
| Context-extension curriculum | '4,096 during pre-training, and extended it to 32,768 and 131,072 during the mid-training stage' [S10] |
| Mid-training stage? | yes, explicitly named mid-training stage [S10] |
| Distillation (where, teacher) | 'stage 2 (Unified Training), we employ self-distillation techniques to integrate multiple experts'; 'Iterative Distillation' of RL-trained agent model into SFT [S10] |
| SFT | SFT cold start in expert stage; SFT distillation in unified stage [S10] |
| RL algorithms | GRPO-family with 'dynamic sampling temperatures ... and adaptive clipping'; 'single-stage RL over the full 64K context with a difficulty-based curriculum' [S10] |
| Reward sources | verifiable QA and 'execution-based feedback on real-world SWE tasks' [S10] |
| Async / off-policy RL | slime: 'disaggregated, asynchronous model' for agentic tasks; synchronous colocated for reasoning [S10] |
| Agentic RL environment scale | 'high-concurrency Docker-based runtime that provisions isolated environments for each task' [S10] |
| Reasoning-effort control | thinking / non-thinking modes [S10] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | expert self-distillation into unified model [S10] |
| Ablations / scaling laws | WSD vs cosine ('models trained with the WSD schedule perform worse on general benchmarks'); head-count observation [S10] |
| Explicitly undisclosed | exact RL objective; pretraining token count in report body (blog gives 23T) |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S10, S12 |

#### GLM-4.7 (and 4.7-Flash)

| Field | Value |
|---|---|
| Model | GLM-4.7 (and 4.7-Flash) |
| Lab | Z.ai |
| Release date | 2025-12-22 [S11] |
| Total / active params | same architecture family as GLM-4.5 (355B-A32B); Flash smaller [S11] |
| Architecture family | MoE (GLM-4.5 lineage; HF card cites GLM-4.5 report) [S11] |
| Attention variant | as GLM-4.5 [S11] |
| MoE routing / balancing | as GLM-4.5 [S11] |
| Position encoding | as GLM-4.5 [S11] |
| MTP | MTP layers used for speculative decoding in serving [S10,S11] |
| Optimizer | as GLM-4.5 (Muon) [S11] |
| Pre-training tokens | undisclosed (not addressed in the cited sources) |
| Precision & QAT | FP8 checkpoints [S11] |
| Context-extension curriculum | undisclosed (not addressed in the cited sources) |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | blog: 'think before acting' mechanism; no algorithm disclosed [S11] |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | slime (framework stated by slime docs) [S15] |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | thinking modes [S11] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | nearly all training details; only benchmarks and deployment are published |
| Peer-reviewed venue | none |
| Evidence tier | C (blog only) |
| Verified? | yes |
| Sources | S11 |

#### GLM-5

| Field | Value |
|---|---|
| Model | GLM-5 |
| Lab | Z.ai |
| Release date | 2026-02-11/12 (weights); report v1 2026-02-17 [S12] |
| Total / active params | '744B parameters (40B active)' [S12] |
| Architecture family | MoE + DSA: 'GLM-5 adopts DSA to significantly reduce training and inference costs' [S12] |
| Attention variant | MLA with DSA; 'Muon Split ... split these matrices into smaller matrices for different heads and apply matrix orthogonalization' [S12] |
| MoE routing / balancing | as GLM-4.5 (loss-free balance + sigmoid) [S12] |
| Position encoding | partial RoPE (MLA) [S12] |
| MTP | 'we propose sharing the parameters of 3 MTP layers during training' [S12] |
| Optimizer | Muon with 'Muon Split' per-head orthogonalization; 'the scale of attention logits of GLM-5 remains stable during pre-training without any clipping strategy' [S12] |
| Pre-training tokens | 'Base Model training began with a massive 27 trillion token corpus' (report); blog: '28.5T tokens' [S12] |
| Precision & QAT | 'GLM-5 uses FP8 for rollout inference' [S12] |
| Context-extension curriculum | 'Mid-training phase to progressively extend context length from 4K to 200K' [S12] |
| Mid-training stage? | yes: 'distinct Mid-training phase ... focusing specifically on long-context agentic data' [S12] |
| Distillation (where, teacher) | 'On-Policy Cross-Stage Distillation throughout this process to prevent catastrophic forgetting' [S12] |
| SFT | SFT then sequential RL [S12] |
| RL algorithms | 'sequential Reinforcement Learning pipeline—starting with Reasoning RL, followed by Agentic RL, and finishing with General RL'; 'Direct Double-sided Importance Sampling, which applies a token-level clipping mechanism ([1-eps_l, 1+eps_h])' [S12] |
| Reward sources | 'verifiable training environments across three domains: over 10K real-world Software Engineering (SWE), terminal tasks, and high-difficulty multi-hop search tasks' [S12] |
| Async / off-policy RL | 'fully asynchronous training paradigm for Agentic RL'; 'We discard a sample if its oldest rollout version is too stale'; 'reset the optimizer after each weight update of the inference engine'; 'Token-in-Token-out (TITO) gateway' [S12] |
| Agentic RL environment scale | 'over 10K real-world Software Engineering (SWE), terminal tasks' [S12] |
| Reasoning-effort control | 'reasoning_effort' parameter with Max/High levels (GitHub) [S12] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | 'On-Policy Cross-Stage Distillation' (explicit) [S12] |
| Ablations / scaling laws | MLA-vs-GQA-8 under Muon (Table 1); MTP acceptance length vs DeepSeek-V3.2 (Table 2) [S12] |
| Explicitly undisclosed | exact token count reconciliation (27T vs 28.5T); RL compute |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S12 |

#### GLM-5.1

| Field | Value |
|---|---|
| Model | GLM-5.1 |
| Lab | Z.ai |
| Release date | 2026-04-07 [S13] |
| Total / active params | 744B-A40B (GitHub table; VentureBeat: 754B) [S13] |
| Architecture family | MoE + DSA (GLM-5 base) [S13] |
| Attention variant | as GLM-5 [S13] |
| MoE routing / balancing | as GLM-5 [S13] |
| Position encoding | as GLM-5 [S13] |
| MTP | 'MTP step parameters are shared as in GLM-5.1' (GLM-5.2 blog) [S14] |
| Optimizer | as GLM-5 [S13] |
| Pre-training tokens | undisclosed (not addressed in the cited sources) |
| Precision & QAT | FP8 checkpoint [S13] |
| Context-extension curriculum | 200K context [S13] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | 'Built with multi-turn SFT, RL, and a process-quality evaluation framework' (docs.z.ai) [S13] |
| RL algorithms | RL (unnamed; slime) [S13,S15] |
| Reward sources | 'process-quality evaluation framework' [S13] |
| Async / off-policy RL | slime asynchronous [S15] |
| Agentic RL environment scale | 'sustains optimization over hundreds of rounds and thousands of tool calls' [S13] |
| Reasoning-effort control | thinking effort levels (API) [S13] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | algorithm, data, compute (blog only) |
| Peer-reviewed venue | none |
| Evidence tier | C (blog) |
| Verified? | yes |
| Sources | S13, S14 |

#### GLM-5.2

| Field | Value |
|---|---|
| Model | GLM-5.2 |
| Lab | Z.ai |
| Release date | 2026-06-16 [S14] |
| Total / active params | 744B-A40B (753B checkpoint tensors per SemiAnalysis) [S14] |
| Architecture family | MoE + DSA with IndexShare [S14] |
| Attention variant | 'IndexShare, which reuses the same indexer across every four sparse attention layers, reducing per-token FLOPs by 2.9x at a 1M context length' [S14] |
| MoE routing / balancing | as GLM-5 [S14] |
| Position encoding | as GLM-5 [S14] |
| MTP | 'improve GLM-5.2's MTP layer for speculative decoding, increasing the acceptance length by up to 20%' (ablation 4.56 -> 5.47) [S14] |
| Optimizer | as GLM-5 [S14] |
| Pre-training tokens | undisclosed (not addressed in the cited sources) |
| Precision & QAT | FP8 checkpoint [S14] |
| Context-extension curriculum | 'trained with IndexShare from mid-training with 128K sequence length'; 'solid 1M-token context' [S14] |
| Mid-training stage? | yes (IndexShare from mid-training) [S14] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | 'SAO for RL on long-horizon tasks' with compaction (named in GLM-5.3 blog) [S15] |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | slime asynchronous [S15] |
| Agentic RL environment scale | long-horizon environments [S15] |
| Reasoning-effort control | 'multiple thinking effort levels' (High, Max) [S14] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | MTP acceptance-length ablation [S14] |
| Explicitly undisclosed | SAO definition; data; compute |
| Peer-reviewed venue | none |
| Evidence tier | C (blog + model card) |
| Verified? | yes |
| Sources | S14, S15 |

#### GLM-5.3 (and 5.3-Flash)

| Field | Value |
|---|---|
| Model | GLM-5.3 (and 5.3-Flash) |
| Lab | Z.ai |
| Release date | 2026-08-14 (API); weights promised ~2 weeks later [S15] |
| Total / active params | 744B-A40B; Flash 320B-A18B [S15] |
| Architecture family | MoE + DSA/IndexShare (GLM-5.2 base) [S15] |
| Attention variant | as GLM-5.2 [S15] |
| MoE routing / balancing | as GLM-5 [S15] |
| Position encoding | as GLM-5 [S15] |
| MTP | as GLM-5.2 [S15] |
| Optimizer | as GLM-5 [S15] |
| Pre-training tokens | 'It uses the same base model as GLM-5.2 — every gain comes from post-training' [S15] |
| Precision & QAT | FP8 checkpoint planned [S15] |
| Context-extension curriculum | 1M context (inherited) [S15] |
| Mid-training stage? | n/a (post-training only) [S15] |
| Distillation (where, teacher) | slime adds 'top-k and full-vocabulary OPD'; 'multi-teacher OPD: with dynamic teacher switching and prefetching' [S15] |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | 'SAO with compaction'; 'R3-style setups and full numerical alignment between the training and rollout paths' [S15] |
| Reward sources | 'reliable binary rewards' from verified synthesized environments (Tabbit summary of blog) [S15] |
| Async / off-policy RL | 'slime for large-scale asynchronous training'; 'average difference in log probabilities (logprob) was controlled at the 1e-7 level' [S15] |
| Agentic RL environment scale | 'more environments, more diverse tasks'; RL throughput 'improved end-to-end RL training throughput by more than 2.3x' [S15] |
| Reasoning-effort control | effort levels low/high/max (docs) [S15] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | multi-teacher OPD support stated [S15] |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | SAO algorithm; environment counts; compute |
| Peer-reviewed venue | none |
| Evidence tier | C (blog) |
| Verified? | yes |
| Sources | S15 |

### Qwen / MiniMax / Meta / OpenAI-oss / Google open / Mistral / NVIDIA

#### Qwen3 (235B-A22B, 30B-A3B, dense 0.6B–32B)

| Field | Value |
|---|---|
| Model | Qwen3 (235B-A22B, 30B-A3B, dense 0.6B–32B) |
| Lab | Alibaba Qwen |
| Release date | 2025-04-29 (weights); report v1 2025-05-14 [S16] |
| Total / active params | 'parameter scales ranging from 0.6 to 235 billion'; MoE '128 total experts with 8 activated experts per token' [S16] |
| Architecture family | dense + MoE (fine-grained, no shared experts) [S16] |
| Attention variant | 'Grouped Query Attention (GQA), SwiGLU, Rotary Positional Embeddings (RoPE)' with QK-Norm [S16] |
| MoE routing / balancing | 'we adopt the global-batch load balancing loss (Qiu et al., 2025) to encourage expert specialization' (auxiliary loss, not loss-free) [S16] |
| Position encoding | RoPE; 'increase the base frequency of RoPE from 10,000 to 1,000,000 using the ABF technique'; 'YARN and Dual Chunk Attention (DCA) to achieve a four-fold increase in sequence length' [S16] |
| MTP | not used in Qwen3 (introduced later in Qwen3-Next) [S17] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | 'pre-trained on 36 trillion tokens covering up to 119 languages and dialects' [S16] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | three-stage pretraining; final long-context stage to 32K (4x via YaRN+DCA to 128K) [S16] |
| Mid-training stage? | stage-wise pretraining (reasoning stage, long-context stage) [S16] |
| Distillation (where, teacher) | 'Strong-to-Weak Distillation ... off-policy and on-policy knowledge transfer from larger models'; on-policy 'aligning its logits with those of a teacher model (Qwen3-32B or Qwen3-235B-A22B)' [S16] |
| SFT | 'Long-CoT Cold Start'; 'Thinking Mode Fusion' via continual SFT [S16] |
| RL algorithms | 'employed GRPO (Shao et al., 2024) to update the model parameters' (Reasoning RL); later Qwen3 updates used GSPO ('GSPO ... contributed to the remarkable improvements in the latest Qwen3 models') [S16] |
| Reward sources | 'rule-based rewards' (reasoning RL); general RL 'across more than 20 general-domain tasks' [S16] |
| Async / off-policy RL | GSPO paper notes Routing Replay used under GRPO for MoE [S16] |
| Agentic RL environment scale | general RL includes 'agent capabilities' [S16] |
| Reasoning-effort control | 'thinking budget mechanism'; stop-thinking instruction inserted at threshold ('not explicitly trained but emerges naturally') [S16] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'distillation achieves significantly better performance than reinforcement learning while requiring approximately only 1/10 of the GPU hours' (Table 21); thinking-budget scaling curves [S16] |
| Explicitly undisclosed | optimizer, precision, pretraining hyper-parameters |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S16 |

#### Qwen3-Next-80B-A3B

| Field | Value |
|---|---|
| Model | Qwen3-Next-80B-A3B |
| Lab | Alibaba Qwen |
| Release date | 2025-09-11/12 [S17] |
| Total / active params | '80B total parameters, but only ~3B activated'; 512 experts, 10 routed + 1 shared [S17] |
| Architecture family | hybrid linear attention MoE: 'Gated DeltaNet + Gated Attention' 3:1 [S17] |
| Attention variant | 'mix Gated DeltaNet with standard attention at a 3:1 ratio'; output gating; head dim 256 [S17] |
| MoE routing / balancing | 'with global load balancing [4], increasing total expert parameters while keeping activated experts fixed steadily reduces training loss' [S17] |
| Position encoding | 'Apply rotary position encoding only to the first 25% of position dimensions' [S17] |
| MTP | 'native Multi-Token Prediction (MTP) ... multi-step training that maintains consistency between training and inference' [S17] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | 'Trained on a 15 trillion-token subset of Qwen3's 36 trillion-token pre-training corpus' [S17] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | 'natively supports context lengths of up to 262,144 tokens'; YaRN to 1M validated [S17] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | 'We solve the long-standing stability and efficiency issues in reinforcement learning (RL) training caused by the hybrid attention + high-sparsity MoE architecture' (algorithm unnamed) [S17] |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | Instruct and Thinking variants [S17] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'Zero-Centered RMSNorm, and applies weight decay to norm weights'; Gated DeltaNet vs SWA/Mamba2 comparison stated [S17] |
| Explicitly undisclosed | optimizer; RL algorithm; post-training data |
| Peer-reviewed venue | none |
| Evidence tier | C (blog + model card) |
| Verified? | yes |
| Sources | S17 |

#### Qwen3.5 (397B-A17B flagship; 122B-A10B, 35B-A3B, 27B, small)

| Field | Value |
|---|---|
| Model | Qwen3.5 (397B-A17B flagship; 122B-A10B, 35B-A3B, 27B, small) |
| Lab | Alibaba Qwen |
| Release date | 2026-02-16 [S18] |
| Total / active params | '397 billion total parameters, just 17 billion are activated per forward pass'; 512 experts, '10 Routed + 1 Shared' [S18] |
| Architecture family | hybrid linear attention MoE, native VLM: 'fuses linear attention (via Gated Delta Networks) with a sparse mixture-of-experts' [S18] |
| Attention variant | '15 * (3 * (Gated DeltaNet -> MoE) -> 1 * (Gated Attention -> MoE))'; 'Number of Attention Heads: 32 for Q and 2 for KV' [S18] |
| MoE routing / balancing | inherited Qwen3-Next design (global load balancing) [S17,S18] |
| Position encoding | 'Rotary Position Embedding Dimension: 64' (partial RoPE) [S18] |
| MTP | 'MTP: trained with multi-steps' [S18] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | 'Early fusion training on trillions of multimodal tokens' (count undisclosed) [S18] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | '262,144 natively and extensible up to 1,010,000 tokens' [S18] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | Qwen3.5-Omni report (same base): 'Specialist Distillation' + 'On-Policy Distillation' stages [S18] |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | 'Reinforcement learning scaled across million-agent environments'; Omni report: 'adopt GSPO ... to further improve overall capability'; DPO also used [S18] |
| Reward sources | 'rule-based rewards' (Omni report) [S18] |
| Async / off-policy RL | 'asynchronous RL frameworks supporting massive-scale agent scaffolds and environment orchestration' [S18] |
| Agentic RL environment scale | 'RL environment scaling ... virtually all RL tasks and environments we could conceive' [S18] |
| Reasoning-effort control | thinking / instant modes; adaptive tool use (Plus) [S18] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'Additional scaling results ... will be detailed in our upcoming technical report' (none found by 2026-09-05) [S18] |
| Explicitly undisclosed | pretraining token count, optimizer, precision, RL algorithm for the LLM itself (only Omni sibling names GSPO) |
| Peer-reviewed venue | none |
| Evidence tier | C (blog + model card; no LLM tech report found) |
| Verified? | yes |
| Sources | S18 |

#### Qwen3.8-27B (and Qwen3.8-2.4T-A95B hosted)

| Field | Value |
|---|---|
| Model | Qwen3.8-27B (and Qwen3.8-2.4T-A95B hosted) |
| Lab | Alibaba Qwen |
| Release date | 2026-08-14 [S19] |
| Total / active params | 27B dense (open); 'Qwen3.8-2.4T-A95B' hosted [S19] |
| Architecture family | hybrid linear attention dense: '16 x (3 x (Gated DeltaNet -> FFN) -> 1 x (Gated Attention -> FFN))' [S19] |
| Attention variant | Gated DeltaNet + Gated Attention; '24 for Q and 4 for KV' [S19] |
| MoE routing / balancing | n/a (dense open model) [S19] |
| Position encoding | 'Rotary Position Embedding Dimension: 64' [S19] |
| MTP | 'MTP (Multi-Token Prediction): trained with multiple steps' [S19] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | undisclosed (not addressed in the cited sources) |
| Precision & QAT | FP8 checkpoint offered [S19] |
| Context-extension curriculum | '262,144 natively and extensible up to 1,000,000 tokens' [S19] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | undisclosed (not addressed in the cited sources) |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | 'reasoning_effort' dial with 'xhigh (default), medium, and low' [S19] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | all training details (model card only) |
| Peer-reviewed venue | none |
| Evidence tier | C (model card) |
| Verified? | yes |
| Sources | S19 |

#### MiniMax-M1 (40k/80k)

| Field | Value |
|---|---|
| Model | MiniMax-M1 (40k/80k) |
| Lab | MiniMax |
| Release date | 2025-06-16 [S20] |
| Total / active params | '456 billion parameters with 45.9 billion parameters activated per token' (MiniMax-Text-01 base) [S20] |
| Architecture family | hybrid linear attention MoE: 'hybrid Mixture-of-Experts (MoE) architecture combined with a lightning attention mechanism' [S20] |
| Attention variant | lightning (linear) attention with periodic softmax attention (7:1 per Step-3 description of 'MM M1 ... 70 layers of linear attention and 10 layers of GQA full attention') [S20,S41] |
| MoE routing / balancing | 32 experts (inherited Text-01) [S20] |
| Position encoding | inherited [S20] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | 'We employ the AdamW optimizer'; 'FP32 precision for the LM output head' fix [S20] |
| Pre-training tokens | n/a (continued from Text-01; 7.5T continued pretraining in report) [S20] |
| Precision & QAT | LM head FP32 for RL stability [S20] |
| Context-extension curriculum | 'natively supports a context length of 1 million tokens'; RL length ramp to 80K [S20] |
| Mid-training stage? | continued pretraining + SFT cold start [S20] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | long-CoT SFT to 'inject certain chain-of-thought (CoT) patterns' [S20] |
| RL algorithms | 'CISPO clips importance sampling weights rather than token updates'; 'no KL penalty term'; dynamic sampling and length penalty from DAPO [S20] |
| Reward sources | 'rule-based verifiers ... or from a reward model'; 'sandbox-based, real-world software engineering environments' [S20] |
| Async / off-policy RL | '16 rounds of off-policy updates per generation batch' [S20] |
| Agentic RL environment scale | 'complete RL training completed in three weeks using 512 H800 GPUs' [S20] |
| Reasoning-effort control | 40k and 80k output-length variants [S20] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | CISPO vs GRPO/DAPO on Qwen2.5-32B ('2x speedup compared to DAPO') [S20] |
| Explicitly undisclosed | pretraining recipe of base; reward model details |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S20 |

#### MiniMax-M2 (series M2 -> M2.1 -> M2.5 -> M2.7)

| Field | Value |
|---|---|
| Model | MiniMax-M2 (series M2 -> M2.1 -> M2.5 -> M2.7) |
| Lab | MiniMax |
| Release date | 2025-10-27 (M2); series report v1 2026-05-26 [S21] |
| Total / active params | '229.9B total parameters with only 9.8B activated per token'; 62 layers; 256 experts, 8 active [S21] |
| Architecture family | MoE, full attention: 'full multi-head attention across all layers ... 48 query heads and 8 key-value heads (GQA)' — 'departs from the hybrid attention mechanisms explored in MiniMax-Text-01' [S21] |
| Attention variant | GQA full attention; RoPE throughout [S21] |
| MoE routing / balancing | 'sigmoid gating with learnable expert-specific bias terms, which improves load balancing while greatly reducing reliance on auxiliary losses' [S21] |
| Position encoding | 'Rotary Position Embeddings (RoPE) are applied throughout the model' [S21] |
| MTP | 'single MTP module (K=1) ... MTP loss weight of 0.3, which is annealed to 0.1'; expanded to K=3 'via weight copying' in decay phase [S21] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | 'pre-trained on 29.2T tokens with a maximum context length of 192K' [S21] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | '192K-token native context window' via progressive long-context training [S21] |
| Mid-training stage? | continued pre-training decay phase (MTP expansion) [S21] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | agent-driven data pipelines (SFT + RL) [S21] |
| RL algorithms | CISPO in Forge: 'We use CISPO as the core algorithm'; 'Unified Mixed-Domain Training'; 'Reward-to-go' [S21] |
| Reward sources | 'artifact-aligned reward'; 'Process Reward'; 'Task Completion Time Reward' [S21] |
| Async / off-policy RL | 'Windowed FIFO' scheduling; 'prefix tree merging ... up to 40x training speedup'; asynchronous controller [S21] |
| Agentic RL environment scale | 'over a hundred thousand distinct real-world agent scaffolds and environments' (M2.5) [S21,S22] |
| Reasoning-effort control | interleaved thinking [S21] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'MTP consistently improves model performance across benchmarks' (Table 1); hybrid vs full attention preference stated [S21] |
| Explicitly undisclosed | optimizer, precision, pretraining schedule |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S21, S22 |

#### MiniMax-M2.5

| Field | Value |
|---|---|
| Model | MiniMax-M2.5 |
| Lab | MiniMax |
| Release date | 2026-02-12 [S22] |
| Total / active params | M2 backbone (230B/10B active) [S22] |
| Architecture family | MoE (M2) [S22] |
| Attention variant | as M2 [S22] |
| MoE routing / balancing | as M2 [S22] |
| Position encoding | as M2 [S22] |
| MTP | MTP heads co-trained in RL ('Top-K KL loss') [S21] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | as M2 [S22] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | 200K RL context [S21] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | CISPO (Forge blog) [S21] |
| Reward sources | composite: process reward, completion-time reward, verifiable [S21] |
| Async / off-policy RL | Windowed FIFO asynchronous controller [S21] |
| Agentic RL environment scale | 'Extensively trained with reinforcement learning in hundreds of thousands of complex real-world environments' [S22] |
| Reasoning-effort control | 'Trained to reason efficiently'; Lightning variant [S22] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | everything beyond RL-system description |
| Peer-reviewed venue | none |
| Evidence tier | C (blog) |
| Verified? | yes |
| Sources | S22, S21 |

#### MiniMax-M3

| Field | Value |
|---|---|
| Model | MiniMax-M3 |
| Lab | MiniMax |
| Release date | 2026-06-01 (API); weights ~2026-06-11; MSA paper v1 2026-06-11 [S23] |
| Total / active params | '~428B parameters and ~23B activated parameters' [S23] |
| Architecture family | MoE + trained block-sparse attention, native multimodal: 'M3 is powered by MiniMax Sparse Attention (MSA)' [S23] |
| Attention variant | 'blockwise sparse attention built upon Grouped Query Attention (GQA). A lightweight Index Branch scores key–value blocks and independently selects a Top-k subset for each GQA group' [S23] |
| MoE routing / balancing | MSA ablation model: '128 routed experts, 1 shared expert, and top-4' (109B proxy) [S23] |
| Position encoding | RoPE (RoPE dim 64 in proxy) [S23] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | count for M3 undisclosed; proxy '3T tokens' [S23] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | '1M context'; MSA-CPT '~140B tokens of long-context training' in proxy [S23] |
| Mid-training stage? | 'mixed-modality training from Step 0' [S23] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | not in MSA paper (Forge/CISPO lineage assumed, not stated) [S23] |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'extensive ablations scaling up to a 109B-parameter MoE model with native multi modal training'; MSA-PT vs MSA-CPT vs Full [S23] |
| Explicitly undisclosed | M3-specific pretraining tokens, optimizer, post-training |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S23 |

#### Llama 4 (Scout 109B-A17B, Maverick 400B-A17B; Behemoth preview)

| Field | Value |
|---|---|
| Model | Llama 4 (Scout 109B-A17B, Maverick 400B-A17B; Behemoth preview) |
| Lab | Meta |
| Release date | 2025-04-05 [S24] |
| Total / active params | Scout '17 billion active parameters, 16 experts, and 109 billion total'; Maverick '17B active parameters and 400B total' [S24] |
| Architecture family | MoE, early-fusion multimodal: 'alternating dense and mixture-of-experts (MoE) layers' [S24] |
| Attention variant | 'interleaved attention layers without positional embeddings' (iRoPE); chunked attention (8192) in RoPE layers; 'inference time temperature scaling of attention' [S24] |
| MoE routing / balancing | '128 routed experts and a shared expert. Each token is sent to the shared expert and also to one of the 128 routed experts' [S24] |
| Position encoding | iRoPE: NoPE every 4th layer, RoPE elsewhere [S24] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | 'MetaP that allows us to reliably set critical model hyper-parameters such as per-layer learning rates and initialization scales' [S24] |
| Pre-training tokens | 'more than 30 trillion tokens'; model card: Scout '~40T', Maverick '~22T' [S24] |
| Precision & QAT | 'pre-training our Llama 4 Behemoth model using FP8 and 32K GPUs, we achieved 390 TFLOPs/GPU' [S24] |
| Context-extension curriculum | 'Llama 4 Scout is both pre-trained and post-trained with a 256K context length' [S24] |
| Mid-training stage? | mid-training for long context (blog/model card) [S24] |
| Distillation (where, teacher) | 'codistilled the Llama 4 Maverick model from Llama 4 Behemoth ... novel distillation loss function that dynamically weights the soft and hard targets' [S24] |
| SFT | 'lightweight supervised fine-tuning (SFT) > online reinforcement learning (RL) > lightweight direct preference optimization (DPO)' [S24] |
| RL algorithms | 'continuous online RL strategy'; 'dynamically filtering out prompts with zero advantage' [S24] |
| Reward sources | 'Llama models as a judge' for difficulty; pass@k curriculum [S24] |
| Async / off-policy RL | 'fully asynchronous online RL training framework' (~10x efficiency) [S24] |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'hyper-parameters transfer well across different values of batch size, model width, depth, and training tokens' [S24] |
| Explicitly undisclosed | RL algorithm name, rewards, hyper-parameters; no technical report |
| Peer-reviewed venue | none |
| Evidence tier | C (blog + model card) |
| Verified? | yes |
| Sources | S24 |

#### gpt-oss-120b / gpt-oss-20b

| Field | Value |
|---|---|
| Model | gpt-oss-120b / gpt-oss-20b |
| Lab | OpenAI |
| Release date | 2025-08-05 [S25] |
| Total / active params | '116.8B total parameters and 5.1B active'; 20.9B/3.6B [S25] |
| Architecture family | MoE (GPT-2/3 lineage) [S25] |
| Attention variant | 'attention blocks alternate between banded window and fully dense patterns, where the bandwidth is 128 tokens'; GQA 8 KV heads; 'learned bias in the denominator of the softmax ... attention sinks' [S25] |
| MoE routing / balancing | top-4 of 128 experts (120b) — balancing method not stated [S25] |
| Position encoding | 'rotary position embeddings and extend the context length of dense layers to 131,072 tokens using YaRN' [S25] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | 'text-only dataset with trillions of tokens'; '2.1 million H100-hours' [S25] |
| Precision & QAT | 'post-trained the models with quantization of the MoE weights to MXFP4 format, where weights are quantized to 4.25 bits per parameter' [S25] |
| Context-extension curriculum | YaRN to 128K [S25] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | 'supervised fine-tuning stage and a high-compute RL stage' (blog) [S25] |
| RL algorithms | 'similar CoT RL techniques as OpenAI o3' (unnamed) [S25] |
| Reward sources | 'deliberative alignment' for safety; task rewards unnamed [S25] |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | tool use (browsing, python) trained [S25] |
| Reasoning-effort control | 'three reasoning levels: low, medium, and high ... configured in the system prompt' [S25] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'smooth test-time scaling of accuracy when increasing the reasoning level' [S25] |
| Explicitly undisclosed | RL algorithm, optimizer, token count, balancing |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S25 |

#### Gemma 3 (1B–27B)

| Field | Value |
|---|---|
| Model | Gemma 3 (1B–27B) |
| Lab | Google DeepMind |
| Release date | 2025-03-12; report v1 2025-03-25 [S26] |
| Total / active params | 1B, 4B, 12B, 27B dense [S26] |
| Architecture family | dense, local/global interleave [S26] |
| Attention variant | '5 local layers for every global layer'; local span 1024; QK-norm [S26] |
| MoE routing / balancing | n/a [S26] |
| Position encoding | 'increase RoPE base frequency from 10k to 1M on global self-attention layers'; scaling factor 8 to 128K [S26] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | '14T tokens for Gemma 3 27B, 12T for the 12B version, 4T for the 4B, and 2T tokens for the 1B' [S26] |
| Precision & QAT | 'Quantization Aware Training (QAT) ... per-channel int4, per-block int4, and switched fp8' [S26] |
| Context-extension curriculum | 'pre-train our models with 32K sequences and then scale ... up to 128K tokens at the end of pre-training while rescaling RoPE' [S26] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | 'All Gemma 3 models are trained with knowledge distillation'; 'sample 256 logits per token, weighted by teacher probabilities' [S26] |
| SFT | post-training 'improved version of knowledge distillation ... from a large IT teacher' [S26] |
| RL algorithms | 'RL finetuning phase based on improved versions of BOND, WARM, and WARP' [S26] |
| Reward sources | 'weight averaged reward models trained with human feedback data, code execution feedback, and ground-truth rewards for solving math problems' [S26] |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | WARP/WARM weight-averaging; dev blog: 'combination of distillation, reinforcement learning, and model merging' [S26] |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | local:global ratio and sliding-window ablations ('minimal impact on perplexity') [S26] |
| Explicitly undisclosed | optimizer; teacher identity; RL hyper-parameters |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S26 |

#### Gemma 3n (E2B, E4B)

| Field | Value |
|---|---|
| Model | Gemma 3n (E2B, E4B) |
| Lab | Google DeepMind |
| Release date | 2025-05-20 (preview); 2025-06-26 (full) [S27] |
| Total / active params | 'total parameter count of 5B and 8B'; effective 2B/4B [S27] |
| Architecture family | dense, MatFormer nested: 'a 2B effective parameter (E2B) sub-model is simultaneously optimized within it' [S27] |
| Attention variant | local/global with 'KV Cache Sharing' ('keys and values of the middle layer ... shared with all the top layers') [S27] |
| MoE routing / balancing | n/a [S27] |
| Position encoding | undisclosed (not addressed in the cited sources) |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | undisclosed (not addressed in the cited sources) |
| Precision & QAT | 'advanced activation quantization' [S27] |
| Context-extension curriculum | undisclosed (not addressed in the cited sources) |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | undisclosed (not addressed in the cited sources) |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | MatFormer 'mix'n'match' submodel extraction [S27] |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | training recipe (no report; 'Stay tuned for ... upcoming technical report') |
| Peer-reviewed venue | none |
| Evidence tier | C (blog) |
| Verified? | yes |
| Sources | S27 |

#### Gemma 4 (E2B, E4B, 12B, 26B-A4B MoE, 31B; DiffusionGemma)

| Field | Value |
|---|---|
| Model | Gemma 4 (E2B, E4B, 12B, 26B-A4B MoE, 31B; DiffusionGemma) |
| Lab | Google DeepMind |
| Release date | 2026-04-02; report v1 2026-07-02 [S28] |
| Total / active params | 'dense architectures (2.3B, 4.5B, 12B, and 31B parameters) and a Mixture-of-Experts variant with 3.8B activated and 26B total' [S28] |
| Architecture family | dense + MoE; encoder-free 12B; DiffusionGemma 'generates text using discrete diffusion' on the 26B-A4B base (HF blog) [S28] |
| Attention variant | '5:1 ratio of local sliding window to global self-attention (4:1 for the 2.3B model)'; 'reuse of keys as values in global layers' [S28] |
| MoE routing / balancing | 26B-A4B '8 active experts out of 128 plus 1 shared' (HF blog) [S28] |
| Position encoding | 'p-RoPE ... with p=0.25 on global attention layers and with RoPE on local attention layers' [S28] |
| MTP | 'autoregressive multi-token prediction (MTP) drafter head ... 4-layer Transformer block that cross-attends to the KVs of the main model' [S28] |
| Optimizer | 'optimizer state is sharded using an implementation of ZeRO-3' (optimizer unnamed) [S28] |
| Pre-training tokens | 'We follow a similar pre-training as Gemma 3' (count not given) [S28] |
| Precision & QAT | 'quantized versions of our models trained with quantization-aware training (QAT)'; 'mix of int2 and int4' mobile; Q4_0 [S28] |
| Context-extension curriculum | 256K context [S28] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | Gemma 3-style distillation implied ('similar pre-training as Gemma 3') [S28] |
| SFT | 'similar post-training approach as in Gemma 3. A significant difference is the addition of a thinking mode' [S28] |
| RL algorithms | inherits Gemma 3 RL (BOND/WARM/WARP) by reference [S28] |
| Reward sources | as Gemma 3 [S28] |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | thinking mode on/off [S28] |
| Model / expert merging | inherited (WARP) [S28] |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | token count, optimizer, RL details, diffusion training recipe |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S28 |

#### Mistral Large 3 (and Ministral 3)

| Field | Value |
|---|---|
| Model | Mistral Large 3 (and Ministral 3) |
| Lab | Mistral AI |
| Release date | 2025-12-02 [S29] |
| Total / active params | '41B active and 675B total parameters'; 'Granular MoE Language Model with 673B params and 39B active' + '2.5B Vision Encoder' [S29] |
| Architecture family | granular MoE, multimodal [S29] |
| Attention variant | undisclosed (not addressed in the cited sources) |
| MoE routing / balancing | undisclosed (not addressed in the cited sources) |
| Position encoding | undisclosed (not addressed in the cited sources) |
| MTP | Eagle draft model released separately [S29] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | 'trained from scratch on 3000 of NVIDIA's H200 GPUs' (tokens undisclosed) [S29] |
| Precision & QAT | NVFP4 and FP8 post-training checkpoints [S29] |
| Context-extension curriculum | 256K context [S29] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | 'post-trained on instruction-and-answer datasets and human preferences' [S29] |
| RL algorithms | undisclosed (not addressed in the cited sources) |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | reasoning variants for Ministral 3 [S29] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | virtually all training details |
| Peer-reviewed venue | none |
| Evidence tier | C (announcement + model card) |
| Verified? | yes |
| Sources | S29 |

#### Magistral Medium / Small

| Field | Value |
|---|---|
| Model | Magistral Medium / Small |
| Lab | Mistral AI |
| Release date | 2025-06-10; report v1 2025-06-12 [S30] |
| Total / active params | Medium on Mistral Medium 3 (undisclosed size); Small 24B [S30] |
| Architecture family | dense (Small); Medium undisclosed [S30] |
| Attention variant | undisclosed (not addressed in the cited sources) |
| MoE routing / balancing | n/a |
| Position encoding | undisclosed (not addressed in the cited sources) |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | n/a (post-training) [S30] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | RL length ramp '16k -> 24k and 24k -> 32k' [S30] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | 'Magistral Small, which began with SFT traces derived from Magistral Medium'; Medium 'with pure RL, with no distillation from pre-existing reasoning models' [S30] |
| SFT | Small: SFT on Medium traces + 10% general data [S30] |
| RL algorithms | GRPO with 'Eliminating KL divergence', 'Loss normalization', 'Advantage normalization', 'Clip-Higher' (eps_high 0.26–0.28) [S30] |
| Reward sources | formatting, correctness (SymPy, test execution), length penalty, language consistency [S30] |
| Async / off-policy RL | 'operate the generators continuously at maximum throughput without ever waiting for the trainers'; in-flight weight updates without KV refresh [S30] |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | entropy bonus and partial code rewards tried and rejected; batch-size studies [S30] |
| Explicitly undisclosed | Medium architecture and size |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S30 |

#### Devstral 2 (123B) / Devstral Small 2 (24B)

| Field | Value |
|---|---|
| Model | Devstral 2 (123B) / Devstral Small 2 (24B) |
| Lab | Mistral AI |
| Release date | 2025-12-09 [S31] |
| Total / active params | '123B-parameter dense transformer supporting a 256K context window'; Small 24B [S31] |
| Architecture family | dense [S31] |
| Attention variant | undisclosed (not addressed in the cited sources) |
| MoE routing / balancing | n/a |
| Position encoding | undisclosed (not addressed in the cited sources) |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | undisclosed (not addressed in the cited sources) |
| Precision & QAT | FP4/FP8 weights supported [S31] |
| Context-extension curriculum | 256K [S31] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | undisclosed (not addressed in the cited sources) |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | all training details |
| Peer-reviewed venue | none |
| Evidence tier | C (announcement) |
| Verified? | yes |
| Sources | S31 |

#### NVIDIA Nemotron 3 Nano (30B-A3B)

| Field | Value |
|---|---|
| Model | NVIDIA Nemotron 3 Nano (30B-A3B) |
| Lab | NVIDIA |
| Release date | 2025-12-15; report v1 2025-12-23 [S32] |
| Total / active params | '31.6B total parameters out of which only 3.2B are activated' [S32] |
| Architecture family | hybrid Mamba-2 + attention + MoE: 'predominantly interleave MoE layers with cheaper Mamba-2 layers' [S32] |
| Attention variant | GQA in a few layers (6 of 52) [S32] |
| MoE routing / balancing | 'granular MoE architecture along with shared experts ... learnt MLP router with sigmoid gating'; 'DeepSeek's aux-loss-free load balancing strategy ... in conjunction with the standard load balancing loss' (coef 1e-4) [S32] |
| Position encoding | 'We do not use any positional embeddings' (NoPE) [S32] |
| MTP | none for Nano ('MTP layers in the two larger models') [S32] |
| Optimizer | 'AdamW ... weight decay of 0.1' [S32] |
| Pre-training tokens | '25 trillion tokens' with 'Warmup-Stable-Decay' schedule (20T stable, 5T decay) [S32] |
| Precision & QAT | BF16 training; FP8 post-training quantization [S32] |
| Context-extension curriculum | LC phase '121 billion tokens' to 1M [S32] |
| Mid-training stage? | 'Phase 2 (1.5T) emphasizes high-quality sources' [S32] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | SFT with 'reasoning budget control, reasoning on/off control' data [S32] |
| RL algorithms | 'synchronous GRPO with masked importance sampling'; 'freeze the MoE router weights' [S32] |
| Reward sources | 'multi-environment reinforcement learning from verifiable rewards (RLVR)'; RLHF with 'generative reward model (GenRM)' trained by GRPO [S32] |
| Async / off-policy RL | synchronous, on-policy ('making our updates on-policy') [S32] |
| Agentic RL environment scale | '7 reward environments' (docs); Nemo-Gym [S32] |
| Reasoning-effort control | 'randomly truncate 3% of reasoning traces to different reasoning budgets' [S32] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | none major; full recipe released |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S32 |

#### NVIDIA Nemotron 3 Super (120B-A12B)

| Field | Value |
|---|---|
| Model | NVIDIA Nemotron 3 Super (120B-A12B) |
| Lab | NVIDIA |
| Release date | 2026-03-10; report v1 2026-04-14 [S33] |
| Total / active params | '120.6B total parameters ... 12.7B active' [S33] |
| Architecture family | hybrid Mamba-2 + attention + LatentMoE [S33] |
| Attention variant | 'Grouped-Query Attention (GQA) with 32 query heads and 2 KV heads' as 'global anchors' [S33] |
| MoE routing / balancing | '512 total experts and a top-22 routing'; 'sigmoid router score function complemented by expert biasing ... auxiliary-loss-free load balancing strategy ... update rate of 1e-3' [S33] |
| Position encoding | 'we omit positional embeddings' (NoPE) [S33] |
| MTP | 'include MTP layers for inference acceleration through native speculative decoding' [S33] |
| Optimizer | as Nano (AdamW) [S33] |
| Pre-training tokens | '25 trillion tokens' (20T + 5T phases), WSD schedule [S33] |
| Precision & QAT | 'first model in the Nemotron 3 family to 1) be pre-trained in NVFP4' [S33] |
| Context-extension curriculum | 'up to 1M context length' via LC phase [S33] |
| Mid-training stage? | phase 2 high-quality 5T [S33] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | two-stage SFT [S33] |
| RL algorithms | GRPO (RLVR) + RLHF with GenRM ('Qwen3-Nemotron-235B-A22B-GenRM-2603') [S33] |
| Reward sources | verifiable + GenRM [S33] |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | 'substantially scaled the breadth of our RL environments' [S33] |
| Reasoning-effort control | reasoning budget control [S33] |
| Model / expert merging | 'Tracking Merge Evaluation ... individual trained checkpoints' merged during WSD stable phase [S33] |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | LatentMoE accuracy-per-FLOP analysis [S33] |
| Explicitly undisclosed | RL algorithm variants; compute |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S33 |

#### NVIDIA Nemotron 3 Ultra (550B-A55B)

| Field | Value |
|---|---|
| Model | NVIDIA Nemotron 3 Ultra (550B-A55B) |
| Lab | NVIDIA |
| Release date | ~2026-06-04; report v1 2026-06-12 [S34] |
| Total / active params | '550 billion total and 55 billion active parameter' [S34] |
| Architecture family | hybrid Mamba-Attention LatentMoE [S34] |
| Attention variant | as Super [S34] |
| MoE routing / balancing | LatentMoE + aux-loss-free (as Super) [S34] |
| Position encoding | NoPE (as Super) [S34] |
| MTP | 'native Multi-Token Prediction ... two heads during pre-training ... share the same parameters' [S34] |
| Optimizer | AdamW with 'Warmup-Stable-Decay (WSD) learning rate schedule over a total horizon of 20 trillion tokens' [S34] |
| Pre-training tokens | '20 trillion text tokens' (15T + 5T) [S34] |
| Precision & QAT | 'NVFP4 layers use the E2M1 datatype with two-dimensional block quantization on weights, Random Hadamard Transforms on inputs to wgrad, and stochastic rounding on gradients'; 'kept the final 15% of the network (16 layers)' in BF16 [S34] |
| Context-extension curriculum | 'extended the context length to 1M tokens' (LC-Phase CPT, LR 2.5e-6) [S34] |
| Mid-training stage? | phase 2 high-quality + LC-Phase [S34] |
| Distillation (where, teacher) | 'Multi-teacher On-Policy Distillation (MOPD) consolidated these teachers into Ultra through dense token-level guidance on student-generated rollouts' [S34] |
| SFT | 'Multi-domain Supervised Fine-tuning with shared-weight MTP objective' [S34] |
| RL algorithms | 'unified RLVR' (GRPO per NeMo-RL docs: 'GRPO with verifiable rewards'); RLHF teacher; 'MTP Boosting' [S34] |
| Reward sources | verifiable; 'GenRM used for RLHF'; LLM-judge equivalence [S34] |
| Async / off-policy RL | 'MOPD Asynchronous on-policy distillation merges specialized teachers' [S34] |
| Agentic RL environment scale | 'more than ten domain-specialized teacher models'; SWE/terminal environments [S34] |
| Reasoning-effort control | 'reasoning effort control ... inference-time adjustment of the accuracy–compute trade-off'; medium-effort SFT from 'GPT-OSS-120B in its medium-effort mode' [S34] |
| Model / expert merging | none (MOPD consolidation) [S34] |
| Continual / cross-stage distillation | MOPD (multi-teacher OPD) [S34] |
| Ablations / scaling laws | NVFP4 vs BF16 loss gap ('0.4% on average'); divergence note [S34] |
| Explicitly undisclosed | RL hyper-parameters beyond NeMo-RL configs |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S34 |

### Other open-weights labs

#### Olmo 3 (7B, 32B; Think / Instruct / RL-Zero)

| Field | Value |
|---|---|
| Model | Olmo 3 (7B, 32B; Think / Instruct / RL-Zero) |
| Lab | Ai2 |
| Release date | 2025-11-20; report v1 2025-12-15 [S35] |
| Total / active params | 7B and 32B dense [S35] |
| Architecture family | dense decoder with 'sliding window attention (SWA) pattern' in some layers [S35] |
| Attention variant | SWA interleaved with full attention [S35] |
| MoE routing / balancing | n/a |
| Position encoding | RoPE (Olmo 2 lineage) [S35] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | AdamW (Olmo 2 lineage; 'bfloat16 precision throughout') [S35] |
| Pre-training tokens | 'three stages of pretraining for up to 5.9T tokens, midtraining for 100 billion tokens, and ... long-context extension for 50B ... or 100B' [S35] |
| Precision & QAT | 'using bfloat16 precision throughout' [S35] |
| Context-extension curriculum | 'supporting up to 65K context after extension' (Dolma 3 Longmino) [S35] |
| Mid-training stage? | 'Midtraining ... Dolma 3 Dolmino Mix' 100B tokens [S35] |
| Distillation (where, teacher) | SFT on synthetic reasoning traces (Dolci Think SFT) [S35] |
| SFT | Dolci Think SFT / Instruct SFT [S35] |
| RL algorithms | OlmoRL, GRPO-based with 'Token-level loss, truncated importance sampling, clip-higher, no KL term, group-advantaged filtering' (secondary summaries of Sec 4.4) [S35] |
| Reward sources | 'reinforcement learning across both verifiable and non-verifiable domains'; LLM judges [S35] |
| Async / off-policy RL | 'in-flight weight updates, continuous batching' ('4x more efficient'); truncated importance sampling [S35] |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | 'Midtraining consisted of two parallel runs ... followed by model merging'; post-training 'merging, and checkpoint confirmation' [S35] |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | RL-Zero controlled study; Delta Learning preference data [S35] |
| Explicitly undisclosed | none major (fully open); RL Sec 4.4 not fetched in full here |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S35 |

#### SmolLM3-3B

| Field | Value |
|---|---|
| Model | SmolLM3-3B |
| Lab | Hugging Face |
| Release date | 2025-07-08 [S36] |
| Total / active params | 3B dense [S36] |
| Architecture family | dense (Llama-style, tied embeddings) [S36] |
| Attention variant | 'grouped-query attention using 4 groups' [S36] |
| MoE routing / balancing | n/a |
| Position encoding | 'NoPE ... selectively removing rotary position embeddings from every 4th layer'; YaRN at inference [S36] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | '11.2T tokens using a three-stage training strategy' [S36] |
| Precision & QAT | 'Precision: bfloat16' [S36] |
| Context-extension curriculum | 'two stages for 50B tokens each: first ... 4k to 32k context with RoPE theta increased to 1.5M, then from 32k to 64k ... 5M' [S36] |
| Mid-training stage? | 'mid-training stage to incorporate reasoning capabilities ... 140B tokens' [S36] |
| Distillation (where, teacher) | mid-training on 'reasoning traces from R1' (OpenThoughts3, Llama-Nemotron) [S36] |
| SFT | SFT 1.8B tokens, 4 epochs [S36] |
| RL algorithms | 'alignment using Anchored Preference Optimization (APO) - a recent variant of DPO' (no online RL) [S36] |
| Reward sources | preference pairs [S36] |
| Async / off-policy RL | n/a |
| Agentic RL environment scale | n/a |
| Reasoning-effort control | '/think and /no_think flags' [S36] |
| Model / expert merging | model merging used to recover long-context after APO (blog) [S36] |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | GQA and NoPE ablations on 3B/100B tokens [S36] |
| Explicitly undisclosed | optimizer hyper-parameters in blog (configs released) |
| Peer-reviewed venue | none |
| Evidence tier | C (blog) |
| Verified? | yes |
| Sources | S36 |

#### Apertus (8B, 70B)

| Field | Value |
|---|---|
| Model | Apertus (8B, 70B) |
| Lab | Swiss AI Initiative (EPFL/ETH/CSCS) |
| Release date | 2025-09-02; arXiv v1 2025-09-17; ACL 2026 [S37] |
| Total / active params | 'Released at 8B and 70B scales' dense [S37] |
| Architecture family | dense with 'xIELU activation function, the AdEMAMix optimizer, QK-Norm, Pre-Norm' [S37] |
| Attention variant | GQA + QK-Norm [S37] |
| MoE routing / balancing | n/a |
| Position encoding | RoPE [S37] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | 'We pretrain using the AdEMAMix optimizer ... a first for an LLM at this scale' [S37] |
| Pre-training tokens | 'training on 15T tokens from over 1800 languages'; 'Goldfish objective during pretraining' (2% masking) [S37] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | 'split training into multiple phases to adapt the maximum context length iteratively' [S37] |
| Mid-training stage? | 5-stage data curriculum; 'Warmup-Stable-Decay (WSD) learning rate schedule' with decay at 13.5T [S37] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | SFT with AdEMAMix [S37] |
| RL algorithms | 'Quantile Reward Policy Optimization algorithm (QRPO)' [S37] |
| Reward sources | absolute reward (QRPO) from reward model [S37] |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'experiments with our architecture and optimization setup improve efficiency by 30–40% both at 1B and 3B scale' [S37] |
| Explicitly undisclosed | none major (fully open) |
| Peer-reviewed venue | ACL 2026 long paper (aclanthology 2026.acl-long.2172) [S37] |
| Evidence tier | A (ACL 2026) + C |
| Verified? | yes |
| Sources | S37 |

#### LongCat-Flash (560B, ~27B active)

| Field | Value |
|---|---|
| Model | LongCat-Flash (560B, ~27B active) |
| Lab | Meituan |
| Release date | 2025-08-31/09-01 [S38] |
| Total / active params | '560-billion-parameter ... activates 18.6B–31.3B (27B on average) per token' [S38] |
| Architecture family | MoE with 'Zero-computation Experts' and 'Shortcut-connected MoE (ScMoE)' [S38] |
| Attention variant | 'two Multi-head Latent Attention (MLA) block' per layer [S38] |
| MoE routing / balancing | 'expert bias adjusted by a PID-controller, maintaining an average of ~27 billion activated parameters'; 'router-gradient balancing' [S38] |
| Position encoding | RoPE within MLA [S38] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | 'fine-tuned optimizer configurations'; hyper-parameter transfer 'Adam LR Full Align' [S38] |
| Pre-training tokens | 'more than 20 trillion tokens within 30 days' [S38] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | 'context length is extended to 128k through training on long context corpora' [S38] |
| Mid-training stage? | 'Reasoning and coding capabilities are further enhanced using trillions of data' (stage 2) [S38] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | 'targeted mid- and post-training on reasoning, code, and instructions' [S38] |
| RL algorithms | RL used (non-thinking model); algorithm not in fetched sections [S38] |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'hyperparameter transfer strategy based on width scaling'; 'model growth ... stacking r copies of the small model' (r=2); 'hidden z-loss' [S38] |
| Explicitly undisclosed | RL algorithm and rewards (not in fetched sections) |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S38 |

#### Ling 2.0 (Ling-mini-2.0 16B-A1.4B, Ling-flash-2.0 103B-A6.1B, Ling-1T 1T-A51B)

| Field | Value |
|---|---|
| Model | Ling 2.0 (Ling-mini-2.0 16B-A1.4B, Ling-flash-2.0 103B-A6.1B, Ling-1T 1T-A51B) |
| Lab | Ant Group (inclusionAI) |
| Release date | Ling-1T 2025-10-09; report v1 2025-10-25 [S39] |
| Total / active params | 'Ling-1T: 1 trillion total parameters with 51B activated' [S39] |
| Architecture family | MoE 'high-sparsity, fine-grained' [S39] |
| Attention variant | 'standard grouped-query attention (GQA)'; 'QKNorm' [S39] |
| MoE routing / balancing | '256 routed experts, activates 8 experts plus 1 shared expert ... 3.5% activation'; 'Aux-loss-free, sigmoid-scoring expert routing with zero-mean updates' [S39] |
| Position encoding | 'Partial RoPE ... only to the first 64 dimensions' [S39] |
| MTP | 'High-Sparsity MoE with MTP' [S39] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | 'Pre-trained on 20 trillion+ high-quality, reasoning-dense tokens' [S39] |
| Precision & QAT | 'full-scale FP8 training'; 'largest FP8-trained foundation model known to date' [S39] |
| Context-extension curriculum | 128K [S39] |
| Mid-training stage? | 'mid-training CoT activation'; 'WSM (Warmup–Stable–Merge) LR scheduler with mid-train checkpoint merging' [S39] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | 'reinforcement-based fine-tuning (DFT, Evo-CoT)' [S39] |
| RL algorithms | DFT, Evo-CoT (Ling); GRPO/IcePop in Ring [S39,S40] |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | non-thinking (Ling) vs thinking (Ring) [S39] |
| Model / expert merging | 'WSM ... mid-train checkpoint merging simulates LR decay' [S39] |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'Ling Scaling Law' / 'Ling Wind Tunnel' ('predict the final training loss to within an error of 0.01') [S39] |
| Explicitly undisclosed | optimizer name; RL reward details |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S39 |

#### Ring-1T

| Field | Value |
|---|---|
| Model | Ring-1T |
| Lab | Ant Group (inclusionAI) |
| Release date | 2025-10-14; report v1 2025-10-21 [S40] |
| Total / active params | '1 trillion total parameters and activates approximately 50 billion per token' [S40] |
| Architecture family | MoE (Ling 2.0 base) [S40] |
| Attention variant | GQA (Ling 2.0) [S40] |
| MoE routing / balancing | Ling 2.0 aux-loss-free; 'MoE router bias held fixed' in RL [S40] |
| Position encoding | partial RoPE [S40] |
| MTP | Ling 2.0 MTP [S39] |
| Optimizer | RL: 'AdamW optimizer with hyperparameters beta1=0.9, beta2=0.999' [S40] |
| Pre-training tokens | n/a (Ling-1T-base) [S40] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | 'maximum length of 65,536 tokens' in RL [S40] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | 'Long Chain-of-Thought Supervised Fine-Tuning (Long-CoT SFT)' [S40] |
| RL algorithms | 'IcePop, a variant of GRPO that suppresses unstable training updates through double-sided masking calibration'; 'C3PO++'; general RL 'GRPO with a learning rate of 3e-6, a KL coefficient of 0.0' [S40] |
| Reward sources | 'Reinforcement Learning with Verifiable Rewards (RLVR)'; 'RLHF'; 'hybrid reward system utilizing large-scale Serverless Sandbox' [S40] |
| Async / off-policy RL | 'ASystem is a high-performance reinforcement learning (RL) framework designed for large-scale asynchronous training'; 'budget-controlled rollout partition' [S40] |
| Agentic RL environment scale | ASandbox 'over 10 programming languages, and supports a request throughput of up to 10K/s' [S40] |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | IcePop vs GRPO stability; C3PO++ throughput [S40] |
| Explicitly undisclosed | RL compute; data |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S40 |

#### Step-3 (321B VLM; 316B LLM, 38B active)

| Field | Value |
|---|---|
| Model | Step-3 (321B VLM; 316B LLM, 38B active) |
| Lab | StepFun |
| Release date | 2025-07-25 (report); weights 2025-07-31 [S41] |
| Total / active params | '321 billion total parameters, while for each text token, 38B parameters are activated' [S41] |
| Architecture family | MoE (48 experts, top-3 + 1 shared) [S41] |
| Attention variant | 'Multi-Matrix Factorization Attention (MFA) ... 64 query heads and they share a Key and a Value head, all with a dimension of 256' [S41] |
| MoE routing / balancing | 'shared expert design inspired by DeepSeekMoE' [S41] |
| Position encoding | undisclosed (not addressed in the cited sources) |
| MTP | 'no MTP' in headline throughput (MTP compatible) [S41] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | undisclosed (not addressed in the cited sources) |
| Precision & QAT | FP8 serving [S41] |
| Context-extension curriculum | 65536 max [S41] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | undisclosed (not addressed in the cited sources) |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | decoding-cost analysis vs DeepSeek-V3/Qwen3 [S41] |
| Explicitly undisclosed | 'In the future, we will release more details on the model side for Step-3' — training recipe undisclosed [S41] |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S41 |

#### Xiaomi MiMo-7B

| Field | Value |
|---|---|
| Model | Xiaomi MiMo-7B |
| Lab | Xiaomi |
| Release date | 2025-04-30; report v1 2025-05-12 [S42] |
| Total / active params | 7B dense [S42] |
| Architecture family | dense [S42] |
| Attention variant | GQA [S42] |
| MoE routing / balancing | n/a |
| Position encoding | RoPE [S42] |
| MTP | MTP 'to enhance training performance and accelerate inference decoding' (MiMo-7B) [S42,S43] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | 25T (report abstract) [S42] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | undisclosed (not addressed in the cited sources) |
| Mid-training stage? | three-stage data mixture [S42] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | SFT then RL [S42] |
| RL algorithms | GRPO-style with 'test-difficulty driven' reward; 'Seamless Rollout Engine' [S42] |
| Reward sources | rule-based math/code [S42] |
| Async / off-policy RL | rollout engine optimizations [S42] |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | details not re-fetched here (verified via abs page only) |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes (abs page) |
| Sources | S42 |

#### Xiaomi MiMo-V2-Flash (309B-A15B)

| Field | Value |
|---|---|
| Model | Xiaomi MiMo-V2-Flash (309B-A15B) |
| Lab | Xiaomi |
| Release date | 2025-12-16; report v1 2026-01-06 [S43] |
| Total / active params | '309B total parameters and 15B active parameters' [S43] |
| Architecture family | MoE + hybrid SWA/global: 'interleaves Sliding Window Attention (SWA) with global attention, with a 128-token sliding window under a 5:1 hybrid ratio' [S43] |
| Attention variant | SWA:GA 5:1 with 'learnable attention sink bias' [S43] |
| MoE routing / balancing | '256 experts in total, with 8 activated per token, and contains no shared experts' [S43] |
| Position encoding | RoPE [S43] |
| MTP | 'pre-trained on 27 trillion tokens with Multi-Token Prediction (MTP)'; lightweight MTP block '0.33B' [S43] |
| Optimizer | 'AdamW optimizer with beta1 = 0.9, beta2 = 0.95, and a weight decay of 0.1' [S43] |
| Pre-training tokens | '27 trillion tokens' [S43] |
| Precision & QAT | 'Trained on 27T tokens using FP8 mixed precision' (GitHub) [S43] |
| Context-extension curriculum | 'native 32k context length and subsequently extended to 256k' (Stage 3, 26–27T) [S43] |
| Mid-training stage? | Stage 2 data distribution shift; Stage 3 context extension [S43] |
| Distillation (where, teacher) | 'Multi-Teacher On-Policy Distillation (MOPD) paradigm ... domain-specialized teachers ... provide dense and token-level reward' [S43] |
| SFT | SFT before RL/MOPD [S43] |
| RL algorithms | large-scale RL for teachers; MOPD for student [S43] |
| Reward sources | teacher token-level rewards; verifiable RL [S43] |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | 'large-scale agentic RL' [S43] |
| Reasoning-effort control | thinking modes [S43] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | MOPD (multi-teacher) [S43] |
| Ablations / scaling laws | attention-architecture ablation ('All GA baseline, a hybrid SWA model ... with attention sinks bias'); 'our current architectural exploration remains preliminary, with limited analysis of design trade-offs' [S43] |
| Explicitly undisclosed | RL algorithm for teachers |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S43 |

#### Tencent Hunyuan-A13B (80B-A13B)

| Field | Value |
|---|---|
| Model | Tencent Hunyuan-A13B (80B-A13B) |
| Lab | Tencent Hunyuan |
| Release date | 2025-06-27 [S44] |
| Total / active params | '80 billion parameters with 13 billion active parameters' [S44] |
| Architecture family | fine-grained MoE: '1 shared expert and 64 non-shared experts, with 8 experts activated' (secondary) [S44] |
| Attention variant | 'Grouped Query Attention (GQA)' [S44] |
| MoE routing / balancing | undisclosed (not addressed in the cited sources) |
| Position encoding | RoPE with NTK-aware scaling (secondary) [S44] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | 'pretrained on a rigorously filtered 20T token corpus' (report abstract) [S44] |
| Precision & QAT | FP8-static PTQ; GPTQ-Int4 [S44] |
| Context-extension curriculum | 'Natively supports a 256K context window' (32K then 256K) [S44] |
| Mid-training stage? | fast annealing stage (secondary) [S44] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | SFT with CoT data [S44] |
| RL algorithms | GRPO (report, via secondary summaries) [S44] |
| Reward sources | 'LLM based verifier'; 'generative reward model or GRM' (secondary) [S44] |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | 'over 30 agent instruction types' (secondary) [S44] |
| Reasoning-effort control | 'dual-mode Chain-of-Thought (CoT) framework' ('/think', '/no_think') [S44] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | balancing, optimizer, precision (report PDF not directly fetched) |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes (GitHub); report details via secondary |
| Sources | S44 |

#### Tencent Hy3 (295B-A21B)

| Field | Value |
|---|---|
| Model | Tencent Hy3 (295B-A21B) |
| Lab | Tencent Hy |
| Release date | 2026-04-23 (preview); 2026-07-06 (final) [S44] |
| Total / active params | '295B-parameter Mixture-of-Experts (MoE) model with 21B active parameters and 3.8B MTP layer parameters' [S44] |
| Architecture family | MoE ('192 experts, top-8') [S44] |
| Attention variant | '64 (GQA, 8 KV heads, head dim 128)' [S44] |
| MoE routing / balancing | undisclosed (not addressed in the cited sources) |
| Position encoding | undisclosed (not addressed in the cited sources) |
| MTP | 'Number of MTP Layers: 1' [S44] |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | undisclosed (not addressed in the cited sources) |
| Precision & QAT | BF16 + FP8 checkpoint [S44] |
| Context-extension curriculum | 256K [S44] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | 'joint optimization of SFT and RL' [S44] |
| RL algorithms | 'scaled up RL training' (unnamed) [S44] |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | 'hybrid fast-and-slow-thinking model' [S44] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | no technical report; all recipe details |
| Peer-reviewed venue | none |
| Evidence tier | C (blog + card) |
| Verified? | yes |
| Sources | S44 |

#### ByteDance Seed-OSS-36B

| Field | Value |
|---|---|
| Model | ByteDance Seed-OSS-36B |
| Lab | ByteDance Seed |
| Release date | 2025-08-20 [S45] |
| Total / active params | 36B dense; 'Number of QKV Heads 80 / 8 / 8' [S45] |
| Architecture family | dense [S45] |
| Attention variant | GQA [S45] |
| MoE routing / balancing | n/a |
| Position encoding | 'RoPE Base Frequency 1e7' [S45] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | 'Trained with 12T tokens' [S45] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | 'Trained with up-to-512K long context natively' [S45] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | undisclosed (not addressed in the cited sources) |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | 'thinking budget ... the model periodically triggers self-reflection to estimate the consumed and remaining budget' [S45] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | base released with and without synthetic instruction data [S45] |
| Explicitly undisclosed | all post-training details |
| Peer-reviewed venue | none |
| Evidence tier | C (GitHub card) |
| Verified? | yes |
| Sources | S45 |

#### IBM Granite 4.0 (H-Small 32B-A9B, H-Tiny 7B-A1B, H-Micro 3B, Micro 3B)

| Field | Value |
|---|---|
| Model | IBM Granite 4.0 (H-Small 32B-A9B, H-Tiny 7B-A1B, H-Micro 3B, Micro 3B) |
| Lab | IBM |
| Release date | 2025-10-02 [S46] |
| Total / active params | 'Granite-4.0-H-Small, a hybrid mixture of experts (MoE) model with 32B total parameters (9B active)' [S46] |
| Architecture family | hybrid Mamba-2/transformer: 'combines Mamba-2 layers and conventional transformer blocks sequentially in a 9:1 ratio' [S46] |
| Attention variant | standard attention blocks (1 in 10) [S46] |
| MoE routing / balancing | 'fine-grained mixture of experts (MoE) block ... first MoEs to utilize shared experts that are always activated' [S46] |
| Position encoding | 'The Granite 4.0-H architecture uses no positional encoding (NoPE)' [S46] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | undisclosed (not addressed in the cited sources) |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | 'trained on sequences of over half a million tokens and validated to 128,000' (IBM Think) [S46] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | Instruct variants [S46] |
| RL algorithms | undisclosed (not addressed in the cited sources) |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | tokens, optimizer, post-training algorithms (no report) |
| Peer-reviewed venue | none |
| Evidence tier | C (announcement) |
| Verified? | yes |
| Sources | S46 |

#### Falcon-H1 (0.5B–34B)

| Field | Value |
|---|---|
| Model | Falcon-H1 (0.5B–34B) |
| Lab | TII |
| Release date | 2025-05-20; report v1 2025-07-30 [S47] |
| Total / active params | '0.5B, 1.5B, 1.5B-deep, 3B, 7B, and 34B' [S47] |
| Architecture family | parallel hybrid SSM+attention: 'combine attention and Mamba-2 heads in parallel within our hybrid mixer block' [S47] |
| Attention variant | GQA heads in parallel with Mamba-2 (e.g., 34B '20/4, 32') [S47] |
| MoE routing / balancing | n/a |
| Position encoding | RoPE [S47] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | AdamW with 'customized Maximal Update Parametrization (µP)' ('35 fine-grained groups' of multipliers) [S47] |
| Pre-training tokens | 34B '~18T'; 7B '~12T' [S47] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | 256K for 7B/34B; post-training 'WSD: 50MT warmup, 1.5GT stable, 1.5GT decay' + 128k stage [S47] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | SFT 16k then 128k stage [S47] |
| RL algorithms | DPO (post-training docs) [S47] |
| Reward sources | preference data [S47] |
| Async / off-policy RL | n/a |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | 'detailed ablations and coarse grid searches on 300M to 1.5B parameter proxy models'; state-dimension vs groups grid [S47] |
| Explicitly undisclosed | none major |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S47 |

#### xAI Grok 2.5 (open weights)

| Field | Value |
|---|---|
| Model | xAI Grok 2.5 (open weights) |
| Lab | xAI |
| Release date | 2025-08-23/24 (weights on HF) [S48] |
| Total / active params | ~268–270B MoE, '8 experts' with 2 active (community reading of config) [S48] |
| Architecture family | MoE [S48] |
| Attention variant | GQA (config) [S48] |
| MoE routing / balancing | undisclosed (not addressed in the cited sources) |
| Position encoding | RoPE (config) [S48] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | undisclosed (not addressed in the cited sources) |
| Pre-training tokens | undisclosed (not addressed in the cited sources) |
| Precision & QAT | 'serve with SGLang using FP8' [S48] |
| Context-extension curriculum | undisclosed (not addressed in the cited sources) |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | undisclosed (not addressed in the cited sources) |
| RL algorithms | undisclosed (not addressed in the cited sources) |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | undisclosed (not addressed in the cited sources) |
| Explicitly undisclosed | 'The release includes checkpoints and inference notes, not the complete training data or end-to-end pipeline' — no training details [S48] |
| Peer-reviewed venue | none |
| Evidence tier | C (weights only) |
| Verified? | yes (release event; HF card not fetchable) |
| Sources | S48 |

#### Microsoft Phi-4-reasoning / -plus

| Field | Value |
|---|---|
| Model | Microsoft Phi-4-reasoning / -plus |
| Lab | Microsoft |
| Release date | 2025-04-30 [S49] |
| Total / active params | '14-billion parameter reasoning model' [S49] |
| Architecture family | dense (Phi-4) [S49] |
| Attention variant | Phi-4 (dense) [S49] |
| MoE routing / balancing | n/a |
| Position encoding | 'RoPE base frequency was doubled ... maximum length of 32K' [S49] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | AdamW (SFT); Adam (RL, lr 5e-8) [S49] |
| Pre-training tokens | n/a (post-training of Phi-4); SFT '16B tokens' [S49] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | 16K -> 32K [S49] |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | 'reasoning demonstrations generated using o3-mini' (SFT distillation) [S49] |
| SFT | 'over 1.4M prompts ... totaling 8.3 billion unique tokens' [S49] |
| RL algorithms | 'Group Relative Policy Optimization (GRPO) algorithm, incorporating modifications tailored specifically to our setup' (verl) [S49] |
| Reward sources | outcome-based verifiable math rewards ('~6K high-quality math-focused problems with verifiable solutions') [S49] |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | n/a |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | teacher comparison ('o3-mini with medium reasoning effort ... similar effect to DeepSeek-R1'); RL step ablations [S49] |
| Explicitly undisclosed | GRPO modifications detail |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S49 |

#### Apple Foundation Models 2025 (~3B on-device; PT-MoE server)

| Field | Value |
|---|---|
| Model | Apple Foundation Models 2025 (~3B on-device; PT-MoE server) |
| Lab | Apple |
| Release date | 2025-06-09 (WWDC); report v1 2025-07-17 [S50] |
| Total / active params | '~3B-parameter on-device model'; server PT-MoE (size undisclosed) [S50] |
| Architecture family | dense (on-device) + 'Parallel-Track Mixture-of-Experts (PT-MoE) transformer' with 'interleaved global–local attention' [S50] |
| Attention variant | 'KV-cache sharing' (on-device); global–local interleave (server) [S50] |
| MoE routing / balancing | 'top-k routing is implemented via the grouped general matrix multiplication (GEMM), ensuring that no tokens are dropped' [S50] |
| Position encoding | undisclosed (not addressed in the cited sources) |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | AdamW for QAT ('more stable than Adafactor') [S50] |
| Pre-training tokens | MoE 'using only 1T high-quality data' then on-device 'last 10% of tokens (about 1.4T) using a distillation loss from the MoE teacher' [S50] |
| Precision & QAT | 'compressed the on-device model to 2 bits-per-weight using Quantization-Aware-Training (QAT)'; server '3.56 bits-per-weight using Adaptive Scalable Texture Compression (ASTC)' [S50] |
| Context-extension curriculum | undisclosed (not addressed in the cited sources) |
| Mid-training stage? | undisclosed (not addressed in the cited sources) |
| Distillation (where, teacher) | on-device 'distillation loss from the MoE teacher' during pretraining [S50] |
| SFT | SFT then RLHF [S50] |
| RL algorithms | 'REINFORCE Leave-One-Out (RLOO) method as our main RLHF algorithm' [S50] |
| Reward sources | 'reward model, ground truth verification, code execution, LLM-as-a-judge' [S50] |
| Async / off-policy RL | 'distributed asynchronous RL infrastructure consisting of replicas of trajectory generators (TGs) and a policy updater (PU)' with replay buffer [S50] |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | undisclosed (not addressed in the cited sources) |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | balanced 2-bit set vs unbalanced [S50] |
| Explicitly undisclosed | server model size, token totals, RL compute |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S50 |

#### Apple Foundation Models 2026

| Field | Value |
|---|---|
| Model | Apple Foundation Models 2026 |
| Lab | Apple |
| Release date | NOT VERIFIED — no 2026 tech report found (searches returned only the 2024 and 2025 reports) |
| Total / active params | n/a |
| Architecture family | n/a |
| Attention variant | n/a |
| MoE routing / balancing | n/a |
| Position encoding | n/a |
| MTP | n/a |
| Optimizer | n/a |
| Pre-training tokens | n/a |
| Precision & QAT | n/a |
| Context-extension curriculum | n/a |
| Mid-training stage? | n/a |
| Distillation (where, teacher) | n/a |
| SFT | n/a |
| RL algorithms | n/a |
| Reward sources | n/a |
| Async / off-policy RL | n/a |
| Agentic RL environment scale | n/a |
| Reasoning-effort control | n/a |
| Model / expert merging | n/a |
| Continual / cross-stage distillation | n/a |
| Ablations / scaling laws | n/a |
| Explicitly undisclosed | n/a |
| Peer-reviewed venue | n/a |
| Evidence tier | n/a |
| Verified? | no |
| Sources | S50 |

#### Arcee Trinity Large (400B-A13B; Mini 26B-A3B; Nano 6B-A1B)

| Field | Value |
|---|---|
| Model | Arcee Trinity Large (400B-A13B; Mini 26B-A3B; Nano 6B-A1B) |
| Lab | Arcee AI (with Prime Intellect, DatologyAI) |
| Release date | 2026-01-27 (Preview/Base); report v1 2026-02-19 [S51] |
| Total / active params | '400B total parameters and 13B activated per token' [S51] |
| Architecture family | sparse MoE with 'interleaved local and global attention, gated attention, depth-scaled sandwich norm' [S51] |
| Attention variant | '48 heads ... 8 KV heads'; local window 4096 [S51] |
| MoE routing / balancing | 'sigmoid routing following Wang et al. (2024a)'; 'Soft-clamped Momentum Expert Bias Updates (SMEBU)' + 'small per-sequence balance loss' [S51] |
| Position encoding | RoPE (local/global) [S51] |
| MTP | undisclosed (not addressed in the cited sources) |
| Optimizer | 'We train the models using the Muon optimizer' (Muon for hidden, AdamW for embeddings/output); z-loss [S51] |
| Pre-training tokens | 'Trinity Large was pre-trained on 17 trillion tokens' (10T/4T/3T phases; 'over 8 trillion tokens of synthetic data') [S51] |
| Precision & QAT | undisclosed (not addressed in the cited sources) |
| Context-extension curriculum | 'We train to 256k context for inference at 512k' [S51] |
| Mid-training stage? | three data phases [S51] |
| Distillation (where, teacher) | undisclosed (not addressed in the cited sources) |
| SFT | 'particularly light post-training' (Preview) [S51] |
| RL algorithms | undisclosed (not addressed in the cited sources) |
| Reward sources | undisclosed (not addressed in the cited sources) |
| Async / off-policy RL | undisclosed (not addressed in the cited sources) |
| Agentic RL environment scale | undisclosed (not addressed in the cited sources) |
| Reasoning-effort control | reasoning variant pending [S51] |
| Model / expert merging | undisclosed (not addressed in the cited sources) |
| Continual / cross-stage distillation | undisclosed (not addressed in the cited sources) |
| Ablations / scaling laws | vocabulary ablation; batch-size increase after 4.9T 'roughly following MiniMax et al. (2025)' [S51] |
| Explicitly undisclosed | post-training/RL (still ongoing at report time) |
| Peer-reviewed venue | none |
| Evidence tier | C |
| Verified? | yes |
| Sources | S51 |

### Proprietary (system cards / blogs only)

#### OpenAI o3 (and o4-mini)

| Field | Value |
|---|---|
| Model | OpenAI o3 (and o4-mini) |
| Lab | OpenAI |
| Release date | 2025-04-16 [S52] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | undisclosed (system card does not address it) |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | undisclosed (system card does not address it) |
| Precision & QAT | undisclosed (system card does not address it) |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | undisclosed (system card does not address it) |
| SFT | undisclosed (system card does not address it) |
| RL algorithms | 'The OpenAI o-series models are trained with large-scale reinforcement learning on chains of thought' [S52] |
| Reward sources | 'deliberative alignment' (safety); task rewards undisclosed [S52] |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | 'The models use tools in their chains of thought' (browsing, Python, image) [S52] |
| Reasoning-effort control | reasoning effort levels (API) [S52] |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | undisclosed (system card does not address it) |
| Explicitly undisclosed | architecture, optimizer, data scale, RL algorithm — all undisclosed |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S52 |

#### GPT-5 (gpt-5-main / gpt-5-thinking / router)

| Field | Value |
|---|---|
| Model | GPT-5 (gpt-5-main / gpt-5-thinking / router) |
| Lab | OpenAI |
| Release date | 2025-08-07 [S53] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | 'a unified system with a smart and fast model ... a deeper reasoning model ... and a real-time router' [S53] |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | undisclosed (system card does not address it) |
| Precision & QAT | undisclosed (system card does not address it) |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | undisclosed (system card does not address it) |
| SFT | undisclosed (system card does not address it) |
| RL algorithms | 'trained to reason through reinforcement learning'; router 'continuously trained on real signals' [S53] |
| Reward sources | 'safe-completions' training; measured correctness signals for router [S53] |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | undisclosed (system card does not address it) |
| Reasoning-effort control | router chooses thinking; API reasoning effort; 'gpt-5-thinking-pro ... parallel test time compute' [S53] |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | undisclosed (system card does not address it) |
| Explicitly undisclosed | architecture, optimizer, data scale, RL algorithm — all undisclosed |
| Peer-reviewed venue | none (arXiv 2601.03267 is the system card) |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S53 |

#### GPT-5.5 (and GPT-5.5 Pro)

| Field | Value |
|---|---|
| Model | GPT-5.5 (and GPT-5.5 Pro) |
| Lab | OpenAI |
| Release date | 2026-04-23 [S54] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | undisclosed (system card does not address it) |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | undisclosed (system card does not address it) |
| Precision & QAT | undisclosed (system card does not address it) |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | undisclosed (system card does not address it) |
| SFT | undisclosed (system card does not address it) |
| RL algorithms | undisclosed (system card does not address it) |
| Reward sources | undisclosed (system card does not address it) |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | 'writing code, researching online ... moving across tools' (capabilities only) [S54] |
| Reasoning-effort control | 'GPT-5.5 Pro, which is the same underlying model using a setting that makes use of parallel test time compute' [S54] |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | undisclosed (system card does not address it) |
| Explicitly undisclosed | architecture, optimizer, data scale, RL algorithm — all undisclosed |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S54 |

#### GPT-5.6 Sol (with Terra, Luna)

| Field | Value |
|---|---|
| Model | GPT-5.6 Sol (with Terra, Luna) |
| Lab | OpenAI |
| Release date | 2026-07-09 [S55] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | 'a new family of three models: Sol, our new flagship model; Terra ...; and Luna' [S55] |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | undisclosed (system card does not address it) |
| Precision & QAT | undisclosed (system card does not address it) |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | undisclosed (system card does not address it) |
| SFT | undisclosed (system card does not address it) |
| RL algorithms | undisclosed (system card does not address it) |
| Reward sources | red-team model GPT-Red 'trained using self-play reinforcement learning' (not Sol's own reward) [S55] |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | undisclosed (system card does not address it) |
| Reasoning-effort control | undisclosed (system card does not address it) |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | 'CoT controllability ... GPT-5.6 Sol successfully controls 1.3% of CoTs around 5k tokens long' [S55] |
| Explicitly undisclosed | architecture, optimizer, data scale, RL algorithm — all undisclosed |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S55 |

#### Claude Opus 4 / Sonnet 4

| Field | Value |
|---|---|
| Model | Claude Opus 4 / Sonnet 4 |
| Lab | Anthropic |
| Release date | 2025-05-22 [S56] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | undisclosed (system card does not address it) |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | data 'as of March 2025' (no count) [S56] |
| Precision & QAT | undisclosed (system card does not address it) |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | undisclosed (system card does not address it) |
| SFT | 'pretrained on large, diverse datasets to acquire language capabilities' then HHH training [S56] |
| RL algorithms | 'human feedback, Constitutional AI ... and the training of selected character traits' [S56] |
| Reward sources | human feedback; Constitutional AI (AI feedback) [S56] |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | undisclosed (system card does not address it) |
| Reasoning-effort control | 'hybrid models offering two modes: near-instant responses and extended thinking' [S56] |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | undisclosed (system card does not address it) |
| Explicitly undisclosed | architecture, optimizer, data scale, RL algorithm — all undisclosed |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S56 |

#### Claude Opus 4.5

| Field | Value |
|---|---|
| Model | Claude Opus 4.5 |
| Lab | Anthropic |
| Release date | 2025-11-24 [S57] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | undisclosed (system card does not address it) |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | data 'up to May 2025' [S57] |
| Precision & QAT | undisclosed (system card does not address it) |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | undisclosed (system card does not address it) |
| SFT | undisclosed (system card does not address it) |
| RL algorithms | 'reinforcement learning from human feedback (RLHF) and reinforcement learning from AI feedback' [S57] |
| Reward sources | human and AI feedback [S57] |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | undisclosed (system card does not address it) |
| Reasoning-effort control | 'A new effort parameter gives users control over how extensively Claude Opus 4.5 reasons ... applies over all tokens, including thinking tokens, function calls' [S57] |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | undisclosed (system card does not address it) |
| Explicitly undisclosed | architecture, optimizer, data scale, RL algorithm — all undisclosed |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S57 |

#### Claude Opus 4.7

| Field | Value |
|---|---|
| Model | Claude Opus 4.7 |
| Lab | Anthropic |
| Release date | 2026-04-16 [S58] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | undisclosed (system card does not address it) |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | undisclosed (system card does not address it) |
| Precision & QAT | undisclosed (system card does not address it) |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | undisclosed (system card does not address it) |
| SFT | undisclosed (system card does not address it) |
| RL algorithms | undisclosed (system card does not address it) |
| Reward sources | undisclosed (system card does not address it) |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | undisclosed (system card does not address it) |
| Reasoning-effort control | effort parameter incl. 'xhigh' and 'max' (platform docs) [S60] |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | AI R&D evals only (e.g., 'Kernel task ... 371.75x') [S58] |
| Explicitly undisclosed | architecture, optimizer, data scale, RL algorithm — all undisclosed |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S58, S60 |

#### Claude Opus 4.8

| Field | Value |
|---|---|
| Model | Claude Opus 4.8 |
| Lab | Anthropic |
| Release date | 2026-05-28 [S59] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | undisclosed (system card does not address it) |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | undisclosed (system card does not address it) |
| Precision & QAT | undisclosed (system card does not address it) |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | undisclosed (system card does not address it) |
| SFT | undisclosed (system card does not address it) |
| RL algorithms | undisclosed (system card does not address it) |
| Reward sources | undisclosed (system card does not address it) |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | undisclosed (system card does not address it) |
| Reasoning-effort control | effort levels incl. 'xhigh', 'max' (platform docs) [S60] |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | undisclosed (system card does not address it) |
| Explicitly undisclosed | architecture, optimizer, data scale, RL algorithm — all undisclosed |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S59, S60 |

#### Claude Fable 5 / Claude Mythos 5 (same weights, different safeguards)

| Field | Value |
|---|---|
| Model | Claude Fable 5 / Claude Mythos 5 (same weights, different safeguards) |
| Lab | Anthropic |
| Release date | 2026-06-09 [S60] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | undisclosed (system card does not address it) |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | 'trained on a proprietary mix of publicly available information from the internet, public and private datasets, and synthetic data generated by other models' [S60] |
| Precision & QAT | undisclosed (system card does not address it) |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | 'synthetic data generated by other models' (pretraining data statement) [S60] |
| SFT | 'substantial post-training and fine-tuning, with the goal of making it an assistant whose behavior aligns with the values described in Claude's constitution' [S60] |
| RL algorithms | undisclosed (system card does not address it) |
| Reward sources | undisclosed (system card does not address it) |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | undisclosed (system card does not address it) |
| Reasoning-effort control | 'max ... Available on Claude Fable 5, Claude Mythos 5'; 'xhigh ... Long-running agentic and coding tasks (over 30 minutes) with token budgets in the millions' [S60] |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | undisclosed (system card does not address it) |
| Explicitly undisclosed | architecture, optimizer, data scale, RL algorithm — all undisclosed |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S60 |

#### Gemini 2.5 Pro / Flash

| Field | Value |
|---|---|
| Model | Gemini 2.5 Pro / Flash |
| Lab | Google DeepMind |
| Release date | 2025-03-25 (Pro exp); GA 2025-06-17; report v1 2025-07-07 [S61] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | 'sparse mixture-of-experts (MoE) transformers with native multimodal support' [S61] |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | undisclosed (system card does not address it) |
| Precision & QAT | TPUv5p training; precision undisclosed [S61] |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | 'The smaller models in the Gemini 2.5 series — Flash size and below — use distillation ... approximate it using a k-sparse distribution over the vocabulary' [S61] |
| SFT | undisclosed (system card does not address it) |
| RL algorithms | 'Gemini Thinking models are trained with Reinforcement Learning'; 'Algorithmic changes to the RL process have also improved stability' (unnamed) [S61] |
| Reward sources | 'verifiable rewards and model-based generative rewards'; RL*F: 'Data Reward Model (DRM) ... and a Critic, a prompted model that grades responses according to pre-defined rubrics' [S61] |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | 'more diverse and complex RL environments, including those requiring multi-step actions and tool use' [S61] |
| Reasoning-effort control | 'ability to set a Thinking budget, constraining the model to respond within a desired number of tokens' [S61] |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | 'considerable progress in enhancing large-scale training stability, signal propagation and optimization dynamics' (no numbers) [S61] |
| Explicitly undisclosed | architecture, optimizer, data scale, RL algorithm — all undisclosed |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S61 |

#### Gemini 3 Pro

| Field | Value |
|---|---|
| Model | Gemini 3 Pro |
| Lab | Google DeepMind |
| Release date | 2025-11-18 [S62] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | 'sparse mixture-of-experts (MoE) transformer-based models with native multimodal support' [S62] |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | undisclosed (system card does not address it) |
| Precision & QAT | TPUs; JAX/ML Pathways (precision undisclosed) [S62] |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | undisclosed (system card does not address it) |
| SFT | undisclosed (system card does not address it) |
| RL algorithms | 'trained using reinforcement learning techniques that can leverage multi-step reasoning, problem-solving and theorem-proving data' [S62] |
| Reward sources | 'reinforcement learning data, and human-preference data' [S62] |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | undisclosed (system card does not address it) |
| Reasoning-effort control | 'new thinking level' API parameter; Deep Think mode [S62] |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | undisclosed (system card does not address it) |
| Explicitly undisclosed | architecture, optimizer, data scale, RL algorithm — all undisclosed |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S62 |

#### Gemini Diffusion (experimental)

| Field | Value |
|---|---|
| Model | Gemini Diffusion (experimental) |
| Lab | Google DeepMind |
| Release date | 2025-05-20 [S63] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | 'state-of-the-art text diffusion model that learns to generate outputs by converting random noise into coherent text or code' [S63] |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | undisclosed (system card does not address it) |
| Precision & QAT | undisclosed (system card does not address it) |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | undisclosed (system card does not address it) |
| SFT | undisclosed (system card does not address it) |
| RL algorithms | undisclosed (system card does not address it) |
| Reward sources | undisclosed (system card does not address it) |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | undisclosed (system card does not address it) |
| Reasoning-effort control | undisclosed (system card does not address it) |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | undisclosed (system card does not address it) |
| Explicitly undisclosed | 'we have no details' (Nathan Lambert, quoted by Fortune); no card [S63] |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S63 |

#### xAI Grok 4 / Grok 4 Heavy

| Field | Value |
|---|---|
| Model | xAI Grok 4 / Grok 4 Heavy |
| Lab | xAI |
| Release date | 2025-07-09; model card 2025-08-20 [S64] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | undisclosed (system card does not address it) |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | undisclosed (system card does not address it) |
| Precision & QAT | undisclosed (system card does not address it) |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | undisclosed (system card does not address it) |
| SFT | undisclosed (system card does not address it) |
| RL algorithms | 'a variety of reinforcement learning techniques—human feedback, verifiable rewards, and model grading—along with supervised finetuning of specific capabilities' [S64] |
| Reward sources | 'human feedback, verifiable rewards, and model grading' [S64] |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | 'Colossus, our 200,000 GPU cluster, to run reinforcement learning training that refines Grok's reasoning abilities at pretraining scale'; 'expanded our verifiable training data from primarily math and coding data to many more domains' [S64] |
| Reasoning-effort control | 'Grok 4 Heavy ... parallel test-time compute' [S64] |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | 'increased the compute efficiency of our training by 6x' (unspecified) [S64] |
| Explicitly undisclosed | architecture, optimizer, data scale, RL algorithm — all undisclosed |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | yes |
| Sources | S64 |

#### xAI Grok 5

| Field | Value |
|---|---|
| Model | xAI Grok 5 |
| Lab | xAI |
| Release date | NOT RELEASED as of 2026-09-05 (xAI confirmed 'in training' Jan 2026; interim Grok 4.5 2026-07-08, Grok 4.6 2026-08-12) [S65] |
| Total / active params | undisclosed (system card does not address it) |
| Architecture family | undisclosed (system card does not address it) |
| Attention variant | undisclosed (system card does not address it) |
| MoE routing / balancing | undisclosed (system card does not address it) |
| Position encoding | undisclosed (system card does not address it) |
| MTP | undisclosed (system card does not address it) |
| Optimizer | undisclosed (system card does not address it) |
| Pre-training tokens | undisclosed (system card does not address it) |
| Precision & QAT | undisclosed (system card does not address it) |
| Context-extension curriculum | undisclosed (system card does not address it) |
| Mid-training stage? | undisclosed (system card does not address it) |
| Distillation (where, teacher) | undisclosed (system card does not address it) |
| SFT | undisclosed (system card does not address it) |
| RL algorithms | undisclosed (system card does not address it) |
| Reward sources | undisclosed (system card does not address it) |
| Async / off-policy RL | undisclosed (system card does not address it) |
| Agentic RL environment scale | undisclosed (system card does not address it) |
| Reasoning-effort control | undisclosed (system card does not address it) |
| Model / expert merging | undisclosed (system card does not address it) |
| Continual / cross-stage distillation | undisclosed (system card does not address it) |
| Ablations / scaling laws | undisclosed (system card does not address it) |
| Explicitly undisclosed | everything; Grok 4.6 card notes 'an improved optimizer and recipe' and 'supplemental training on anonymized Cursor workflow data' for the 1.5T-scale family [S65] |
| Peer-reviewed venue | none |
| Evidence tier | C (system card / blog) |
| Verified? | no (does not exist as a released model; no model card) |
| Sources | S65 |

## Method adoption matrix

Rows = named methods; columns = models (split into groups for width). Cells: `D`/`H`/`A`/`U` with `[S#]` pointer for D/H. Evidence quotes for every D/H cell are listed in the notes after the tables.

### Moonshot / DeepSeek / Zhipu (1–10)

| Method | Kimi K2 | Kimi K2 Thinking | Kimi K2.5 | Kimi K3 | DeepSeek-V3.1 | DeepSeek-V3.2-Exp | DeepSeek-V3.2 | DeepSeek-V4 | DeepSeek-R1 / R1-Zero | GLM-4.5 / GLM-4.5-Air |
|---|---|---|---|---|---|---|---|---|---|---|
| Muon optimizer | D [S1] | H [S2] | D [S3] | D [S4] | U | U | U | D [S8] | U | D [S10] |
| Per-Head Muon / Muon Split | A | U | U | D [S4] | U | U | U | U | U | A |
| muP / CompleteP / HP transfer | U | U | U | U | U | U | U | U | U | U |
| Multi-token prediction (MTP) | H [S4] | H [S4] | H [S4] | D [S4] | H [S5] | H [S6] | H [S7] | D [S8] | H [S9] | D [S10] |
| DSA or other trained sparse attention | A | U | U | A | A | D [S7] | D [S7] | D [S8] | U | A |
| Hybrid linear attention | A | U | U | D [S4] | U | U | U | A | U | A |
| Latent MoE | A | U | U | D [S4] | U | U | U | U | U | A |
| Aux-loss-free balancing | H [S1] | H [S2] | H [S3] | A | H [S5] | H [S6] | H [S7] | H [S8] | H [S9] | D [S10] |
| Quantile Balancing | A | U | U | D [S4] | U | U | U | U | U | U |
| Attention Residuals | A | U | U | D [S4] | U | U | U | U | U | U |
| NoPE | A | U | U | H [S4] | U | U | U | A | U | A |
| FP8 training | U | U | U | H [S4] | D [S5] | H [S7] | H [S7] | H [S8] | U | A |
| MXFP4 / 4-bit QAT | A | A | A | D [S4] | U | U | U | H [S8] | U | U |
| WSD schedule | D [S1] | U | U | A | U | U | U | U | U | A |
| RPT (reinforcement pre-training) | U | U | U | U | U | U | U | U | U | U |
| Diffusion objective | U | U | U | U | U | U | U | U | U | U |
| On-policy distillation | U | U | U | D [S4] | U | A | A | D [S8] | A | H [S10] |
| Cross-stage distillation | U | U | U | H [S4] | U | U | H [S7] | H [S8] | U | H [S10] |
| Expert merging via OPD | U | U | U | D [S4] | U | U | U | D [S8] | U | H [S10] |
| Model (weight) merging | U | U | U | A | U | U | U | A | U | U |
| GRPO | A | U | A | A | U | D [S7] | D [S7] | D [S8] | D [S9] | D [S10] |
| DAPO-style clip-higher | U | U | U | U | U | U | H [S7] | U | U | H [S10] |
| GSPO | U | U | U | U | U | U | U | U | U | U |
| Critic-based PPO | A | U | A | A | U | A | A | A | A | A |
| Async RL with staleness correction | U | U | H [S3] | D [S4] | U | U | D [S7] | U | U | H [S10] |
| Rubric rewards | D [S1] | H [S2] | H [S3] | H [S4] | U | H [S7] | D [S7] | U | A | U |
| Generative RMs | H [S1] | U | D [S3] | H [S4] | U | H [S7] | D [S7] | H [S8] | H [S9] | U |
| Self-play | U | U | U | U | U | U | U | U | U | U |
| Effort control | D [S1] | H [S2] | H [S3] | D [S4] | D [S5] | D [S6] | D [S7] | D [S8] | U | D [S10] |
| Sandboxed agentic RL | H [S1] | H [S2] | D [S3] | D [S4] | U | U | D [S7] | H [S8] | U | D [S10] |
| Continual-pretraining conversion | A | U | U | A | H [S5] | D [S6] | D [S7] | A | U | A |
| Upcycling | A | U | U | A | U | U | U | A | U | A |

### Moonshot / DeepSeek / Zhipu (11–15)

| Method | GLM-4.7 | GLM-5 | GLM-5.1 | GLM-5.2 | GLM-5.3 |
|---|---|---|---|---|---|
| Muon optimizer | H [S11] | D [S12] | H [S13] | H [S14] | H [S15] |
| Per-Head Muon / Muon Split | U | D [S12] | H [S13] | H [S14] | H [S15] |
| muP / CompleteP / HP transfer | U | U | U | U | U |
| Multi-token prediction (MTP) | H [S11] | D [S12] | D [S14] | D [S14] | H [S15] |
| DSA or other trained sparse attention | U | D [S12] | H [S13] | D [S14] | H [S15] |
| Hybrid linear attention | U | A | U | U | U |
| Latent MoE | U | U | U | U | U |
| Aux-loss-free balancing | H [S11] | D [S12] | H [S13] | H [S14] | H [S15] |
| Quantile Balancing | U | U | U | U | U |
| Attention Residuals | U | U | U | U | U |
| NoPE | U | A | U | U | U |
| FP8 training | U | H [S12] | U | U | U |
| MXFP4 / 4-bit QAT | U | U | U | U | U |
| WSD schedule | U | U | U | U | U |
| RPT (reinforcement pre-training) | U | U | U | U | U |
| Diffusion objective | U | U | U | U | U |
| On-policy distillation | U | D [S12] | U | U | D [S15] |
| Cross-stage distillation | U | D [S12] | U | U | H [S15] |
| Expert merging via OPD | U | H [S12] | U | U | H [S15] |
| Model (weight) merging | U | U | U | U | U |
| GRPO | H [S11] | D [S12] | H [S13] | H [S15] | H [S15] |
| DAPO-style clip-higher | U | H [S12] | U | U | U |
| GSPO | U | U | U | U | U |
| Critic-based PPO | U | A | U | U | U |
| Async RL with staleness correction | H [S15] | D [S12] | H [S15] | H [S15] | D [S15] |
| Rubric rewards | U | U | U | U | U |
| Generative RMs | U | U | U | U | U |
| Self-play | U | U | U | U | U |
| Effort control | H [S11] | D [S12] | D [S13] | D [S14] | D [S15] |
| Sandboxed agentic RL | H [S11] | D [S12] | D [S13] | D [S15] | D [S15] |
| Continual-pretraining conversion | U | A | U | U | U |
| Upcycling | U | A | U | U | U |

### Qwen / MiniMax / Meta / OpenAI-oss / Google open / Mistral / NVIDIA (1–10)

| Method | Qwen3 | Qwen3-Next-80B-A3B | Qwen3.5 | Qwen3.8-27B | MiniMax-M1 | MiniMax-M2 | MiniMax-M2.5 | MiniMax-M3 | Llama 4 | gpt-oss-120b / gpt-os… |
|---|---|---|---|---|---|---|---|---|---|---|
| Muon optimizer | U | U | U | U | A | U | U | U | U | U |
| Per-Head Muon / Muon Split | U | U | U | U | U | U | U | U | U | U |
| muP / CompleteP / HP transfer | U | U | U | U | U | U | U | U | H [S24] | U |
| Multi-token prediction (MTP) | A | D [S17] | D [S18] | D [S19] | U | D [S21] | D [S21] | U | U | U |
| DSA or other trained sparse attention | A | U | U | U | A | A | U | D [S23] | U | A |
| Hybrid linear attention | A | D [S17] | D [S18] | D [S19] | D [S20] | A | U | U | A | U |
| Latent MoE | U | U | U | U | U | U | U | U | U | U |
| Aux-loss-free balancing | A | A | H [S17,S18] | U | U | D [S21] | H [S22] | U | U | U |
| Quantile Balancing | U | U | U | U | U | U | U | U | U | U |
| Attention Residuals | U | U | U | U | U | U | U | U | U | U |
| NoPE | A | H [S17] | H [S18] | H [S19] | U | A | U | U | D [S24] | A |
| FP8 training | U | U | U | U | U | U | U | U | D [S24] | U |
| MXFP4 / 4-bit QAT | U | U | U | U | U | U | U | U | U | D [S25] |
| WSD schedule | U | U | U | U | U | U | U | U | U | U |
| RPT (reinforcement pre-training) | U | U | U | U | U | U | U | U | U | U |
| Diffusion objective | U | U | U | U | U | U | U | U | U | U |
| On-policy distillation | D [S16] | U | D [S18] | U | U | U | U | U | H [S24] | U |
| Cross-stage distillation | H [S16] | U | H [S18] | U | U | U | U | U | U | U |
| Expert merging via OPD | U | U | H [S18] | U | U | U | U | U | U | U |
| Model (weight) merging | U | U | U | U | U | U | U | U | U | U |
| GRPO | D [S16] | U | U | U | A | A | A | H [S23] | U | U |
| DAPO-style clip-higher | U | U | U | U | H [S20] | H [S21] | U | U | U | U |
| GSPO | D [S16] | H [S17] | D [S18] | U | U | U | U | U | U | U |
| Critic-based PPO | A | U | U | U | A | A | U | U | U | U |
| Async RL with staleness correction | U | U | H [S18] | U | D [S20] | D [S21] | D [S21] | U | H [S24] | U |
| Rubric rewards | U | U | U | U | U | U | U | U | U | U |
| Generative RMs | H [S16] | U | U | U | H [S20] | H [S21] | H [S21] | U | H [S24] | U |
| Self-play | U | U | U | U | U | U | U | U | U | U |
| Effort control | D [S16] | H [S17] | H [S18] | D [S19] | H [S20] | H [S21] | H [S22] | U | U | D [S25] |
| Sandboxed agentic RL | H [S16] | U | D [S18] | U | D [S20] | D [S21] | D [S22] | U | U | H [S25] |
| Continual-pretraining conversion | A | U | U | U | H [S20] | A | U | D [S23] | U | U |
| Upcycling | A | U | U | U | U | U | U | U | U | U |

### Qwen / MiniMax / Meta / OpenAI-oss / Google open / Mistral / NVIDIA (11–19)

| Method | Gemma 3 | Gemma 3n | Gemma 4 | Mistral Large 3 | Magistral Medium / Sm… | Devstral 2 | NVIDIA Nemotron 3 Nano | NVIDIA Nemotron 3 Sup… | NVIDIA Nemotron 3 Ult… |
|---|---|---|---|---|---|---|---|---|---|
| Muon optimizer | U | U | U | U | U | U | A | A | A |
| Per-Head Muon / Muon Split | U | U | U | U | U | U | U | U | U |
| muP / CompleteP / HP transfer | U | U | U | U | U | U | U | U | U |
| Multi-token prediction (MTP) | U | U | D [S28] | H [S29] | U | U | A | D [S33] | D [S34] |
| DSA or other trained sparse attention | A | U | U | U | U | U | U | U | U |
| Hybrid linear attention | A | U | U | U | U | U | D [S32] | D [S33] | D [S34] |
| Latent MoE | U | U | U | U | U | U | A | D [S33] | D [S34] |
| Aux-loss-free balancing | U | U | U | U | U | U | D [S32] | D [S33] | D [S34] |
| Quantile Balancing | U | U | U | U | U | U | U | U | U |
| Attention Residuals | U | U | U | U | U | U | U | U | U |
| NoPE | A | U | H [S28] | U | U | U | D [S32] | D [S33] | D [S34] |
| FP8 training | U | U | U | U | U | U | A | H [S33] | H [S34] |
| MXFP4 / 4-bit QAT | H [S26] | H [S27] | H [S28] | H [S29] | U | H [S31] | U | H [S33] | H [S34] |
| WSD schedule | U | U | U | U | U | U | D [S32] | D [S33] | D [S34] |
| RPT (reinforcement pre-training) | U | U | U | U | U | U | U | U | U |
| Diffusion objective | U | U | H [S28] | U | U | U | U | U | U |
| On-policy distillation | A | U | H [S28] | U | A | U | U | U | D [S34] |
| Cross-stage distillation | U | U | U | U | U | U | U | U | H [S34] |
| Expert merging via OPD | U | U | U | U | U | U | U | U | D [S34] |
| Model (weight) merging | D [S26] | H [S27] | H [S28] | U | U | U | U | D [S33] | A |
| GRPO | A | U | A | U | D [S30] | U | D [S32] | D [S33] | H [S34] |
| DAPO-style clip-higher | U | U | U | U | D [S30] | U | U | U | U |
| GSPO | U | U | U | U | U | U | U | U | U |
| Critic-based PPO | U | U | U | U | A | U | A | A | A |
| Async RL with staleness correction | U | U | U | U | D [S30] | U | A | U | D [S34] |
| Rubric rewards | U | U | U | U | U | U | U | U | U |
| Generative RMs | H [S26] | U | U | U | A | U | D [S32] | D [S33] | D [S34] |
| Self-play | U | U | U | U | U | U | U | U | U |
| Effort control | U | U | D [S28] | H [S29] | U | U | D [S32] | D [S33] | D [S34] |
| Sandboxed agentic RL | U | U | U | U | H [S30] | U | H [S32] | H [S33] | H [S34] |
| Continual-pretraining conversion | A | U | U | U | U | U | A | U | U |
| Upcycling | U | U | U | U | U | U | A | U | U |

### Other open-weights labs (1–10)

| Method | Olmo 3 | SmolLM3-3B | Apertus | LongCat-Flash | Ling 2.0 | Ring-1T | Step-3 | Xiaomi MiMo-7B | Xiaomi MiMo-V2-Flash | Tencent Hunyuan-A13B |
|---|---|---|---|---|---|---|---|---|---|---|
| Muon optimizer | A | U | A | A | U | A | U | U | A | U |
| Per-Head Muon / Muon Split | U | U | U | U | U | U | U | U | U | U |
| muP / CompleteP / HP transfer | U | U | U | H [S38] | U | U | U | U | U | U |
| Multi-token prediction (MTP) | U | U | U | U | D [S39] | H [S39] | H [S41] | D [S42] | D [S43] | U |
| DSA or other trained sparse attention | U | U | U | A | U | U | A | U | A | U |
| Hybrid linear attention | A | U | U | A | U | U | U | U | A | U |
| Latent MoE | U | U | U | U | U | U | U | U | U | U |
| Aux-loss-free balancing | U | U | U | H [S38] | D [S39] | D [S40] | U | U | U | U |
| Quantile Balancing | U | U | U | U | U | U | U | U | U | U |
| Attention Residuals | U | U | U | U | U | U | U | U | U | U |
| NoPE | A | D [S36] | A | U | A | U | U | A | A | U |
| FP8 training | A | A | U | U | D [S39] | H [S39] | H [S41] | U | D [S43] | U |
| MXFP4 / 4-bit QAT | U | U | U | U | U | U | U | U | U | U |
| WSD schedule | U | U | D [S37] | U | A | U | U | U | U | U |
| RPT (reinforcement pre-training) | U | U | U | U | U | U | U | U | U | U |
| Diffusion objective | U | U | U | U | U | U | U | U | U | U |
| On-policy distillation | A | A | U | U | U | U | U | U | D [S43] | U |
| Cross-stage distillation | U | U | U | U | U | U | U | U | H [S43] | U |
| Expert merging via OPD | U | U | U | U | U | U | U | U | D [S43] | U |
| Model (weight) merging | D [S35] | D [S36] | U | U | D [S39] | U | U | U | U | U |
| GRPO | D [S35] | A | A | U | H [S40] | D [S40] | U | D [S42] | U | H [S44] |
| DAPO-style clip-higher | D [S35] | U | U | U | U | H [S40] | U | U | U | U |
| GSPO | U | U | U | U | U | U | U | U | U | U |
| Critic-based PPO | A | A | A | U | U | A | U | A | U | U |
| Async RL with staleness correction | D [S35] | A | U | U | U | D [S40] | U | H [S42] | U | U |
| Rubric rewards | U | U | U | U | U | U | U | U | U | U |
| Generative RMs | H [S35] | U | H [S37] | U | U | H [S40] | U | A | U | H [S44] |
| Self-play | U | U | U | U | U | U | U | U | U | U |
| Effort control | U | D [S36] | U | U | H [S39] | U | U | U | H [S43] | D [S44] |
| Sandboxed agentic RL | H [S35] | U | U | U | U | D [S40] | U | H [S42] | H [S43] | H [S44] |
| Continual-pretraining conversion | U | U | U | U | U | U | U | U | U | U |
| Upcycling | U | U | U | H [S38] | U | U | U | U | U | U |

### Other open-weights labs (11–19)

| Method | Tencent Hy3 | ByteDance Seed-OSS-36B | IBM Granite 4.0 | Falcon-H1 | xAI Grok 2.5 | Microsoft Phi-4-reaso… | Apple Foundation Mode… | Apple Foundation Mode… | Arcee Trinity Large |
|---|---|---|---|---|---|---|---|---|---|
| Muon optimizer | U | U | U | A | U | A | U | U | D [S51] |
| Per-Head Muon / Muon Split | U | U | U | U | U | U | U | U | U |
| muP / CompleteP / HP transfer | U | U | U | D [S47] | U | U | U | U | U |
| Multi-token prediction (MTP) | D [S44] | U | U | U | U | U | U | U | U |
| DSA or other trained sparse attention | U | U | U | U | U | U | U | U | U |
| Hybrid linear attention | U | U | D [S46] | D [S47] | U | U | U | U | A |
| Latent MoE | U | U | U | U | U | U | U | U | U |
| Aux-loss-free balancing | U | U | U | U | U | U | U | U | D [S51] |
| Quantile Balancing | U | U | U | U | U | U | U | U | U |
| Attention Residuals | U | U | U | U | U | U | U | U | U |
| NoPE | U | A | D [S46] | A | U | U | U | U | D [S51] |
| FP8 training | U | U | U | U | H [S48] | U | U | U | U |
| MXFP4 / 4-bit QAT | U | U | U | U | U | U | H [S50] | U | U |
| WSD schedule | U | U | U | D [S47] | U | U | U | U | H [S51] |
| RPT (reinforcement pre-training) | U | U | U | U | U | U | U | U | U |
| Diffusion objective | U | U | U | U | U | U | U | U | U |
| On-policy distillation | U | U | U | U | U | A | A | U | U |
| Cross-stage distillation | U | U | U | U | U | U | U | U | U |
| Expert merging via OPD | U | U | U | U | U | U | U | U | U |
| Model (weight) merging | U | U | U | U | U | U | U | U | U |
| GRPO | U | U | U | A | U | D [S49] | A | U | U |
| DAPO-style clip-higher | U | U | U | U | U | U | U | U | U |
| GSPO | U | U | U | U | U | U | U | U | U |
| Critic-based PPO | U | U | U | A | U | A | A | U | U |
| Async RL with staleness correction | U | U | U | U | U | U | H [S50] | U | U |
| Rubric rewards | U | U | U | U | U | U | U | U | U |
| Generative RMs | U | U | U | U | U | A | H [S50] | U | U |
| Self-play | U | U | U | U | U | U | U | U | U |
| Effort control | D [S44] | D [S45] | U | U | U | U | U | U | U |
| Sandboxed agentic RL | U | U | U | U | U | U | U | U | U |
| Continual-pretraining conversion | U | U | U | U | U | U | U | U | U |
| Upcycling | U | U | U | U | U | U | U | U | U |

### Proprietary (system cards / blogs only) (1–10)

| Method | OpenAI o3 | GPT-5 | GPT-5.5 | GPT-5.6 Sol | Claude Opus 4 / Sonne… | Claude Opus 4.5 | Claude Opus 4.7 | Claude Opus 4.8 | Claude Fable 5 / Clau… | Gemini 2.5 Pro / Flash |
|---|---|---|---|---|---|---|---|---|---|---|
| Muon optimizer | U | U | U | U | U | U | U | U | U | U |
| Per-Head Muon / Muon Split | U | U | U | U | U | U | U | U | U | U |
| muP / CompleteP / HP transfer | U | U | U | U | U | U | U | U | U | U |
| Multi-token prediction (MTP) | U | U | U | U | U | U | U | U | U | U |
| DSA or other trained sparse attention | U | U | U | U | U | U | U | U | U | U |
| Hybrid linear attention | U | U | U | U | U | U | U | U | U | U |
| Latent MoE | U | U | U | U | U | U | U | U | U | U |
| Aux-loss-free balancing | U | U | U | U | U | U | U | U | U | U |
| Quantile Balancing | U | U | U | U | U | U | U | U | U | U |
| Attention Residuals | U | U | U | U | U | U | U | U | U | U |
| NoPE | U | U | U | U | U | U | U | U | U | U |
| FP8 training | U | U | U | U | U | U | U | U | U | U |
| MXFP4 / 4-bit QAT | U | U | U | U | U | U | U | U | U | U |
| WSD schedule | U | U | U | U | U | U | U | U | U | U |
| RPT (reinforcement pre-training) | U | U | U | U | U | U | U | U | U | U |
| Diffusion objective | U | U | U | U | U | U | U | U | U | U |
| On-policy distillation | U | U | U | U | U | U | U | U | U | A |
| Cross-stage distillation | U | U | U | U | U | U | U | U | U | U |
| Expert merging via OPD | U | U | U | U | U | U | U | U | U | U |
| Model (weight) merging | U | U | U | U | U | U | U | U | U | U |
| GRPO | U | U | U | U | U | U | U | U | U | U |
| DAPO-style clip-higher | U | U | U | U | U | U | U | U | U | U |
| GSPO | U | U | U | U | U | U | U | U | U | U |
| Critic-based PPO | U | U | U | U | U | U | U | U | U | U |
| Async RL with staleness correction | U | U | U | U | U | U | U | U | U | U |
| Rubric rewards | U | U | U | U | U | U | U | U | U | D [S61] |
| Generative RMs | U | U | U | U | H [S56] | H [S57] | U | U | U | D [S61] |
| Self-play | U | U | U | H [S55] | U | U | U | U | U | U |
| Effort control | D [S52] | D [S53] | H [S54] | U | H [S56] | D [S57] | D [S60] | D [S60] | D [S60] | D [S61] |
| Sandboxed agentic RL | H [S52] | H [S53] | U | U | U | U | U | U | U | H [S61] |
| Continual-pretraining conversion | U | U | U | U | U | U | U | U | U | U |
| Upcycling | U | U | U | U | U | U | U | U | U | U |

### Proprietary (system cards / blogs only) (11–14)

| Method | Gemini 3 Pro | Gemini Diffusion | xAI Grok 4 / Grok 4 H… | xAI Grok 5 |
|---|---|---|---|---|
| Muon optimizer | U | U | U | U |
| Per-Head Muon / Muon Split | U | U | U | U |
| muP / CompleteP / HP transfer | U | U | U | U |
| Multi-token prediction (MTP) | U | U | U | U |
| DSA or other trained sparse attention | U | U | U | U |
| Hybrid linear attention | U | U | U | U |
| Latent MoE | U | U | U | U |
| Aux-loss-free balancing | U | U | U | U |
| Quantile Balancing | U | U | U | U |
| Attention Residuals | U | U | U | U |
| NoPE | U | U | U | U |
| FP8 training | U | U | U | U |
| MXFP4 / 4-bit QAT | U | U | U | U |
| WSD schedule | U | U | U | U |
| RPT (reinforcement pre-training) | U | U | U | U |
| Diffusion objective | U | D [S63] | U | U |
| On-policy distillation | U | U | U | U |
| Cross-stage distillation | U | U | U | U |
| Expert merging via OPD | U | U | U | U |
| Model (weight) merging | U | U | U | U |
| GRPO | U | U | U | U |
| DAPO-style clip-higher | U | U | U | U |
| GSPO | U | U | U | U |
| Critic-based PPO | U | U | U | U |
| Async RL with staleness correction | U | U | U | U |
| Rubric rewards | U | U | U | U |
| Generative RMs | H [S62] | U | D [S64] | U |
| Self-play | U | U | U | U |
| Effort control | D [S62] | U | H [S64] | U |
| Sandboxed agentic RL | U | U | H [S64] | U |
| Continual-pretraining conversion | U | U | U | U |
| Upcycling | U | U | U | U |

### Matrix evidence notes (all D/H cells)

- **Kimi K2 (Instruct/Base)**: Muon optimizer = disclosed [S1] 'MuonClip ... integrate Muon with weight decay, consistent RMS matching, and QK-Clip'; Multi-token prediction (MTP) = hinted [S4] K3 table lists K2 with '1 layer' MTP; Aux-loss-free balancing = hinted [S1] follows DeepSeek-V3 routing; WSD schedule = disclosed [S1] 'the WSD learning rate schedule [26], processing a total of 15.5T tokens'; Rubric rewards = disclosed [S1] 'self-critique rubric reward mechanism'; Generative RMs = hinted [S1] self-critique critic model judges responses; Effort control = disclosed [S1] 'per-sample maximum token budget throughout RL training'; Sandboxed agentic RL = hinted [S1] 'interactions with real and synthetic environments'
- **Kimi K2 Thinking**: Muon optimizer = hinted [S2] K2 base; Multi-token prediction (MTP) = hinted [S4]; Aux-loss-free balancing = hinted [S2]; Rubric rewards = hinted [S2] inherits K2 RL; Effort control = hinted [S2] 'heavy' mode reported by third parties; Sandboxed agentic RL = hinted [S2] '200 - 300 sequential tool calls'
- **Kimi K2.5**: Muon optimizer = disclosed [S3] 'employs the token-efficient MuonClip optimizer'; Multi-token prediction (MTP) = hinted [S4]; Aux-loss-free balancing = hinted [S3] K2 backbone; Async RL with staleness correction = hinted [S3] 'every agent task as an independent asynchronous coroutine' (no staleness correction named); Rubric rewards = hinted [S3] K2 lineage; Generative RMs = disclosed [S3] 'Generative Reward Model (GRM)'; Effort control = hinted [S3] instant/thinking modes; Sandboxed agentic RL = disclosed [S3] 'agent swarm of up to 100 sub-agents ... 1,500 coordinated steps'
- **Kimi K3**: Muon optimizer = disclosed [S4] 'adopts Muon [53] as the optimizer for its matrix parameters'; Per-Head Muon / Muon Split = disclosed [S4] 'Per-Head Muon extends Muon by optimizing attention heads independently'; Multi-token prediction (MTP) = disclosed [S4] 'pre-trained with a multi-token-prediction (MTP) layer'; Hybrid linear attention = disclosed [S4] '69 KDA + 24 Gated MLA'; Latent MoE = disclosed [S4] 'Stable LatentMoE'; Quantile Balancing = disclosed [S4] 'Quantile Balancing derives expert allocation directly from router-score quantiles'; Attention Residuals = disclosed [S4] 'Attention Residuals (AttnRes) allows each layer to selectively attend to representations from all preceding layers'; NoPE = hinted [S4] KDA layers carry position; MLA layers rotary; FP8 training = hinted [S4] 'MXFP8 activations' at QAT stage; pre-training precision not stated; MXFP4 / 4-bit QAT = disclosed [S4] 'MXFP4 weights with MXFP8 activations'; 'QAT from the SFT stage onward'; On-policy distillation = disclosed [S4] 'multi-teacher on-policy distillation' (MOPD); Cross-stage distillation = hinted [S4] MOPD consolidates RL experts; Expert merging via OPD = disclosed [S4] 'Domain- and effort-specialized policies are consolidated into a unified model through multi-teacher on-policy distillation'; Async RL with staleness correction = disclosed [S4] 'data staleness ... Our policy optimization algorithm inherently tolerates such an extreme off-policy regime through a per-token regularization'; Rubric rewards = hinted [S4] K2 lineage; Generative RMs = hinted [S4]; Effort control = disclosed [S4] 'reasoning_effort ... low, high, max'; '-1 reward override' when budget exceeded; Sandboxed agentic RL = disclosed [S4] 'resumable microVM sandboxes'; 'hundreds or thousands of tool calls'
- **DeepSeek-V3.1**: Multi-token prediction (MTP) = hinted [S5] inherited V3; Aux-loss-free balancing = hinted [S5] 'e_score_correction_bias' in config; FP8 training = disclosed [S5] 'trained using the UE8M0 FP8 scale data format on both model weights and activations'; Effort control = disclosed [S5] 'Think & Non-Think - one model, two modes'; Continual-pretraining conversion = hinted [S5] continued pre-training for context (630B+209B tokens), not architecture conversion
- **DeepSeek-V3.2-Exp**: Multi-token prediction (MTP) = hinted [S6]; DSA or other trained sparse attention = disclosed [S7] 'lightning indexer and a fine-grained token selection mechanism'; Aux-loss-free balancing = hinted [S6]; FP8 training = hinted [S7] indexer 'can be implemented in FP8'; GRPO = disclosed [S7] same pipeline as V3.2; Rubric rewards = hinted [S7]; Generative RMs = hinted [S7]; Effort control = disclosed [S6] think/non-think; Continual-pretraining conversion = disclosed [S6] continued training from V3.1-Terminus: dense warm-up then sparse training
- **DeepSeek-V3.2 (and V3.2-Speciale)**: Multi-token prediction (MTP) = hinted [S7]; DSA or other trained sparse attention = disclosed [S7] 'retrieves only the key-value entries corresponding to the top-k index scores'; Aux-loss-free balancing = hinted [S7] 'Keep Routing'; FP8 training = hinted [S7]; Cross-stage distillation = hinted [S7] specialists -> unified; GRPO = disclosed [S7] 'we still adopt Group Relative Policy Optimization (GRPO)'; DAPO-style clip-higher = hinted [S7] 'Off-Policy Sequence Masking' as clipping alternative; Async RL with staleness correction = disclosed [S7] 'Off-Policy Sequence Masking'; multi-minibatch off-policy updates; Rubric rewards = disclosed [S7] generative reward model with per-prompt rubrics; Generative RMs = disclosed [S7] 'we employ a generative reward model'; Effort control = disclosed [S7] think/non-think; Speciale; Sandboxed agentic RL = disclosed [S7] 'Large-Scale Agentic Task Synthesis Pipeline'; code/Jupyter environments; Continual-pretraining conversion = disclosed [S7] from V3.1-Terminus 128K checkpoint
- **DeepSeek-V4 (Pro / Flash, preview)**: Muon optimizer = disclosed [S8] 'we introduce the Muon optimizer to the training of DeepSeek-V4 series'; Multi-token prediction (MTP) = disclosed [S8] 'retain the DeepSeekMoE framework and Multi-Token Prediction (MTP) strategy'; DSA or other trained sparse attention = disclosed [S8] 'Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA)'; Aux-loss-free balancing = hinted [S8] DeepSeekMoE; Hash-MoE bootstrap; FP8 training = hinted [S8] V3 lineage; FP4 for routed experts; MXFP4 / 4-bit QAT = hinted [S8] 'FP4 quantization-aware training for MoE expert weights' (FP4, not MXFP4-named); On-policy distillation = disclosed [S8] 'unified model consolidation via on-policy distillation'; Cross-stage distillation = hinted [S8]; Expert merging via OPD = disclosed [S8] experts -> unified via reverse-KL OPD; GRPO = disclosed [S8] 'Reinforcement Learning (RL) is applied using Group Relative Policy Optimization (GRPO)'; Generative RMs = hinted [S8] 'reward models tailored to specific success criteria'; Effort control = disclosed [S8] 'Non-think, Think High, and Think Max'; Sandboxed agentic RL = hinted [S8] agent expert domain
- **DeepSeek-R1 / R1-Zero**: Multi-token prediction (MTP) = hinted [S9]; Aux-loss-free balancing = hinted [S9]; GRPO = disclosed [S9] 'use Group Relative Policy Optimization (GRPO)'; Generative RMs = hinted [S9] 'model-based rewards for general data'
- **GLM-4.5 / GLM-4.5-Air**: Muon optimizer = disclosed [S10] 'We employed the Muon optimizer for all parameters except word embedding, bias, and weights for RMSNorm'; Multi-token prediction (MTP) = disclosed [S10] 'we add an MoE layer as the MTP (Multi-Token Prediction) layer'; Aux-loss-free balancing = disclosed [S10] 'loss-free balance routing and sigmoid gates'; On-policy distillation = hinted [S10] 'self-distillation techniques to integrate multiple experts'; Cross-stage distillation = hinted [S10] iterative distillation of RL experts; Expert merging via OPD = hinted [S10] expert self-distillation into unified model; GRPO = disclosed [S10] 'Our overall RL algorithm builds upon the GRPO [31] framework, excluding the KL loss term'; DAPO-style clip-higher = hinted [S10] 'adaptive clipping'; Async RL with staleness correction = hinted [S10] slime 'disaggregated, asynchronous model' for agentic RL; no staleness correction named; Effort control = disclosed [S10] thinking / non-thinking modes; Sandboxed agentic RL = disclosed [S10] 'high-concurrency Docker-based runtime that provisions isolated environments for each task'
- **GLM-4.7 (and 4.7-Flash)**: Muon optimizer = hinted [S11] as GLM-4.5; Multi-token prediction (MTP) = hinted [S11]; Aux-loss-free balancing = hinted [S11]; GRPO = hinted [S11]; Async RL with staleness correction = hinted [S15] slime; Effort control = hinted [S11]; Sandboxed agentic RL = hinted [S11]
- **GLM-5**: Muon optimizer = disclosed [S12] Muon with 'Muon Split'; Per-Head Muon / Muon Split = disclosed [S12] 'Muon Split ... split these matrices into smaller matrices for different heads and apply matrix orthogonalization'; Multi-token prediction (MTP) = disclosed [S12] 'sharing the parameters of 3 MTP layers during training'; DSA or other trained sparse attention = disclosed [S12] MLA with DSA; Aux-loss-free balancing = disclosed [S12] as GLM-4.5 loss-free + sigmoid; FP8 training = hinted [S12] 'GLM-5 uses FP8 for rollout inference'; On-policy distillation = disclosed [S12] 'on-policy cross-stage distillation as the final stage, adopting an on-policy distillation algorithm'; Cross-stage distillation = disclosed [S12] 'On-Policy Cross-Stage Distillation throughout this process to prevent catastrophic forgetting'; Expert merging via OPD = hinted [S12]; GRPO = disclosed [S12] 'Our RL algorithm builds upon GRPO [40] and incorporates the IcePop technique'; DAPO-style clip-higher = hinted [S12] 'token-level clipping mechanism ([1-eps_l, 1+eps_h])'; Async RL with staleness correction = disclosed [S12] 'Direct Double-sided Importance Sampling ... controlling off-policy bias without tracking historical policy checkpoints'; 'discard a sample if its oldest rollout version is too stale'; Effort control = disclosed [S12] 'reasoning_effort' Max/High; Sandboxed agentic RL = disclosed [S12] 'over 10K real-world Software Engineering (SWE), terminal tasks'
- **GLM-5.1**: Muon optimizer = hinted [S13]; Per-Head Muon / Muon Split = hinted [S13]; Multi-token prediction (MTP) = disclosed [S14] 'MTP step parameters are shared as in GLM-5.1'; DSA or other trained sparse attention = hinted [S13]; Aux-loss-free balancing = hinted [S13]; GRPO = hinted [S13]; Async RL with staleness correction = hinted [S15] slime; Effort control = disclosed [S13] thinking effort levels; Sandboxed agentic RL = disclosed [S13] 'hundreds of rounds and thousands of tool calls'
- **GLM-5.2**: Muon optimizer = hinted [S14]; Per-Head Muon / Muon Split = hinted [S14]; Multi-token prediction (MTP) = disclosed [S14] 'improve GLM-5.2's MTP layer ... acceptance length by up to 20%'; DSA or other trained sparse attention = disclosed [S14] 'IndexShare, which reuses the same indexer across every four sparse attention layers'; Aux-loss-free balancing = hinted [S14]; GRPO = hinted [S15]; Async RL with staleness correction = hinted [S15]; Effort control = disclosed [S14] 'multiple thinking effort levels'; Sandboxed agentic RL = disclosed [S15] long-horizon environments (SAO)
- **GLM-5.3 (and 5.3-Flash)**: Muon optimizer = hinted [S15]; Per-Head Muon / Muon Split = hinted [S15]; Multi-token prediction (MTP) = hinted [S15]; DSA or other trained sparse attention = hinted [S15]; Aux-loss-free balancing = hinted [S15]; On-policy distillation = disclosed [S15] slime 'top-k and full-vocabulary OPD'; 'multi-teacher OPD'; Cross-stage distillation = hinted [S15]; Expert merging via OPD = hinted [S15] multi-teacher OPD support; GRPO = hinted [S15]; Async RL with staleness correction = disclosed [S15] 'slime for large-scale asynchronous training'; logprob difference 'controlled at the 1e-7 level'; Effort control = disclosed [S15] low/high/max; Sandboxed agentic RL = disclosed [S15] 'more environments, more diverse tasks'; SAO with compaction
- **Qwen3 (235B-A22B, 30B-A3B, dense 0.6B–32B)**: On-policy distillation = disclosed [S16] 'Strong-to-Weak Distillation ... on-policy knowledge transfer ... aligning its logits'; Cross-stage distillation = hinted [S16] off-policy then on-policy phases; GRPO = disclosed [S16] 'employed GRPO (Shao et al., 2024)'; GSPO = disclosed [S16] GSPO paper 2507.18071: applied to latest Qwen3 models; Generative RMs = hinted [S16] model-based rewards in general RL; Effort control = disclosed [S16] 'thinking budget mechanism'; Sandboxed agentic RL = hinted [S16] agent capabilities in general RL
- **Qwen3-Next-80B-A3B**: Multi-token prediction (MTP) = disclosed [S17] 'native Multi-Token Prediction (MTP)'; Hybrid linear attention = disclosed [S17] 'mix Gated DeltaNet with standard attention at a 3:1 ratio'; NoPE = hinted [S17] RoPE on 25% of dims (partial RoPE); GSPO = hinted [S17] RL stability for hybrid attention + sparse MoE 'solved' (algorithm unnamed; GSPO paper covers Qwen3); Effort control = hinted [S17] Instruct/Thinking
- **Qwen3.5 (397B-A17B flagship; 122B-A10B, 35B-A3B, 27B, small)**: Multi-token prediction (MTP) = disclosed [S18] 'MTP: trained with multi-steps'; Hybrid linear attention = disclosed [S18] '3 * (Gated DeltaNet -> MoE) -> 1 * (Gated Attention -> MoE)'; Aux-loss-free balancing = hinted [S17,S18]; NoPE = hinted [S18] RoPE dim 64 partial; On-policy distillation = disclosed [S18] Omni report (same base): 'On-Policy Distillation' stage; Cross-stage distillation = hinted [S18] Specialist Distillation -> OPD; Expert merging via OPD = hinted [S18]; GSPO = disclosed [S18] Omni report: 'adopt GSPO'; Async RL with staleness correction = hinted [S18] 'asynchronous RL frameworks supporting massive-scale agent scaffolds'; Effort control = hinted [S18]; Sandboxed agentic RL = disclosed [S18] 'million-agent environments'
- **Qwen3.8-27B (and Qwen3.8-2.4T-A95B hosted)**: Multi-token prediction (MTP) = disclosed [S19] 'MTP (Multi-Token Prediction): trained with multiple steps'; Hybrid linear attention = disclosed [S19] Gated DeltaNet + Gated Attention; NoPE = hinted [S19] RoPE dim 64; Effort control = disclosed [S19] 'reasoning_effort' 'xhigh (default), medium, and low'
- **MiniMax-M1 (40k/80k)**: Hybrid linear attention = disclosed [S20] lightning attention with periodic softmax attention (7:1); DAPO-style clip-higher = hinted [S20] dynamic sampling and length penalty from DAPO; IS-weight clipping; Async RL with staleness correction = disclosed [S20] '16 rounds of off-policy updates per generation batch' with clipped IS weights; Generative RMs = hinted [S20] 'or from a reward model'; Effort control = hinted [S20] 40k/80k variants; Sandboxed agentic RL = disclosed [S20] 'sandbox-based, real-world software engineering environments'; Continual-pretraining conversion = hinted [S20] continued pre-training from Text-01 (7.5T tokens)
- **MiniMax-M2 (series M2 -> M2.1 -> M2.5 -> M2.7)**: Multi-token prediction (MTP) = disclosed [S21] 'single MTP module (K=1) ... expanded to K=3 via weight copying'; Aux-loss-free balancing = disclosed [S21] 'sigmoid gating with learnable expert-specific bias terms ... reducing reliance on auxiliary losses'; DAPO-style clip-higher = hinted [S21] CISPO IS clipping; Async RL with staleness correction = disclosed [S21] 'Windowed FIFO'; 'prefix tree merging'; Generative RMs = hinted [S21] 'Process Reward'; Effort control = hinted [S21] interleaved thinking; Sandboxed agentic RL = disclosed [S21] 'over a hundred thousand distinct real-world agent scaffolds and environments'
- **MiniMax-M2.5**: Multi-token prediction (MTP) = disclosed [S21] MTP heads co-trained in RL ('Top-K KL loss'); Aux-loss-free balancing = hinted [S22]; Async RL with staleness correction = disclosed [S21] Windowed FIFO; Generative RMs = hinted [S21]; Effort control = hinted [S22]; Sandboxed agentic RL = disclosed [S22] 'hundreds of thousands of complex real-world environments'
- **MiniMax-M3**: DSA or other trained sparse attention = disclosed [S23] 'blockwise sparse attention ... A lightweight Index Branch scores key-value blocks'; GRPO = hinted [S23] Forge/CISPO lineage not restated; Continual-pretraining conversion = disclosed [S23] 'MSA-CPT' ~140B tokens converting from full attention
- **Llama 4 (Scout 109B-A17B, Maverick 400B-A17B; Behemoth preview)**: muP / CompleteP / HP transfer = hinted [S24] 'MetaP ... reliably set critical model hyper-parameters such as per-layer learning rates and initialization scales'; NoPE = disclosed [S24] 'interleaved attention layers without positional embeddings' (iRoPE); FP8 training = disclosed [S24] 'pre-training our Llama 4 Behemoth model using FP8'; On-policy distillation = hinted [S24] 'codistilled ... from Llama 4 Behemoth' with dynamic soft/hard loss (during pre-training); Async RL with staleness correction = hinted [S24] 'fully asynchronous online RL training framework'; Generative RMs = hinted [S24] 'Llama models as a judge'
- **gpt-oss-120b / gpt-oss-20b**: MXFP4 / 4-bit QAT = disclosed [S25] 'post-trained the models with quantization of the MoE weights to MXFP4 format'; Effort control = disclosed [S25] 'three reasoning levels: low, medium, and high'; Sandboxed agentic RL = hinted [S25] tool use trained
- **Gemma 3 (1B–27B)**: MXFP4 / 4-bit QAT = hinted [S26] QAT in 'per-channel int4, per-block int4, and switched fp8' (not MXFP4); Model (weight) merging = disclosed [S26] 'improved versions of BOND, WARM, and WARP'; Generative RMs = hinted [S26] weight-averaged reward models
- **Gemma 3n (E2B, E4B)**: MXFP4 / 4-bit QAT = hinted [S27] 'advanced activation quantization'; Model (weight) merging = hinted [S27] MatFormer mix'n'match submodel extraction
- **Gemma 4 (E2B, E4B, 12B, 26B-A4B MoE, 31B; DiffusionGemma)**: Multi-token prediction (MTP) = disclosed [S28] 'multi-token prediction (MTP) drafter head ... 4-layer Transformer block'; NoPE = hinted [S28] 'p-RoPE ... p=0.25 on global attention layers'; MXFP4 / 4-bit QAT = hinted [S28] QAT 'mix of int2 and int4'; Diffusion objective = hinted [S28] DiffusionGemma sibling announced; objective not described in report; On-policy distillation = hinted [S28] Gemma 3-style distillation implied; Model (weight) merging = hinted [S28] inherits WARP; Effort control = disclosed [S28] thinking mode on/off
- **Mistral Large 3 (and Ministral 3)**: Multi-token prediction (MTP) = hinted [S29] Eagle draft model released separately; MXFP4 / 4-bit QAT = hinted [S29] NVFP4 checkpoints (post-training quantization); Effort control = hinted [S29] reasoning variants
- **Magistral Medium / Small**: GRPO = disclosed [S30] GRPO with 'Eliminating KL divergence', 'Clip-Higher'; DAPO-style clip-higher = disclosed [S30] 'Clip-Higher' eps_high 0.26-0.28; Async RL with staleness correction = disclosed [S30] 'off-policy corrections inherent to the loss function'; in-flight weight updates; Sandboxed agentic RL = hinted [S30] test execution
- **Devstral 2 (123B) / Devstral Small 2 (24B)**: MXFP4 / 4-bit QAT = hinted [S31] FP4/FP8 weights supported
- **NVIDIA Nemotron 3 Nano (30B-A3B)**: Hybrid linear attention = disclosed [S32] Mamba-2 hybrid; Aux-loss-free balancing = disclosed [S32] 'DeepSeek's aux-loss-free load balancing'; NoPE = disclosed [S32] 'We do not use any positional embeddings'; WSD schedule = disclosed [S32] 'using the Warmup-Stable-Decay (Hu et al., 2024) learning rate schedule on 25 trillion tokens'; GRPO = disclosed [S32] 'synchronous GRPO with masked importance sampling'; Generative RMs = disclosed [S32] 'generative reward model (GenRM)'; Effort control = disclosed [S32] 'randomly truncate 3% of reasoning traces to different reasoning budgets'; Sandboxed agentic RL = hinted [S32] multi-environment RLVR (Nemo-Gym)
- **NVIDIA Nemotron 3 Super (120B-A12B)**: Multi-token prediction (MTP) = disclosed [S33] 'include MTP layers'; Hybrid linear attention = disclosed [S33]; Latent MoE = disclosed [S33] LatentMoE; Aux-loss-free balancing = disclosed [S33] 'auxiliary-loss-free load balancing'; NoPE = disclosed [S33] 'we omit positional embeddings'; FP8 training = hinted [S33] NVFP4 pre-training with higher-precision fallback layers; MXFP4 / 4-bit QAT = hinted [S33] 'pre-trained in NVFP4' (4-bit pre-training, not MXFP4 QAT); WSD schedule = disclosed [S33] merge during WSD stable phase; Model (weight) merging = disclosed [S33] 'Tracking Merge Evaluation'; GRPO = disclosed [S33]; Generative RMs = disclosed [S33] GenRM; Effort control = disclosed [S33]; Sandboxed agentic RL = hinted [S33]
- **NVIDIA Nemotron 3 Ultra (550B-A55B)**: Multi-token prediction (MTP) = disclosed [S34] 'two heads during pre-training ... share the same parameters'; Hybrid linear attention = disclosed [S34]; Latent MoE = disclosed [S34]; Aux-loss-free balancing = disclosed [S34]; NoPE = disclosed [S34]; FP8 training = hinted [S34]; MXFP4 / 4-bit QAT = hinted [S34] 'NVFP4 layers use the E2M1 datatype'; WSD schedule = disclosed [S34] 'Warmup-Stable-Decay (WSD) learning rate schedule over a total horizon of 20 trillion tokens'; On-policy distillation = disclosed [S34] 'Multi-teacher On-Policy Distillation (MOPD)'; Cross-stage distillation = hinted [S34]; Expert merging via OPD = disclosed [S34] 'consolidated these teachers into Ultra through dense token-level guidance'; GRPO = hinted [S34] NeMo-RL 'GRPO with verifiable rewards'; Async RL with staleness correction = disclosed [S34] 'MOPD Asynchronous on-policy distillation'; Generative RMs = disclosed [S34] 'GenRM used for RLHF'; Effort control = disclosed [S34] 'reasoning effort control'; Sandboxed agentic RL = hinted [S34] SWE/terminal environments
- **Olmo 3 (7B, 32B; Think / Instruct / RL-Zero)**: Model (weight) merging = disclosed [S35] 'two parallel runs ... followed by model merging'; GRPO = disclosed [S35] OlmoRL GRPO-based; DAPO-style clip-higher = disclosed [S35] 'clip-higher, no KL term'; Async RL with staleness correction = disclosed [S35] 'in-flight weight updates, continuous batching'; truncated importance sampling; Generative RMs = hinted [S35] LLM judges; Sandboxed agentic RL = hinted [S35]
- **SmolLM3-3B**: NoPE = disclosed [S36] 'NoPE ... removing rotary position embeddings from every 4th layer'; Model (weight) merging = disclosed [S36] merging to recover long context after APO; Effort control = disclosed [S36] '/think and /no_think flags'
- **Apertus (8B, 70B)**: WSD schedule = disclosed [S37] 'Warmup-Stable-Decay (WSD) learning rate schedule'; Generative RMs = hinted [S37] reward model
- **LongCat-Flash (560B, ~27B active)**: muP / CompleteP / HP transfer = hinted [S38] 'hyperparameter transfer strategy based on width scaling'; Aux-loss-free balancing = hinted [S38] 'expert bias adjusted by a PID-controller'; Upcycling = hinted [S38] 'model growth ... stacking r copies of the small model'
- **Ling 2.0 (Ling-mini-2.0 16B-A1.4B, Ling-flash-2.0 103B-A6.1B, Ling-1T 1T-A51B)**: Multi-token prediction (MTP) = disclosed [S39] 'High-Sparsity MoE with MTP'; Aux-loss-free balancing = disclosed [S39] 'Aux-loss-free, sigmoid-scoring expert routing'; FP8 training = disclosed [S39] 'full-scale FP8 training'; Model (weight) merging = disclosed [S39] WSM checkpoint merging; GRPO = hinted [S40] Ring; Effort control = hinted [S39]
- **Ring-1T**: Multi-token prediction (MTP) = hinted [S39]; Aux-loss-free balancing = disclosed [S40] 'MoE router bias held fixed'; FP8 training = hinted [S39]; GRPO = disclosed [S40] 'IcePop, a variant of GRPO'; DAPO-style clip-higher = hinted [S40] 'double-sided masking calibration'; Async RL with staleness correction = disclosed [S40] ASystem 'large-scale asynchronous training'; IcePop corrects train-inference mismatch; Generative RMs = hinted [S40] hybrid reward system; RLHF; Sandboxed agentic RL = disclosed [S40] ASandbox 'request throughput of up to 10K/s'
- **Step-3 (321B VLM; 316B LLM, 38B active)**: Multi-token prediction (MTP) = hinted [S41] MTP-compatible, 'no MTP' in headline; FP8 training = hinted [S41] FP8 serving
- **Xiaomi MiMo-7B**: Multi-token prediction (MTP) = disclosed [S42] MTP 'to enhance training performance and accelerate inference decoding'; GRPO = disclosed [S42] GRPO-style with test-difficulty driven reward; Async RL with staleness correction = hinted [S42] 'Seamless Rollout Engine'; Sandboxed agentic RL = hinted [S42] code sandbox
- **Xiaomi MiMo-V2-Flash (309B-A15B)**: Multi-token prediction (MTP) = disclosed [S43] 'pre-trained on 27 trillion tokens with Multi-Token Prediction (MTP)'; FP8 training = disclosed [S43] 'FP8 mixed precision'; On-policy distillation = disclosed [S43] 'Multi-Teacher On-Policy Distillation (MOPD)'; Cross-stage distillation = hinted [S43]; Expert merging via OPD = disclosed [S43] domain-specialized teachers -> student; Effort control = hinted [S43]; Sandboxed agentic RL = hinted [S43] 'large-scale agentic RL'
- **Tencent Hunyuan-A13B (80B-A13B)**: GRPO = hinted [S44] GRPO via secondary; Generative RMs = hinted [S44] 'generative reward model or GRM'; Effort control = disclosed [S44] 'dual-mode Chain-of-Thought'; Sandboxed agentic RL = hinted [S44] agent RL
- **Tencent Hy3 (295B-A21B)**: Multi-token prediction (MTP) = disclosed [S44] 'Number of MTP Layers: 1'; Effort control = disclosed [S44] 'hybrid fast-and-slow-thinking'
- **ByteDance Seed-OSS-36B**: Effort control = disclosed [S45] 'thinking budget ... periodically triggers self-reflection'
- **IBM Granite 4.0 (H-Small 32B-A9B, H-Tiny 7B-A1B, H-Micro 3B, Micro 3B)**: Hybrid linear attention = disclosed [S46] Mamba-2 hybrid; NoPE = disclosed [S46] 'uses no positional encoding (NoPE)'
- **Falcon-H1 (0.5B–34B)**: muP / CompleteP / HP transfer = disclosed [S47] 'customized Maximal Update Parametrization (muP)'; Hybrid linear attention = disclosed [S47] parallel Mamba-2 + attention; WSD schedule = disclosed [S47] 'WSD: 50MT warmup, 1.5GT stable, 1.5GT decay'
- **xAI Grok 2.5 (open weights)**: FP8 training = hinted [S48] FP8 serving
- **Microsoft Phi-4-reasoning / -plus**: GRPO = disclosed [S49] 'Group Relative Policy Optimization (GRPO) algorithm'
- **Apple Foundation Models 2025 (~3B on-device; PT-MoE server)**: MXFP4 / 4-bit QAT = hinted [S50] 2-bit QAT; Async RL with staleness correction = hinted [S50] 'trajectory generators (TGs) and a policy updater (PU)' with replay buffer; Generative RMs = hinted [S50] 'LLM-as-a-judge'
- **Arcee Trinity Large (400B-A13B; Mini 26B-A3B; Nano 6B-A1B)**: Muon optimizer = disclosed [S51] 'We train the models using the Muon optimizer'; Aux-loss-free balancing = disclosed [S51] 'sigmoid routing following Wang et al. (2024a)'; SMEBU + small per-sequence balance loss; NoPE = disclosed [S51] 'global layer without positional embeddings (NoPE)'; WSD schedule = hinted [S51] stable phase then 'cosine decay to 1/10 of the peak'
- **OpenAI o3 (and o4-mini)**: Effort control = disclosed [S52] reasoning effort levels; Sandboxed agentic RL = hinted [S52] 'The models use tools in their chains of thought'
- **GPT-5 (gpt-5-main / gpt-5-thinking / router)**: Effort control = disclosed [S53] router + reasoning effort; 'parallel test time compute' for Pro; Sandboxed agentic RL = hinted [S53]
- **GPT-5.5 (and GPT-5.5 Pro)**: Effort control = hinted [S54] Pro 'parallel test time compute'
- **GPT-5.6 Sol (with Terra, Luna)**: Self-play = hinted [S55] GPT-Red red-team model 'trained using self-play reinforcement learning' (not Sol itself)
- **Claude Opus 4 / Sonnet 4**: Generative RMs = hinted [S56] Constitutional AI (AI feedback); Effort control = hinted [S56] 'two modes: near-instant responses and extended thinking'
- **Claude Opus 4.5**: Generative RMs = hinted [S57] RLAIF; Effort control = disclosed [S57] 'A new effort parameter gives users control over how extensively Claude Opus 4.5 reasons'
- **Claude Opus 4.7**: Effort control = disclosed [S60] 'xhigh' and 'max' effort
- **Claude Opus 4.8**: Effort control = disclosed [S60]
- **Claude Fable 5 / Claude Mythos 5 (same weights, different safeguards)**: Effort control = disclosed [S60] 'max ... Available on Claude Fable 5, Claude Mythos 5'
- **Gemini 2.5 Pro / Flash**: Rubric rewards = disclosed [S61] 'a Critic, a prompted model that grades responses according to pre-defined rubrics'; Generative RMs = disclosed [S61] 'model-based generative rewards'; Effort control = disclosed [S61] 'Thinking budget'; Sandboxed agentic RL = hinted [S61] 'RL environments ... multi-step actions and tool use'
- **Gemini 3 Pro**: Generative RMs = hinted [S62] 'human-preference data'; Effort control = disclosed [S62] 'new thinking level' parameter
- **Gemini Diffusion (experimental)**: Diffusion objective = disclosed [S63] 'text diffusion model that learns to generate outputs by converting random noise into coherent text or code'
- **xAI Grok 4 / Grok 4 Heavy**: Generative RMs = disclosed [S64] 'model grading'; Effort control = hinted [S64] Grok 4 Heavy parallel test-time compute; Sandboxed agentic RL = hinted [S64] 'verifiable training data ... many more domains'

### Absent-cell rationale (all A cells with a stated alternative)

- **Kimi K2 (Instruct/Base)**: Per-Head Muon / Muon Split: [S1] global MuonClip; per-head variant introduced in K3; DSA or other trained sparse attention: [S1] MLA full attention; Hybrid linear attention: [S1] MLA only; Latent MoE: [S1] DeepSeek-V3-style MoE; Quantile Balancing: [S4] introduced in K3; Attention Residuals: [S4] introduced in K3; NoPE: [S1] RoPE in MLA; MXFP4 / 4-bit QAT: [S2] no QAT; INT4 QAT arrives with K2 Thinking; GRPO: [S1] K1.5-style policy gradient with regularizer, no GRPO; Critic-based PPO: [S1] critic-free; Continual-pretraining conversion: [S1] from scratch; Upcycling: [S1] from scratch
- **Kimi K2 Thinking**: MXFP4 / 4-bit QAT: [S2] 'INT4 weight-only quantization ... QAT' (INT4, not MXFP4)
- **Kimi K2.5**: MXFP4 / 4-bit QAT: [S3] 'same native int4 quantization method as Kimi-K2-Thinking'; GRPO: [S3] K2-style policy optimization; PARL; Critic-based PPO: [S3]
- **Kimi K3**: DSA or other trained sparse attention: [S4] KDA + Gated MLA, no token-selection sparse attention; Aux-loss-free balancing: [S4] replaced by Quantile Balancing; WSD schedule: [S4] 'cosine decay consistently achieves a lower final loss than WSD'; Model (weight) merging: [S4] no weight merging; GRPO: [S4] K2-lineage per-token regularized policy gradient; Critic-based PPO: [S4]; Continual-pretraining conversion: [S4] from scratch; Upcycling: [S4] from scratch
- **DeepSeek-V3.1**: DSA or other trained sparse attention: [S6] introduced in V3.2-Exp
- **DeepSeek-V3.2-Exp**: On-policy distillation: [S7] specialist distillation via data; Critic-based PPO: [S7]
- **DeepSeek-V3.2 (and V3.2-Speciale)**: On-policy distillation: [S7] 'Specialist Distillation' via generated data, then RL; Critic-based PPO: [S7]
- **DeepSeek-V4 (Pro / Flash, preview)**: Hybrid linear attention: [S8]; NoPE: [S8] RoPE; Model (weight) merging: [S8]; Critic-based PPO: [S8]; Continual-pretraining conversion: [S8] from scratch; Upcycling: [S8]
- **DeepSeek-R1 / R1-Zero**: On-policy distillation: [S9] SFT distillation into Qwen/Llama with 800k samples; Critic-based PPO: [S9] critic-free; Rubric rewards: [S9] rule-based accuracy/format
- **GLM-4.5 / GLM-4.5-Air**: Per-Head Muon / Muon Split: [S12] plain Muon; Muon Split arrives in GLM-5; DSA or other trained sparse attention: [S10] GQA full attention; Hybrid linear attention: [S10]; Latent MoE: [S10]; NoPE: [S10] partial RoPE; FP8 training: [S10] 'BF16 for training while leveraging FP8 for inference'; WSD schedule: [S10] 'models trained with the WSD schedule perform worse on general benchmarks' (cosine used); Critic-based PPO: [S10]; Continual-pretraining conversion: [S10]; Upcycling: [S10]
- **GLM-5**: Hybrid linear attention: [S12]; NoPE: [S12]; Critic-based PPO: [S12]; Continual-pretraining conversion: [S12]; Upcycling: [S12]
- **Qwen3 (235B-A22B, 30B-A3B, dense 0.6B–32B)**: Multi-token prediction (MTP): [S17] not used in Qwen3; introduced in Qwen3-Next; DSA or other trained sparse attention: [S16] GQA; Hybrid linear attention: [S16]; Aux-loss-free balancing: [S16] 'global-batch load balancing loss'; NoPE: [S16] RoPE + ABF; Critic-based PPO: [S16]; Continual-pretraining conversion: [S16]; Upcycling: [S16]
- **Qwen3-Next-80B-A3B**: Aux-loss-free balancing: [S17] 'global load balancing'
- **MiniMax-M1 (40k/80k)**: Muon optimizer: [S20] 'We employ the AdamW optimizer'; DSA or other trained sparse attention: [S20]; GRPO: [S20] CISPO instead; Critic-based PPO: [S20] 'no KL penalty term'
- **MiniMax-M2 (series M2 -> M2.1 -> M2.5 -> M2.7)**: DSA or other trained sparse attention: [S21]; Hybrid linear attention: [S21] returned to full GQA attention; NoPE: [S21] RoPE throughout; GRPO: [S21] 'We use CISPO as the core algorithm'; Critic-based PPO: [S21]; Continual-pretraining conversion: [S21]
- **MiniMax-M2.5**: GRPO: [S21] CISPO
- **Llama 4 (Scout 109B-A17B, Maverick 400B-A17B; Behemoth preview)**: Hybrid linear attention: [S24]
- **gpt-oss-120b / gpt-oss-20b**: DSA or other trained sparse attention: [S25] fixed banded/dense alternation; NoPE: [S25] RoPE + YaRN
- **Gemma 3 (1B–27B)**: DSA or other trained sparse attention: [S26] local/global sliding; Hybrid linear attention: [S26]; NoPE: [S26] RoPE; On-policy distillation: [S26] offline logit distillation ('sample 256 logits per token'); GRPO: [S26] BOND/WARP; Continual-pretraining conversion: [S26]
- **Gemma 4 (E2B, E4B, 12B, 26B-A4B MoE, 31B; DiffusionGemma)**: GRPO: [S28] BOND/WARM/WARP by reference
- **Magistral Medium / Small**: On-policy distillation: [S30] Small started from SFT on Medium traces; Critic-based PPO: [S30]; Generative RMs: [S30] formatting/correctness/length/language rewards
- **NVIDIA Nemotron 3 Nano (30B-A3B)**: Muon optimizer: [S32] 'AdamW'; Multi-token prediction (MTP): [S32] 'MTP layers in the two larger models'; Latent MoE: [S33] introduced in Super; FP8 training: [S32] BF16 training; FP8 post-training; Critic-based PPO: [S32]; Async RL with staleness correction: [S32] synchronous, on-policy; Continual-pretraining conversion: [S32]; Upcycling: [S32]
- **NVIDIA Nemotron 3 Super (120B-A12B)**: Muon optimizer: [S33] AdamW; Critic-based PPO: [S33]
- **NVIDIA Nemotron 3 Ultra (550B-A55B)**: Muon optimizer: [S34] AdamW; Model (weight) merging: [S34]; Critic-based PPO: [S34]
- **Olmo 3 (7B, 32B; Think / Instruct / RL-Zero)**: Muon optimizer: [S35] AdamW; Hybrid linear attention: [S35] SWA; NoPE: [S35]; FP8 training: [S35] 'bfloat16 precision throughout'; On-policy distillation: [S35] SFT on traces; Critic-based PPO: [S35]
- **SmolLM3-3B**: FP8 training: [S36] bfloat16; On-policy distillation: [S36] mid-training on R1 traces; GRPO: [S36] APO (DPO variant); Critic-based PPO: [S36]; Async RL with staleness correction: [S36] no online RL
- **Apertus (8B, 70B)**: Muon optimizer: [S37] 'AdEMAMix optimizer'; NoPE: [S37]; GRPO: [S37] QRPO; Critic-based PPO: [S37]
- **LongCat-Flash (560B, ~27B active)**: Muon optimizer: [S38] Adam LR transfer; DSA or other trained sparse attention: [S38] MLA; Hybrid linear attention: [S38]
- **Ling 2.0 (Ling-mini-2.0 16B-A1.4B, Ling-flash-2.0 103B-A6.1B, Ling-1T 1T-A51B)**: NoPE: [S39] partial RoPE; WSD schedule: [S39] WSM: 'mid-train checkpoint merging simulates LR decay'
- **Ring-1T**: Muon optimizer: [S40] AdamW in RL; Critic-based PPO: [S40]
- **Step-3 (321B VLM; 316B LLM, 38B active)**: DSA or other trained sparse attention: [S41] MFA
- **Xiaomi MiMo-7B**: NoPE: [S42]; Critic-based PPO: [S42]; Generative RMs: [S42] rule-based
- **Xiaomi MiMo-V2-Flash (309B-A15B)**: Muon optimizer: [S43] 'AdamW optimizer'; DSA or other trained sparse attention: [S43]; Hybrid linear attention: [S43] SWA:GA 5:1 hybrid (sliding, not linear); NoPE: [S43]
- **ByteDance Seed-OSS-36B**: NoPE: [S45] RoPE
- **Falcon-H1 (0.5B–34B)**: Muon optimizer: [S47] AdamW; NoPE: [S47]; GRPO: [S47] DPO; Critic-based PPO: [S47]
- **Microsoft Phi-4-reasoning / -plus**: Muon optimizer: [S49] AdamW/Adam; On-policy distillation: [S49] SFT on o3-mini traces; Critic-based PPO: [S49]; Generative RMs: [S49] verifiable math
- **Apple Foundation Models 2025 (~3B on-device; PT-MoE server)**: On-policy distillation: [S50] offline distillation loss from MoE teacher; GRPO: [S50] 'REINFORCE Leave-One-Out (RLOO)'; Critic-based PPO: [S50]
- **Arcee Trinity Large (400B-A13B; Mini 26B-A3B; Nano 6B-A1B)**: Hybrid linear attention: [S51] local/global attention
- **Gemini 2.5 Pro / Flash**: On-policy distillation: [S61] k-sparse offline distillation for Flash and below

## Undisclosed / unverified summary

- **Kimi K2 (Instruct/Base)** — verified: yes; undisclosed: data composition per domain quantities; RL compute; MoE balancing hyper-parameters; whether MTP used
- **Kimi K2 Thinking** — verified: yes; undisclosed: RL algorithm, reward design, data; only INT4 QAT and tool-call scaling are disclosed
- **Kimi K2.5** — verified: yes; undisclosed: policy-optimization loss specifics; RL compute; data mixture
- **Kimi K3** — verified: yes; undisclosed: pretraining token count and compute; RL objective beyond budget rule; data mixture sizes
- **DeepSeek-V3.1** — verified: yes; undisclosed: post-training algorithm, rewards, data; no technical report
- **DeepSeek-V3.2-Exp** — verified: yes; undisclosed: training compute; hyper-parameters beyond DSA stage
- **DeepSeek-V3.2 (and V3.2-Speciale)** — verified: yes; undisclosed: RL compute totals; hyper-parameters delta, beta
- **DeepSeek-V4 (Pro / Flash, preview)** — verified: yes; undisclosed: training compute; balancing hyper-parameters; RL environments
- **DeepSeek-R1 / R1-Zero** — verified: yes; undisclosed: RL infrastructure details (Supplementary); compute
- **GLM-4.5 / GLM-4.5-Air** — verified: yes; undisclosed: exact RL objective; pretraining token count in report body (blog gives 23T)
- **GLM-4.7 (and 4.7-Flash)** — verified: yes; undisclosed: nearly all training details; only benchmarks and deployment are published
- **GLM-5** — verified: yes; undisclosed: exact token count reconciliation (27T vs 28.5T); RL compute
- **GLM-5.1** — verified: yes; undisclosed: algorithm, data, compute (blog only)
- **GLM-5.2** — verified: yes; undisclosed: SAO definition; data; compute
- **GLM-5.3 (and 5.3-Flash)** — verified: yes; undisclosed: SAO algorithm; environment counts; compute
- **Qwen3 (235B-A22B, 30B-A3B, dense 0.6B–32B)** — verified: yes; undisclosed: optimizer, precision, pretraining hyper-parameters
- **Qwen3-Next-80B-A3B** — verified: yes; undisclosed: optimizer; RL algorithm; post-training data
- **Qwen3.5 (397B-A17B flagship; 122B-A10B, 35B-A3B, 27B, small)** — verified: yes; undisclosed: pretraining token count, optimizer, precision, RL algorithm for the LLM itself (only Omni sibling names GSPO)
- **Qwen3.8-27B (and Qwen3.8-2.4T-A95B hosted)** — verified: yes; undisclosed: all training details (model card only)
- **MiniMax-M1 (40k/80k)** — verified: yes; undisclosed: pretraining recipe of base; reward model details
- **MiniMax-M2 (series M2 -> M2.1 -> M2.5 -> M2.7)** — verified: yes; undisclosed: optimizer, precision, pretraining schedule
- **MiniMax-M2.5** — verified: yes; undisclosed: everything beyond RL-system description
- **MiniMax-M3** — verified: yes; undisclosed: M3-specific pretraining tokens, optimizer, post-training
- **Llama 4 (Scout 109B-A17B, Maverick 400B-A17B; Behemoth preview)** — verified: yes; undisclosed: RL algorithm name, rewards, hyper-parameters; no technical report
- **gpt-oss-120b / gpt-oss-20b** — verified: yes; undisclosed: RL algorithm, optimizer, token count, balancing
- **Gemma 3 (1B–27B)** — verified: yes; undisclosed: optimizer; teacher identity; RL hyper-parameters
- **Gemma 3n (E2B, E4B)** — verified: yes; undisclosed: training recipe (no report; 'Stay tuned for ... upcoming technical report')
- **Gemma 4 (E2B, E4B, 12B, 26B-A4B MoE, 31B; DiffusionGemma)** — verified: yes; undisclosed: token count, optimizer, RL details, diffusion training recipe
- **Mistral Large 3 (and Ministral 3)** — verified: yes; undisclosed: virtually all training details
- **Magistral Medium / Small** — verified: yes; undisclosed: Medium architecture and size
- **Devstral 2 (123B) / Devstral Small 2 (24B)** — verified: yes; undisclosed: all training details
- **NVIDIA Nemotron 3 Nano (30B-A3B)** — verified: yes; undisclosed: none major; full recipe released
- **NVIDIA Nemotron 3 Super (120B-A12B)** — verified: yes; undisclosed: RL algorithm variants; compute
- **NVIDIA Nemotron 3 Ultra (550B-A55B)** — verified: yes; undisclosed: RL hyper-parameters beyond NeMo-RL configs
- **Olmo 3 (7B, 32B; Think / Instruct / RL-Zero)** — verified: yes; undisclosed: none major (fully open); RL Sec 4.4 not fetched in full here
- **SmolLM3-3B** — verified: yes; undisclosed: optimizer hyper-parameters in blog (configs released)
- **Apertus (8B, 70B)** — verified: yes; undisclosed: none major (fully open)
- **LongCat-Flash (560B, ~27B active)** — verified: yes; undisclosed: RL algorithm and rewards (not in fetched sections)
- **Ling 2.0 (Ling-mini-2.0 16B-A1.4B, Ling-flash-2.0 103B-A6.1B, Ling-1T 1T-A51B)** — verified: yes; undisclosed: optimizer name; RL reward details
- **Ring-1T** — verified: yes; undisclosed: RL compute; data
- **Step-3 (321B VLM; 316B LLM, 38B active)** — verified: yes; undisclosed: 'In the future, we will release more details on the model side for Step-3' — training recipe undisclosed [S41]
- **Xiaomi MiMo-7B** — verified: yes (abs page); undisclosed: details not re-fetched here (verified via abs page only)
- **Xiaomi MiMo-V2-Flash (309B-A15B)** — verified: yes; undisclosed: RL algorithm for teachers
- **Tencent Hunyuan-A13B (80B-A13B)** — verified: yes (GitHub); report details via secondary; undisclosed: balancing, optimizer, precision (report PDF not directly fetched)
- **Tencent Hy3 (295B-A21B)** — verified: yes; undisclosed: no technical report; all recipe details
- **ByteDance Seed-OSS-36B** — verified: yes; undisclosed: all post-training details
- **IBM Granite 4.0 (H-Small 32B-A9B, H-Tiny 7B-A1B, H-Micro 3B, Micro 3B)** — verified: yes; undisclosed: tokens, optimizer, post-training algorithms (no report)
- **Falcon-H1 (0.5B–34B)** — verified: yes; undisclosed: none major
- **xAI Grok 2.5 (open weights)** — verified: yes (release event; HF card not fetchable); undisclosed: 'The release includes checkpoints and inference notes, not the complete training data or end-to-end pipeline' — no training details [S48]
- **Microsoft Phi-4-reasoning / -plus** — verified: yes; undisclosed: GRPO modifications detail
- **Apple Foundation Models 2025 (~3B on-device; PT-MoE server)** — verified: yes; undisclosed: server model size, token totals, RL compute
- **Apple Foundation Models 2026** — verified: no; undisclosed: n/a
- **Arcee Trinity Large (400B-A13B; Mini 26B-A3B; Nano 6B-A1B)** — verified: yes; undisclosed: post-training/RL (still ongoing at report time)
- **OpenAI o3 (and o4-mini)** — verified: yes; undisclosed: architecture, optimizer, data scale, RL algorithm — all undisclosed
- **GPT-5 (gpt-5-main / gpt-5-thinking / router)** — verified: yes; undisclosed: architecture, optimizer, data scale, RL algorithm — all undisclosed
- **GPT-5.5 (and GPT-5.5 Pro)** — verified: yes; undisclosed: architecture, optimizer, data scale, RL algorithm — all undisclosed
- **GPT-5.6 Sol (with Terra, Luna)** — verified: yes; undisclosed: architecture, optimizer, data scale, RL algorithm — all undisclosed
- **Claude Opus 4 / Sonnet 4** — verified: yes; undisclosed: architecture, optimizer, data scale, RL algorithm — all undisclosed
- **Claude Opus 4.5** — verified: yes; undisclosed: architecture, optimizer, data scale, RL algorithm — all undisclosed
- **Claude Opus 4.7** — verified: yes; undisclosed: architecture, optimizer, data scale, RL algorithm — all undisclosed
- **Claude Opus 4.8** — verified: yes; undisclosed: architecture, optimizer, data scale, RL algorithm — all undisclosed
- **Claude Fable 5 / Claude Mythos 5 (same weights, different safeguards)** — verified: yes; undisclosed: architecture, optimizer, data scale, RL algorithm — all undisclosed
- **Gemini 2.5 Pro / Flash** — verified: yes; undisclosed: architecture, optimizer, data scale, RL algorithm — all undisclosed
- **Gemini 3 Pro** — verified: yes; undisclosed: architecture, optimizer, data scale, RL algorithm — all undisclosed
- **Gemini Diffusion (experimental)** — verified: yes; undisclosed: 'we have no details' (Nathan Lambert, quoted by Fortune); no card [S63]
- **xAI Grok 4 / Grok 4 Heavy** — verified: yes; undisclosed: architecture, optimizer, data scale, RL algorithm — all undisclosed
- **xAI Grok 5** — verified: no (does not exist as a released model; no model card); undisclosed: everything; Grok 4.6 card notes 'an improved optimizer and recipe' and 'supplemental training on anonymized Cursor workflow data' for the 1.5T-scale family [S65]

## Search log

Every query and fetch issued for this register (session 2026-09-05, UTC times). Large Exa results were persisted by the harness to tool-result files and read via grep/KWIC rather than inline.

| Time | Channel | Query / URL |
|---|---|---|
| 21:22:50 | Exa fetch | https://arxiv.org/abs/2507.20534 ; https://arxiv.org/abs/2607.24653 ; https://arxiv.org/abs/2602.15763 ; https://arxiv.org/abs/2512.02556 ; https://arxiv.org/abs/2508.06471 |
| 21:22:52 | Exa fetch | https://arxiv.org/abs/2505.09388 ; https://arxiv.org/abs/2506.13585 ; https://arxiv.org/abs/2508.10925 ; https://arxiv.org/abs/2503.19786 ; https://www.nature.com/articles/s41586-025-09422-z |
| 21:22:53 | Exa fetch | https://arxiv.org/abs/2509.14233 ; https://arxiv.org/abs/2509.01322 ; https://arxiv.org/abs/2507.19427 ; https://arxiv.org/abs/2505.07608 ; https://arxiv.org/abs/2507.22448 |
| 21:22:54 | Exa fetch | https://arxiv.org/abs/2504.21318 ; https://arxiv.org/abs/2507.13575 ; https://arxiv.org/abs/2506.10910 ; https://arxiv.org/abs/2507.06261 ; https://arxiv.org/abs/2512.13961 |
| 21:22:55 | Exa search | Kimi K2.5 technical report Moonshot AI arXiv 2026 multimodal agentic |
| 21:22:56 | Exa search | DeepSeek-V4 technical report release 2026 open weights |
| 21:22:57 | Exa search | GLM-5.1 GLM-5.2 GLM-5.3 Zhipu Z.ai release 2026 open weights technical report |
| 21:22:58 | Exa search | Qwen3.5 technical report Alibaba 2026 release open weights |
| 21:22:59 | Exa search | MiniMax M2.5 or MiniMax M3 technical report release 2026 |
| 21:23:00 | Exa search | NVIDIA Nemotron 3 Nano Super Ultra technical report arXiv hybrid Mamba MoE |
| 21:23:00 | Exa search | Gemma 4 release Google DeepMind open model 2026 |
| 21:23:01 | Exa search | GPT-5.5 or GPT-5.6 Sol OpenAI system card 2026 |
| 21:23:03 | Exa search | Anthropic Claude Opus 4.7 or Opus 4.8 or Claude Fable 5 or Mythos 5 system card 2026 |
| 21:23:03 | Exa search | Arcee Trinity Large open weights MoE model technical report 2026 |
| 21:23:04 | Exa search | xAI Grok 5 release 2026 model card |
| 21:24:20 | Exa fetch | https://arxiv.org/html/2507.20534 ; https://arxiv.org/html/2607.24653 ; https://arxiv.org/html/2602.02276 |
| 21:24:20 | Exa fetch | https://arxiv.org/html/2512.02556 ; https://arxiv.org/html/2606.19348 ; https://arxiv.org/abs/2501.12948 |
| 21:24:20 | Exa fetch | https://arxiv.org/html/2602.15763 ; https://arxiv.org/html/2508.06471 ; https://arxiv.org/html/2505.09388 |
| 21:24:21 | Exa fetch | https://arxiv.org/html/2506.13585 ; https://arxiv.org/html/2605.26494 ; https://arxiv.org/html/2606.13392 |
| 21:24:23 | Exa fetch | https://arxiv.org/html/2508.10925 ; https://arxiv.org/html/2503.19786 ; https://arxiv.org/html/2607.02770 |
| 21:24:24 | Exa fetch | https://arxiv.org/html/2512.20848 ; https://arxiv.org/html/2604.12374 ; https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf |
| 21:24:25 | Exa fetch | https://arxiv.org/html/2512.13961 ; https://arxiv.org/html/2509.14233 ; https://arxiv.org/html/2509.01322 |
| 21:24:26 | Exa fetch | https://arxiv.org/html/2507.19427 ; https://arxiv.org/html/2507.22448 ; https://arxiv.org/html/2504.21318 |
| 21:24:27 | Exa fetch | https://arxiv.org/html/2507.13575 ; https://arxiv.org/html/2506.10910 ; https://arxiv.org/html/2602.17004 |
| 21:24:28 | Exa fetch | https://arxiv.org/html/2507.06261 ; https://arxiv.org/html/2505.07608 |
| 21:24:29 | Exa search | DeepSeek-V3.1 release August 2025 hybrid thinking mode model card UE8M0 FP8 continued pretraining long context |
| 21:24:30 | Exa search | DeepSeek-V3.2-Exp September 2025 DeepSeek Sparse Attention lightning indexer technical report |
| 21:24:31 | Exa search | GLM-4.7 release December 2025 Z.ai blog open weights |
| 21:24:32 | Exa search | GLM-5.1 release date April 2026 Z.ai blog agentic engineering open weights |
| 21:24:33 | Exa search | Qwen3-Next 80B-A3B September 2025 blog hybrid Gated DeltaNet gated attention multi-token prediction zero-centered RMSNorm |
| 21:24:34 | Exa search | Qwen3.5 technical report arXiv 2026 Qwen Team pretraining reinforcement learning |
| 21:24:35 | Exa search | Llama 4 Scout Maverick April 2025 Meta blog iRoPE interleaved attention MetaP natively multimodal mixture of experts FP8 30 trillion tokens |
| 21:24:37 | Exa search | Gemma 3n June 2025 Per-Layer Embeddings MatFormer KV cache sharing model announcement |
| 21:24:38 | Exa search | Mistral Large 3 December 2025 open weights mixture of experts 675B announcement Mistral 3 family |
| 21:24:39 | Exa search | Devstral 2 December 2025 Mistral coding model open weights announcement |
| 21:24:40 | Exa search | SmolLM3 3B Hugging Face July 2025 NoPE grouped query attention 11 trillion tokens dual mode reasoning technical blog or arXiv report |
| 21:24:41 | Exa search | Ling 2.0 Ling-1T Ant Group technical report arXiv Every Activation Boosted scaling 1 trillion open language foundation model |
| 21:24:42 | Exa search | Ring-1T Ant Group thinking model technical report arXiv IcePop C3PO ASystem |
| 21:24:44 | Exa search | Xiaomi MiMo-V2-Flash technical report December 2025 hybrid sliding window attention MoE multi-token prediction |
| 21:24:44 | Exa search | Tencent Hunyuan-A13B technical report 2025 open weights MoE hybrid reasoning arXiv |
| 21:24:45 | Exa search | ByteDance Seed-OSS-36B August 2025 open source model 12 trillion tokens thinking budget GitHub |
| 21:24:47 | Exa search | IBM Granite 4.0 October 2025 hybrid Mamba-2 transformer mixture of experts NoPE release announcement |
| 21:24:47 | Exa search | xAI Grok 2.5 open weights release August 2025 Hugging Face 270B mixture of experts |
| 21:24:48 | Exa search | Apple Intelligence Foundation Language Models Tech Report 2026 arXiv |
| 21:24:49 | Exa search | OpenAI o3 and o4-mini system card April 2025 |
| 21:24:50 | Exa search | GPT-5 system card August 2025 OpenAI unified system real-time router reasoning |
| 21:24:50 | Exa search | GPT-5.5 system card OpenAI 2026 deployment safety hub |
| 21:24:52 | Exa search | Claude Opus 4 and Claude Sonnet 4 system card May 2025 Anthropic training data process |
| 21:24:53 | Exa search | Claude Opus 4.8 system card May 2026 Anthropic |
| 21:24:53 | Exa search | Gemini 3 Pro model card November 2025 Google DeepMind training details sparse mixture of experts TPU |
| 21:24:55 | Exa search | Gemini Diffusion experimental text diffusion model Google DeepMind May 2025 announcement |
| 21:24:56 | Exa search | Grok 4 model card xAI July 2025 reinforcement learning pretraining scale |
| 21:24:56 | Exa search | Kimi K2 Thinking November 2025 Moonshot blog native INT4 quantization-aware training interleaved thinking 200-300 tool calls |
| 21:26 | local | Built KWIC index (kwic.txt) over all persisted Exa fetch outputs; ~90 method keywords, ±200-char context |
| 21:26:17 | Exa search | Kimi K2 technical report reinforcement learning verifiable rewards self-critique rubric reward budget control PTX auxiliary loss temperature decay |
| 21:26:17 | Exa search | Kimi K3 technical report post-training reinforcement learning reasoning effort levels optimizer MuonClip pre-training tokens Stable LatentMoE |
| 21:26:19 | Exa search | DeepSeek-V3.2 technical report GRPO unbiased KL estimate off-policy sequence masking keep routing mixed RL specialist distillation rubric generative reward model |
| 21:26:20 | Exa search | GLM-5 technical report asynchronous reinforcement learning algorithm off-policy correction slime pre-training details Muon optimizer MTP FP8 |
| 21:26:21 | Exa search | GLM-4.5 technical report slime RL infrastructure expert model iteration self-distillation Muon optimizer QK-Norm MTP loss-free balance |
| 21:26:23 | Exa search | Qwen3 technical report post-training thinking mode fusion strong-to-weak distillation GSPO reasoning RL thinking budget global-batch load balancing |
| 21:26:23 | Exa search | MiniMax-M1 CISPO clipped importance sampling policy optimization RL algorithm lightning attention hybrid 7:1 |
| 21:26:25 | Exa search | MiniMax-M2 series technical report Forge RL system windowed-FIFO prefix-tree merging optimizer pretraining FP8 MTP GQA sigmoid gating RL algorithm |
| 21:26:26 | Exa search | MiniMax M3 technical report arXiv 2606.13392 MiniMax Sparse Attention MSA pretraining tokens optimizer post-training RL native multimodal |
| 21:26:27 | Exa search | gpt-oss model card MXFP4 quantization attention sinks reinforcement learning variable effort reasoning training deliberative alignment pretraining tokens |
| 21:26:28 | Exa search | Gemma 4 technical report post-training reinforcement learning distillation quantization-aware training MTP drafters local global attention ratio positional encoding |
| 21:26:29 | Exa search | Nemotron 3 Ultra technical report Multi-teacher On-Policy Distillation MOPD RLVR GRPO reasoning budget control asynchronous |
| 21:26:31 | Exa search | Olmo 3 technical report Dolci post-training SFT DPO RLVR OlmoRL asynchronous Dolma 3 pretraining tokens midtraining long-context extension |
| 21:26:32 | Exa search | Apertus technical report Goldfish objective xIELU AdEMAMix WSD schedule 15T tokens QRPO post-training |
| 21:26:33 | Exa search | LongCat-Flash technical report zero-computation experts shortcut-connected MoE hyperparameter transfer model growth initialization 20T tokens RL DORA |
| 21:26:34 | Exa search | Step-3 technical report multi-matrix factorization attention MFA attention-FFN disaggregation 316B 38B active pretraining tokens |
| 21:26:35 | Exa search | Falcon-H1 technical report muP maximal update parametrization hybrid Mamba-2 attention parallel 18T tokens tokenizer WSD schedule |
| 21:26:36 | Exa search | Phi-4-reasoning technical report SFT on o3-mini traces Phi-4-reasoning-plus GRPO outcome-based reinforcement learning |
| 21:26:38 | Exa search | Apple Intelligence Foundation Models 2025 tech report Parallel-Track MoE PT-MoE 2-bit quantization-aware training reinforcement learning REINFORCE leave-one-out asynchronous RL platform pretraining tokens |
| 21:26:39 | Exa search | Magistral technical report GRPO modifications eliminating KL penalty clip-higher length normalization asynchronous RL infrastructure reward shaping |
| 21:26:41 | Exa search | Gemini 2.5 technical report sparse mixture-of-experts architecture thinking budget reinforcement learning distillation Flash TPU pre-training |
| 21:26:41 | Exa search | Hunyuan-A13B technical report pretraining 20T tokens dual-mode chain of thought GRPO reinforcement learning scaling laws MoE |
| 21:26:43 | Exa search | Claude Opus 4.5 system card effort parameter thinking control training data process Anthropic November 2025 |
| 21:26:44 | Exa search | Claude Fable 5 Mythos 5 system card training data and process section model architecture and training methodology |
| 21:26:45 | Exa search | DeepSeek-R1 Nature paper GRPO rule-based rewards cold-start distillation Qwen Llama peer review DeepSeek-R1-Zero |
| 21:26:46 | Exa search | Qwen3.8 27B release August 2026 model card architecture training details |
| 21:26:47 | Exa search | Tencent Hunyuan open weights 2026 HY3 or Hunyuan 3 release technical report |
| 21:26:48 | Exa search | Mistral Large 3 technical details pretraining tokens optimizer architecture granular MoE model card training methodology |
| 21:28 | local | KWIC extracts persisted: be8ojqu10.txt, brctufuqm.txt, bh7rx9jjt.txt, bsnehmxsy.txt (tool-results dir) |
| 21:28:30 | Exa search | Llama 4 post-training lightweight SFT online RL lightweight DPO codistillation Behemoth teacher asynchronous online RL continuous |
| 21:28:31 | Exa search | Olmo 3 OlmoRL algorithm GRPO modifications clip higher no KL loss token-level loss truncated importance sampling active sampling continuous batching in-flight updates |
| 21:28:33 | Exa search | Kimi K2 technical report MuonClip QK-Clip architecture MLA 384 experts sparsity scaling law rephrasing 15.5T tokens WSD learning rate schedule context 128K YaRN |
| 21:28:34 | Exa search | Gemma 3 technical report distillation 14T tokens local global attention 5:1 1024 window QAT post-training RL BOND WARM WARP reward |
| 21:28:35 | Exa search | Nemotron 3 Nano technical report RL multi-environment GRPO reasoning budget control Warmup-Stable-Decay 25 trillion tokens FP8 pretraining aux loss load balancing Mamba-2 no positional embeddings |
| 21:29:44 | Exa fetch | https://arxiv.org/abs/2607.24653v1 ; https://arxiv.org/abs/2606.19348 ; https://arxiv.org/abs/2602.02276 ; https://arxiv.org/abs/2606.15007 ; https://arxiv.org/abs/2604.12374 |
| 21:29:44 | Exa search | Kimi K3 technical report pre-training data trillion tokens curriculum learning rate schedule context extension 1M |
| 21:29:45 | Exa search | Gemma 4 technical report pre-training tokens trillion distillation from Gemini teacher post-training RL reward |
| 21:29:46 | Exa search | Olmo 3 technical report section 4.4 Reinforcement Learning with OlmoRL truncated importance sampling no KL clip higher active sampling PipelineRL in-flight weight updates |
| 21:29:48 | WebFetch | https://z.ai/blog/glm-5.3  -> EGRESS_BLOCKED (z.ai); replaced by Exa search highlights |
| 21:29:50 | Exa search | MiniMax M2 release October 27 2025 open weights 230B total 10B active interleaved thinking announcement |
| 21:29:50 | Exa search | Kimi K2.5 released January 27 2026 open weights Moonshot announcement |
| 21:31:08 | Exa search | z.ai blog GLM-5.3 SAO compaction long-horizon RL slime asynchronous throughput 2.3x training rollout logprob agreement 1e-7 |
| 21:31:08 | Exa search | Kimi K3 pre-training corpus size tokens "trillion tokens" data mixture rephrasing multimodal joint pre-training 2.8T |
| 22:02 | local | Targeted KWIC re-checks for matrix cells: GLM-4.5 GRPO; GLM-5 Direct Double-sided IS; Nemotron Nano WSD; Trinity schedule; Kimi K2 WSD; K3 staleness; Magistral off-policy |
