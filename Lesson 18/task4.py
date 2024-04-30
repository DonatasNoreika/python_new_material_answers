class ElectronicDevice:
    def __init__(self, brand, price, warranty_period):
        self.brand = brand
        self._price = price
        self.warranty_period = warranty_period
        self.__stock = 20

    def get_details(self):
        print(f"Brand: {self.brand}, price: {self._price}, warranty: {self.warranty_period}")

    def purchase(self):
        self.__stock -= 1
        print(f"Item purchased. Stock: {self.__stock}")


class Laptop(ElectronicDevice):
    def __init__(self, brand, price, warranty_period, ram, storage):
        super().__init__(brand, price, warranty_period)
        self.ram = ram
        self.storage = storage

    def get_details(self):
        super().get_details()
        print(f"RAM: {self.ram}, storage: {self.storage}")


class Smartphone(ElectronicDevice):
    def __init__(self, brand, price, warranty_period, screen_size, battery_capacity):
        super().__init__(brand, price, warranty_period)
        self.screen_size = screen_size
        self.battery_capacity = battery_capacity

    def get_details(self):
        super().get_details()
        print(f"Screen size: {self.screen_size}, battery: {self.battery_capacity}")


class Television(ElectronicDevice):
    def __init__(self, brand, price, warranty_period, screen_size, resolution):
        super().__init__(brand, price, warranty_period)
        self.screen_size = screen_size
        self.resolution = resolution

    def get_details(self):
        super().get_details()
        print(f"Screen size: {self.screen_size}, resolution: {self.resolution}")


class Discount:
    def get_price(self, item: ElectronicDevice, percentage):
        return item._price * (100 - percentage) / 100


device1 = ElectronicDevice("Toyota Prius", 42000, 36)
device2 = Laptop("Lenovo Legion", 1500, 36, 16, 2000)
device3 = Smartphone("Samsung Galaxy S24", 900, 36, 6.2, 4000)
device4 = Television("Xiaomi A Pro", 249, 24, 43, "3840x2160")

device1.get_details()
device2.get_details()
device3.get_details()
device4.get_details()
device1.purchase()
device2.purchase()
device1.purchase()
device1.purchase()
device1.purchase()

discount = Discount()
print(discount.get_price(device4, 50))
