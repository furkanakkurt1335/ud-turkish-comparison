import os, json

tb_dir = 'treebanks'
data_files = [i for i in os.listdir(tb_dir) if i.endswith('.json')]
data_files.sort()
lemma_d = {}
for file in data_files:
    file_base = os.path.splitext(file)[0]
    if file_base not in lemma_d:
        lemma_d[file_base] = {}
    with open(os.path.join(tb_dir, file), 'r', encoding='utf-8') as f:
        data = json.load(f)
    for annotation in data:
        md, table = annotation['md'], annotation['table']
        lines = table.split('\n')
        for line in lines:
            fields = line.split('\t')
            id_t, form_t, lemma_t, upos_t, xpos_t, feats_t, head_t, deprel_t, deps_t, misc_t = fields
            if upos_t == 'PART':
                if lemma_t not in lemma_d[file_base]:
                    lemma_d[file_base][lemma_t] = 0
                lemma_d[file_base][lemma_t] += 1
with open('upos_part_lemmas.json', 'w', encoding='utf-8') as f:
    json.dump(lemma_d, f, ensure_ascii=False, indent=4)
