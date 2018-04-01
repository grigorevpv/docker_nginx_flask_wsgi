import datetime

from numpy.core import number


class CpuLoader(object):

    def __init__(self, load_time: number = None):
        self._load_time = load_time

    def load(self):

        start = datetime.now()
        delta = datetime.timedelta(milliseconds=self._load_time)

        while True:

            now = datetime.now()
            if now - start > delta:
                break
