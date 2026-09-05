# Sweep protocol (shared by all literature-sweep agents)

Date of execution: 2026-09-05. Window: work whose first public date (arXiv v1 date, OpenReview submission date, or journal/proceedings publication date) falls between 2024-12-31 and 2026-09-05 inclusive. Older work may be recorded only as an explicitly labelled baseline.

## Working channels in this sandbox
- mcp__Exa__web_search_exa: semantic web search. Describe the ideal page in a full sentence. numResults up to 10. Reaches arxiv.org, proceedings.neurips.cc, papers.nips.cc, proceedings.mlr.press, aclanthology.org, openreview.net PDFs, github, lab blogs.
- mcp__Exa__web_fetch_exa: fetches full page text. WORKS for https://arxiv.org/abs/<id> and https://arxiv.org/html/<id>. Batch up to 5 URLs per call; set maxCharacters 1500 for abs pages, 6000 for html pages when you need method details. OpenReview forum pages return a browser-check page; use WebSearch domain-filtered snippets for OpenReview instead.
- WebSearch with allowed_domains: use ["openreview.net"], ["arxiv.org"], ["proceedings.neurips.cc","papers.nips.cc"], ["proceedings.mlr.press"], ["aclanthology.org"], ["colmweb.org"], ["jmlr.org"], ["nature.com"] to sweep venues. Snippets often carry the "Comments:" venue line and acceptance status.
- mcp__Scholar_Gateway__semanticSearch: full-text index of Wiley journals. Use start_year 2025, end_year 2026, topN 10. Output is large and gets saved to a file path; parse it with python3 json (results[i].metadata.additionalMetadata has title, publicationDate, journalTitle, link, abstract). Use for peer-reviewed journal coverage only; it does not index arXiv.
- BLOCKED (do not retry): curl/WebFetch to arxiv.org, export.arxiv.org, openreview.net, api.semanticscholar.org, api.openalex.org, huggingface.co, scholar.google.com. Use the Exa tools for those hosts.

## Evidence tiers (record one per item, with the evidence string that justifies it)
- A: peer-reviewed and published. Main track of NeurIPS 2025, ICML 2025/2026, ICLR 2025/2026, ACL/EMNLP/NAACL/COLING 2025/2026, COLM 2025/2026, AISTATS, TMLR, JMLR, Nature/Science family, IEEE/ACM journals, Wiley journals. Evidence: proceedings URL, aclanthology URL, OpenReview "Published" venue line, DOI, or arXiv Comments line naming acceptance.
- B: submitted and under review, or accepted with camera-ready pending. Evidence: arXiv Comments "under review"/"submitted to", OpenReview submission page with reviews, or NeurIPS 2026 submission status (notifications are due 2026-09-24, so every NeurIPS 2026 submission is Tier B today). ICLR 2027 deadline is 2026-09-25, so no ICLR 2027 submissions are public yet.
- C: industrial technical report or model card from a frontier or open-weights lab (Kimi, DeepSeek, Zhipu/Z.ai, Qwen, Meta, OpenAI, Anthropic, Google, NVIDIA, Mistral, MiniMax, AI2, Apple, xAI, Microsoft, Amazon, Cohere, StepFun, Meituan, Ant, Tencent, ByteDance/Seed, Xiaomi, Baidu). Primary source for what frontier recipes use.
- D: preprint with no review signal found. Keep only when it is the primary statement of a method that matters to the path; label it D.

## Required fields per item
id (arXiv ID or DOI) | title | first author et al. | affiliation(s) | v1 date | latest version date | tier | tier evidence (quoted) | venue | one-sentence method | largest scale tested (params, tokens, or model names) | headline claim (number if given) | path relevance | known frontier adoption (name the report) | verified (yes/no)

## Verification rule
Before writing an item as verified, fetch its arxiv.org/abs page through mcp__Exa__web_fetch_exa (or the proceedings/aclanthology/journal page) and confirm title, first author, and date. Never write an arXiv ID from memory. If a fetch fails twice, mark verified=no and keep the item only if it matters.

## Also collect
1. Open-problem statements: sentences in limitations or future-work sections, or in surveys, naming something untested at frontier scale. Quote briefly with the source id.
2. Survey papers in the window covering the path (record separately).
3. Negative or null results (methods that failed to scale), which are evidence for the gap analysis.

## Output
Write two files:
- <path>.md: a summary table (all fields above) sorted by tier then date, followed by "Open problems", "Surveys", "Negative results", and "Search log" (every query you ran, with the channel and the hit count you kept).
- <path>.json: an array of the same items with the same field names in snake_case.
Targets: at least 30 verified items, at least 12 of them Tier A, at least 6 Tier B or newer than 2026-05-01. Prefer breadth of distinct methods over many papers on one method. Stop expanding when a new query returns only items you already hold.
