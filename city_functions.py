

def get_name(city_name, country_name,population=""):
    if population:
     a= f"{city_name}, {country_name} -{population}"
    else: 
     a= f"{city_name}, {country_name}"
    return a

class Employee:
  
  def __init__(self ,f_n,l_n , salary):
    self.f_n=f_n
    self.l_n=l_n
    self.salary=salary
  def give_raise(self,hike=5000):
    self.salary+=hike 



     
    