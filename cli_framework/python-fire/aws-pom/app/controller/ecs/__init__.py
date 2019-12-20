from app.controller.ecs.instance import Instance


class Ecs():
    '''
    for AWS ECS
    '''
    def __init__(self):
        self.instance = Instance()
