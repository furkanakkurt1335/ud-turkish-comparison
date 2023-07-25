import os, re, json

annotation_pattern = '(# .+? = .+?\n)*?(((.+?\t){9}.+?\n)+?)\n'
unique_forms_dir = 'unique_forms'
if not os.path.exists(unique_forms_dir):
    os.mkdir(unique_forms_dir)
unique_deprels_dir = 'unique_deprels'
if not os.path.exists(unique_deprels_dir):
    os.mkdir(unique_deprels_dir)
unique_xpos_dir = 'unique_xpos'
if not os.path.exists(unique_xpos_dir):
    os.mkdir(unique_xpos_dir)
unique_misc_dir = 'unique_misc'
if not os.path.exists(unique_misc_dir):
    os.mkdir(unique_misc_dir)
tb_dir = 'treebanks'
data_files = [i for i in os.listdir(tb_dir) if i.endswith('.json')]
data_files.sort()
for file in data_files:
    file_base = os.path.splitext(file)[0]
    with open(os.path.join(tb_dir, file), 'r', encoding='utf-8') as f:
        data = json.load(f)
    form_d, deprel_d, xpos_d, misc_d = {}, {}, {}, {}
    for annotation in data:
        md, table = annotation['md'], annotation['table']
        lines = table.split('\n')
        for line in lines:
            fields = line.split('\t')
            id_t, form_t, lemma_t, upos_t, xpos_t, feats_t, head_t, deprel_t, deps_t, misc_t = fields
            if form_t not in form_d:
                form_d[form_t] = 0
            form_d[form_t] += 1
            if deprel_t not in deprel_d:
                deprel_d[deprel_t] = 0
            deprel_d[deprel_t] += 1
            if xpos_t not in xpos_d:
                xpos_d[xpos_t] = 0
            xpos_d[xpos_t] += 1
            if misc_t not in misc_d:
                misc_d[misc_t] = 0
            misc_d[misc_t] += 1
    with open(os.path.join(unique_forms_dir, file), 'w', encoding='utf-8') as f:
        form_d = {k: v for k, v in sorted(form_d.items(), key=lambda item: item[1], reverse=True)}
        json.dump(form_d, f, ensure_ascii=False, indent=4)
    with open(os.path.join(unique_deprels_dir, file), 'w', encoding='utf-8') as f:
        deprel_d = {k: v for k, v in sorted(deprel_d.items(), key=lambda item: item[1], reverse=True)}
        json.dump(deprel_d, f, ensure_ascii=False, indent=4)
    with open(os.path.join(unique_xpos_dir, file), 'w', encoding='utf-8') as f:
        xpos_d = {k: v for k, v in sorted(xpos_d.items(), key=lambda item: item[1], reverse=True)}
        json.dump(xpos_d, f, ensure_ascii=False, indent=4)
    with open(os.path.join(unique_misc_dir, file), 'w', encoding='utf-8') as f:
        misc_d = {k: v for k, v in sorted(misc_d.items(), key=lambda item: item[1], reverse=True)}
        json.dump(misc_d, f, ensure_ascii=False, indent=4)