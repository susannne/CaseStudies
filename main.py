from pyomo.environ import *
from pyomo.opt import SolverFactory
from datafile import read_excel
from model import model

#creates model instance, still error when using solver

trips = []
trips = read_excel("/home/runner/case_studies_trips_09-10_2017.xlsx", "Blatt1")

# Create model object

solver = SolverFactory()
instance = model.create_instance("/home/runner/paths.dat")
instance.pprint()
results = solver.solve(instance)
instance.display()

