from git import Git
import re


class TestWorker():

    def run(self):
        sha = '503676ab639054b579f566a1de834349d75e7c37'
        print('real TestWorker.start method')
        self.__gitBranchFromSha(sha)

        codebuild = TestPhotonCodeBuild()
        codebuild.build()

    def __gitBranchFromSha(self, sha: str):
        git = Git()
        branchs = git.branch(contains=sha, r=True).split()
        print(branchs)

        pattern = re.compile('^origin\/(release|prerelease|hotfix|support)\/\d*\.\d*\.\d*(-.*)?$')
        filter_obj = filter(pattern.search, branchs)
        match_list = list(filter_obj)

        if match_list:
            print(match_list[0])

        else:
            print(None)


class TestPhotonCodeBuild():

    def build(self):
        print('called real codebuild.build')


if __name__ == "__main__":
    cls = TestWorker()
    cls.run()

