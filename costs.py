""" Contains function for calculation of incurred costs for each path consisting of:
  - dead head distances 
  - bus use
  - overnight stay of bus bus driver
   Input: 
   - dist_dead: distance from/ back to depot, between trips in kilometers
   - time_dep: departure time of path in minutes
   - time_arr: arrival time of path in minutes
   - cost_km: cost per kilometer
   - dayrate
  
   
"""
import math

def calculate_costs(dist_dead, time_dep, time_arr,  bus_size=50, day_rate=504, cost_km=1.1):
  cost_dead= cost_km * dist_dead
  
  days=(time_arr-time_dep)/(24*60) #duration of path in days 
  rest_hr=(days-math.floor(days))*24 # time less than whole day in hours
  if 0 <= rest_hr < 4:
    cost_bus=(math.floor(days)+0.4*rest_hr)*day_rate
  if 4 <= rest_hr <10:
    cost_bus=(math.floor(days)+0.1*rest_hr)*day_rate
  if rest_hr >10:
    cost_bus=(math.floor(days)+1)*day_rate
  cost_night=math.floor(days)*75 #75€ per night
  cost=cost_night+cost_bus+cost_dead 
  
  return float("{0:.2f}".format(cost)) #round on two decimal places

