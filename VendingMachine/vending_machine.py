'''
Vending machine
accessibility -> 1 machine with single use at a time

item types: drink and snack
max quantity for each = 10
cost of each item = 20

cash input

2 set of users:
employee --> purchase item and check items
admin --> employee + add and remove items

'''

from manager.user.user_manager import UserManager
from manager.item.item_manager import ItemManager
from manager.item.item import Item
from manager.user.user import User
import functools

class VendingMachine:
    '''
    Vending machine
    '''

    def __init__(self, max_quantity, cost_of_each_item):
        '''
        Initialize vending machine
        '''
        self.max_quantity = max_quantity
        self.item_cost = cost_of_each_item
        self.user_manager = UserManager()
        
        self.item_manager = {
            'drink': ItemManager(self.max_quantity, self.item_cost),
            'snack': ItemManager(self.max_quantity, self.item_cost),
        }
        
        self.login_user = None

    def login(self, username: str):
        self.login_user = self.user_manager.get_user_by_name(username)
        if self.login_user is None:
            print('Invalid User')
    
    def auth(callback_func):
        @functools.wraps(callback_func)
        def wrapper(self, *args, **kwargs):
            if self.login_user is not None:
                return callback_func(self, *args, **kwargs)
            else:
                print('Login first')
                return False
        return wrapper

    def auth_admin(callback_func):
        @functools.wraps(callback_func)
        def wrapper(self, *args, **kwargs):
            if self.login_user is not None and self.user_manager.is_admin_user(self.login_user):
                return callback_func(self, *args, **kwargs)
            else:
                print('Unathorised')
                return False
        return wrapper

    def get_items(self):
        '''Get available items'''
        for item_type in self.item_manager:
            self.item_manager[item_type].get_item()    
        
    def logout(self):
        self.login_user = None

    @auth
    def add_cash(self, cash: int):
        if self.login_user:
            self.login_user.add_cash_for_user(cash)

    @auth
    def is_valid_item_type(self, item_type: str) -> bool:
        if item_type in self.item_manager:
            return True
        else: 
            print('Invalid item_type')
            return False

    @auth
    def buy_item(self, item_id: int, quantity: int, item_type: str):
        if self.is_valid_item_type(item_type):
            self.item_manager[item_type].decrease_quantity(item_id, quantity, self.login_user)

    @auth
    def get_available_cash_for_user(self):
        print(f'Available cash for {self.login_user.name} is {self.login_user.available_cash}')
        
    @auth_admin
    def add_item(self, item: Item, item_type: str):
        if self.is_valid_item_type(item_type):
            self.item_manager[item_type].add_item(item)
    
    @auth_admin
    def increase_item_quantity(self, item_id: int, quantity: int, item_type: str):
        if self.is_valid_item_type(item_type):
            self.item_manager[item_type].increase_quantity(item_id, quantity)

    @auth_admin
    def decrease_item_quantity(self, item_id: int, quantity: int, item_type: str):
        if self.is_valid_item_type(item_type):
            self.item_manager[item_type].decrease_quantity(item_id, quantity, None)
    
    @auth_admin
    def delete_item(self, item_id: int, item_type: str):
        if self.is_valid_item_type(item_type):
            self.item_manager[item_type].delete_item(item_id)
    
    @auth_admin
    def get_all_user(self):
        self.user_manager.get_all_users()

    @auth_admin
    def add_user(self, user: User):
        self.user_manager.add_user(user)

    @auth_admin
    def delete_user(self, user_id: int):
        self.user_manager.delete_user(user_id)
