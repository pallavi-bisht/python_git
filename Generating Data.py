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
