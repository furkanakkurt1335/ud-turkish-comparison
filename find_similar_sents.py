import os, json, logging
from rapidfuzz import process, fuzz, utils

logging.basicConfig(level=logging.INFO, filename='find_similar_sents.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.info('Start find_similar_sents.py')

with open('repos.json', 'r', encoding='utf-8') as f:
    repos = json.load(f)
with open('sent_d.json', 'r', encoding='utf-8') as f:
    sent_d = json.load(f)

similar_d = {}
for repo in repos:
    sent_l = []
    for k, v in sent_d.items():
        if k != repo:
            sent_l.extend([(text, sent_id, k) for text, sent_id in v])
    texts, _, _ = zip(*sent_l)
    texts_repo, sent_ids_repo = zip(*sent_d[repo])
    for sent_id, text in zip(sent_ids_repo, texts_repo):
        res = process.extract(text, texts, scorer=fuzz.token_sort_ratio, score_cutoff=90)
        if len(res):
            if repo not in similar_d:
                similar_d[repo] = {}
            if sent_id not in similar_d[repo]:
                similar_d[repo][sent_id] = {'text': text, 'similar': []}
            select_indices = [i[2] for i in res]
            selected = [sent_l[i] for i in select_indices]
            similar_d[repo][sent_id]['similar'].extend(selected)
            logging.info('Found {} similar sentences for {} in {}'.format(len(selected), sent_id, repo))
    with open('similar_d.json', 'w', encoding='utf-8') as f:
        json.dump(similar_d, f, ensure_ascii=False, indent=2)
    logging.info('Saved for {}'.format(repo))

with open('similar_d.json', 'w', encoding='utf-8') as f:
    json.dump(similar_d, f, ensure_ascii=False, indent=2)
logging.info('Saved similar_d.json')