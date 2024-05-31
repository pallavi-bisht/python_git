
from random import randint

class Die:

    def __init__(self,n=6):
        self.n=n

    def roll(self):
      return randint(1,self.n)  
      
         
        