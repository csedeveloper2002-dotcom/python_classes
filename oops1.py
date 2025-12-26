class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(self.brand, self.model, "is starting")

    def stop(self):
        print(self.brand, self.model, "is stopping")


car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2021)

car1.start()
car1.stop()

car2.start()
car2.stop()
