
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
     




