from random import choice

class Randomwalk:

    def __init__(self,number=5000):
        self.x_value=[0]
        self.y_value=[0]
        self.number=number


    def get_step(self):
        
            dir= choice([1,-1])
            dist= choice([0,1,2,3,4])
            step= dir*dist
            return step

    def fill_walk(self):

        while len(self.x_value)<self.number:

          x_step=self.get_step()
          y_step=self.get_step()
          if x_step==0 and y_step==0:
             continue
          x=self.x_value[-1]+ x_step
          y=self.y_value[-1]+ y_step
          self.x_value.append(x)
          self.y_value.append(y)

   

             

        
    
