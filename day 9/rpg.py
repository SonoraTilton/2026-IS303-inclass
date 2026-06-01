class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def attack(self):
        return f"{self.name} attacks!"
    
    def __str__(self):
        return f"{self.name} (HP:{self.hp})"
    
class Warrior(Character):
    def __init__(self, name, hp, armor):
        super().__init__(name, hp)
        self.armor = armor

    def attack(self):
        return f"{self.name} swings sword!"
    
    def __str__(self):
        base = super().__str__()
        return f"{base} [Armor:{self.armor}]"
    
class Mage(Character):
    def __init__(self, name, hp, mana=30):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self):
        self.mana -= 5
        return f"{self.name} casts spell!"
    
    def __str__(self):
        base = super().__str__()
        return f"{base} [Mana:{self.mana}]"

class Healer(Character):
    def __init__(self, name, hp, heal_power):
        super().__init__(name, hp)
        self.heal_power = heal_power

    def attack(self):
        return f"{self.name} heals allies!"
    
    def __str__(self):
        base = super().__str__()
        return f"{base} [Healing Power:{self.heal_power}]"
    
party = {
    Character("Villager", 50),
    Warrior("Aragorn", 120, 25),
    Mage("Gandalf", 80, 100),
    Healer("Elrond", 90, 40)
}

for hero in party:
    print(hero)
    print(hero.attack())