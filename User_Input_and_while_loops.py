message=input("Tell me something i will repeat after you.")
print(message)

Prompt="Tell me something i will repeat after you."
Prompt+="\nsomething interesting"
name =input(Prompt)
print(name)

#TIY 117

car= input('Which is your fav car\n')
print(f"\nlet me find you a {car}")

table=input("How many people are in your group?\t")
 
if int(table)>8:
    print("\nSorry you will have to wait!")
else:
    print("\nyour table is ready!!")     

number= input("Enter a number \t")

if int(number)%10==0:
    print("\nIts is a multiple of 10 .")
else:
    print("\nNot a multiple of 10")    

#TIY 123

prompt="Please enter your topping.\n"
prompt+="Type'quit'to end "

while True:
    i = input(prompt)
    if i =='quit':
      break
    else:
      print(f"\nAdding {i} to your Pizza")

prompt="\nPlease enter your age.\n"
prompt+="Type'quit'to end "

while True:
   age=input(prompt)
   if age =='quit':
      break
   elif int(age)<3:
      print("Ticket is free")
   elif int(age)>=3 and int(age) <12:
      print("Ticket is $10")
   elif int(age) >=12:
      print("Ticket is $15")
     
while 1==1: #infinite loop  hence use cntrl+c to close
   print(True) 

#TIY 127

sandwitch_orders=['Tuna','Veg','avacado','chicken']
finished_sandwitches=[] 
while sandwitch_orders:
    ready=sandwitch_orders.pop()
    print(f"\n I made your {ready} sandwitch!")
    finished_sandwitches.append(ready)
for i in finished_sandwitches:
   print(f"\n {i} sandwitch was made!")    


sandwitch_orders=['Tuna','pastrami','Veg','avacado','pastrami','chicken','pastrami' ]
finished_sandwitches=[] 
print('The Deli has run out of pastrami')
while 'pastrami' in sandwitch_orders:
   sandwitch_orders.remove('pastrami')
print(sandwitch_orders)




   
   
         

        



 
