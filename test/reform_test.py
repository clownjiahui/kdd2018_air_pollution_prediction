import unittest
import numpy as np
import pandas as pd
import const
import numpy.testing as np_test
import pandas.util.testing as pd_test
from src.preprocess import reform


class UtilTest(unittest.TestCase):

    @staticmethod
    def test_window():
        """
            Test splitting a time-series into (x, y) blocks for prediction
        :return:
        """
        # test simple window
        windowed = reform.window(values=pd.Series([1, 2, 3, 4, 5, 6]), window_size=3, step=2)
        expected = np.array([[1, 2, 3], [3, 4, 5]])
        np_test.assert_array_equal(windowed, expected)

        # test windowing into (x, y) for prediction
        x, y = reform.window_for_predict(values=pd.Series([1, 2, 3, 4]),
                                         x_size=2, y_size=1, step=1)
        expected = {'x': np.array([[1, 2], [2, 3]]), 'y': np.array([[3], [4]])}
        np_test.assert_array_equal(x, expected['x'])
        np_test.assert_array_equal(y, expected['y'])

    @staticmethod
    def test_split():
        values = [1, 2, 3, 4, 5]
        yr = '2018-01-01 '
        times = pd.to_datetime(
            [yr + '12:00:00', yr + '13:00:00', yr + '14:00:00',
             yr + '15:00:00', yr + '16:00:00'], utc=True).tolist()
        t, x = reform.split(times, values, shift=2, step=2, skip=1)
        expected_x = [[2, 3], [4, 5]]
        expected_t = pd.to_datetime(pd.Series(
            [yr + '13:00:00', yr + '14:00:00']
        ), utc=True).tolist()
        np_test.assert_array_equal(expected_t, t)
        np_test.assert_array_equal(expected_x, x)

    @staticmethod
    def test_split_hours():
        """
            Test splitting a time series into hours
        :return:
        """
        values = [1, 2, 3, 4, 5]
        yr = '2018-01-01 '
        times = pd.to_datetime([yr + '12:00:00', yr + '13:00:00', yr + '14:00:00', yr + '15:00:00'],
                               utc=True).tolist()
        t, x, y = reform.split_dual(times, values, unit_x=2, unit_y=2)
        # day of week (1: monday), hour, value of two hours
        expected_x = [[1, 2], [2, 3]]
        expected_y = [[3, 4], [4, 5]]
        expected_t = pd.to_datetime(pd.Series(
            [yr + '12:00:00', yr + '13:00:00']
        ), utc=True).tolist()
        np_test.assert_array_equal(expected_t, t)
        np_test.assert_array_equal(expected_x, x)
        np_test.assert_array_equal(expected_y, y)

    @staticmethod
    def test_group_by_station():
        data = pd.DataFrame(data={const.ID: [1, 2, 3], 'value': [5, 6, 7]})
        stations = pd.DataFrame(data={const.ID: [1, 2, 3], const.PREDICT: [1, 0, 1]})
        grouped = reform.group_by_station(ts=data, stations=stations)
        expected = {
            1: pd.DataFrame(data={const.ID: [1], 'value': [5]}),
            3: pd.DataFrame(data={const.ID: [3], 'value': [7]}),
        }
        pd_test.assert_frame_equal(expected[1], grouped[1])
        pd_test.assert_frame_equal(expected[3], grouped[3])

    @staticmethod
    def test_form():
        value = [1, 2, 3, 4, 5]
        # expected to average from start to end
        average_forward = reform.average(value, 1)
        np_test.assert_array_equal(x=[1, 1.5, 3, 3.5, 5], y=average_forward)
        # expected to average from end to start
        average_backward = reform.average(value, -1)
        np_test.assert_array_equal(x=[1.5, 2, 3.5, 4, 5], y=average_backward)

    @staticmethod
    def test_wind_transform():
        # transform KDD2018 wind-speed and direction to polar values
        direction = pd.Series(data=[0, 90, 180])  # -> (90, 0, 270)
        speed = pd.Series(data=[1, 2, 3])
        expected_x = [0, 2, 0]
        expected_y = [1, 0, -3]
        x, y = reform.wind_transform(speed=speed, direction=direction)
        np_test.assert_almost_equal(expected_x, x, decimal=5)
        np_test.assert_almost_equal(expected_y, y, decimal=5)
