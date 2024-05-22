
alien_colors='green'

if alien_colors=='green':
    print("Player just earned 5 points!")
elif alien_colors!='green':
    print("Player just earned 10 points!")    
else:
    print("No color match !")

Fruit=['mango','watermellon','chikoo','apple']    

if 'mango' in Fruit:
    print('Mango is here !')
if 'watermellon' in Fruit :
    print("you like watermellon")  

for i in Fruit:
    print(i)
    
#Try it yourself page 88

users=['admin','pallavi','karan','shweta','varun']
#usee below code when  to chcek empty list
# users=[]

if users:
 for user in users:
  if user=='admin':
     print('hello admin would like to see status report!')
  else:
     print(f"Hello {user} Thak you for logging again.")
else: print("we need to find some users!")   


Current_users =['pallavi','kanch','diksha','varun','rohit']
Current_users_upper=[]
for j in Current_users:
  Current_users_upper.append(j.upper())

New_users=['diksha','gulnaar','kanch','Rohit']
for i in New_users:
   if i.upper() in Current_users_upper:
      print(f"{i} please enter new user name")
   else: 
      print(f"{i} username is avaialble!")
        
jkl=[i for i in range(1,10)]
print(jkl)

for i in jkl:
 if i==1:
  print("1st")
 elif  i==2:
  print("2nd")
 elif  i==3:
  print("3rd")
 else:
    print(f"{i}th")


     




