# 2D  Plotting in Python: Citys Climate 2023

# Including temperature statistics in °C and precipitation in millimeter

import numpy as np

# Beijing
Beijing_temp_max        = np.array([ -1.1,  2.3,  9.1, 18.4, 25.0, 30.1, 31.9, 30.8, 26.2, 18.5,  8.3,  0.5])
Beijing_temp_min        = np.array([-10.0, -7.7, -1.6,  6.4, 13.8, 19.3, 23.1, 22.3, 15.5,  6.9, -2.2, -8.2])
Beijing_temp_ave        = np.array([ -5.5, -2.8,  3.7, 12.4, 19.4, 24.7, 27.4, 26.5, 20.6, 12.7,  3.1, -3.9])
Beijing_precipitation   = np.array([  3.0,  4.0,  8.0, 25.0, 44.0, 78.0,185.0,165.0, 37.0, 12.0,  3.0,  2.0])

# Shanghai
Shanghai_temp_max       = np.array([  8.3,  9.2, 12.8, 18.1, 23.0, 27.1, 31.1, 31.3, 27.4, 22.8, 17.6, 12.5])
Shanghai_temp_min       = np.array([  0.5,  1.5,  5.3, 10.7, 15.8, 20.2, 24.1, 23.9, 19.4, 14.2,  8.7,  3.7])
Shanghai_temp_ave       = np.array([  4.3,  5.3,  9.0, 14.4, 19.4, 23.6, 27.6, 27.5, 23.4, 18.5, 13.1,  8.1])
Shanghai_precipitation  = np.array([ 53.0, 59.0, 94.0, 87.0, 89.0,152.0,221.0,157.0,121.0, 63.0, 46.0, 43.0])

# Sydney
Sydney_temp_max         = np.array([ 26.6, 26.5, 25.1, 22.6, 19.2, 16.4, 15.6, 17.1, 19.2, 21.5, 23.2, 25.2])
Sydney_temp_min         = np.array([ 19.5, 19.7, 18.8, 15.6, 12.2,  9.4,  8.5,  9.4, 11.3, 13.6, 16.2, 18.5])
Sydney_temp_ave         = np.array([ 23.0, 23.1, 22.0, 19.1, 15.7, 12.9, 12.0, 13.3, 15.3, 17.5, 19.7, 21.8])
Sydney_precipitation    = np.array([102.0,126.0,122.0,131.0,120.0,128.0, 83.0, 81.0, 71.0, 74.0, 85.0, 90.0])

# Calgary
Calgary_temp_max        = np.array([ -0.6,  1.2,  5.6, 11.9, 17.4, 21.4, 23.9, 23.0, 18.0, 11.9,  3.5, -2.5])
Calgary_temp_min        = np.array([-13.7,-12.7, -7.8, -1.3,  3.8,  8.1,  9.7,  8.9,  4.7, -0.5, -8.0,-14.1])
Calgary_temp_ave        = np.array([ -7.2, -5.8, -1.1,  5.3, 10.6, 14.8, 16.8, 15.9, 11.4,  5.7, -2.3, -8.3])
Calgary_precipitation   = np.array([ 11.4, 10.5, 17.3, 31.6, 52.4, 77.7, 71.2, 57.0, 40.2, 23.6, 13.8, 12.3])

# Toronto
Toronto_temp_max        = np.array([ -1.0, -0.4,  4.1, 11.0, 18.3, 23.0, 26.0, 25.1, 21.0, 14.2,  7.4,  0.6])
Toronto_temp_min        = np.array([-10.0, -7.7, -1.6,  6.4, 13.8, 19.3, 23.1, 22.3, 15.5,  6.9, -2.2, -8.2])
Toronto_temp_ave        = np.array([ -5.5, -2.8,  3.7, 12.4, 19.4, 24.7, 27.4, 26.5, 20.6, 12.7,  3.1, -3.9])
Toronto_precipitation   = np.array([  3.0,  4.0,  8.0, 25.0, 44.0, 78.0,185.0,165.0, 37.0, 12.0,  3.0,  2.0])

# LA
