""" Contains path model
    Input: datafile .dat containing set of paths with following parameters:
    - cost per path, calculated separately
    - node sequence
    -set of trips with parameter:required seats per trip
    - set of depots
    - possible extensions: bus capacity, two drivers

    solution approach with SolverFactory for first try
"""

from pyomo.environ import *
from pyomo.opt import SolverFactory


#create a model
model = AbstractModel()

#Sets
#set of feasible paths
model.paths = Set()

model.depots = Set()  # set of depots 
model.trips = Set()  # set of trips 


#parameters
model.req_seats = Param(model.trips, within=NonNegativeIntegers)  #required seats per trip
model.costs = Param(model.paths, within=NonNegativeReals)  # costs per paths
model.node_seq = Param(model.paths)
#Variables
model.amount = Var(
    model.paths, domain=NonNegativeIntegers)  #amount of buses using a path
#constant, fixed bus capacity of 50 seats
bus_cap = 50 
#objective expression
def obj_expression(model):
  return sum(model.costs[i] * model.amount[i] for i in model.paths)
model.OBJ = Objective(rule=obj_expression)

#constraints
#minimum number of seats per trip
def minSeatRule(model, trip):
	return  sum(bus_cap *model.amount[i] for i in model.paths) >= model.req_seats[trip]


model.seatConstraint = Constraint(
    model.trips, rule=minSeatRule)  #constraint for each trip

