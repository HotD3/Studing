class Cls:
    def __init__(self,n ,m):
        self.n=n
        self.m=m
    def info(self):
        print(f"n:{self.n}, m:{self.m}")
Cls
p1= Cls('N',"M")
p2= Cls('N1',"M1")
p1.info()
p2.info()

#Есть объекты p1/p2 . По умолчанию их значения N,M/N1,M1. Нужно присвоить значение аргументов (через консоль) обьекту. 
