import r_world
import config


# BASE ITEM
class Item(object):
    def __init__(self, item):
        self.item = r_world.get_item_data(item)
        self.name = self.item[config.NAME]
        self.shortdesc = self.item[config.SHORTDESC]
        self.longdesc = self.item[config.LONGDESC]
        self.takeable = self.item[config.TAKEABLE]
        self.descwords = self.item[config.DESCWORDS]
        self.loottype = self.item[config.LOOTTYPE]

    def __str__(self):
        return self.name


class Weapon(Item):
    headdmg = 13000

    def __init__(self, item):
        super().__init__(item)
        self.damage = self.item[config.DAMAGE]


# LEVEL 1 DERIVED
class Consumable(Item):
    def __init__(self, item, amount = 1):
        super().__init__(item)
        self.amount = amount

    def __str__(self):
        return "{0}, {1}".format(self.name, self.amount)

    def use(self):
        """Use this item"""
        self.amount -= 1


if __name__ == '__main__':
    item = Item('bandage')
    flrs = Consumable('roadflares',10)
    print(flrs)
    flrs.use()
    print(flrs)