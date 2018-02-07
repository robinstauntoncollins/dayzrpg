from Item import Item
class Consumable(Item):
    def __init__(self, names, description, amount):
        self.amount = amount
        super().__init(name, description)

class Bandage(Consumable):
    def __init__(name = "Bandage",
                 description = "A packaged bandage for covering wounds",
                 amount = 1)
    def apply():
        '''Allows the player to apply a bandage to himself'''
        pass
    def use():
        '''Allows player to apply a bandage to another character'''
        pass
