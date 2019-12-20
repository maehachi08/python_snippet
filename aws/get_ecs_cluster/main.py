import sys
import boto3
import json

from botocore.exceptions import ClientError


class EcsCluster:
    """
    get ecs cluster list of ap-northeast-1
    """

    def cluster_list(self) -> dict:
        """
        get source ami name
        """
        ecs = boto3.client('ecs')
        return ecs.list_clusters()


if __name__ == '__main__':
    client = EcsCluster()
    response = client.cluster_list()
    print(response)

