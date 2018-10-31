import unittest
import main

from unittest.mock import Mock, patch, MagicMock


class TestMain(unittest.TestCase):

    def setUp(self):
        self.target = main.EcsCluster()

    @patch('main.boto3.client')
    def test_cluster_list_success(self, mocked_boto3):
        response = self.target.cluster_list()

        # mocked_boto3が引数 'ecs' で1度実行されていること
        args, kwargs = mocked_boto3.call_args
        self.assertEqual(args[0], 'ecs')
        self.assertEqual(mocked_boto3.call_count, 1)

        # mocked_boto3('ecs').list_clusters が1度実行されていること
        self.assertEqual(mocked_boto3('ecs').list_clusters.call_count, 1)



