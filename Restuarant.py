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