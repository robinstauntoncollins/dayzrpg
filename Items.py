######## BASE ITEM ############
class Item(object):
    '''The base class for all items'''
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return "{}\n{}".format(self.name, self.description)

##### LEVEL 1 DERIVED ####
class Consumable(Item):
    def __init__(self, name, description, amount):
        self.amount = amount
        super().__init__(name, description)

    def use(self):
        '''Use this item'''
        self.amount -=1


class Weapon(Item):
    headdmg = 13000
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)


####### TOOLS ##############
class Flashlight(Item):
    def __init__(self):
        super().__init__(name = "Flashlight",
                         description = "A battery powered torch. Illuminates dark areas.")


###### LEVEL 2 Derived #######
########## WEAPONS ############
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


class Roadflares(Consumable):
    def __init__(self):
        self.damage = 0
        super().__init__(name = "Roadflares",
                         description = "10 individual Roadflares. Produces very bright red light in a large area.",
                         amount = 10
                         )

    def use(self):
        '''Use this item'''
        self.amount -=1
        self.description = "{} individual Roadflares. Produces very bright red light in a large area.".format(self.amount)



########## CONSUMABLES ###############
class Bandage(Consumable):
    def __init__(self):
        super().__init__(name = "Bandage",
                         description = "A packaged bandage for covering wounds",
                         amount = 1)
    def apply(self):
        '''Allows the player to apply a bandage to himself'''
        self.amount -=1
        return "You apply a bandage to yourself"


if __name__ == '__main__':
    roadflares = Roadflares()
