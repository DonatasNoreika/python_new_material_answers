my_menu = [
    {"name": "cinnamon roll",
     "type": "food",
     "price": 1},
    {"name": "iced coffee",
     "type": "drink",
     "price": 1.17},
    {"name": "lemonade",
     "type": "drink",
     "price": 0.50},
    {"name": "orange juice",
     "type": "drink",
     "price": 0.60},
    {"name": "cranberry juice",
     "type": "drink",
     "price": 0.60},
    {"name": "pineapple juice",
     "type": "drink",
     "price": 0.70},
    {"name": "lemon iced tea",
     "type": "drink",
     "price": 1},
    {"name": "vanilla chai latte",
     "type": "drink",
     "price": 1.2},
    {"name": "hot chocolate",
     "type": "drink",
     "price": 1.5},
    {"name": "tuna sandwich",
     "type": "food",
     "price": 2},
    {"name": "ham and cheese sandwich",
     "type": "food",
     "price": 2.5},
    {"name": "bacon and egg",
     "type": "food",
     "price": 2.5},
    {"name": "steak",
     "type": "food",
     "price": 4},
    {"name": "hamburger",
     "type": "food",
     "price": 4},
]


class CoffeeShop:
    def __init__(self, name):
        self.name = name
        self._menu = my_menu
        self.__orders = []
        self.__total = 0

    def _get_price(self, item_name):
        for item in self._menu:
            if item["name"] == item_name:
                return item["price"]

    def add_order(self, item_name):
        names = [item['name'] for item in self._menu]
        if item_name in names:
            self.__orders.append(item_name)
            self.__total += self._get_price(item_name)
            print(f"{item_name} added to order!")
        else:
            print("This item is currently unavailable!")

    def fulfill_order(self):
        if self.__orders:
            print(f"{self.__orders[0]} is ready!")
            self.__orders.pop(0)
        else:
            print("All orders have been fulfilled!")

    def list_orders(self):
        print(self.__orders)

    def due_amount(self):
        print(f"Total: {self.__total}")

    def cheapest_item(self):
        cheapest_item = self._menu[0]
        for item in self._menu:
            if item['price'] < cheapest_item['price']:
                cheapest_item = item
        print(f"Cheapest item in menu: {cheapest_item["name"]}")

    def drinks_only(self):
        return [item["name"] for item in self._menu if item['type'] == "drink"]

    def food_only(self):
        return [item["name"] for item in self._menu if item['type'] == "food"]


coffeeshop = CoffeeShop("Best Coffee")
coffeeshop.add_order("lemonade")
coffeeshop.due_amount()
coffeeshop.add_order("bacon and egg")
coffeeshop.due_amount()
coffeeshop.list_orders()
coffeeshop.fulfill_order()
coffeeshop.fulfill_order()
coffeeshop.fulfill_order()
coffeeshop.cheapest_item()
print(coffeeshop.drinks_only())
print(coffeeshop.food_only())
