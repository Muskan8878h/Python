class vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        return f"make:{self.year}, model:{self.make}, year:{self.model}"
class car(vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors=num_doors
    def display_info(self):
        return f"car-{super().display_info()}, number of doors:{self.num_doors}"
class Motorcycle(vehicle):
    def __init__(self,make,model,year,engine_type):
        super().__init__(make,model,year)
        self.engine_type=engine_type
    def display_info(self):
        return f"Motorcycle-{super().display_info()},Engine Type:{self.engine_type}"
car1=car("Toyota","canry",2022,4)
motorcycle1=Motorcycle("Harley-Daridson","sportster",2021,"V-turn")
print(car1.display_info())
print(motorcycle1.display_info())