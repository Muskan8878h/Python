class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
class cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"
dog1=Dog('Buddy')
cat1=cat("whisters")
print(dog1.speak())
print(cat1.speak())