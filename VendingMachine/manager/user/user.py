class User:
    '''User type'''
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.available_cash = 0

    def add_cash_for_user(self, cash):
        if self.is_valid_cash_amount(cash):
            self.available_cash += cash
    
    def decrease_cash_for_user(self, cash):
        if self.is_valid_cash_amount(cash):
            self.available_cash -= cash

    def is_valid_cash_amount(self, cash):
        if cash > 0:
            return True
        else:
            print('Invalid cash amount')
            return False