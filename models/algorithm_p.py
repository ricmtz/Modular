
class AlgorithmP:
    def __init__(self):
        self.threads = []

    def get_bests(self):
        bests = {}
        for i, t in enumerate(self.threads):
            bests[i] = t.get_best()
        return bests

    def get_errors(self):
        errors = {}
        for i, t in enumerate(self.threads):
            errors[i] = t.get_error()
        return errors
