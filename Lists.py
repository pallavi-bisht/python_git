abc=[1,2,3,"sing"]
print(abc)
print(abc[1])
print(abc[-1])

#add
abc.append('pallavi')
print(abc)

#delete  by position
abc=[1,2,3,"sing"]
pop_abc=abc.pop(0)
print(f"{abc} {pop_abc}")

#delete by value
abc=[1,2,3,"sing"]
abc.remove("sing")
print(abc)

#legnth of list
abc=[2,4,1,7]
print(len(abc))

#sort method ,sorted function,reverse method

abc=[2,4,1,7]
abc.sort()
print(abc)
klm=[8,33,45,2]
print(sorted(klm))
abc=[2,4,1,7]
abc.reverse()
print(abc)

#looping
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(f" {magician.title()},that was a great trick!\n")

print('hello')

#Range & simple statistic function
#1
pal=[]
for i in range(0,100,5):
   pal.append(i)

print(pal)
print(min(pal))
print(max(pal))
print(sum(pal))

#2  code in one line 
pal=[i**2 for i in range(1,11)]
print(pal)

pal=[i for i in range(0,100,5)]
print(pal)

#TRy it your self
kcb=[]
for i in range(0,20):
 kcb.append(i+1)
 print(kcb[i])

kcb=[i for i in range(1,1000001)]
print(kcb)  
for j in range(1,len(kcb)):
  print(j)

pqr=[]  
pqr=[i for i in range(1,1000001)]

print(max(pqr))
print(min(pqr))
print(sum(pqr))

cube=[i**3 for i in range(1,11)]
for i in range(0,10):
 print(cube[i])







 



 









