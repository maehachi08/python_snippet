# Description
#
#   git branch --contains <commit_id> をgitPythonで実装しただけ
#
# Args
#
#  git commit id
#
import sys
import re
from git import Git


def findGitBranch(commit_id=None):
    SHA = commit_id
    repo = Git()
    branchs = repo.branch(contains=SHA).split()
    # print(repo.branch(contains=SHA).split())

    pattern = re.compile('^(release|prerelease)\/.*$')
    match = filter(pattern.search, branchs)
    return list(match)[0]


if __name__ == '__main__':
    arguments = sys.argv
    if (len(arguments) != 2):
        print('Usage: # python %s <commit_id>' % arguments[0])
        quit()

    # first argument is self file name.
    script = arguments.pop(0)

    commit_id = arguments.pop(0)
    name = findGitBranch(commit_id)
    print(name)
