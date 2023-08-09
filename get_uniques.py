import os, json

unique_forms_dir = 'unique_forms'
if not os.path.exists(unique_forms_dir):
    os.mkdir(unique_forms_dir)
unique_lemmas_dir = 'unique_lemmas'
if not os.path.exists(unique_lemmas_dir):
    os.mkdir(unique_lemmas_dir)
unique_upos_dir = 'unique_upos'
if not os.path.exists(unique_upos_dir):
    os.mkdir(unique_upos_dir)
unique_xpos_dir = 'unique_xpos'
if not os.path.exists(unique_xpos_dir):
    os.mkdir(unique_xpos_dir)
unique_feats_dir = 'unique_feats'
if not os.path.exists(unique_feats_dir):
    os.mkdir(unique_feats_dir)
unique_deprels_dir = 'unique_deprels'
if not os.path.exists(unique_deprels_dir):
    os.mkdir(unique_deprels_dir)
unique_misc_dir = 'unique_misc'
if not os.path.exists(unique_misc_dir):
    os.mkdir(unique_misc_dir)
tb_dir = 'treebanks'
data_files = [i for i in os.listdir(tb_dir) if i.endswith('.json')]
data_files.sort()
general_form_d, general_lemma_d, general_upos_d, general_xpos_d, general_feats_d, general_deprel_d, general_misc_d = {}, {}, {}, {}, {}, {}, {}
for file in data_files:
    file_base = os.path.splitext(file)[0]
    with open(os.path.join(tb_dir, file), 'r', encoding='utf-8') as f:
        data = json.load(f)
    form_d, lemma_d, upos_d, xpos_d, feats_d, deprel_d, misc_d = {}, {}, {}, {}, {}, {}, {}
    for annotation in data:
        md, table = annotation['md'], annotation['table']
        lines = table.split('\n')
        for line in lines:
            fields = line.split('\t')
            id_t, form_t, lemma_t, upos_t, xpos_t, feats_t, head_t, deprel_t, deps_t, misc_t = fields
            if form_t not in general_form_d:
                general_form_d[form_t] = {}
            if file_base not in general_form_d[form_t]:
                general_form_d[form_t][file_base] = 0
            general_form_d[form_t][file_base] += 1
            if form_t not in form_d:
                form_d[form_t] = 0
            form_d[form_t] += 1
            if lemma_t not in general_lemma_d:
                general_lemma_d[lemma_t] = {}
            if file_base not in general_lemma_d[lemma_t]:
                general_lemma_d[lemma_t][file_base] = 0
            general_lemma_d[lemma_t][file_base] += 1
            if lemma_t not in lemma_d:
                lemma_d[lemma_t] = 0
            lemma_d[lemma_t] += 1
            if upos_t not in general_upos_d:
                general_upos_d[upos_t] = {}
            if file_base not in general_upos_d[upos_t]:
                general_upos_d[upos_t][file_base] = 0
            general_upos_d[upos_t][file_base] += 1
            if upos_t not in upos_d:
                upos_d[upos_t] = 0
            upos_d[upos_t] += 1
            if xpos_t not in general_xpos_d:
                general_xpos_d[xpos_t] = {}
            if file_base not in general_xpos_d[xpos_t]:
                general_xpos_d[xpos_t][file_base] = 0
            general_xpos_d[xpos_t][file_base] += 1
            if xpos_t not in xpos_d:
                xpos_d[xpos_t] = 0
            xpos_d[xpos_t] += 1
            feat_l = feats_t.split('|')
            if not (len(feat_l) == 1 and feat_l[0] == '_'):
                for feat in feat_l:
                    if feat not in general_feats_d:
                        general_feats_d[feat] = {}
                    if file_base not in general_feats_d[feat]:
                        general_feats_d[feat][file_base] = 0
                    general_feats_d[feat][file_base] += 1
                    if feat not in feats_d:
                        feats_d[feat] = 0
                    feats_d[feat] += 1
            if deprel_t not in general_deprel_d:
                general_deprel_d[deprel_t] = {}
            if file_base not in general_deprel_d[deprel_t]:
                general_deprel_d[deprel_t][file_base] = 0
            general_deprel_d[deprel_t][file_base] += 1
            if deprel_t not in deprel_d:
                deprel_d[deprel_t] = 0
            deprel_d[deprel_t] += 1
            misc_l = misc_t.split('|')
            if not (len(misc_l) == 1 and misc_l[0] == '_'):
                for misc in misc_l:
                    if misc not in general_misc_d:
                        general_misc_d[misc] = {}
                    if file_base not in general_misc_d[misc]:
                        general_misc_d[misc][file_base] = 0
                    general_misc_d[misc][file_base] += 1
                    if misc not in misc_d:
                        misc_d[misc] = 0
                    misc_d[misc] += 1
    with open(os.path.join(unique_forms_dir, file), 'w', encoding='utf-8') as f:
        form_d = {k: v for k, v in sorted(form_d.items(), key=lambda item: item[1], reverse=True)}
        json.dump(form_d, f, ensure_ascii=False, indent=4)
    with open(os.path.join(unique_lemmas_dir, file), 'w', encoding='utf-8') as f:
        lemma_d = {k: v for k, v in sorted(lemma_d.items(), key=lambda item: item[1], reverse=True)}
        json.dump(lemma_d, f, ensure_ascii=False, indent=4)
    with open(os.path.join(unique_upos_dir, file), 'w', encoding='utf-8') as f:
        upos_d = {k: v for k, v in sorted(upos_d.items(), key=lambda item: item[1], reverse=True)}
        json.dump(upos_d, f, ensure_ascii=False, indent=4)
    with open(os.path.join(unique_xpos_dir, file), 'w', encoding='utf-8') as f:
        xpos_d = {k: v for k, v in sorted(xpos_d.items(), key=lambda item: item[1], reverse=True)}
        json.dump(xpos_d, f, ensure_ascii=False, indent=4)
    with open(os.path.join(unique_feats_dir, file), 'w', encoding='utf-8') as f:
        feats_d = {k: v for k, v in sorted(feats_d.items(), key=lambda item: item[1], reverse=True)}
        json.dump(feats_d, f, ensure_ascii=False, indent=4)
    with open(os.path.join(unique_deprels_dir, file), 'w', encoding='utf-8') as f:
        deprel_d = {k: v for k, v in sorted(deprel_d.items(), key=lambda item: item[1], reverse=True)}
        json.dump(deprel_d, f, ensure_ascii=False, indent=4)
    with open(os.path.join(unique_misc_dir, file), 'w', encoding='utf-8') as f:
        misc_d = {k: v for k, v in sorted(misc_d.items(), key=lambda item: item[1], reverse=True)}
        json.dump(misc_d, f, ensure_ascii=False, indent=4)
