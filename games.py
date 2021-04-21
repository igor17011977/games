import random

def vibor(n):
    a = random.choice([1,2,3])
    if person2.health<35 and n=="Человек":
        print ("Здоровье компьютера меньше 35 шанс на ваш промах и его исцеление увеличен")
        a = random.choice([2,3])
    z = 0
    if a==1:
        z=random.randrange(10,35)
        z*=-1
    if a==2:
        z = random.randrange(10,15)
        z *= -1
    if a==3:
        z = random.randrange(18,25)
    return (z,a)

class Person:
    def __init__(self, name):
        self.name = name  # устанавливаем имя
        self.health=100
    def shut(self,cv,a1):
        self.health+=cv
        if self.health>100:self.health=100
        if self.health < 0: self.health = 0
        if cv<0:
            print(self.name+"y нанесен урон",cv, "едениц здоровья")
        else:

            print("Промах",self.name, " востанови", cv, "едениц здоровья")
        if self.health<=0:
            print ("!!!!!!!!!!!!!!", self.name, "ПРОИГРАЛ !!!!!!!!!!!!!!!")

person1 = Person("Человек")
person2= Person("Компьютер")

while person1.health >0 and person2.health>0: #Цикл пока здоровье одного из участников не будет равно 0
    name=random.choice(["Человек","Компьютер"])
    print("-----------ХОД ",name+"а-------------")
    cv, a1 = vibor(str(name))
    if name=="Человек":
        person2.shut(cv, a1)
    else:
        person1.shut(cv, a1)
    print("У Компьютера осталось здоровья=", person2.health)
    print("У Человека осталось здоровье=", person1.health)