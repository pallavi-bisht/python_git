import pandas as pd

data = pd.read_csv('data.csv')
k=data.head(10)
"""print(k)

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
   

