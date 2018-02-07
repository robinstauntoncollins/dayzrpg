from Being import Being

class Zombie(Being):
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def is_alive(self):
        return self.hp > 0

class Farmer(Zombie):
    def __init__(self):
        super().__init__(name"Farmer Zombie", hp = 12000, damage = 1000)

class Military(Zombie):
    def __init__(self):
        super().__init__(name"Military Zombie", hp = 15000, damage = 1200)

