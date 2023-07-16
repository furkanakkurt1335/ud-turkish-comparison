import subprocess, json

repos_path = 'repos.json'
with open(repos_path, 'r') as f:
    repos = json.load(f)
for repo in repos:
    url = 'https://github.com/UniversalDependencies/' + repo
    subprocess.run(['git', 'clone', url])