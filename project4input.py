import numpy as np
import matplotlib.pyplot as plt
import random

# configurable parameters
temperature = 900 # in Kelvin
pressure = 750
flow_rate = 0.4 # in standard cubic centimeters per minute (sccm)

# simulate chemical vapor deposition process
# https://www.geeksforgeeks.org/numpy-random-randn-python/
x = np.random.rand(500) # random distribution of graphene
y = np.random.rand(500)

#https://geo-python.github.io/site/notebooks/L3/conditional-statements.html
# set parameter boundaries
if temperature > 100:
    x *= 2
if pressure > 1000:
    y *= 2
if flow_rate > 0.3:
    x /= 1
    y /= 1

# simulate characterization of the graphene
monolayer = []
bilayer = []
multilayer = []
 # https://stackoverflow.com/questions/477486/how-do-i-use-a-decimal-step-value-for-range
for i in range(len(x)):
    if 0 <= x[i] <= 0.25: # or 0.4 <= x[i] <= 0.44 or 0.58 <= x[i] <= 0.7:
        monolayer.append([x[i], y[i]])
    elif 0.25 <= x[i] <= 0.45: # or 0.46 <= x[i] <= 0.5 or 0.9 <= x[i] <= 0.93:
        bilayer.append([x[i], y[i]])
 #   elif 0.1 <= x[i] <= 0.15 or 0.49 <= x[i] <= 0.58:
    #or 0.75 <= x[i] <= 1:
 #       multilayer.append([x[i], y[i]])
    else:
         multilayer.append([x[i], y[i]])
# write to text file
with open('4output.txt', 'w') as f:
    f.write(f"Temperature: {temperature} \n")
    f.write(f"Pressure: {pressure} \n")
    f.write(f"Flow rate: {flow_rate} \n")
    f.write(f"Monolayer: {len(monolayer)}\n")
    f.write(f"Bilayer: {len(bilayer)}\n")
    f.write(f"Multilayer: {len(multilayer)}\n")
