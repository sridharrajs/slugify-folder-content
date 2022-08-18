import subprocess
from datetime import date
from string import Template

# Utility script to commit and push
# the changes within the current folder
# to the remote repo


def get_current_branch():
    stdout = subprocess.run(["git", "branch"], check=True,
                            capture_output=True, text=True).stdout
    return stdout.split()[1]


def stage_files():
    subprocess.run(["git", "add", "."], check=True,
                   capture_output=True, text=True).stdout


def assert_file_count(staged_file_count):
    if staged_file_count == 0:
        print('No changes to commit')
        quit()


def compute_staged_file_count():
    stateged_info = subprocess.run(
        ["git", "diff", "--name-only", "--cached"], check=True, capture_output=True, text=True).stdout

    total_changes = 0
    for file_name in stateged_info.split('\n'):
        if len(file_name.strip()) > 0:
            total_changes = total_changes + 1

    return total_changes


def build_commit_msg(staged_file_count, current_branch_name):
    today = date.today()

    commit_msg = Template(
        'Committed $change_count changes to $branch_name on $commit_date')
    msg = commit_msg.safe_substitute(
        branch_name=current_branch_name, commit_date=today, change_count=staged_file_count)

    return msg


def set_commit_msg(msg):
    commit_msg_file = open('.git/COMMIT_EDITMSG', 'w')

    commit_msg_file.writelines(msg)
    commit_msg_file.close()


def commit_changes():
    subprocess.run(["git", "commit", "-F", ".git/COMMIT_EDITMSG"],
                   check=True, capture_output=True, text=True).stdout



def push_to_origin(current_branch_name):
    subprocess.run(["git", "push", "origin", current_branch_name,
                   "-f"], check=True, capture_output=True, text=True).stdout
    subprocess.run(["git", "push", "bb", current_branch_name,
                   "-f"], check=True, capture_output=True, text=True).stdout
    subprocess.run(["git", "push", "gl", current_branch_name,
                   "-f"], check=True, capture_output=True, text=True).stdout


if __name__ == '__main__':
    current_branch_name = get_current_branch()
    stage_files()

    staged_file_count = compute_staged_file_count()
    assert_file_count(staged_file_count)
    msg = build_commit_msg(staged_file_count, current_branch_name)

    set_commit_msg(msg)
    commit_changes()
    push_to_origin(current_branch_name)

    print(msg)
