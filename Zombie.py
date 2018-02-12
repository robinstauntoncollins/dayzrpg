class Zombie(object):
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def is_alive(self):
        return self.hp > 0


class Farmer(Zombie):
    def __init__(self):
        super().__init__("Farmer Zombie", 12000, 1000)


class Military(Zombie):
    def __init__(self):
        super().__init__("Military Zombie", 15000, 1200)

