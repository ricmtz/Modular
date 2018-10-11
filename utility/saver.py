import json


class Saver:

    @staticmethod
    def __load():
        data = None
        with open('results.json') as j_file:
            data = json.load(j_file)
        return data

    @staticmethod
    def __save(data):
        with open('results.json', 'w') as j_file:
            json.dump(data, j_file)

    @staticmethod
    def save_results(algorithm='', params=[], evolution=[]):
        data = Saver.__load()
        data[algorithm] = {
            'params': params,
            'evolution': evolution
        }
        Saver.__save(data)

    @staticmethod
    def get_results():
        return Saver.__load()
