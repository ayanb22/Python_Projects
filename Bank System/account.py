class Account:
    @staticmethod 
    def bank_name():
        print("Welcome to ABC Bank...")
    next_account_no = 1001
    def __init__(self, name, balance):
        self.account_no = Account.next_account_no
        self.name = name
        self.balance = balance
        Account.next_account_no += 1

    def new_user_details(self):
        print("------Account Details------")
        print(f"Account Number: {self.account_no}")
        print(f"Account Holder: {self.name}")
        print(f"Account Balance: {self.balance}")


    def deposit(self, amount):
        self.amount = amount 
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

    def withdraw(self, amount):
        self.amount = amount
        while True:
            if amount > self.balance:
                print("Try again that is an invalid amount....")
                amount = int(input("Enter the amount you want to withdraw : "))
            else:
                self.balance -= amount               
                print(f"Amount Rs.{amount} is debited")
                print(f"Your Current Balance is {self.balance}")
                print("Withdrawal Successful")
                break

    def checkbalance(self):
        print(f"Your Current Balance is {self.balance}")


        
