"""A module with functions to handle interaction with data in JSON files"""
import json
import config
import random
import Items

PATH = r'D:\Users\RSTAUNTO\Desktop\Python\dayzrpg\resources'
WORLDPATH = PATH + '\maps\Chernarus_v5.json'
WORLDITEMSPATH = PATH + '\items'
ALLITEMS = WORLDITEMSPATH + '\worldItems.json'
WEAPONS = WORLDITEMSPATH + '\weapons.json'
FOOD = WORLDITEMSPATH + '\food.json'
MEDICAL = WORLDITEMSPATH + '\medical.json'
start = config.starting_location


def get_world_data(path=WORLDPATH,room_name=None, mode='r'):
    """A function that returns world dictionary if no name is given
    and returns specific room if name is given."""
    with open(path, mode) as file:
        world = json.load(file)
        
    if room_name is None:
        return world
    else:
        return world[room_name]


def get_item_data(path=ALLITEMS, item_name=None, mode='r'):
    """A function to retrieve data from worldItems file.
    Can be given a specific item"""
    with open(path,  mode) as file:
        world_items = json.load(file)

    if item_name is None:
        return world_items
    else:
        return world_items[item_name]


def get_location(loc):
    """Get world location name and other info from JSON file"""
    if loc is None:
        print("r_world.get_location() Failed!")
        return
    world = get_world_data()
    for location,info in world.items():
        if loc == location:
            return location,info


def generate_items(item_type):
    """Generates a list of appropriate items based on type"""
    items = get_item_data()
    item_dict = {}
    for k,v in items.items():
        if v[config.SPAWNTYPE] == item_type:
            item_dict[k] = v

    return item_dict

def create_object(name, description):
    the_object = Items.Item(name, description)
    return the_object

def create_weapon(name, description, damage):
    """Creates a weapon object using name and description from the json object"""
    the_object = Items.Weapon(name,description, damage)
    return the_object


def populate_room(loctype):
    """Function to populate a room's ground list based on it's loot type with item objects
    when the room object is created."""
    #Look t
    room_items = []
    world_items = get_item_data()
    for item,info in world_items.items():
        if info[config.SPAWNTYPE] == loctype:
            room_items.append(create_object(item, info[config.SHORTDESC]))
            if info[config.LOOTTYPE] == 'weapon':
                room_items.append(create_weapon(item, info[config.SHORTDESC], info[config.DAMAGE]))
            elif info[config.LOOTTYPE] == 'medical':
                room_items.append(create_object(item, info[config.SHORTDESC]))
            else:
                room_items.append(create_object(item, info[config.SHORTDESC]))

            
    return room_items


def get_all_desc_words(item_list):
    """Returns a list of "description words" for each item named in item_list from world_items"""
    world_items = get_item_data()
    unique_item_list = list(set(item_list))  # make itemList unique
    desc_words = []
    for item in unique_item_list:
        desc_words.extend(world_items[item][config.DESCWORDS])
    return list(set(desc_words))


def get_all_first_desc_words(item_list):
    """Returns a list of the first "description word" in the list of
    description words for each item named in itemList."""
    world_items = get_item_data()
    unique_item_list = list(set(item_list))  # make itemList unique
    desc_words = []
    for item in unique_item_list:
        desc_words.append(world_items[item.name][config.DESCWORDS][0])
    return list(set(desc_words))


def get_first_item_matching_desc(desc, item_list):
    world_items = get_item_data()
    unique_item_list = list(set(item_list))  # make itemList unique
    for item in unique_item_list:
        if desc in world_items[item.name][config.DESCWORDS]:
            return item, world_items
    return None


def get_all_items_matching_desc(desc, item_list):
    world_items = get_item_data()
    unique_item_list = list(set(item_list))  # make itemList unique
    matching_items = []
    for item in unique_item_list:
        if desc in world_items[item.name][config.DESCWORDS]:
            matching_items.append(item)
    return matching_items,world_items

        

if __name__ == '__main__':
    world_items = get_item_data()

    
