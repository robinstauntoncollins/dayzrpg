import config
import Items
import random
import Room

class Player(object):
    
    def __init__(self, name = "Survivor", sex = "Male"):
        ###PLAYERINFO##
        ###STATS###
        self.name = name
        self.sex = sex
        self.hp = 12000
        self.hunger = 100
        self.thirst = 100

        ###FLAGS###
        self.bleeding = False
        ###OTHER###
        self.location = config.starting_location
        self.victory = False
        ###EQUIPMENT###
        self.inventory = [Items.Bandage(), Items.Roadflares()]
        self.primary = []
        self.secondry = []
        self.got_backpack = True
        self.backpack = [Items.Crowbar(), Items.Rock()]
        self.toolbelt = [Items.Flashlight()]
        
    #STATUS#    
    def is_alive(self):
        return self.hp > 0
    
    #MOVEMENT#
    def move_direction(self, direction, room):
        if direction in room.exits.keys():
            print("You move to the {}".format(direction))
            self.location  = room.exits[direction]
            #room = Room.Location(self.location)
        else:
            print("You can't go that way\n")
    #COMBAT#
    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            print(i)
            if isinstance(i, Items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
                    
      
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))


    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
##        available_moves = tile.adjacent_moves()
##        r = random.randint(0, len(available_moves) - 1)
##        self.do_action(available_moves[r])
        pass


    #INVENTORY/EQUIPMENT#
    def print_inventory(self):
        print('='*2+"Items"+'='*2)
        for item in self.inventory:
            print(item.name)
        print('='*2+"Toolbelt"+'='*2)
        for item in self.toolbelt:
            print(item.name)
        if self.got_backpack:
            print('='*2+"Backpack"+'='*2)
            for item in self.backpack:
                print(item.name)

    def equip_primary(self, item):
        """Equips an item from player's inventory"""
        # Does player have this in their inventory?
        on_player = [self.inventory, self.backpack, self.toolbelt]
        print(on_player)
        if item not in on_player:
            return "You don't have a {} in your inventory".format(item.name)
        # Can player equip this item here? (Must be a weapon)
        _parent_type = type(item).__bases__[0]
        if not _parent_type == Items.Weapon: 
            return "You can't equip a {} in your primary slot".format(item.name)

        #Is there an item already present in primary?
        if self.primary:
            print("You put your {} back in your inventory".format(self.primary[0].name))
            self.inventory.append(self.primary.pop()) #put currently equipped it back in inventory
            self.primary.append(item) #Equip item
            print("You equip your {}".format(self.primary[0].name))
        #If primary slot free
        else:
            self.inventory.remove(item)
            self.primary.append(item) #Add this item to primary slot
            print("You equip your {}".format(self.primary[0].name))

    def equip_secondary(self, item):
        """Equips and item from player's inventory to secondary slot"""
        # Does player have this in their inventory?
        if item not in self.inventory:
            return "You don't have a {} in your inventory".format(item.name)

    def unequip_primary(self):
        """Unequips item in player's primary slot and puts it in player's inventory"""
        if self.primary:
            print("You unequip your {}".format(self.primary[0].name))
            self.inventory.append(self.primary.pop())
        else:
            print("You currently have nothing equipped in your primary slot")

    def get_item_from_string(self, string, inv_location):
        """This function takes the string argument passed by command and translates that into
        a class object in one of the players inventory spaces"""
        print(string)
        print(inv_location)
        for item in inv_location:
            print(item.name)
            if item.name == string:
                return item
            else:
                print("Could not find item there")
                return None
        
    def drop_from_main_inventory(self, string):
        """Function should take item from player inventory and add it to GROUND location
        of the current room"""
        item = self.get_item_from_string(string, self.inventory)
        print(item)
        if item == None:
            return "You don't have a {} to drop".format(item)
        else:
            self.inventory.remove(item)
            return "You dropped a {}".format(item.name)

    def take(self, item):
        """Function to take item from area/location into inventory"""
        self.inventory.append(item)
        return "You took the {}".format(item.name)


if __name__ == '__main__':
    player = Player()
    player.print_inventory()
    print()
    player.drop_from_main_inventory("Roadflares")
    print()
    player.print_inventory()
    
