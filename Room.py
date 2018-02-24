import textwrap
import config
import json
import r_world


class MapTile(object):
    """Abstract Base Class For World locations"""
    def __init__(self):
        pass

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()


class Location(MapTile):
    """Generic Class for any Location Room."""
    def __init__(self, loc):
        super().__init__()
        self.location,self.info = r_world.get_location(loc)
        self.name = self.info[config.NAME]
        self.desc = self.info[config.DESC]
        self.exits = self.info[config.EXITS]
        self.ground = self.info[config.GROUND]
        self.loctype = self.info[config.LOCTYPE]
        self.items = []
        self.spawn_items()
        self.intro_text()

    def intro_text(self):
        print(self.name+'\n'+'='*len(self.name))
        for line in textwrap.wrap(self.desc, config.SCREEN_WIDTH):
            print(line)

        self.show_exits()
        # self.show_ground_items()

    def modify_player(self, player):
        # Area has no effect on Player
        pass

    def show_exits(self):
        print('='*len(self.name))
        print("You see the following exits: ")
        for direction,location in self.exits.items():
            print("{} to {}".format(direction,location))

    def show_ground_items(self):
        if len(self.ground) == 0:
            print("\nYou see nothing on the ground")
        else:
            print("\nOn the ground you see: ")
            for item in self.ground:
                if hasattr(item, 'amount'):
                    print(item.name, item.amount)
                else:
                    print(item.name)

    def spawn_items(self):
        """A function to handle spawning of items in this location"""
        self.items = r_world.populate_room(self.loctype)
        self.ground.extend(self.items)


class Building(MapTile):
    """A class for Buildings in the world."""
    pass


if __name__ == '__main__':
    # cl = Location(config.starting_location)
    cl = Location(config.starting_location)
    for item in cl.ground:
        print(item.name)
    print(cl.ground)
