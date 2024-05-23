response={}
prompt1="What is you name.\n"
prompt2="what is favourite destination?\n "

while True:
    name=input(prompt1)
    place=input(prompt2)
    response[name]=place
    ans=input("Do you want to quit! (y/n)")
    if ans=='y':
      break
      
print(response)