with open(os.path.join(unique_forms_dir, 'general.json'), 'w', encoding='utf-8') as f:
    general_form_d = {k: v for k, v in sorted(general_form_d.items(), key=lambda item: item[0])}
    json.dump(general_form_d, f, ensure_ascii=False, indent=4)
with open(os.path.join(unique_lemmas_dir, 'general.json'), 'w', encoding='utf-8') as f:
    general_lemma_d = {k: v for k, v in sorted(general_lemma_d.items(), key=lambda item: item[0])}
    json.dump(general_lemma_d, f, ensure_ascii=False, indent=4)
with open(os.path.join(unique_upos_dir, 'general.json'), 'w', encoding='utf-8') as f:
    general_upos_d = {k: v for k, v in sorted(general_upos_d.items(), key=lambda item: item[0])}
    json.dump(general_upos_d, f, ensure_ascii=False, indent=4)
with open(os.path.join(unique_xpos_dir, 'general.json'), 'w', encoding='utf-8') as f:
    general_xpos_d = {k: v for k, v in sorted(general_xpos_d.items(), key=lambda item: item[0])}
    json.dump(general_xpos_d, f, ensure_ascii=False, indent=4)
with open(os.path.join(unique_feats_dir, 'general.json'), 'w', encoding='utf-8') as f:
    general_feats_d = {k: v for k, v in sorted(general_feats_d.items(), key=lambda item: item[0])}
    json.dump(general_feats_d, f, ensure_ascii=False, indent=4)
with open(os.path.join(unique_deprels_dir, 'general.json'), 'w', encoding='utf-8') as f:
    general_deprel_d = {k: v for k, v in sorted(general_deprel_d.items(), key=lambda item: item[0])}
    json.dump(general_deprel_d, f, ensure_ascii=False, indent=4)
with open(os.path.join(unique_misc_dir, 'general.json'), 'w', encoding='utf-8') as f:
    general_misc_d = {k: v for k, v in sorted(general_misc_d.items(), key=lambda item: item[0])}
    json.dump(general_misc_d, f, ensure_ascii=False, indent=4)