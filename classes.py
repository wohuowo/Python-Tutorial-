#a class is a user defined blueprint or prototype from which objects are created. Classes provide a means of bundling data
#and functionality together. creating a new class creates a new type of object, allowing new instances of that type to be made
#methods are function unique to objects
#instances creating new objects
#child and parent classes

class  Vehicle():#parent
    def __init__(self, name,  fuel,  size):#constructor method
        self.name = name
        self.fuel = fuel
        self.size = size
    def car_ability (self, speed):#method each class has one and theyre unique
        self.speed = 20
        print("This is automatic speed of vehicle ", self.speed)
 #subclass / child class
        #truck inherits methods from vehicles
class Truck(Vehicle):
    def __init__(self , name, truck):
        self.truck = truck
        self.name = name
        print("Name of the truck", self.name)
        print("Color of truck", self.truck)
   #overwriting car ability
    def car_ability(self):
        print("This is me overwriting the main class!")


h = Truck("Truck", "Blue")
print(h.car_ability())
#we use classes to define specific objects
