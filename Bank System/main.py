import json
from account import Account

Account.bank_name()
with open("accounts.json", "r") as file:
    accounts = json.load(file)
if len(accounts) == 0:
    Account.next_account_no = 1001
else:
    Account.next_account_no = accounts[-1]["account_no"] + 1


while True:
    print("Enter 1 to create new account, Enter 2 to log into your existing account, Enter 3 to exit")
    try:
        response = int(input("Enter your response: "))
        if response == 1:
            name = input("Enter Your Name: ")
            while True:
                try:
                    balance = int(input("Enter the initial deposit for your account: "))
                    break
                except ValueError:
                    print("Enter the valid number to initial deposit")
                    print("------------------------x------------------------")
            customer = Account(name, balance)
            print("Account created successfully!")
            customer.new_user_details()
            new_account = {
                "account_no": customer.account_no,
                "name": customer.name,
                "balance": customer.balance
            }

            accounts.append(new_account)

            with open("accounts.json", "w") as file:
                json.dump(accounts, file, indent=4)
            print("------------------------x------------------------")
            (input("press Enter to go to the main menu....."))

        elif response == 2:
            while True:
                try:
                    account_no = int(input("Enter your account number: "))
                    break
                except ValueError:
                    print("Enter the valid account number")
                    print("------------------------x------------------------")
            found = False

            for account in accounts:
                if account["account_no"] == account_no:
                    found = True

                    customer = Account(
                    account["name"],
                    account["balance"]
                    )

                    customer.account_no = account["account_no"]

                    print("Login Successful")
                    print(f"Welcome {account['name']}!")
                    customer.new_user_details()
                    print("------------------------x------------------------")
                    


                    while True:   
                        print("Enter 1 to check balance, Enter 2 to deposit, Enter 3 to withdraw, Enter 4 to logout")
                        try:
                            response = int(input("Enter Your response: "))
                            if response == 1:
                                customer.checkbalance()
                                print("------------------------x------------------------")         
        
                            elif response == 2:
                                while True:
                                    try:
                                        amount = int(input("Enter the amount you want to deposit: "))
                                        customer.deposit(amount)
                                        print("------------------------x------------------------")
                                        account["balance"] = customer.balance
                                        with open("accounts.json", "w") as file:
                                            json.dump(accounts, file, indent=4)
                                        break
                                    except ValueError:
                                        print("Enter the valid number to deposit")
                                        print("------------------------x------------------------") 

                            elif response == 3:
                                while True:
                                    try:
                                        amount = int(input("Enter the amount you want to withdraw: "))
                                        customer.withdraw(amount)
                                        print("------------------------x------------------------")
                                        account["balance"] = customer.balance
                                        with open("accounts.json", "w") as file:
                                            json.dump(accounts, file, indent=4)
                                        break
                                    except ValueError:
                                        print("Enter the valid number to withdraw")
                                        print("------------------------x------------------------") 

                            elif response == 4:
                                print("Logged out successfully")
                                break

                            else:
                                print("Enter the valid number to continue")
                                print("------------------------x------------------------")
                        except ValueError:
                            print("Enter the valid number to continue")
                            print("------------------------x------------------------")
                    break

            if not found:
                 print("Account Not Found")

        elif response == 3:
            print("Thank you for banking with ABC Bank!")
            break

        else:
             print("Enter a valid input......")
    except ValueError:
         print("Enter the valid number to deposit")
         print("------------------------x------------------------")