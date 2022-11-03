import os

# sample
# repos = [{'name': 'sample-repo', 'location': '/home/user/sample-repo'}]
repos = []

if len(repos) == 0:
    print('please add repo configuration')

for repo in repos:
    print('Checking ...', repo.get('name'))
    os.chdir(repo.get('location'))
    os.system('git pull')
    os.system('echo "-------------------"')

