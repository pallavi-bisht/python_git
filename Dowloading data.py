from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path=Path("Weather/weather_2024.csv")
line =path.read_text(encoding='utf-8').splitlines()

reader=csv.reader(line)
header=next(reader)
print(header)
for i , ch in enumerate(header):
    print(i,ch)

prcp,snwd,date=[],[],[]

for row in reader:
   try:
      high=(row[6])
      low=(row[10])
      dt= row[5]
      
   except ValueError:
    print(f"Error in date {row[5]}")
   
   else:
    prcp.append(high)
    snwd.append(low)
    date.append(dt)

print(prcp,snwd,date)
plt.style.use("seaborn-v0_8")
fig, ax=plt.subplots()
ax.plot(date,prcp)
ax.plot(date,snwd)
plt.show()   


#TIY 342

from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


path=Path('Weather/sitka_weather_2021_full.csv')
path2=Path('Weather/death_valley_2021_full.csv')
lines=path.read_text().splitlines()
lines2 =path2.read_text().splitlines()

reader=csv.reader(lines)
reader2=csv.reader(lines2)
head=next(reader)
head2=next(reader2)

for i,j in enumerate(head):
  print(i,j)
for i,j in enumerate(head2):
  print(i,j)  


date,prcp,date2,prcp2=[],[],[],[]
for row in reader:
  d=datetime.strptime(row[2],'%Y-%m-%d')
  prp=row[5]
  date.append(d)
  prcp.append(prp)

for row2 in reader2:
  d2=datetime.strptime(row2[2],'%Y-%m-%d')
  prp2=row2[3]
  date2.append(d2)
  prcp2.append(prp2)


#print(date,prcp)
plt.style.use("seaborn-v0_8")
fig,ax=plt.subplots()
ax.plot(date,prcp)
ax.plot(date2,prcp2)
plt.show()

#TIY 352

from pathlib import Path 
import json
import plotly.express as px

path=Path('Weather/eq_data_1_day_m1.geojson')
content =path.read_text(encoding='utf-8')
all_data= json.loads(content)

path= Path('Weather/NeW_file.geojson')
k= json.dumps(all_data,indent=4)
path.write_text(k)



all_dict=all_data["features"]


long,lats,mag,title=[],[],[],[]

for i in all_dict :
  mag.append(i['properties']['mag'])
  title.append(i['properties']['title'])
  long.append(i['geometry']['coordinates'][0])
  lats.append(i['geometry']['coordinates'][1])


fig=px.scatter_geo(lat=lats,lon=long,size=mag,projection='natural earth',color=mag,hover_name=title,labels={'color':'Magnitude'})
fig.show()