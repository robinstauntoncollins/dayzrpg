from Being import Being
import Item
import Consumable
class Player(Being):

    thirst_level = 100
    hunger_level = 100
    #hp = 12000

    inventory = {}
    def __init__(self, name = "Survivor", sex = "Male"):
        self.name = name
        self.sex = sex
        self.inventory = [Item.Flashlight(), Consumable.Bandage(), Consumable.Roadflares()]
        self.hp = 12000
        
    def is_alive(self):
        return self.hp > 0
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
