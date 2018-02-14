"""A module with functions handle interaction with worldItems json file"""
import Room
import json
import config

WORLDITEMSPATH = r'D:\Users\RSTAUNTO\Desktop\Python\dayzrpg\resources\worldItems.json'


def get_item_data(item=None):
    """A function to retrieve data from 'worldItems' json file. Can be given a specific item
    or left blank for all items"""
    with open(WORLDITEMSPATH, 'r') as file:
        world_items = json.load(file)

    if item is None:
        return world_items
    else:
        return world_items[item]


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
        desc_words.append(world_items[item][config.DESCWORDS][0])
    return list(set(desc_words))


def get_first_item_matching_desc(desc, item_list):
    world_items = get_item_data()
    unique_item_list = list(set(item_list))  # make itemList unique
    for item in unique_item_list:
        if desc in world_items[item][config.DESCWORDS]:
            return item
    return None


def get_all_items_matching_desc(desc, item_list):
    world_items = get_item_data()
    unique_item_list = list(set(item_list))  # make itemList unique
    matching_items = []
    for item in unique_item_list:
        if desc in world_items[item][config.DESCWORDS]:
            matching_items.append(item)
    return matching_items


if __name__ == '__main__':
    # items = ['axe','rock','fountain']
    # result=get_all_desc_words(items)
    # print(result)
    worlditems = get_item_data()