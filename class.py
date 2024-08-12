class car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def get_age(self):
        current_year=2023
        age=current_year - self.year
        return age
    def display_info(self):
        return f"{self.year}{self.make}{self.model}"
car1=car("toyota" ,"camry" ,2020)
print(car1.display_info())
print(f"car age: {car1.get_age()}years")