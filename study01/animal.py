class Animal:
    
    cryMessage = ""

    def cry(self):
        print(self.cryMessage)

class Cat(Animal):
    
    def __init__(self):
        self.cryMessage = "にゃー"


class Dog(Animal):

    def __init__(self):
        self.cryMessage = "わん！"

animal = Cat()
animal.cry()
animal = Dog()
animal.cry()