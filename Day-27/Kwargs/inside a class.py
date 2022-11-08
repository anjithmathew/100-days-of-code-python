class Car:
    def __init__(self,**kargs):
        self.model = kargs["model"]
        self.name = kargs["name"]
         #or no error error 
        self.model = kargs.get("model")
        self.name = kargs.get("name")

my_car = Car(model ="nissan",name = "sunny")

print(my_car.model)
