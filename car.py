#Class car

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

        
if __name__ == "__main__":
    
    my_car = Car("Toyota", "Corolla", 2020)
    
    
    my_car.display_info()