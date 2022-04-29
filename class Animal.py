class Animal:
    def __init__(self, name):
       self.name = name
    def eat(self):
       print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self,name, breed):
        super().__init__( name)
        self.breed = breed
        print(f"Dog's name is a {self.name}, the breed is a {self.breed}")
    def bark(self):
        print(f"{self.name} is barking")
        


class Cat(Animal):
    def meow(self):
        print(f"Kitty {self.name} says meow!")


class Frog(Animal):
    def eat(self):
        print(f"Frog {self.name} is eating")

d = Dog("Bell", "Hound")
d.eat() 
d.bark()
c = Cat("Tom")
c.eat()
c.meow()
f = Frog("Freddy")
f.eat()
