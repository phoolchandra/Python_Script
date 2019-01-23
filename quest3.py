import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from matplotlib.ticker import FormatStrFormatter



csv_file = open('out1.txt','r')

b = csv_file.readlines()
csv_file.close()
n = len(b)
print(n)
xax = []
yax = []
count = 0
for line in b:
    line = line.split(' ')
    line = line[-2].split('=')
    xax.append(float(line[-1]))
plt.xlabel('Latency')
plt.ylabel('Frequency')
plt.title('Bargraph latency vs frequenciec',color="red")

ya =[]
ya.append([])
ya.append([])
k=0
for i in range (n):
    k=1
    for j in range (i+1,n):
        if (xax[i] == xax[j]):
            k = k+1
            # print(xaxis[i],end=' ')
            # print(xaxis[j],end=' ')
            xax[j]=-1
            # print(k)
    if (xax[i] >= float(0)):
        ya[0].append((xax[i]))
        ya[1].append(k)
        

plt.bar(ya[0],ya[1],width=0.01,color =['green'])
# plt.xscale("log",basex=10,subsx = [0,1,2,3,4])
plt.xlim(0.1,2.4)
plt.xticks(np.arange(0.1, 2.4,0.1))
plt.yticks(np.arange(0, 35, 2))
plt.show()
