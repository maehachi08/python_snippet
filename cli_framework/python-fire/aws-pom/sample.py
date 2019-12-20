import fire

# from app.controller.calc import Calculator
from app.controller.ecs import Ecs


class AwsPom(object):
    def __init__(self):
        self.ecs = Ecs()


if __name__ == '__main__':
    fire.Fire(AwsPom)
