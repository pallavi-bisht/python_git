
from User import User
class admin(User):
    
    def __init__(self,f_name,l_name,age):
        super().__init__(f_name,l_name,age)
        self.priv=privileges()

class privileges:

    def __init__(self):
        self.privileges=["can reset post",'can delete post','can ban user']
    def show_prvileges(self):
        print("privileges are :\n")
        for i in self.privileges:
            print(f" {i}\n")  
