"""import pandas as pd

data = pd.read_csv('data.csv')
k=data.head(10)
print(k)

print(data.columns)

n=k.transpose()
print(n)

print(data.shape)

print(data.info())

print(data[0:10])
print(data[-10:])
print(data['city'][0:8])
print(data.iloc[1:3,4:6])

print(data.count(axis=1))
print(data.value_counts('city',normalize=True)*100)
print(data.city.value_counts())

new_data= pd.crosstab(data['city'],data['winner'])
new_data.to_csv('Analysis_1.csv')

print(data[['winner','city','win_by_runs']].sort_values('win_by_runs',ascending=False)[0:5])

data['Win_by']= data['win_by_runs']+data['win_by_wickets']
print(data)

# Self to add Win by column:
r= list(data['win_by_runs'])
w = list(data['win_by_wickets'])
wb=[]
for i in r:
    if i>0:
     wb.append('Win_by_Run')
    else:
     wb.append('Win_by_wickets')

data['win_by']=wb
print(data)
  

print(data.groupby(['winner','win_by'])['win_by_runs'].mean())     
print(data.groupby(['winner','win_by']).mean(['win_by_runs']))    #give all columns mean whete applicable

 """
   

#exercise pg60
"""
import pandas as pd
from datetime import datetime as dt
import math
import seaborn as sn
import matplotlib.pyplot as plt


Bolly_data=pd.read_csv('bollywood.csv')
print(Bolly_data.info())

print(Bolly_data.info())
print(Bolly_data.shape)

print(Bolly_data.value_counts('Genre',ascending=True))
print(Bolly_data.value_counts('Genre',ascending=False)[0:1])


k=pd.crosstab(Bolly_data['Genre'],Bolly_data['ReleaseTime'],dropna=False)
print(k)



Bolly_data['Mon_Release']=pd.DatetimeIndex(Bolly_data['Release Date']).month
print(Bolly_data['Mon_Release'])

print(Bolly_data.value_counts('Mon_Release'))


Bolly_data['Mon_Release']=pd.DatetimeIndex(Bolly_data['Release Date']).month
print(Bolly_data[Bolly_data['Budget']>=25].value_counts('Mon_Release')[0:1])

Bolly_data['ROI']= (Bolly_data['BoxOfficeCollection']-Bolly_data['Budget'])/Bolly_data['Budget']
#print(Bolly_data.sort_values(by='ROI',ascending=False)[['MovieName','ROI']][0:10])

print(Bolly_data.groupby(['ReleaseTime'])['ROI'].mean())


#plt.hist(x=Bolly_data['Budget'])
#sn.distplot(Bolly_data['Budget'])
Bolly_data['ROI']= (Bolly_data['BoxOfficeCollection']-Bolly_data['Budget'])/Bolly_data['Budget']
#sn.distplot(Bolly_data[Bolly_data['Genre'].str.strip()=='Drama']['ROI'],color='r',label='Drama')
#sn.distplot(Bolly_data[Bolly_data['Genre']=='Comedy']['ROI'],color='y',label='Comedy')
#sn.boxplot(x='Genre',y='ROI',data=Bolly_data)

plt.legend()

#plt.scatter(x='BoxOfficeCollection' , y='YoutubeLikes',data=Bolly_data,)
#sn.regplot(x='BoxOfficeCollection' , y='YoutubeLikes',data=Bolly_data,)
#sn.barplot(x='YoutubeLikes',y='Genre',data=Bolly_data)

#sn.pairplot(Bolly_data[['Budget','BoxOfficeCollection',	'YoutubeViews',	'YoutubeLikes',	'YoutubeDislikes']],dropna=False)
sn.heatmap(Bolly_data[['Budget','BoxOfficeCollection',
	'YoutubeViews',	'YoutubeLikes',	'YoutubeDislikes']].corr(),annot=True)
print(Bolly_data[['Budget','BoxOfficeCollection',
	'YoutubeViews',	'YoutubeLikes',	'YoutubeDislikes']].corr())
plt.show()
"""
#Exercise Pg 61

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

sa= pd.read_csv('SAheart.csv')
#print(sa.info())
"""sn.catplot(x='famhist',kind='count',hue='chd',data=sa)

sn.heatmap(sa[['age','sbp']].corr(),annot=True)


sn.distplot(sa[sa['chd']=='Si']['tobacco'],color='y',label='si')
sn.distplot(sa[sa['chd']=='No']['tobacco'],color='r',label='no')
plt.legend()

sn.heatmap(sa[['sbp','obesity','age',	'ldl']].corr(),annot=True)
plt.show()
"""
k=list(sa['age'])
m=[]
for j in k:
    if j in  range(0,15):
        m.append('young')
    elif j in  range(15,35):
        m.append('adults')
    elif j  in  range(35,55):
        m.append('mid')
    else:
        m.append('old')

sa['agegroup'] = m  
mn=sa[sa['chd']=='Si'][:]
#sn.catplot(x='agegroup',kind='count', data=mn,col_order='agegroup')
sn.boxplot(x='ldl',y='agegroup',data=sa)
plt.show()











