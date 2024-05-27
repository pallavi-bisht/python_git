class User:

    def __init__(self,f_name,l_name,age):
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
    
    def  describe_user(self):

        print(f"User's Name is {self.f_name} {self.l_name} and age is {self.age}")

    def greet_user(self):

        print(f"Welcome {self.f_name} {self.l_name} !") 
