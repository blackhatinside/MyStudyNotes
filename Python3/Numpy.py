# NUMPY INTRO

#!pip install numpy
import numpy as np
print(np.__version__)

# PYTHON LIST TO NUMPY ARRAY

pylist = [2, 4, 6, 8] 
pyarray = np.array(pylist)
print(type(pylist))
print(type(pyarray))

# NUMPY ATTRIBUTES 

pyarray1 = np.array(((1, 2, 3), (4, 5, 6)))
print(pyarray1)
print(pyarray1.dtype)         #datatype of the elements in the array
print(pyarray1.shape)         #shape of the array in terms of rows & columns
print(pyarray1.ndim)          #number of dimensions in the array
print(pyarray1.itemsize)      #size of each item in the array in bytes
print(pyarray1.reshape(3,2))  #change the dimensions of the array

# NUMPY ARRAY CREATION ROUTINES

pyarray2 = np.empty([2,2], dtype = int, order = 'C')
print(pyarray2)
pyarray3 = np.zeros([2,3], dtype = int, order = 'C')
print(pyarray3)
pyarray4 = np.ones([3,2], dtype = int, order = 'C')
print(pyarray4)
nparrmat = np.random.rand(2,2)
print(nparrmat)

# ARRAY INDEXING AND SLICING

pyarray5 = np.arange(1,10,2,dtype=float)	      #PRINT RANGE OF ODD FLOATING VALUES FROM 1 to 9
print(pyarray5)
pyarray5 = np.linspace(0,10,5)		              #TO PRINT 5 NUMBERS FROM(INCLUDING) 0-10 JUMPING EQUAL STEPS 
print(pyarray5)
pyarray5 = np.linspace(1,11,5,endpoint=False)		#TO PRINT EQUAL STEPPED NOS. WITHOUT ENDPOINT VALUE CONDITION
print(pyarray5)
pyarray5 = np.linspace(1,21,10,retstep=True)		#TO ALSO PRINT THE STEP VALUE
print(pyarray5)
print("#----------------------#")
pyarray6 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
pyarray6 = np.array(pyarray6)
print(pyarray6[5])		      #PRINT AN ELEMENT
print(pyarray6[[3,6,9]])		#PRINT MULTIPLE ELEMENTS
print(pyarray6[::-1])		   	#PRINT IN REVERSE
print(pyarray6[0:10:3])			#PRINT FROM START TO STOP BY SKIPPING

# NUMPY MATHEMATICAL FUNCTIONS

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(np.add(a,b))			#TO ADD a AND b 
print(np.subtract(b,a))	#TO SUBTRACT a FROM b
print(np.multiply(a,b))	#TO MULTIPLY a WITH b
print(np.divide(b,a))		#TO DIVIDE b BY a
print(np.power(a,2))		#TO FIND a TO THE POWER 2
c = np.array([[1,2],[3,4]])
d = np.array([[11,12],[13,14]])
print(np.dot(c,d))			#TO FIND DOT PRODUCT OF c AND d
print(np.matmul(c,d))		#TO FIND MATRIX PRODUCT OF c AND d
print(np.vdot(c,d))			#TO FIND VECTOR PRODUCT OF c AND d
print(np.inner(c,d))		#TO FIND INNER OF c AND d
print(np.linalg.det(c))	#TO FIND DETERMINANT OF c
print(np.linalg.inv(d)) #TO FIND INVERSE OF d

# NUMPY STATISTICAL FUNCTIONS

pyarray7 = np.array([[1,2,3,4],[5,6,7,8]])
print(np.max(pyarray7))			 #TO FIND MAX VALUE 
print(np.min(pyarray7))			 #TO FIND MIN VALUE
print(np.average(pyarray7))  #TO FIND AVERAGE VALUE
print(np.mean(pyarray7))		 #TO FIND MEAN VALUE
print(np.median(pyarray7))	 #TO FIND MEDIAN VALUE
print(np.std(pyarray7))			 #TO FIND STANDARD DEVIATION
print(np.var(pyarray7))			 #TO FIND VARIANCE
print(np.corrcoef(pyarray7)) #TO FIND CORRELATION COEFFICIENT

# NUMPY MINI PROJECT - Static sine and cosine graphs

import numpy as np 
import matplotlib.pyplot as plt  
# Compute the x and y coordinates for points on sine and cosine curves 
x = np.arange(0, 3 * np.pi, 0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
# Set up a subplot grid that has height 2 and width 1, 
# and set the first such subplot as active. 
#using matplotlib
plt.subplot(2, 1, 1) 
# Make the first plot 
plt.plot(x, y_sin) 
plt.title('Sine')  
# Set the second subplot as active, and make the second plot. 
#using matplotlib
plt.subplot(2, 1, 2) 
plt.plot(x, y_cos) 
plt.title('Cosine')  
# Show the figure. 
plt.show()

# NUMPY MINI PROJECT - Solving Linear Equations
'''
Systems of linear equations can be solved with arrays and NumPy. A system of linear equations is shown below:
8x+3y−2z=9
−4x+7y+5z=15
3x+4y−12z=35
'''

import numpy as np
A = np.array([[8, 3, -2], [-4, 7, 5], [3, 4, -12]])
B = np.array([9, 15, 35])
x = np.linalg.solve(A, B)
print(x)                    # X = x[0]  Y = x[1]  Z = x[2]
Ainv = np.linalg.inv(A)
print(np.matmul(Ainv,B))    #A * X = B ===> A^-1 * B = X

# Animated Sine wave

from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation 
# initializing a figure in 
# which the graph will be plotted 
fig = plt.figure() 
# marking the x-axis and y-axis 
axis = plt.axes(xlim =(0, 4), 
				ylim =(-2, 2)) 
# initializing a line variable 
line, = axis.plot([], [], lw = 3) 
# data which the line will contain (x, y) 
def init(): 
	line.set_data([], []) 
	return line
def animate(i): 
	x = np.linspace(0, 4, 1000) 
	# plots a sine graph 
	y = np.sin(2 * np.pi * (x - 0.01 * i)) 
	line.set_data(x, y) 
	return line, 
# calling the animation function      
anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 20, blit = True)  
# saves the animation in our desktop 
anim.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30)

# NUMPY MINI PROJECT - Histogram

from matplotlib import pyplot as plt 
import numpy as np
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(a, bins = [0,20,40,60,80,100])
plt.title("histogram")
plt.show()

# NUMPY MINI PROJECT - Bar Graph

from matplotlib import pyplot as plt 
x = [5,8,10] 
y = [12,16,6]  
x2 = [6,9,11] 
y2 = [6,15,7] 
plt.bar(x, y, align = 'center') 
plt.bar(x2, y2, color = 'g', align = 'center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis') 
plt.show()
