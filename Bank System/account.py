class Account:
    @staticmethod 
    def bank_name():
        print("Welcome to ABC Bank...")
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self):
        amount = self.amount
        while True:
            if amount > 0:               
                self.balance += amount
                print(f"Amount Rs.{amount} is credited")
                print(f"Your Current Balance is {self.balance}")
                print("Deposit Successful")
                break
            else:
                print("Try again that is an invalid amount....")
                amount = int(input("Enter the amount you want to deposit : "))