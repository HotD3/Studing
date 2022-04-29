class Animal:
    def __init__(self, name):
       self.name = name
    def eat():
       print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self,name, breed):
        Animal.__init__(self, name)
        self.breed = breed
        print(f"Sobaka porodi: {self.breed} i imeni :{self.name} sozdama")
        


#class Cat(Animal):



#class Frog(Animal):


d = Dog("Sobaka", "Dog")
d.eat() #не вызывается функция eat