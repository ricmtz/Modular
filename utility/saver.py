import json


class Saver:

    @staticmethod
    def __load():
        data = None
        with open('results.json', 'r') as j_file:
            data = json.load(j_file)
        return data

    @staticmethod
    def __save(data):
        with open('results.json', 'w') as j_file:
            json.dump(data, j_file)

    @staticmethod
    def save_results(algorithm='', params=[], evolution=[], time=0):
        data = Saver.__load()
        data[algorithm] = {
            'params': params,
            'evolution': evolution,
            'time': time
        }
        Saver.__save(data)

    @staticmethod
    def get_results():
        return Saver.__load()
