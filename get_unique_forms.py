import os, re

annotation_pattern = '(# .+? = .+?\n)*?(((.+?\t){9}.+?\n)+?)\n'
unique_forms_dir = 'unique_forms'
if not os.path.exists(unique_forms_dir):
    os.mkdir(unique_forms_dir)
folders = [i for i in os.listdir() if os.path.isdir(i) and i.startswith('UD_Turkish-')]
folders.sort()
for folder in folders:
    form_d = {}
    conllu_files = [i for i in os.listdir(folder) if i.endswith('.conllu')]
    conllu_files.sort()
    for conllu_file in conllu_files:
        with open(os.path.join(folder, conllu_file), 'r', encoding='utf-8') as f:
            content = f.read()
        annotations = re.findall(annotation_pattern, content)
        for annotation in annotations:
            table = annotation[1].strip()
            lines = table.split('\n')
            for line in lines:
                fields = line.split('\t')
                form = fields[1]
                if form not in form_d:
                    form_d[form] = 0
                form_d[form] += 1
    with open(os.path.join(unique_forms_dir, folder + '.txt'), 'w', encoding='utf-8') as f:
        for form in sorted(form_d, key=form_d.get, reverse=True):
            f.write(form + '\n')