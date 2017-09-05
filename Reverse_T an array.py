#Reverse the given array:
#***********************
from numpy import array, dot
from numpy.linalg import inv
inp = []
out = []
train_inp = array([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1],[1,1,1],[2,2,2],[3,3,3]])
train_out = array([[3,2,1],[2,3,1],[3,1,2],[1,3,2],[2,1,3],[1,2,3],[1,1,1],[2,2,2],[3,3,3]])
weight = dot(dot(inv(dot(train_inp.transpose(),train_inp)),train_inp.transpose()),train_out)
for i in range (0,3):
        array = int(input('Enter an array of[[],[],[]]: '))
        inp.append(array)        
print ("Input array: ",inp)
out = dot(inp,weight)
print ("Output array: ",out)

#*****************
#input: 35, 36, 37
#ouput: 37, 36, 35
#*****************
