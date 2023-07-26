import os, json

tb_dir = 'treebanks'
data_files = [i for i in os.listdir(tb_dir) if i.endswith('.json')]
data_files.sort()
usage_d = {}
usage_l = ['mıştı', 'mişti', 'ecekmiş', 'acakmış', 'ecekti', 'acaktı', 'yormuş', 'yordu']
lemma_l = ['ol', 'ki', 'mi', 'mı', 'de', 'da', 'değil']
deprel_l = ['compound']
for file in data_files:
    file_base = os.path.splitext(file)[0]
    with open(os.path.join(tb_dir, file), 'r', encoding='utf-8') as f:
        data = json.load(f)
    for annotation in data:
        md, table = annotation['md'], annotation['table']
        if 'text' in md and 'sent_id' in md:
            text = md['text'].lower()
            sent_id = md['sent_id']
            for usage in usage_l:
                if usage not in usage_d:
                    usage_d[usage] = {}
                if file_base not in usage_d[usage]:
                    usage_d[usage][file_base] = []
                if usage in text and sent_id not in usage_d[usage][file_base]:
                    usage_d[usage][file_base].append(sent_id)
        else:
            continue
        lines = table.split('\n')
        for line in lines:
            fields = line.split('\t')
            id_t, form_t, lemma_t, upos_t, xpos_t, feats_t, head_t, deprel_t, deps_t, misc_t = fields
            if '-' in id_t:
                if 'split_lemma' not in usage_d:
                    usage_d['split_lemma'] = {}
                if file_base not in usage_d['split_lemma']:
                    usage_d['split_lemma'][file_base] = []
                if sent_id not in usage_d['split_lemma'][file_base]:
                    usage_d['split_lemma'][file_base].append(sent_id)
            if lemma_t in lemma_l:
                if lemma_t not in usage_d:
                    usage_d[lemma_t] = {}
                if file_base not in usage_d[lemma_t]:
                    usage_d[lemma_t][file_base] = []
                if sent_id not in usage_d[lemma_t][file_base]:
                    usage_d[lemma_t][file_base].append(sent_id)
            if deprel_t in deprel_l:
                if deprel_t not in usage_d:
                    usage_d[deprel_t] = {}
                if file_base not in usage_d[deprel_t]:
                    usage_d[deprel_t][file_base] = []
                if sent_id not in usage_d[deprel_t][file_base]:
                    usage_d[deprel_t][file_base].append(sent_id)
with open('usage_d.json', 'w', encoding='utf-8') as f:
    json.dump(usage_d, f, ensure_ascii=False, indent=2)
