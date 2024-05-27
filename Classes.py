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

#TIY 166

class Restaurant:
    
    def __init__(self,rest_name,rest_cuisine):
        self.rest_name=rest_name
        self.rest_cuisine=rest_cuisine
        self.number_served=0

    def describe_rest(self):
        print(f"Restaurant name: {self.rest_name}\n")
        print(f"Cusisine name: {self.rest_cuisine}\n")
        print(f"Number of cusine served {self.number_served}.\n")
    
    def set_number_served(self,number_served):
        self.number_served=number_served
    
    def increment_number_served(self,number_served):
        self.number_served+=number_served


abc= Restaurant("SALT",'North Indian') 
abc.describe_rest()
abc.number_served=20
abc.describe_rest()
abc.set_number_served(18)
abc.describe_rest()
abc.increment_number_served(30)
abc.describe_rest()


class User:

    def __init__(self,f_name,l_name):
        self.f_name=f_name
        self.l_name=l_name
        self.loggin_attempt=0
    
    def  describe_user(self):

        print(f"User's Name is {self.f_name} {self.l_name} and attemt is  {self.loggin_attempt}")
    
    def increment_attempt(self): 
        self.loggin_attempt=self.loggin_attempt+1

    def  reset_attempt(self):
        self.loggin_attempt=0    

pqr=User('pallavi','Bisht')
pqr.describe_user()
pqr.increment_attempt()
pqr.describe_user()
pqr.increment_attempt()
pqr.describe_user()
pqr.increment_attempt()
pqr.describe_user()
pqr.reset_attempt()
pqr.describe_user()

#TIY 173

class Restaurant:
    
    def __init__(self,rest_name,rest_cuisine):
        self.rest_name=rest_name
        self.rest_cuisine=rest_cuisine

    def describe_rest(self):
        print(f"Restaurant name: {self.rest_name}\n")
        print(f"Cusisine name: {self.rest_cuisine}\n")
    
    def open_rest(self):
        print(f"Restaurant {self.rest_name} is open!\n")


class IceCreamStand(Restaurant):

    def __init__(self,rest_name,rest_cuisine):
        super().__init__(rest_name,rest_cuisine)
        self.flavour=['vanilla','chocolate','pista']
    def display_flavor(self):
        for i in self.flavour:
            print(f"{i}\n")

lmn=IceCreamStand('Piggy','Ice Cream')
lmn.display_flavor()

# Instance as attribute 

class User:

    def __init__(self,f_name,l_name,age):
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
    
    def  describe_user(self):

        print(f"User's Name is {self.f_name} {self.l_name} and age is {self.age}")

    def greet_user(self):

        print(f"Welcome {self.f_name} {self.l_name} !") 

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

fgh=admin('Arvind','bisht',20)    
fgh.priv.show_prvileges() 




class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size!=65:
            self.battery_size=65


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()

 #TIY 179  
from Restuarant import Restaurant as R

ghi= R('Google','fried')
ghi.describe_rest()

#from User import User
from admin_privileges import admin as a,privileges as p

dfg=a('Hari','sharma',30)
dfg.describe_user()
dfg.priv.show_prvileges()






            

