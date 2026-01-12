class Hero:
    def __init__(self, name , hp , damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self):
        return f'{self.name} attacks with {self.damage} damage'
    def get_info(self):
        return f'Name:{self.name}, Hp:{self.hp}, Damage:{self.damage}'

class Warrior(Hero):
    def __init__(self, name , hp , damage, armor):
        super(Warrior , self).__init__(name , hp , damage)
        self.armor = armor

    def get_info(self):
        return f'Name:{self.name}, Hp:{self.hp},Damage:{self.damage},Armor:{self.armor}'
    def attack(self):
        return f'{self.name} attacks with {self.damage + 10 } damage'

class Mage(Hero):
    def __init__(self, name , hp , damage , mana):
        super(Mage, self).__init__(name , hp , damage)
        self.mana = mana

    def get_info(self):
        return f'Name:{self.name}, Hp:{self.hp},Damage:{self.damage},Mana:{self.mana}'
    
    def attack(self):
        return f'{self.name} casts a spell with  {self.damage * 2} damage'

heroes = [
    Warrior("Thor", 120, 20, 50),
    Mage("Gandalf", 80, 25, 100),
    Hero("Villager", 50, 5)
]

for hero in heroes:
    print(hero.get_info())