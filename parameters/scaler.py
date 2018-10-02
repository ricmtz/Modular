from sklearn.preprocessing import MinMaxScaler

SCALER = MinMaxScaler(feature_range=(-1, 1))


class Scaler:
    @staticmethod
    def transform(array):
        if array.ndim == 1:
            array = array.reshape(-1, 1)
        return SCALER.fit_transform(array)
