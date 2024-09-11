from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
import sys 
sys.argv 

with open('in.0', 'r') as file: 
    data=file.read()

print(data)

# using the empty list to store x and y values in in.0.txt 
x_data = []
y_data = []

#opening the file in read mode. reading a single line from a file and then remove any leading and trailing whitespaces
with open('in.0', 'r') as file: 
    header = file.readline().strip()
    
    #reading the remainding of the X anad Y values 
    for line in file: 
        x, y = map(int, line.strip().split(','))
        
        #adding on those x_data and y_data values to the list 
        x_data.append(x)
        y_data.append(y)

#using the matplotlib to plot 
plt.plot(x_data, y_data, marker = 'o', linestyle = '-', color = 'b')

plt.savefig('out0.60.png')
plt.show()
