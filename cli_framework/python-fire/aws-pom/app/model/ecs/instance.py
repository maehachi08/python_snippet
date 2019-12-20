import boto3
# from botocore.exceptions import ClientError


class EcsInstanceModel():
    '''
        - ECS Instance関連のロジックを書くmodule
        - Controllerから呼びだされて結果を返す
        - formatやprintのための整形はView Classで行う
    '''
    def __init__(self):
        self.client = boto3.client('ecs')

    def get_cluster_instances(self) -> dict:
        container_inatances_arn = self._get_container_inatances_arn()
        response = self._get_ecs_inatances_info(container_inatances_arn)
        response = [
            {"instance_id": "i-xxxxxxxxxxx", "instance_ip": "192.168.10.10"},
            {"instance_id": "i-xxxxxxxxxxx", "instance_ip": "192.168.10.10"},
            {"instance_id": "i-xxxxxxxxxxx", "instance_ip": "192.168.10.10"}
        ]
        return response

    def _get_container_inatances_arn(self):
        pass

    def _get_ecs_inatances_info(self, container_inatances_arn: list):
        pass

