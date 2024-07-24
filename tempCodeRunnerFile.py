

import random
pqr=[]  
pqr=[i for i in range(1,1000001)]

print(max(pqr))
print(min(pqr))
print(sum(pqr))

x= random.choices(pqr,k=4)
print(x)