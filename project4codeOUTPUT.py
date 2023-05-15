import numpy as np
import matplotlib.pyplot as plt

# read in data from text file
# https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
# https://www.freecodecamp.org/news/the-string-strip-method-in-python-explained/
with open('output.txt', 'r') as f:
    lines = f.readlines()
    temperature = int(lines[0].split(':')[1].strip())
    pressure = int(lines[1].split(':')[1].strip())
    flow_rate = float(lines[2].split(':')[1].strip())
    monolayer_count = int(lines[3].split(':')[1].strip())
    bilayer_count = int(lines[4].split(':')[1].strip())
    multilayer_count = int(lines[5].split(':')[1].strip())

# create bar chart of graphene layer counts
layer_counts = [monolayer_count, bilayer_count, multilayer_count]
layers = ['Monolayer', 'Bilayer', 'Multilayer']
plt.bar(layers, layer_counts)
plt.title('Graphene Layer Counts')
plt.xlabel('Layer Type')
plt.ylabel('Count')
plt.show()

# create scatter plot of graphene distribution
data = np.genfromtxt('output.txt', delimiter='\t', skip_header=6)
x = data[:, 0]
y = data[:, 1]
plt.scatter(x, y)
plt.title('Graphene Distribution')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()






