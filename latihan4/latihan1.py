#latihan1
class Player:
    def __init__(self, name):
        self.name = name
        self.infentory = Infentory()

class Item: 
    def __init__(self, name):
        self.name = name
    
class Infentory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


player = Player("Alip")
sword = Item("sword")
shield = Item('shiled')
player.infentory.add_item(sword)
player.infentory.add_item(shield)
player.infentory.items

