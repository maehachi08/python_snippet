from datetime import datetime


class Hoge():
    def __init__(self):
        self._now = datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S.%f')[:-3]

    @property
    def now(self):
        return self._now

