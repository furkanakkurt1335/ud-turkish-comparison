import os, re, json

annotation_pattern = '(# .+? = .+?\n)*?(((.+?\t){9}.+?\n)+?)\n'
# unique_forms_dir = 'unique_forms'
# if not os.path.exists(unique_forms_dir):
#     os.mkdir(unique_forms_dir)
unique_deprels_dir = 'unique_deprels'
if not os.path.exists(unique_deprels_dir):
    os.mkdir(unique_deprels_dir)
folders = [i for i in os.listdir() if os.path.isdir(i) and i.startswith('UD_Turkish-')]
folders.sort()
for folder in folders:
    # form_d = {}
    deprel_d = {}
    with open(os.path.join(folder, 'treebank.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
    for annotation in data:
        md, table = annotation['md'], annotation['table']
        lines = table.split('\n')
        for line in lines:
            fields = line.split('\t')
            id_t, form_t, lemma_t, upos_t, xpos_t, feats_t, head_t, deprel_t, deps_t, misc_t = fields
            if deprel_t not in deprel_d:
                deprel_d[deprel_t] = 0
            deprel_d[deprel_t] += 1
    with open(os.path.join(unique_deprels_dir, folder + '.txt'), 'w', encoding='utf-8') as f:
        for deprel in sorted(deprel_d, key=deprel_d.get, reverse=True):
            f.write(deprel + '\n')
    #             if form not in form_d:
    #                 form_d[form] = 0
    #             form_d[form] += 1
    # with open(os.path.join(unique_forms_dir, folder + '.txt'), 'w', encoding='utf-8') as f:
    #     for form in sorted(form_d, key=form_d.get, reverse=True):
    #         f.write(form + '\n')