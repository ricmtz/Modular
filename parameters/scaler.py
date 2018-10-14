from sklearn.preprocessing import MinMaxScaler
from parameters import Parameter


MIN_MAX_IA = (min(Parameter.I_ALPHA), max(Parameter.I_ALPHA))
MIN_MAX_IB = (min(Parameter.I_BETA), max(Parameter.I_BETA))
MIN_MAX_W = (min(Parameter.THETA), max(Parameter.THETA))

SCALER = MinMaxScaler(feature_range=(-1, 1))
SCALER_IA = MinMaxScaler(feature_range=MIN_MAX_IA)
SCALER_IB = MinMaxScaler(feature_range=MIN_MAX_IB)
SCALER_W = MinMaxScaler(feature_range=MIN_MAX_W)


class Scaler:
    @staticmethod
    def transform(array):
        if array.ndim == 1:
            array = array.reshape(-1, 1)
        return SCALER.fit_transform(array)

    @staticmethod
    def transform_ia(array):
        if array.ndim == 1:
            array = array.reshape(-1, 1)
        return SCALER_IA.fit_transform(array)

    @staticmethod
    def transform_ib(array):
        if array.ndim == 1:
            array = array.reshape(-1, 1)
        return SCALER_IB.fit_transform(array)

    @staticmethod
    def transform_w(array):
        if array.ndim == 1:
            array = array.reshape(-1, 1)
        return SCALER_W.fit_transform(array)
