from numpy import exp, array, random, dot, genfromtxt
from numpy.linalg import inv
import csv
inp_1 = genfromtxt('reverse_inp__out_CSV.csv', delimiter=',',usecols=(0,1,2))
out_1 = genfromtxt('reverse_inp__out_CSV.csv', delimiter=',',usecols=(3,4,5))

inp = []
weight = dot(dot(inv(dot(inp_1.transpose(),inp_1)),inp_1.transpose()),out_1)
for i in range (0,3):
        array = int(input('Enter an array of[[] [] []]: '))
        inp.append(array)
out = dot(inp,weight)
print (weight)
print (out)
