""" Reads in Excel File containing trip data
    Creates trip objects and saves them in item list
   

"""

import xlrd


class Trip(object):
  
  """ trip object containing data about trips by Flixbus

    Attributes
    ----------
    lat_start: float
        Latitude of start point in degree.
    lon_start: float
        Longitude of start point in degree.
    lat_arr: float
        Latitude of arrival point in degree.
    lon_arr: float
        Longitude of arrival point in degree.
    time_start: float
        Start time of trip.
    time_arr: float
        Arrival time of trip.
    seat_req: float
        Required number of seats.
    lat_depot: float
        Latitude of depot location in degree.
    lon_depot: float
        Longitude of depot location in degree.
    

     """
    def __init__(self, id, lat_start, lon_start, lat_arr, lon_arr, time_start, time_arr, time_break, seat_req, lat_depot, lon_depot):
      
        self.id = id
        self.lat_start = lat_start
        self.lon_start = lon_start
        self.lat_arr = lat_arr
        self.lon_arr = lon_arr
        self.time_start = time_start
        self.time_arr = time_arr
        self.time_break=time_break
        self.seat_req = seat_req
        self.lat_depot = lat_depot
        self.lon_depot = lon_depot



def read_excel(filename)
  
   """ Reads in Excel file containing trip data 
       Creates trip objects and saves them in list

        Parameters
        ----------
        filename: file
          excel file containing trip information
        
        Returns
        -------
        items: list
            list of trip items 

    """
  worksheet = workbook.sheet_by_name(filename)
  
  
      number_of_rows = sheet.nrows
      number_of_columns = sheet.ncols
  
      items = []
  
      rows = []
      for row in range(1, number_of_rows):
          values = []
          for col in range(number_of_columns):
              value  = (sheet.cell(row,col).value)
              try:
                  value = str(int(value))
              except ValueError:
                  pass
              finally:
                  values.append(value)
          item = Trip(*values)
          items.append(item)

return items