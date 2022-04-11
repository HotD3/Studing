import datetime as DT
running = True
date=input('Enter the date:')           #ввод текущей даты
date1=DT.datetime.strptime(date, '%d/%m/%y').date()   
today = DT.datetime.today()  #текущая дата
timedelta=date1-today  #здесь должна вычисляться дельта. в данном случае возраст.
print("{}-{}-{}".format(today.year, today.month, today.day))
timedelta=today - date1
print(timedelta)
#print(date1)
#y1= int(input('Enter ur age of birth:'))
#y2= int(input('Enter current age:'))
class Person:
    def print_info (self, n):
        for i in range(n):
            print(f"Name: {self.name}, Surname: {self.surname}, Where from: {self.Country}, Birth: {self.birth}, How_old: {self.old}")

p1 = Person()
p1.name = "Artur"
p1.surname = "Bugil"
p1.Country = "Ukraine"
p1.birth = "1995"
p1.old = date1
#p1.old = 27
#p1.old = y2-y1
p1.print_info(1)
print(p1.old)
#print(now)
#while running:
 #   if y1<y2:
  #      print ('Correct')
   #     running = False
    #else:
     #   print('Date is not correct')
      #  running = False
        
        
   


2
#нужно узнать, сколько лет, имея дату рождения и текущуюб дату +
#сделать повторный ввод даты, если условие не выполняетс -