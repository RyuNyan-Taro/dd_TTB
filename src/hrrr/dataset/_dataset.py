import numpy as np
from .. import file


def _tude_list(min_tude, max_tude, length) -> list:
    delta_tude = (max_tude-min_tude) / (length-1)

    return [min_tude+delta_tude*_i for _i in range(length)]


class hrrr_dataset:
    def __init__(self, year, month, date):
        self.ds = file.hrrr_dataset(year, month, date)

    def tude_range_list(self, tude: str) -> list:
        if tude == 'latitude':
            min_tude, max_tude = np.min(np.array(self.ds.latitude)), np.max(np.array(self.ds.latitude))
            length = np.shape(self.ds.t)[0]
        elif tude == 'longitude':
            min_tude, max_tude = np.min(np.array(self.ds.longitude)), np.max(np.array(self.ds.longitude))
            length = np.shape(self.ds.t)[1]
        else:
            raise ValueError(f'You must select latitude or longitude as tude. {tude} is not them.')

        tude_list = _tude_list(min_tude, max_tude, length)
        if tude == 'longitude':
            tude_list = [_val-360 for _val in tude_list]  # convert from 360 degree to 180 degree

        return tude_list


