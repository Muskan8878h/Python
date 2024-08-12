class MyCustonClass(object):
    def __init__(self,value):
        self.value=value
    def display(self):
        print("value:", self.value)
obj = MyCustonClass(42)
obj.display()
print(isinstance(obj,object))