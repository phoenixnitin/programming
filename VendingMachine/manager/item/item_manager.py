from .item import Item
from manager.user.user import User
from collections import defaultdict as ddict

class ItemManager:
    '''
    Items
    '''
    def __init__(self, max_quantity: int, cost: int):
        self.max_quantity = max_quantity
        self.cost = cost
        self.items = ddict(lambda: Item)
        self.id = 0

    def get_item(self):
        for item_id in self.items:
            print(f'ID {item_id}: {self.items[item_id].name} of type {self.items[item_id].type}, quantity => {self.items[item_id].quantity}')
    
    def __get_total_quantity(self) -> int:
        quantity = 0
        for key in self.items:
            quantity += self.items[key].quantity
        return quantity

    def decrease_quantity(self, item_id: int, quantity: int, login_user: User) -> bool:
        if quantity <= 0:
            print('Invalid quantity')
            return False

        if self.is_valid_id(item_id):
            if self.items[item_id].quantity - quantity >= 0:
                if login_user is None:
                    self.items[item_id].quantity -= quantity
                    return True
                elif login_user.available_cash - self.cost * quantity >= 0:
                    self.items[item_id].quantity -= quantity
                    login_user.available_cash -= self.cost * quantity
                    return True
                else:
                    print(f'Not enough cash')
            else:
                if self.items[item_id].quantity > 0:
                    print(f'{self.items[item_id].quantity} {self.items[item_id].name} available')
                else:
                    print(f'{self.items[item_id].name} is unavailable')
        return False

    def increase_quantity(self, item_id: int, quantity: int) -> bool:
        if self.is_valid_id(item_id):
            if self.__get_total_quantity() + quantity <= self.max_quantity:
                self.items[item_id].quantity += quantity
                return True
            else:
                print(f'Given Quantity for {self.items[item_id].name} exceeds max quantity')
        return False

    def add_item(self, item: Item) -> bool:
        if self.__get_total_quantity() + item.quantity <= self.max_quantity:
            self.id += 1
            self.items[self.id] = item
            return True
        else:
            print('Quantity exceeds max allowed.')
        return False
    
    def delete_item(self, item_id: int) -> bool:
        if self.is_valid_id(item_id):
            del self.items[item_id]
            return True
        return False


    def is_valid_id(self, item_id: int) -> bool:
        if item_id in self.items:
            return True
        else:
            print('Invalid item id')
            return False

