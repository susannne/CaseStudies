
""" Contains function for calculation of distance between two points
   

"""

import numpy as np
import math


c=40000000 #circumference of earth in meter
f=360  # full circle in degree
f_rad=2*math.pi # full circle in radians

def calculate_distance(lat_start, lat_end, lon_start, lon_end):

    """ Calculates distance of two coordinates in meter

        Parameters
        ----------
        lat_start: float
            latitude of start position
        lon_end: float
            longitude of start position
        lat_end: float
            latitude of end position
        lon_end: float
            longitude of end position

        Returns
        -------
        distance: float
            distance of two positions in meter

    """

    lat2=math.radians(lat_end) # convert from degree to radians
    lat1=math.radians(lat_start)
    lon2=math.radians(lon_end)
    lon1=math.radians(lon_start)


    dlon = lon2 - lon1 # calculate delta
    dlat = lat2 - lat1

    dlat_meter=dlat *c/f_rad  # convert to meter
    dlon_meter=dlon *c/f_rad* math.cos(0.5*(lat2+lat1))

    distance=np.sqrt(dlat_meter**2+dlon_meter**2) #  Pythagoras' theorem

    return distance

