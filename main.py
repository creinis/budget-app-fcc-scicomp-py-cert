# The Budget App

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        pass
    
    def get_balance(self):
        pass
    
    def transfer(self):
        pass
    
    def check_funds(self):
        pass
    
    
    
