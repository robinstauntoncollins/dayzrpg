import textwrap
import config
import json
import r_world
import actions


class MapTile(object):
    """Abstract Base Class For World locations"""
    def __init__(self):
        pass

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        '''Returns all move actions for adjacent tiles'''
        moves = []
        
        

class Location(MapTile):
    """Generic Class for any Location Room."""
    def __init__(self,loc):
        #super().__init__(loc)
        self.location,self.info = r_world.get_location(loc)
        self.available_actions = []
        self.name = self.info[config.NAME]
        self.desc = self.info[config.DESC]
        self.exits = self.info[config.EXITS]
        
    def intro_text(self):
        print(self.name+'\n'+'='*len(self.name))
        for line in textwrap.wrap(self.desc, config.SCREEN_WIDTH):
            print(line)

        self.show_exits()
    
    def show_exits(self):
        print('='*len(self.name))
        print("You see the following exits: ")
        for direction,location in self.exits.items():
            print("{} to {}".format(direction,location))
            
    def modify_player(self, player):
        # Area has no effect on Player
        pass

class Building(MapTile):
    """A class for Buildings in the world."""
    pass

if __name__ == '__main__':
    cl = Location(config.starting_location)
    cl.intro_text()
    cl.show_exits()
