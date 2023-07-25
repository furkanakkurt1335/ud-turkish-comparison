import os, re, json

folders = [i for i in os.listdir() if os.path.isdir(i) and i.startswith('UD_Turkish-')]
folders.sort()
md_pattern = '^# (.+?) = (.+?)$'
for folder in folders:
    tb_l = []
    conllu_files = [i for i in os.listdir(folder) if i.endswith('.conllu')]
    conllu_files.sort()
    for conllu_file in conllu_files:
        with open(os.path.join(folder, conllu_file), 'r', encoding='utf-8') as f:
            content = f.read()
        annotations = content.split('\n\n')
        for i, annotation in enumerate(annotations):
            d, md_d, table = {}, {}, ''
            in_table = False
            for line in annotation.split('\n'):
                if not in_table:
                    md_find = re.search(md_pattern, line)
                    if md_find:
                        md_d[md_find.group(1)] = md_find.group(2)
                    else:
                        if line.startswith('#'):
                            continue
                        in_table = True
                        table += line + '\n'
                else:
                    table += line + '\n'
            table = table.strip()
            if md_d:
                d['md'] = md_d
            if table:
                d['table'] = table.strip()
            if d:
                tb_l.append(d)
    with open(os.path.join(folder, 'treebank.json'), 'w', encoding='utf-8') as f:
        json.dump(tb_l, f, ensure_ascii=False, indent=4)
