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
        print("I do not understand that ocmmand. Type 'help' for a list of commands.")

    def do_quit(self, arg):
        """Quit the game"""
        print("Thanks for playing")
        return True #Exits Cmd application loop in command.cmdloop()

    def help_combat(self):
        print("Combat is not implemented in this program yet.")

    def do_north(self, arg):
        """Go to the north if possible"""
        self.player.move_direction('north',self.location)
        self.location = Location(self.player.location)
        self.location.intro_text()

    def do_northeast(self,arg):
        """Go to the northeast if possible"""
        self.player.move_direction('north east',self.location)
        self.location = Location(self.player.location)
        self.location.intro_text()

    def do_east(self,arg):
        """Go to the east if possible"""
        self.player.move_direction('east',self.location)
        self.location = Location(self.player.location)
        self.location.intro_text()

    def do_southeast(self, arg):
        """Go to the southeast if possible"""
        self.player.move_direction('south east',self.location)
        self.location = Location(self.player.location)
        self.location.intro_text()

    def do_south(self,arg):
        """Go to the south if possible"""
        self.player.move_direction('south',self.location)
        self.location = Location(self.player.location)
        self.location.intro_text()

    def do_southwest(self, arg):
        """Go to the southwest if possible"""
        self.player.move_direction('south west',self.location)
        self.location = Location(self.player.location)
        self.location.intro_text()

    def do_west(self,arg):
        """Go to the wesst if possible"""
        self.player.move_direction('west',self.location)
        self.location = Location(self.player.location)
        self.location.intro_text()

    def do_northwest(self, arg):
        """Go to the northwest if possible"""
        self.player.move_direction('north west',self.location)
        self.location = Location(self.player.location)
        self.location.intro_text()

    def do_inventory(self, arg):
        """Display a list of items in your inventory"""
        self.player.print_inventory()

    def do_look(self, arg):
        """Look at an item, direction, or the area:
        "look" - display the current area's description
        "look <direction>" - display the description of the area in that direction
        "look exits" - display the description of all adjacent areas
        "look <item>" - display the description of an item on the ground or in your inventory"""
        lookingAt = arg.lower()
        # Just 'look' command
        if lookingAt =='':
            self.location.intro_text()
            return
        #'look exits' command
        if lookingAt == 'exits':
            self.location.show_exits()
            return
        #'look <direction>' command
        if lookingAt in config.DIRECTIONS and lookingAt in self.location.exits:
            print("You see {} to the {}".format(self.location.exits[lookingAt], lookingAt))

        else:
            print("You don't see much in that direction")

    def do_take(self, arg):
        """Take an item from ground to inventory"""
        self.player.take(arg)
        return
    def do_hold(self, arg):
        """Equips weapon from inventory to primary or secondary slot"""
        self.player.equip_primary(arg)
        
    def do_drop(self, arg):
        pass
    def do_useItem(self,arg):
        """Command to use a variety of items"""
        pass

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
    
