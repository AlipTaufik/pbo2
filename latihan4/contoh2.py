#latihan2
class Menu:
    def __init__(self, dishes = None):
        if dishes is None:
            self.dishes = []
        else: 
            self.dishes = dishes

    def add_dish(self, dish):
        self.dishes.append(dish)

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

dish1 = Dish("Coel", 13000)
dish2 = Dish("Rumba", 12000)
menu = Menu([dish1, dish2])
restaurant = Restaurant("Kamang Jaya", menu)
restaurant.menu.dishes