#defining Tuple 
# Tuple are list which are immutable
Menu=('Roti','Sabji','Rice','dal','sweet')
for i in Menu:
 print(i)

# can't change value of tuple
Menu=('Roti','Sabji','Rice','dal','sweet')
Menu[4]='cream'

# Reassign tuple compltetely
Menu=('Roti','Sabji','Rice','dal','sweet')
print(Menu)

Menu=('Roti','Sabji',1)
for i in Menu:
 print(i)




