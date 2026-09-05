import re
S='/tmp/claude-0/-home-user-wadelovell-portfolio/2c8d9d81-3f91-5f3d-8b0c-289eaab48cde/scratchpad/'
def section(path, start_pat):
    t=open(path).read()
    i=t.find(start_pat)
    if i<0: return ''
    return t[i:]
out=[]
out.append('# Search Log\n')
out.append('Execution date: September 5, 2026 (UTC). Window: December 31, 2024 through September 5, 2026. Every query below ran through one of the channels named in Section 5 of the research plan. "Kept" counts the hits that entered a sweep register after verification against a primary page.\n')
out.append('## Coverage limits recorded during execution\n')
out.append('''- Direct access to the arXiv API, the OpenReview API, the Semantic Scholar API, OpenAlex, and Hugging Face was blocked by the session's egress policy. arXiv abstract and HTML pages were reached through Exa fetch. OpenReview content was reached only through domain-filtered web-search snippets and PDF links, so acceptance status for some OpenReview submissions could not be confirmed and those items hold Tier B.
- Scholar Gateway indexes Wiley journals only. Four queries (on-policy distillation; pretraining methods; RLVR and self-improvement; knowledge distillation theory) returned 45 Wiley articles, of which one review (WIREs Computational Statistics, October 2025) was on-path. Peer-reviewed evidence for frontier training methods in the window lives in conference proceedings and in Nature, and the sweeps sourced it from proceedings.neurips.cc, proceedings.mlr.press, aclanthology.org, iclr.cc, icml.cc, colmweb.org, and nature.com through Exa and domain-filtered search.
- NeurIPS 2026 notifications are due September 24, 2026, and the ICLR 2027 deadline is September 25, 2026, so no NeurIPS 2026 acceptance and no ICLR 2027 submission was observable. Items carrying "under review" on arXiv hold Tier B.
- The Kimi K3 arXiv HTML page was fetched in full (200,000 characters) and mined for Sections 3.2, 4.1, 4.2, 5.3, and 8. The GLM-5.2 and GLM-5.3 release posts were fetched in full. The DeepSeek-V4 report was read through its arXiv HTML highlights and the Hugging Face model card.
- Four sweep items were kept with verified=no because two fetch attempts failed (2601.05607; 2604.15804; 2603.09938; the ICLR 2026 CoT-Pass@K poster). One Path 3 item, Foreign Sparse Attention, exists only on OpenReview and holds Tier B unverified.
- Wide search returned no Tier A evidence for Muon-class optimizers or maximal-update transfer above roughly 4 billion dense parameters outside lab reports, no Tier A comparison of diffusion or energy-based objectives against autoregressive training above 1e23 FLOPs, and no Tier A long-context extension study above 8 billion parameters.
''')
out.append('## Orchestrator queries\n')
out.append(open(S+'my-search-log.md').read().split('\n',2)[2])
for label,fn,pat in (('Path 1, from scratch','sweeps/path1-from-scratch.md','## Search log'),('Path 2, distillation','sweeps/path2-distillation.md','## Search log'),('Path 3, open-weights bases','sweeps/path3-open-weights.md','## Search log'),('Path 4, post-training','sweeps/path4-post-training.md','## Search log'),('Frontier recipe register','sweeps/frontier-recipe-register.md','## Search log')):
    try:
        sec=section(S+fn,pat)
    except FileNotFoundError:
        sec=''
    if not sec:
        out.append(f'\n## {label}\n\n(log pending)\n'); continue
    body=sec.split('\n',1)[1] if '\n' in sec else ''
    body=re.sub(r'^# PATH 4 search log.*\n','',body,flags=re.M)
    out.append(f'\n## {label}\n')
    out.append(body.strip()+'\n')
open('/home/user/wadelovell-portfolio/research/frontier-training-methods/search-log.md','w').write('\n'.join(out))
print('search-log.md written')
