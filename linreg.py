from scipy import stats
import numpy as np
import matplotlib.pyplot as plt 

#Function to make sure we read a float to user
def readFloat():
    while True: 
        try: 
            value = float(input())
            return value 
        except ValueError:
            print("Please enter a integer or decimal only: ")


#creating an empty list for our x and y axis
x = ([])
y = ([])

#Getting User inputs for our labels of the graph
title = str(input("Please enter the Title for the plot: "))
xLabel = str(input("Please enter label for x-axis: "))
yLabel = str(input("Please enter label for y-axis: "))

print("")


print("Enter number of elements in x-axis:", end = '')
#Use readFloat function to read number of elements and cast it to int
n = int(readFloat())

print("Enter elements into x-axis: ")
#Append each user input to x list for x-axis
for i in range(0, n):
    print("Entry " + str(i+1) + " of " + str(n) + ":", end = '')
    entry = readFloat()
    x.append(entry)

#numpy graphs must be in np.array and not a list, so here we have to cast it.
xAxis = np.array(x)

print("")

print("Enter elements into y-axis: ")
#Append each user input to y list for y-axis
for j in range(0, n):
    print("Entry " + str(j+1) + " of " + str(n) + ":", end = '')
    entry = readFloat()
    y.append(entry)

#numpy graphs must be in np.array and not a list, so here we have to cast it.
yAxis = np.array(y)

#Calculate our points of interest with scippy functions
slope = stats.linregress(xAxis, yAxis)[0]
std_err = stats.linregress(xAxis, yAxis)[4]
intercept = stats.linregress(xAxis, yAxis)[1]

print ("slope = ", slope)
print ("standard error of the slope = ", std_err)
print ("intercept = ", intercept)

#Calculate equation for our least-squares regression line.
fit = intercept + (int(slope) * xAxis)

#Use matplotlib plot function to plott our data
plt.plot(xAxis, yAxis, 'o')
plt.plot(xAxis, fit, 'k-')

#Add our user-generated labels and legend
plt.title(title)
plt.legend(['Measured data', 'Fit'], loc=0, prop={'size':15})
plt.xlabel(xLabel)
plt.ylabel(yLabel)

#Display the graph
plt.show()


