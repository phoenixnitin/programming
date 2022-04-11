'''
Execute usage of vending machine
'''
from manager.item.item import Item
from manager.user.user import User
from vending_machine import VendingMachine
import os

class OperateVendingMachine:
    def __init__(self, test_file_path = './test/input1.txt'):
        if os.path.exists(os.path.join(os.getcwd(), test_file_path)):
            with open(test_file_path, 'r') as read_file:
                self.all_commands = read_file.readlines()
                self.initialize_vending_machine()
                self.process_command_lines()
        else:
            print('Invalid File')

    def initialize_vending_machine(self):
        max_quantity = None
        cost_of_each_item = None
        for line in self.all_commands:
            if len(line) > 0 and (max_quantity is None or cost_of_each_item is None):
                values = list(map(lambda x: x.strip(), line.split(',')))
                match values[0]:
                    case 'maxquantity': max_quantity = int(values[1])
                    case 'costofeachitem': cost_of_each_item = int(values[1])
                    case _: pass
        
        if max_quantity is not None and cost_of_each_item is not None:
            self.vending_machine = VendingMachine(max_quantity, cost_of_each_item)
        else:
            print('Unable to initialize vending machine')
            exit(0)

    def process_command_lines(self):
        for line in self.all_commands:
            if len(line) > 0:
                values = list(map(lambda x: x.strip(), line.split(',')))
                print(values)
                match values[0]:
                    case 'login': self.vending_machine.login(values[1])
                    case 'logout': self.vending_machine.logout()
                    case 'additem': 
                        [item_type, quantity, *name] = values[1].split(' ')
                        item = Item(' '.join(name), item_type, int(quantity))
                        self.vending_machine.add_item(item, item_type)
                    case 'addcash': self.vending_machine.add_cash(int(values[1]))
                    case 'getavailablecash': self.vending_machine.get_available_cash_for_user()
                    case 'getitem': self.vending_machine.get_items()
                    case 'buy': 
                        [item_type, item_id, quantity] = values[1].split(' ')
                        self.vending_machine.buy_item(int(item_id), int(quantity), item_type)
                    case 'deleteitem': 
                        [item_type, item_id] = values[1].split(' ')
                        self.vending_machine.delete_item(item_type=item_type, item_id=int(item_id))
                    case 'decreaseitem': 
                        [item_type, item_id, quantity] = values[1].split(' ')
                        self.vending_machine.decrease_item_quantity(int(item_id), int(quantity), item_type)
                    case 'increaseitem': 
                        [item_type, item_id, quantity] = values[1].split(' ')
                        self.vending_machine.increase_item_quantity(int(item_id), int(quantity), item_type)
                    case 'adduser': 
                        [user_type, *username] = values[1].split(' ')
                        user = User(' '.join(username), user_type)
                        self.vending_machine.add_user(user)
                    case 'getalluser': self.vending_machine.get_all_user()
                    case 'deleteuser': self.vending_machine.delete_user(int(values[1]))
                    case _: 'Invalid command'

# operate_vending_machine = OperateVendingMachine()
operate_vending_machine = OperateVendingMachine('./test/input1.txt')
