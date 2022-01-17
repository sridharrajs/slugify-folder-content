import subprocess
from datetime import date
from string import Template

# Getting current branch.
stdout = subprocess.run(["git", "branch"], check=True, capture_output=True, text=True).stdout
git_branch_name = stdout.split()[1]

## Adding files
subprocess.run(["git", "add", "."], check=True, capture_output=True, text=True).stdout

stateged_info = subprocess.run(["git", "diff", "--name-only","--cached"], check=True, capture_output=True, text=True).stdout

total_changes = 0
for file_name in stateged_info.split('\n'):
    if len(file_name.strip()) > 0:
        total_changes = total_changes + 1

## Writing commit message.
today = date.today()
commit_msg_file = open('.git/COMMIT_EDITMSG', 'w')


commit_msg = Template('Committed $change_count changes to $branch_name on $commit_date')
msg = commit_msg.safe_substitute(branch_name= git_branch_name, commit_date=today, change_count=total_changes)

commit_msg_file.writelines(msg)
commit_msg_file.close()

stdout = subprocess.run(["git", "commit", "-F", ".git/COMMIT_EDITMSG"], check=True, capture_output=True, text=True).stdout
stdout = subprocess.run(["git", "push", "origin", git_branch_name, "-f"], check=True, capture_output=True, text=True).stdout

print(msg)
