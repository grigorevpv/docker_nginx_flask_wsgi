class CpuLoader(object):

    def __init__(self, load_time: number = None) -> void:
        self._load_time = load_time

    @staticmethod
    def load(self) -> void:

        start = datetime.now()
        delta = timedelta(milliseconds=timeout)

        while True:

            now = datetime.now()
            if now - start > delta:
                break
