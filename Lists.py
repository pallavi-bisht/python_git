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

# slicing
cube=[i**3 for i in range(1,11)]
print(cube)
print(cube[:3] ) #top3
print(cube[-3:]) #last3
print(cube[2:4]) #between 2,4 , 2 inclusive
print(cube[::2]) # valune in every 2 place

#looping in slice
cube=[i**3 for i in range(1,11)]
print(cube)
for i in cube[1:6]:
  print(i*10)

#copying List

#1 with keeing two indpendent list then use slice 
cube=[i**3 for i in range(1,11)]
copy_cube=cube[::3]
print(copy_cube)
 
#2 copied list will poin to same reference and if change made to to one 
#list it will automatically change the copied cube

cube=[i**3 for i in range(1,11)]
copy_cube=cube
print (copy_cube)
cube.append(29)
print(copy_cube)


#TRy it yourself page 65
cube=[i**3 for i in range(1,11)]
print(cube)
print(f"the first 3 item in the list are {cube[:3]}")
print(f"the last 3 item in the list are {cube[-3:]}")
a= (len(cube)/2)-1
b=(len(cube)/2)+2
print (f"{a,b}")
print(f"the middle 3 item in the lis are {cube[int(a):int(b)]}")
















 



 








