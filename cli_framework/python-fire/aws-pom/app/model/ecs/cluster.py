import boto3
from botocore.exceptions import ClientError


class EcsClusterModel():
    '''
        ECS Cluster関連のロジックを書くmodule
    '''
    def __init__(self, cluster_name: str = None):
        self.client = boto3.client('ecs')
        self.cluster_name = cluster_name

    def get_cluster_instances(self) -> dict:
        container_inatances_arn = self._get_container_inatances_arn()
        response = self._get_ecs_inatances_info(container_inatances_arn)
        response = {
            "instances": [
                {"instance_id": "i-xxxxxxxxxxx", "instance_ip": "192.168.10.10"},
                {"instance_id": "i-xxxxxxxxxxx", "instance_ip": "192.168.10.10"},
                {"instance_id": "i-xxxxxxxxxxx", "instance_ip": "192.168.10.10"}
            ]
        }
        return response

    def _get_container_inatances_arn(self):
        pass

    def _get_ecs_inatances_info(self, container_inatances_arn: list):
        pass
