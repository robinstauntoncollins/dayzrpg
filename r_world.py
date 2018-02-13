import Room
import json
import config

WORLDPATH = r'D:\Users\RSTAUNTO\Desktop\Python\dayzrpg\resources\Chernarus_v3.json'
start = config.starting_location

def get_world_data(room_name=None):
    '''A function that returns world dictionary if no name is given
    and returns specifc room if name is given.'''
    with open(WORLDPATH, 'r') as file:
        world = json.load(file)
        
    if room_name == None:
        return world
    else:
        return world[room_name]

def get_location(loc):
    '''Get world location info based on their x,y coords'''
    if loc == None:
        print("r_world.get_location() Failed!")
        return
    world = get_world_data()
    for location,info in world.items():
        if loc == location:
            return location,info

##def spawn_loot(room):
##    """A function to spawn loot in a Room when it is created
##    based on the type of room"""
##    thisRoom=get_world_data(room)
##    if thisRoom[config.LOOTTYPE] = 'residential':
        
    
    
            


if __name__ == '__main__':
    #world = get_world_data(start)
    loc,info = get_location(start)
