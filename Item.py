
class Item(object):
    '''The base class for all items'''
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return "{}\n=======\n{}".format(self.name, self.description)

class Flashlight(Item):
    def __init__(self):
        super().__init__(name = "Flashlight",
                         description = "A battery powered torch. Illuminates dark areas.")
