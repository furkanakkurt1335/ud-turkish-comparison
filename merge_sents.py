import os, json

tb_dir = 'treebanks'
data_files = [i for i in os.listdir(tb_dir) if i.endswith('.json')]
data_files.sort()
sent_l = []
sent_d = {}
for file in data_files:
    file_base = os.path.splitext(file)[0]
    if file_base not in sent_d:
        sent_d[file_base] = []
    with open(os.path.join(tb_dir, file), 'r', encoding='utf-8') as f:
        data = json.load(f)
    for annotation in data:
        md, table = annotation['md'], annotation['table']
        if 'text' in md and 'sent_id' in md:
            text = md['text']
            sent_id = md['sent_id']
            sent_l.append((text, sent_id))
            sent_d[file_base].append((text, sent_id))
        else:
            print('No text or sent_id in metadata for {}'.format(annotation))
            continue

with open('sent_l.json', 'w', encoding='utf-8') as f:
    json.dump(sent_l, f, ensure_ascii=False, indent=2)
with open('sent_d.json', 'w', encoding='utf-8') as f:
    json.dump(sent_d, f, ensure_ascii=False, indent=2)