import os
# from pathlib import Path
from unittest import TestCase
from datetime import datetime
import tempfile
import pandas as pd
import pytest
from pyrtlib.apiwebservices import WyomingUpperAir
from pyrtlib.apiwebservices.erafive import ERA5Reanalysis

# TEST_DIR = Path(__file__).parent
# DATA_DIR = os.path.join(TEST_DIR, 'data')
THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class Test(TestCase):

    # @pytest.mark.datafiles(DATA_DIR)
    def test_wyom_get_stations(self):
        df = WyomingUpperAir.get_stations('pac')
        b = df[df.station_id=='45004'].station_name == 'Kings Park'

        assert b.values
        
    @pytest.mark.skip()
    def test_get_era5(self):
        lonlat = (15.13, 37.87)
        date = datetime(2022, 7, 22, 12)
        nc_file = ERA5Reanalysis.request_data(tempfile.gettempdir(), date, lonlat)
        print(nc_file)
        df_era5 = ERA5Reanalysis.read_data(nc_file, lonlat)
        
        assert df_era5.attrs['units']['t'] == 'K'
        assert df_era5.attrs['units']['p'] == 'hPa'
        assert df_era5.attrs['units']['rh'] == '%'
