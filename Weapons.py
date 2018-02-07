from Item import Item

class Weapon(Item):
    headdmg = 13000
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                       description = "Melee: A head-sized rock. Smashy Smashy!",
                       damage = 3000)
class Axe(Weapon):
    def __init__(self):
        super().__init__(name="Axe",
                       description = "Melee: A full sized chopping axe. Good for chopping down trees.",
                       damage = 6000)
class Crowbar(Weapon):
    def __init__(self):
        super().__init__(name="Crowbar",
                       description = "Melee: A crowbar. Used for prying things open",
                       damage = 6000)

