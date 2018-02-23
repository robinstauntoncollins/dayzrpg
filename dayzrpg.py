import config
from Room import Location
import cmd
from Player import Player


class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.player = Player()
        self.location = Location(config.starting_location)
        
    prompt = '\n>'

    def default(self, arg):
        """Called when none of other do_* commands match"""
        print("I do not understand that command. Type 'help' for a list of commands.")

    def do_quit(self, arg):
        """Quit the game"""
        print("Thanks for playing")
        return True  # Exits Cmd application loop in command.cmdloop()

    def help_combat(self):
        print("Combat is not implemented in this program yet.")

    def do_north(self, arg):
        """Go to the north if possible"""
        self.player.move_direction('north', self.location)
        self.location = Location(self.player.location)

    def do_northeast(self, arg):
        """Go to the northeast if possible"""
        self.player.move_direction('north east', self.location)
        self.location = Location(self.player.location)

    def do_east(self, arg):
        """Go to the east if possible"""
        self.player.move_direction('east', self.location)
        self.location = Location(self.player.location)

    def do_southeast(self, arg):
        """Go to the southeast if possible"""
        self.player.move_direction('south east', self.location)
        self.location = Location(self.player.location)

    def do_south(self, arg):
        """Go to the south if possible"""
        self.player.move_direction('south', self.location)
        self.location = Location(self.player.location)

    def do_southwest(self, arg):
        """Go to the southwest if possible"""
        self.player.move_direction('south west', self.location)
        self.location = Location(self.player.location)

    def do_west(self, arg):
        """Go to the wesst if possible"""
        self.player.move_direction('west', self.location)
        self.location = Location(self.player.location)

    def do_northwest(self, arg):
        """Go to the northwest if possible"""
        self.player.move_direction('north west', self.location)
        self.location = Location(self.player.location)

    def do_inventory(self, arg):
        """Display a list of items in your inventory"""
        self.player.print_inventory()
        # self.player.print_inv_dict()

    def do_look(self, arg):
        """Look at an item, direction, or the area:
        "look" - display the current area's description
        "look <direction>" - display the description of the area in that direction
        "look exits" - display the description of all adjacent areas
        "look <item>" - display the description of an item on the ground or in your inventory"""
        looking_at = arg.lower()
        # Just 'look' command
        if looking_at == '':
            self.location.intro_text()
            return
        # 'look exits' command
        if looking_at == 'exits':
            self.location.show_exits()
            return
        # 'look <direction>' command
        if looking_at in config.DIRECTIONS and looking_at in self.location.exits:
            print("You see {} to the {}".format(self.location.exits[looking_at], looking_at))

        if looking_at == 'ground':
            self.location.show_ground_items()
            
        else:
            print("You don't see much in that direction")

    def do_take(self, arg):
        """Take an item from ground to inventory"""
        item_to_take = arg.lower()  # format string
        if item_to_take == '':  # if nothing print message and exit
            print("Take what? Type 'look ground' to see what lies here")
            return
        cant_take = False
        matching_items = []
        for item in self.location.ground:
            if item_to_take in item.descwords:
                matching_items.append(item)
        # print(matching_items)

        for item in matching_items:
            if not item.takeable:
                cant_take = True
                continue
            print("You take {}".format(item.name))
            self.player.transfer_object(item, self.player.inventory)
            self.location.ground.remove(item)
            return
            # for inv_item in self.player.inventory:
            #     if item.name == inv_item.name:
            #         if hasattr(item, 'amount'):
            #             self.player.inventory[matching_items.index(item)].amount += 1
            #             self.location.ground.remove(item)
            #     else:
            #         self.location.ground.remove(item)
            #         self.player.inventory.append(item)
            # return
        if cant_take:
            print("You can't take {}".format(item_to_take))
        else:
            print("You don't find that on the ground")

    def do_hold(self, arg):
        """Equips weapon from inventory to primary or secondary slot"""
        self.player.equip_primary(arg.lower())

    def do_drop(self, arg):
        item_to_drop = arg.lower()
        print(item_to_drop)
        if item_to_drop == '':
            print("Drop what? Type 'i' to see your inventory")
            return
        matching_items = []
        for item in self.player.inventory:
            if item_to_drop in item.descwords:
                matching_items.append(item)
        # for k,v in self.player.inv_dict.items():
        #    if item_to_drop in v.descwords:
        #        matching_items.append(v)
        # print(matching_items)

        for item in matching_items:
            if item is not None:
                if hasattr(item, 'amount'):
                    if self.player.inventory[matching_items.index(item)].amount > 1:
                        self.player.inventory[matching_items.index(item)].amount -= 1
                    else:
                        self.player.inventory.remove(item)

                    print("You drop {}".format(item.name))
                    self.location.ground.append(item)
                else:
                    # del self.player.inv_dict[item_to_drop]
                    self.player.inventory.remove(item)
                    print("You drop {}".format(item.name))
                    for gr_item in self.location.ground:
                        if gr_item.name == item.name and hasattr(gr_item, 'amount'):
                            gr_item.amount +=1
                        else:
                            self.location.ground.append(item)
            else:
                print("You have no {} in your inventory".format(item_to_drop))
            return

        
#    def do_useItem(self,arg):
#        """Command to use a variety of items"""
#        itemToUse = arg.lower()
#        items = []
#        for item in self.player.inventory:
#            items.append(item.name.lower())
#        invDescWords = r_world.get_all_desc_words(items)
#        if itemToUse not in invDescWords:
#            print("You do not have a {} in your inventory.".format(itemToDrop))
#            return
#        item,w
#    def search_inv(self, arg):
#        itemToUse = arg.lower()
#        items = []
#        for item in self.player.inventory:
#            items.append(item.name.lower())
#        invDescWords = r_world.get_all_desc_words(items)
#        if itemToUse not in invDescWords:
#            print("You do not have a {} in your inventory.".format(itemToDrop))
#            return

    do_n = do_north
    do_ne = do_northeast
    do_e = do_east
    do_se = do_southeast
    do_s = do_south
    do_sw = do_southwest
    do_w = do_west
    do_nw = do_northwest

    do_i = do_inventory


if __name__ == '__main__':
    print('='*5+" DayZ RPG "+'='*5)
    print('='*18)
    print()
    print('(Type "help" for commands.)')
    print()
    g = Game()
    g.cmdloop()
