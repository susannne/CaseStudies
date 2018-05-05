
""" Reads in Excel File containing trip data
    Creates trip objects and saves them in item list
   
   Version 0.3 edited by Susanne
   
   Dates are read in wrong

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
    time_arr: date
        Arrival time of trip.
    time_break : integer
        Required break time
    seat_req: integer
        Required number of seats.
    lat_depot: float
        Latitude of depot location in degree.
    lon_depot: float
        Longitude of depot location in degree.
    

     """

  def __init__(self, id, lat_start, lon_start, lat_arr, lon_arr,    time_start, time_arr, time_break, seat_req, lat_depot,   lon_depot):
        
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
   

def read_excel(filepath, sheet):

#Probleme mit Kommentarblock, spaeter wieder einfuegen..

  workbook= xlrd.open_workbook(filepath)
  #z.B. ("/home/runner/case_studies_trips_09-10_2017.xlsx",)
  
  worksheet= workbook.sheet_by_name(sheet)
  #worksheet = workbook.sheet_by_name(filename)
  
  number_of_rows = worksheet.nrows
  
  number_of_columns = worksheet.ncols
  
  items = []
  
  rows = []
  
  for row in range(1,number_of_rows):
    values = []
    
    for col in range(11):
      value  = (worksheet.cell(row,col).value)
      
      try:
        value = float(value)
        
        
      except ValueError:
        pass
      finally:
        values.append(value)
        
        #Datum kann so nicht eingelesen werden, wir muessen das umwandeln am besten in Excel (erstes Datum = Minute 0)
    #print(values)
    item = Trip(*values)
    items.append(item)
    #print(items)
  return items
