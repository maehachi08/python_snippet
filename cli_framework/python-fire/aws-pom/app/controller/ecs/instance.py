# import boto3
# from botocore.exceptions import ClientError
from app.model.ecs.instance import EcsInstanceModel
from app.view.ecs.instance import EcsInstanceView


class Instance(object):
    '''
      for ECS Instance
    '''

    def __init__(self):
        self._inatance_model = EcsInstanceModel()
        self._inatance_view = EcsInstanceView()

    def show(self, cluster_name=''):
        '''
        :param name (str): the name of the person
        '''
        if type(cluster_name) is bool or not cluster_name:
            raise ValueError('please specific cluster name!')
        else:
            self.cluster_name = cluster_name
        self._inatance_info = self._inatance_model.get_cluster_instances()
        self.__inatances = self._inatance_view.instance(self._inatance_info)
        return self.__inatances

    def exec_command(self):
        return 'please implements'
