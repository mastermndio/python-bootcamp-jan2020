class Animal():
    def __init__(self, name = "Beijing"):
        self.name = name

    def introduceMyself(self):
        print(f"Hello sirs and madammes, my name is {self.name}!")

class Kitty(Animal):
    def __init__(self, age):
        self.name = "Inside Child"
        self.age = age

    def introduceMyself(self):
        print(self.name)

    def introduceMyAge(self):
        print(self.age)


rex = Animal()
shadow = Kitty(567)

rex.introduceMyself()
shadow.introduceMyAge()
