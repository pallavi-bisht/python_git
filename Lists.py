abc=[1,2,3,"sing"]
print(abc)
print(abc[1])
print(abc[-1])

#add
abc.append('pallavi')
print(abc)

#del statment
abc=[1,2,3,"sing"]
del abc[0]
print(abc)

#delete  by position
abc=[1,2,3,"sing"]
pop_abc=abc.pop(0)
print(f"{abc} {pop_abc}")

#delete by value
abc=[1,2,3,"sing","sing"]
abc.remove("sing")# remove only 1st occurence of sing
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


# try it yourself pg41

guest=['Kohli','Virat','Thor','sharukh']
k= guest.index('Kohli')
for i in guest:
  print(f"{i} welcome to my Party!!")

print(f"\n{guest[k]}  couldn't make it!!\n") 

guest.remove('Kohli')
guest.insert(k,"karan")
for i in guest:
  print(f"{i} welcome to my Party!!\n")

print("We have found a new bigger table!\n")  

guest.insert(0,'Diksha')
guest.insert(int(len(guest)/2),'Varun')
guest.append('shweta')

for i in guest:
  print(f"{i} welcome to my Party!!")

print("\n Sorry I can invite only 2 people\n") 

for i in range(0,len(guest)):
  if len(guest)>2:
   name= guest.pop()
   print(f"{name},sorry your have to leave!\n")

for i in guest:
  print(f"{i} You are still invited to my Party!!")

del guest[0:2]
print(guest)
   
#TRy yourself pg 45

Dest=['Switzerland','Italy','Amalfi','Goa','Garhwal']
print(Dest)
print(sorted(Dest))
print(Dest)  #no modification to original list
print(sorted(Dest,reverse=True))
print(Dest)  
Dest.reverse()
print(Dest)
Dest.reverse()
print(Dest) #back to original list
Dest.sort()
print(Dest)
Dest.sort(reverse=True)
print(Dest)

guest=['Kohli','Virat','Thor','sharukh']
print(f"Iam inviting {len(guest)} guests today.")


#TRy it yourself page



  

















 



 









