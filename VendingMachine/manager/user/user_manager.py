from .user import User
from collections import defaultdict as ddict

class UserManager:
    '''Manage users'''

    def __init__(self):
        self.id = 1
        default_admin_user = User('administrator', 'admin')
        self.users: ddict(lambda: User) = {self.id : default_admin_user}

    def get_all_users(self):
        for user_id in self.users:
            print(f'ID {user_id} : {self.users[user_id].name} : type -> {self.users[user_id].type} : available cash -> {self.users[user_id].available_cash}')

    def add_user(self, user: User) -> bool:
        if user.type in ['admin', 'employee']:
            self.id += 1
            self.users[self.id] = user
            return True
        print('Invalid user type')
        return False
    
    def delete_user(self, user_id: int) -> bool:
        if self.is_valid_id(user_id):            
            del self.users[user_id]
            return True
        else:
            print('Invalid user id to delete')

    def is_admin_user_by_username(self, username: str) -> bool:
        for id in self.users:
            if self.users[id].name == username and self.users[id].type == 'admin':
                return True
        return False
    
    def is_admin_user(self, user: User) -> bool:
        return user.type == 'admin'
    
    def is_valid_id(self, id) -> bool:
        if id in self.users:
            return True
        else:
            return False
    
    def get_user_by_id(self, id) -> User:
        if self.is_valid_id(id):
            return self.users[id]
        else:
            print('Invalid user id')

    def get_user_by_name(self, username) -> User:
        for id in self.users:
            if self.users[id].name == username:
                return self.users[id]
  