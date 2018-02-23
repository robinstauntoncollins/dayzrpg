import config
import Items
from Container import Container


class Player(object):
    
    def __init__(self, name = "Survivor", gender="Male", location = config.starting_location):
        # PLAYER_INFO
        # STATS
        self.name = name
        self.gender = gender
        self.hp = 12000
        self.hunger = 100
        self.thirst = 100

        # FLAGS
        self.bleeding = False
        self.pain = False
        self.arm_broken = False
        self.leg_broken = False
        # OTHER
        self.location = location
        self.victory = False

        # EQUIPMENT
        self.inv_dict = {'bandage': Items.Consumable('bandage'),'roadflares': Items.Consumable('roadflares', 10)}
        self.inventory = [Items.Consumable('bandage'), Items.Consumable('roadflares',10)]
        self.primary = []
        self.secondary = []
        self.got_backpack = False
        self.backpack = []
        self.backpack_dict = {}
        self.toolbelt = [Items.Item('flashlight')]
        self.toolbelt_dict = {'flashlight': Items.Item('flashlight')}

    # STATUS
    def is_alive(self):
        return self.hp > 0
    
    # MOVEMENT
    def move_direction(self, direction, room):
        if direction in room.exits.keys():
            print("You move to the {}".format(direction))
            self.location  = room.exits[direction]
            # room = Room.Location(self.location)
        else:
            print("You can't go that way\n")

    # COMBAT
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

    # INVENTORY/EQUIPMENT
    def print_inv_dict(self):
        item_count = {}
        print('=' * 2 + "Items" + '=' * 2)
        for k,v in self.inv_dict.items():
            if v.name in item_count.keys():
                item_count[v.name] += 1
            else:
                item_count[v.name] = 1

        for k,v in self.inv_dict.items():
            print(v.name,item_count[v.name])
            if item_count[v.name] > 1:
                print(v.name , item_count[v.name])
            else:
                print(v.name)
            
        print('='*2+"Toolbelt"+'='*2)
        for k,v in self.toolbelt_dict.items():
            if hasattr(v, 'amount'):
                print(v.name, v.amount)
            else:
                print(v.name)

        if self.got_backpack:
            print('='*2+"Backpack"+'='*2)
            for k,v in self.backpack_dict.items():
                if hasattr(v, 'amount'):
                    print(v.name, v.amount)
                else:
                    print(v.name)

    def print_inventory(self):
        print('=' * 2 + "Items" + '=' * 2)
        #for item in self.inventory:
        #    if item_count[item.name] > 1:
        #        print(item.name , item_count[item.name])
        #    else:
        #        print(item.name)
        for item in self.inventory:
            if hasattr(item, 'amount'):
                print(item.name, item.amount)
            else:
                print(item.name)
        print('=' * 2 + "Toolbelt" + '=' * 2)
        for item in self.toolbelt:
            if hasattr(item, 'amount'):
                print(item.name, item.amount)
            else:
                print(item.name)
        if self.got_backpack:
            print('='*2+"Backpack"+'='*2)
            for item in self.backpack:
                if hasattr(item, 'amount'):
                    print(item.name, item.amount)
                else:
                    print(item.name)

    def transfer_object(self, obj, target_list):
        """Function to handle transferring an object from location.ground to player.inventory"""
        # print("Object: ", obj.name)
        # print()
        for item in target_list:
            # print(item.name)
            if item.name == obj.name:
               # print("Obj found in inventory")
                if hasattr(item, 'amount'):
                   # print("Item has amount")
                    item.amount += 1
                    #print(item.name, item.amount)
                    return
                else:
                    #print("Item has no amount")
                    target_list.append(obj)
                    return
            else:
                #print("Item not found in inventory, adding it")
                target_list.append(obj)
                return

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

        # Is there an item already present in primary?
        if self.primary:
            print("You put your {} back in your inventory".format(self.primary[0].name))
            self.inventory.append(self.primary.pop())  # put currently equipped it back in inventory
            self.primary.append(item)  # Equip item
            print("You equip your {}".format(self.primary[0].name))
        # If primary slot free
        else:
            self.inventory.remove(item)
            self.primary.append(item)  # Add this item to primary slot
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
        if item is None:
            return "You don't have a {} to drop".format(item)
        else:
            self.inventory.remove(item)
            return "You dropped a {}".format(item.name)

    def take(self, item):
        """Function to take item from area/location into inventory"""
        self.inventory.append(item)
        return "You took the {}".format(item[config.NAME])



if __name__ == '__main__':
    player = Player()
    player.print_inventory()

