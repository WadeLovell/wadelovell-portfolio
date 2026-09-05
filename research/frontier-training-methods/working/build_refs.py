import json, re, sys, os
S='/tmp/claude-0/-home-user-wadelovell-portfolio/2c8d9d81-3f91-5f3d-8b0c-289eaab48cde/scratchpad/sweeps/'
files={'1':'path1-from-scratch.json','2':'path2-distillation.json','3':'path3-open-weights.json','4':'path4-post-training.json'}
rank={'A':0,'B':1,'C':2,'D':3}
def norm_tier(t):
    t=str(t).strip()
    m=re.match(r'([ABCD])',t)
    return m.group(1) if m else 'D'
def g(it,*ks):
    for k in ks:
        if k in it and it[k] not in (None,''): return it[k]
    return ''
merged={}
for path,fn in files.items():
    d=json.load(open(S+fn)); items=d if isinstance(d,list) else d['items']
    for it in items:
        iid=str(it['id']).strip()
        key=iid.lower().replace('arxiv:','')
        rec=merged.get(key)
        tier=norm_tier(it['tier']); base=str(it['tier']).lower().find('baseline')>=0
        cand={'id':iid,'title':str(g(it,'title')).strip(),'first_author':str(g(it,'first_author_et_al','first_author')).strip(),
              'v1':str(g(it,'v1_date')).strip(),'tier':tier,'tier_raw':str(it['tier']),'evidence':str(g(it,'tier_evidence')).strip(),
              'venue':str(g(it,'venue')).strip(),'paths':{path},'baseline':base,'verified':str(g(it,'verified')).lower() in ('yes','true','1')}
        if rec is None: merged[key]=cand
        else:
            rec['paths'].add(path)
            # keep the strongest tier whose evidence names a concrete venue artifact
            if rank[cand['tier']]<rank[rec['tier']] and re.search(r'proceedings|aclanthology|icml\.cc|iclr\.cc|neurips|pmlr|doi|nature|published|poster|oral|colm|acm|kdd|tmlr|jmlr', cand['evidence'].lower()):
                rec.update({k:cand[k] for k in ('tier','tier_raw','evidence','venue')})
            if not rec['first_author'] and cand['first_author']: rec['first_author']=cand['first_author']
            if not rec['v1'] and cand['v1']: rec['v1']=cand['v1']
            rec['verified']=rec['verified'] or cand['verified']
recs=sorted(merged.values(), key=lambda r:(rank[r['tier']], r['baseline'], r['v1'], r['title'].lower()))
counts={t:sum(1 for r in recs if r['tier']==t and not r['baseline']) for t in 'ABCD'}
print('unique sources:',len(recs),'counts:',counts, file=sys.stderr)
def link(iid):
    if re.match(r'^\d{4}\.\d{4,5}$',iid): return f'https://arxiv.org/abs/{iid}'
    if iid.startswith('10.'): return f'https://doi.org/{iid}'
    if iid.startswith('openreview:'): return f'https://openreview.net/forum?id={iid.split(":",1)[1]}'
    if iid.startswith('aclanthology:'): return f'https://aclanthology.org/{iid.split(":",1)[1]}/'
    if iid.startswith('iclr2026:'): return f'https://iclr.cc/virtual/2026/{iid.split(":",1)[1]}'
    if iid.startswith('http'): return iid
    if iid.startswith('hf:'): return f'https://huggingface.co/{iid[3:]}'
    if iid.startswith('github:'): return f'https://github.com/{iid[7:]}'
    if iid.startswith('zai-blog:') or iid.startswith('zai:'): return f'https://z.ai/blog/{iid.split(":",1)[1]}'
    if iid.startswith('tml:'): return 'https://thinkingmachines.ai/blog/on-policy-distillation/'
    if iid.startswith('blog:thinkingmachines-lora'): return 'https://thinkingmachines.ai/blog/lora/'
    if iid.startswith('openai:'): return 'https://openai.com/research'
    if iid.startswith('gdm:'): return 'https://deepmind.google/models/gemini/'
    if iid.startswith('anthropic:'): return 'https://www.anthropic.com/'
    if 'kexue.fm' in iid: return 'https://kexue.fm/archives/11619'
    if 'novasky' in iid or 'ai.meta.com' in iid: return 'https://'+iid
    return ''
out=[]
out.append('# References\n')
out.append('Every source the sweeps verified, grouped by evidence tier. Tier A is peer-reviewed and published. Tier B is submitted and under review or accepted with camera-ready pending. Tier C is an industrial technical report, model card, or lab post. Tier D is a preprint or post with no review signal found. "Paths" lists the training paths (1 from scratch, 2 distillation, 3 open-weights bases, 4 post-training) whose sweep returned the source. Labelled baselines predate the window and appear only because in-window work depends on them. Counts exclude baselines.\n')
out.append(f"| Tier | Count |\n|---|---|\n| A | {counts['A']} |\n| B | {counts['B']} |\n| C | {counts['C']} |\n| D | {counts['D']} |\n| Total | {sum(counts.values())} |\n")
for t,name in (('A','Tier A: peer-reviewed and published'),('B','Tier B: submitted and under review'),('C','Tier C: technical reports, model cards, and lab posts'),('D','Tier D: preprints and posts with no review signal')):
    out.append(f'\n## {name}\n')
    out.append('| Identifier | First author | Date | Title | Venue or status | Evidence of status | Paths | Verified |\n|---|---|---|---|---|---|---|---|')
    for r in recs:
        if r['tier']!=t: continue
        l=link(r['id']); idc=f"[{r['id']}]({l})" if l else r['id']
        title=r['title'].replace('|','/')
        ev=r['evidence'].replace('|','/')[:140]
        ven=r['venue'].replace('|','/')[:60]
        base=' (baseline)' if r['baseline'] else ''
        out.append(f"| {idc} | {r['first_author'].replace('|','/')[:40]} | {r['v1'][:10]} | {title[:110]}{base} | {ven} | {ev} | {','.join(sorted(r['paths']))} | {'yes' if r['verified'] else 'no'} |")
open('/home/user/wadelovell-portfolio/research/frontier-training-methods/references.md','w').write('\n'.join(out)+'\n')
json.dump([{k:(sorted(v) if isinstance(v,set) else v) for k,v in r.items()} for r in recs], open('/tmp/claude-0/-home-user-wadelovell-portfolio/2c8d9d81-3f91-5f3d-8b0c-289eaab48cde/scratchpad/merged_refs.json','w'), indent=1)
