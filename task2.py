import random 

class Warrior:

    def __init__(self, n):
        self.name = n
        self.hp = 100
    
    def attack(self):
        self.hp = self.hp - 20

unit1 = Warrior("Unit 1")
unit2 = Warrior("Unit 2")

while(1):
    if(unit1.hp <= 0 or unit2.hp <= 0):
        break        
    else:
        rand = random.randint(1, 2)
        if(rand == 1):
            unit2.attack()
            print(unit1.name,"(",unit1.hp,")", "⟹  ", unit2.name,"(",unit2.hp,")") 
        else:            
            unit1.attack()
            print(unit1.name,"(",unit1.hp,")", "⟸  ", unit2.name,"(",unit2.hp,")") 
