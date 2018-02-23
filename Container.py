class Item(object):
    def __init__(self, name, quantity=1):
        self.name = name
        self.raw = name.strip().lower()
        self.quantity = quantity


class Container(object):

    def __init__(self, name):
        self.name = name
        self.inside = {}

    def __iter__(self):
        return iter(list(self.inside.items()))

    def __len__(self):
        return len(self.inside)

    def __contains__(self, item):
        return item.raw in self.inside

    def __getitem__(self, item):
        return self.inside[item.raw]

    def __setitem__(self, item, value):
        self.inside[item.raw] = value
        return self[item]

    def add(self, item, quantity=1):
        if quantity < 0:
            raise ValueError("Negative Quantity, use remove()")

        if item in self:
            self[item].quantity += quantity
        else:
            self[item] = item

    def remove(self, item, quantity=1):
        if item not in self:
            raise KeyError("Not in container")
        if quantity < 0:
            raise ValueError("Negative quantity, use add() instead")

        if self[item].quantity <= quantity:
            del self.inside[item.raw]
        else:
            self[item].quantity -= quantity


if __name__ == '__main__':
    bag = Container("BagOfHolding")

    sword = Item("Sword", 10)
    potion = Item("Potion", 5)
    gold = Item("Gold coin", 50)
    bag.add(sword)
    bag.add(gold)
    print(sword in bag)
    print(potion in bag)

    bag.add(potion)
    bag.remove(gold,5)
