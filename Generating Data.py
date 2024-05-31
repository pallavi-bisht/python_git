import matplotlib.pyplot as plt

squares=[1,4,9,16,25,36,49,64,81,100]
fig,ax= plt.subplots()
ax.plot(squares,linewidth=3)
plt.show()

#TIY 311
import matplotlib.pyplot as plt

x_value= range(1,5001)
y_value= [x**3 for x  in x_value ]
plt.style.use('seaborn-v0_8')
fig,ax= plt.subplots()
ax.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,s=5)
ax.set_title("Cube Number")
#ax.axis([1,50001,1,130000000000])
#ax.plot(x_value,y_value)
plt.show()

#TIY319

import matplotlib.pyplot as plt
from Random_walk import Randomwalk

rw= Randomwalk(4000)
rw.fill_walk()

plt.style.use('classic')
fig,ax=plt.subplots()
pt=range(rw.number)
#ax.plot(rw.x_value,rw.y_value,linewidth=3)
ax.scatter(rw.x_value,rw.y_value,c=pt,cmap=plt.cm.Blues,s=15)
ax.set_aspect('equal')
plt.show()

#TIY 328
import plotly.express as px
from Dice import Die

# To Get Random Result
d= Die(8)
result=[]
i=1
while  i<=1000:
    value=d.roll()
    result.append(value)
    i+=1
print(result)  

#now to count Result

freq=[]

for i in range(1,d.n+1):
    x=result.count(i)
    freq.append(x)
print(freq)    

#plot on bar
fig= px.bar(x=range(1,d.n+1),y=freq)
fig.show()



