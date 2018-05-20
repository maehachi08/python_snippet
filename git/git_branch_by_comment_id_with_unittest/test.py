import unittest
from unittest.mock import MagicMock
from gitbranch import TestWorker
from gitbranch import TestPhotonCodeBuild


def mocked_codebuild_build():
    print('called mocked_codebuild_build')


def mocked_gitBranchFromSha(sha: str):
    print('called mocked_gitBranchFromSha')
    if sha == '503676ab639054b579f566a1de834349d75e7c37':
        return 'release/0.0.0'


class TestTashizan(unittest.TestCase):

    #######################
    # @mock.patch の書き方
    #  module名.クラス名.メソッド名
    #
    #    e.g.)
    #      photon.codebuild.build まで指定すればOKかも?
    #######################
    # @patch('gitbranch.TestPhotonCodeBuild.build', side_effect=self.mocked_codebuild_build())
    def test_case1(self):
        print('unittest start')

        cls = TestWorker()

        # gitbranch.TestWorker.gitBranchFromSha メソッドが呼び出された時にモックを呼び出す
        cls._TestWorker__gitBranchFromSha = MagicMock(name='gitBranchFromSha', side_effect=mocked_gitBranchFromSha)

        # gitbranch.TestClass.gitBranchFromSha の返り値をモックで再現
        cls._TestWorker__gitBranchFromSha.return_value = 'release/0.0.0'

        # codebuild.build メソッドが呼び出された時にモックを呼び出す
        TestPhotonCodeBuild.build = MagicMock(name='gitBranchFromSha', side_effect=mocked_codebuild_build)

        # cls.run()

        # 想定の引数で呼び出されたことをテストする
        res = cls._TestWorker__gitBranchFromSha(sha='503676ab639054b579f566a1de834349d75e7c37')
        cls._TestWorker__gitBranchFromSha.assert_called_once_with(sha='503676ab639054b579f566a1de834349d75e7c37')
        print(res)


if __name__ == "__main__":
    unittest.main()
