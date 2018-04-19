DEFAULT = 'DEFAULT'

OBSERVED = 'OBSERVED'
OBSERVED_MISSING = 'OBSERVED_MISSING'
AQ = 'AQ'
AQ_REST = 'AQ_REST'
AQ_LIVE = 'AQ_LIVE'
AQ_STATIONS = 'AQ_STATIONS'
MEO = 'MEO'
MEO_LIVE = 'MEO_LIVE'
STATIONS = 'STATIONS'
FEATURES = 'FEATURES'
POLLUTANT = 'pollutant'
LOSS_FUNCTION = 'loss'
IS_TEST = 'is_test'

MEAN_ABSOLUTE = 'mean_absolute_error'
MEAN_PERCENT = 'mean_absolute_percentage_error'

BJ_AQ = 'BJ_AQ'
BJ_AQ_REST = 'BJ_AQ_REST'
BJ_AQ_LIVE = 'BJ_AQ_LIVE'
BJ_AQ_STATIONS = 'BJ_AQ_STATIONS'
BJ_MEO = 'BJ_MEO'
BJ_MEO_LIVE = 'BJ_MEO_LIVE'
BJ_GRID_DATA = 'BJ_GRID_DATA'
BJ_GRID_URL = 'BJ_GRID_URL'
BJ_GRID_LIVE = 'BJ_GRID_LIVE'
BJ_OBSERVED = 'BJ_OBSERVED'
BJ_OBSERVED_AUG = 'BJ_OBSERVED_AUG'
BJ_OBSERVED_MISS = 'BJ_OBSERVED_MISS'
BJ_STATIONS = 'BJ_STATIONS'
BJ_GRIDS = 'BJ_GRIDS'
BJ_READ_LIVE = 'BJ_READ_LIVE'
BJ_PM25_ = 'BJ_PM25_'
BJ_PM10_ = 'BJ_PM10_'
BJ_O3_ = 'BJ_O3_'

LD_AQ = 'LD_AQ'
LD_AQ_REST = 'LD_AQ_REST'
LD_AQ_LIVE = 'LD_AQ_LIVE'
LD_AQ_STATIONS = 'LD_AQ_STATIONS'
LD_OBSERVED = 'LD_OBSERVED'
LD_OBSERVED_AUG = 'LD_OBSERVED_AUG'
LD_GRID_DATA = 'LD_GRID_DATA'
LD_GRIDS = 'LD_GRIDS'
LD_GRID_URL = 'LD_GRID_URL'
LD_GRID_LIVE = 'LD_GRID_LIVE'
LD_OBSERVED_MISS = 'LD_OBSERVED_MISS'
LD_STATIONS = 'LD_STATIONS'
LD_READ_LIVE = 'LD_READ_LIVE'
LD_FEATURES = 'LD_FEATURES'
LD_PM25_ = 'LD_PM25_FEATURES'
LD_PM10_ = 'LD_PM10_FEATURES'

MODEL = 'model'
GRIDS = 'grids'
GRID_DATA = 'grid_data'
GRID_URL = 'grid_url'
GRID_LIVE = 'grid_live'

ID = 'station_id'
GID = 'grid_id'
TIME = 'utc_time'
PREDICT = 'predict'
LONG = 'longitude'
LAT = 'latitude'
TEMP = 'temperature'
PRES = 'pressure'
HUM = 'humidity'
WSPD = 'wind_speed'
WDIR = 'wind_direction'
S_TYPE = 'station_type'
T_FORMAT = '%y-%m-%d %H'
T_FORMAT_FULL = '%Y-%m-%d %H:%M:%S'

MNIST_FOLDER = 'MNIST_FOLDER'


def func():
    global DEFAULT
    global OBSERVED, OBSERVED_MISSING, IS_TEST
    global AQ, AQ_REST, AQ_LIVE, AQ_STATIONS
    global BJ_AQ, BJ_AQ_REST, BJ_AQ_LIVE, AQ_LIVE
    global MEO, MEO_LIVE, BJ_MEO, BJ_MEO_LIVE
    global BJ_STATIONS
    global BJ_OBSERVED, BJ_OBSERVED_AUG
    global BJ_OBSERVED_MISS
    global BJ_STATIONS
    global BJ_READ_LIVE
    global LD_AQ, LD_AQ_REST, LD_AQ_LIVE
    global LD_AQ_STATIONS
    global LD_OBSERVED
    global LD_OBSERVED_MISS
    global LD_STATIONS
    global LD_READ_LIVE
    global ID, GID, TIME, PREDICT, LONG, LAT, TEMP, PRES, HUM, WSPD, WDIR, S_TYPE
    global T_FORMAT
    global FEATURES, BJ_PM25_, BJ_PM10_, BJ_O3_
    global LD_FEATURES, LD_PM25_, LD_PM10_
    global POLLUTANT
    global LOSS_FUNCTION, MEAN_ABSOLUTE, MEAN_PERCENT
    global MODEL
    global GRIDS, GRID_DATA, GRID_LIVE, GRID_URL, BJ_GRIDS, BJ_GRID_DATA, BJ_GRID_URL
    global LD_GRIDS, LD_GRID_DATA, LD_GRID_URL, BJ_GRID_LIVE, LD_GRID_LIVE
    global MNIST_FOLDER
