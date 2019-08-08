class Person:
    #Class Variables
    wage_rate=1.4
    counter=0
    def __init__(self,name,surname,salary,):#Constructor
        self.name=name
        self.surname=surname
        self.salary=salary
        self.mail=name+surname+"@outlook.com"
        Person.counter+=1 #Self.counter yapsaydık her nesnede 0 alıp 1 yazacaktı.Bu şekilde toplam person sayısını bulabilirim.....
    def giveNameSurname(self):
        return self.name + " " + self.surname
    def increaseWage(self):
        self.salary=int(self.salary*self.wage_rate)
#Self dışardan gelen parametreleri kullanmamızı sağlayan nesnedir.Her objenin selfi farklıdır
Person1=Person("metin","yorgun",5900)
print(Person1.giveNameSurname())
print("First Salary:",Person1.salary)   
Person1.increaseWage()
print("New Salary:",Person1.salary)
