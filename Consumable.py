from Item import Item
class Consumable(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

class Bandage(Consumable):
    def __init__(self):
        super().__init__(name = "Bandage",
                         description = "A packaged bandage for covering wounds")
    def apply(self):
        '''Allows the player to apply a bandage to himself'''
        pass
    def use(self):
        '''Allows player to apply a bandage to another character'''
        pass

class Roadflares(Consumable):
    def __init__(self):
        super().__init__(name = "Roadflares",
                         description = "10 individual Roadflares. Produces very bright red light in a large area.")
