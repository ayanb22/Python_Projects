class Account:
    @staticmethod 
    def bank_name():
        print("Welcome to ABC Bank...")
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount