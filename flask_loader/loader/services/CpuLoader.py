import datetime


class CpuLoader(object):

    def __init__(self, load_time):
        self._load_time = load_time

    def load(self):

        start = datetime.datetime.now()
        delta = datetime.timedelta(milliseconds=self._load_time)

        while True:

            now = datetime.datetime.now()
            if now - start > delta:
                break

