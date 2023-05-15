# PHSX815_Project4
The purpose of this code is to simualte the location of differnt graphene types grown on a substrate.

This program reads the data from the 'graphene_data.txt' file generated by Program 1, and plots the graphene points on a scatter plot with different colors for each layer category. The program reads the data from the 'graphene_data.txt' file using numpy's 'genfromtxt' function. This function automatically sorts the text file and stores the data in a numpy array. The program creates scatter plots for each layer category using the x and y coordinates from the corresponding data subset.

The configurable parameters influence the resulting graphene distribution, allowing for the investigation of various growth scenarios if desired.
