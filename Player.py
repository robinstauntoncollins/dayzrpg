import config
import Items


class Player(object):
    
    def __init__(self, name = "Survivor", gender="Male", location = config.starting_location):
        # PLAYER_INFO
        # STATS
        self.name = name
        self.gender = gender
        self.stats = {'hp': 12000, 'hunger': 100, 'thirst': 100}
        # FLAGS
        self.flags = {'bleeding': False, 'pain': False, 'arm_broken': False, 'leg_broken': False}
        # OTHER
        self.location = location

        # EQUIPMENT
        self.inventory = []
        self.primary = []
        self.secondary = []
        self.got_backpack = False
        self.backpack = []
        self.backpack_dict = {}
        self.toolbelt = []

    # STATUS
    def is_alive(self):
        return self.stats['hp'] > 0
    
    # MOVEMENT
    def move_direction(self, direction, room):
        if direction in room.exits.keys():
            print("You move to the {}".format(direction))
            self.location  = room.exits[direction]
            self.stats['hunger'] -= 10
            self.stats['thirst'] -= 15
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
        # available_moves = tile.adjacent_moves()
        # r = random.randint(0, len(available_moves) - 1)
        # self.do_action(available_moves[r])
        pass

    # INVENTORY/EQUIPMENT
    def print_amount_items(self, item):
        if hasattr(item, 'amount'):
            print(item.name, item.amount)
        else:
            print(item.name)

    def print_stats(self):
        print()
        for k,v in self.stats.items():
            print(k,v)

    def print_equipment(self):
        print()
        if len(self.primary) == 0:
            print("Nothing in primary")
        else:
            print('=' * 2 + "Primary " + '=' * 2)
            print(self.primary[0].name)
        print()
        if len(self.secondary) == 0:
            print("Nothing in secondary")
        else:
            print('=' * 2 + "Secondary" + '=' * 2)
            print(self.secondary[0].name)

    def print_inventory(self):
        print()
        if len(self.inventory) == 0:
            print("Nothing in inventory")
        else:
            print('=' * 2 + "Items" + '=' * 2)
            for item in self.inventory:
                self.print_amount_items(item)
            print()
        if len(self.toolbelt) == 0:
            print("Toolbelt is empty")
        else:
            print('=' * 2 + "Toolbelt" + '=' * 2)
            for item in self.toolbelt:
                self.print_amount_items(item)
        if self.got_backpack:
            if len(self.backpack) == 0:
                print("Backpack is empty")
            else:
                print('='*2+"Backpack"+'='*2)
                for item in self.backpack:
                    self.print_amount_items(item)
        else:
            print("You aren't wearing a backpack")

    def equip_primary(self, item):
        """Equips an item from player's inventory"""
        # Does player have this in their inventory?
        # print(item.name, item.shortdesc)
        on_player = self.inventory + self.backpack + self.toolbelt
        # print("On Player: ", on_player)
        if item not in on_player:
            print("You don't have a {} in your inventory".format(item.name))
            return
        # Can player equip this item here? (Must be a weapon)
        # _parent_type = type(item).__bases__[0]
        obj_type = type(item)
        # print(obj_type)
        if not obj_type == Items.Weapon:
            print("You can't equip a {} in your primary slot".format(item.name))
            return

        # Is there an item already present in primary?
        if len(self.primary) != 0:
            print("You put your {} back in your inventory".format(self.primary[0].name))
            self.inventory.append(self.primary.pop())  # put currently equipped it back in inventory
            self.primary.append(item)  # Equip item
            self.inventory.remove(item)
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

    def take(self, item):
        """Function to take item from area/location into inventory"""
        self.inventory.append(item)
        return "You took the {}".format(item[config.NAME])

    def use(self, item):
        # Should check if item is consumable or has 'use' function
        result, amount = item.use()
        print("Effect: ", result)
        print()
        if 'null' in result:
            print("Null, returning")
            return

        if result['property'] in self.flags:
            print("{} in self.flags".format(result['property']))
            self.flags[result['property']] += result['value']
            print("You used {}".format(item.name))
        elif result['property'] in self.stats:
            print("{} in self.stats".format(result['property']))
            self.stats[result['property']] += result['value']
            print("You used {}".format(item.name))
        else:
            print("Couldn't find that property. Item not used")

        # except TypeError:
        #     self.inventory.remove(item)
        #     print("You can't use this")
        # except:
        #     print("Something went wrong in player.use()")
        if amount == 0:
            print("You used your last {}".format(item.name))
            self.inventory.remove(item)
            return


if __name__ == '__main__':
    player = Player()
    player.print_inventory()
    beans = Items.Consumable('baked beans')
    flrs = Items.Consumable('roadflares')
    player.inventory.append(beans)
    player.flags['hunger'] = 85
    print(player.flags)
    player.use(beans)
    print(player.flags)