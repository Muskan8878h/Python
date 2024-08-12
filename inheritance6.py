class Vehicle:
    pass
class car(Vehicle):
    pass
class Bicycle(Vehicle):
    pass
my_car=car()
my_bicycle=Bicycle()
print(isinstance(my_car ,car))
print(isinstance(my_bicycle ,car))
print(isinstance(my_bicycle ,Bicycle))
print(isinstance(my_car ,Vehicle))
print(isinstance(my_car ,(car,Vehicle)))