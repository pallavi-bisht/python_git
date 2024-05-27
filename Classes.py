#TIY 162

class Restaurant:
    
    def __init__(self,rest_name,rest_cuisine):
        self.rest_name=rest_name
        self.rest_cuisine=rest_cuisine

    def describe_rest(self):
        print(f"Restaurant name: {self.rest_name}\n")
        print(f"Cusisine name: {self.rest_cuisine}\n")
    
    def open_rest(self):
        print(f"Restaurant {self.rest_name} is open!\n")


abc= Restaurant("SALT",'North Indian') 
abc.describe_rest()
abc.open_rest()


class User:

    def __init__(self,f_name,l_name,age):
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
    
    def  describe_user(self):

        print(f"User's Name is {self.f_name} {self.l_name} and age is {self.age}")

    def greet_user(self):

        print(f"Welcome {self.f_name} {self.l_name} !")    

pqr=User('pallavi','Bisht','30')
pqr.describe_user()
pqr.greet_user()






            

