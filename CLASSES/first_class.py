class Car:
    def __init__(self, color, make, model, year, hp):
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.hp = hp


    def installMods(self):
        self.hp += 40
        print(self.hp)



class superCar(Car):
    pass

myCar = superCar("blue", "ford", "GT350", "67'", 306)

print(myCar.color)
