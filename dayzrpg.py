import config
from Room import Location
import cmd
from Player import Player
import Items


class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.player = Player()
        self.player.inventory = [Items.Consumable('bandage'), Items.Consumable('roadflares',1)]
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

        # 'look exits' command
        elif looking_at == 'exits':
            self.location.show_exits()

        # 'look <direction>' command
        elif looking_at in config.DIRECTIONS and looking_at in self.location.exits:
            print("You see {} to the {}".format(self.location.exits[looking_at], looking_at))

        elif looking_at == 'ground':
            self.location.show_ground_items()

        elif looking_at == 'self':
            self.player.print_equipment()
            self.player.print_inventory()
            self.player.print_stats()
        else:
            print("You don't see much in that direction")

    def get_matching_items(self, input_item, location):
        matching_items = []
        for item in location:
            if input_item in item.descwords:
                matching_items.append(item)
        return matching_items

    def transfer_object(self, origin, obj, destination):
        """Function to handle transferring an object from location.ground to player.inventory"""
        # Check if origin item has amount attribute
        for ori_item in origin:
            if ori_item.name == obj.name:
                if hasattr(ori_item, 'amount') and ori_item.amount > 1:
                    ori_item.amount -= 1
                else:
                    origin.remove(ori_item)

        # Check if destination item has amount attribute
        for dest_item in destination:
            if dest_item.name == obj.name:
                if hasattr(dest_item, 'amount'):
                    dest_item.amount += 1
                    return
                else:
                    destination.append(obj)
                    return
        destination.append(obj)

    def do_take(self, arg):
        """Take an item from ground to inventory"""
        item_to_take = arg.lower()  # format string

        if item_to_take == '':  # if nothing print message and exit
            print("Take what? Type 'look ground' to see what lies here")
            return

        cant_take = False
        for item in self.get_matching_items(item_to_take, self.location.ground):
            if not item.takeable:
                cant_take = True
                continue
            print("You take the {}".format(item.name))
            self.transfer_object(self.location.ground, item, self.player.inventory)
            return

        if cant_take:
            print("You can't take {}".format(item_to_take))
        else:
            print("You don't find that on the ground")

    def do_drop(self, arg):
        """Drops item from inventory to ground.
        Type 'drop <item>' """
        item_to_drop = arg.lower()

        if item_to_drop == '':
            print("Drop what? Type 'i' to see your inventory")
            return

        for item in self.get_matching_items(item_to_drop, self.player.inventory):
            if item is not None:
                self.transfer_object(self.player.inventory, item, self.location.ground)
                print("You drop {}".format(item.name))
            else:
                print("You have no {} in your inventory".format(item_to_drop))
            return

    def do_hold(self, arg):
        """Equips weapon from inventory to primary or secondary slot"""
        matching_items = self.get_matching_items(arg.lower(), self.player.inventory)
        self.player.equip_primary(matching_items[0])

    def do_unhold(self, arg):
        """Un-equips weapon from primary slot to inventory"""
        # matching_items = self.get_matching_items(arg.lower(), self.player.primary)
        self.player.unequip_primary()

    def do_use(self,arg):
        """Command to use a variety of items"""
        item_to_use = arg.lower()
        matching_items = self.get_matching_items(item_to_use, self.player.inventory)
        if not matching_items:
            print("You have no {} in your inventory".format(item_to_use))
            return
        for item in matching_items:
            if not type(item) == Items.Consumable:
                print("You can't use that")
            else:
                self.player.use(item)

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
