from bank import Bank
from savings_account import SavingsAccount
from checking_account import CheckingAccount

bank = Bank()
print("--------------------Welcome To The Bank Management System--------------------")

while True:
    print("""
          How can i help you :
          
          1. Create Account 
          2. Your Account Details
          3. Show Your Balance
          4. Modify Your Account
          5. Delete Your Account
          6. Show All Accounts
          7. Exit The Program
          """)
    try : 
        choice = int(input("Enter your choice : "))
        if choice == 1:
             account_number = input("Enter account number: ")
             if bank.account_exists(account_number):
                print(f"Account number {account_number} already exists. Please choose a different account number.")
                continue
             owner = input("Enter owner name: ")
             balance = float(input("Enter initial balance: "))
             if balance < 1000:
                 print("The initial balance should be at least 1000")
                 continue
             account_type = input("Enter account type (savings/checking): ")

             if account_type == 'savings':
                interest_rate = float(input("Enter interest rate: "))
                account = SavingsAccount(account_number, owner, balance, interest_rate)
             elif account_type == 'checking':
                overdraft_limit = float(input("Enter overdraft limit: "))
                account = CheckingAccount(account_number, owner, balance, overdraft_limit)
             else:
                print("Invalid account type!")
                continue

             bank.add_account(account)
             print("Account created successfully.")
        elif choice == 2:
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print(account)
            else:
                print("Account not found.")
        elif choice == 3:
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Balance of Account {account_number}: {account._balance}")
            else:
                print("Account not found.")
        elif choice == 4:
            account_number = input("Enter account number: ")
            owner = input("Enter new owner name (leave blank to keep current): ")
            balance = input("Enter new balance (leave blank to keep current): ")
            interest_rate = input("Enter new interest rate (leave blank to keep current, applicable for savings accounts): ")
            overdraft_limit = input("Enter new overdraft limit (leave blank to keep current, applicable for checking accounts): ")

            kwargs = {}
            if owner:
                kwargs['owner'] = owner
            if balance:
                kwargs['balance'] = float(balance)
            if interest_rate:
                kwargs['interest_rate'] = float(interest_rate)
            if overdraft_limit:
                kwargs['overdraft_limit'] = float(overdraft_limit)

            bank.modify_account(account_number, **kwargs)
            print("Account modified successfully.")
        elif choice == 5:
            account_number = input("Enter account number: ")
            bank.delete_account(account_number)
            print("Account deleted successfully.")
        elif choice == 6:
            username = 'admin'
            password = 'admin1'
            input_username = input('username: ')
            input_password = input('password: ')
            if input_username == username and input_password == password:
                accounts = bank.get_all_accounts()
                for acc in accounts:
                    print(acc)
            else:
                print('WRONG USERNAME OR PASSWORD!')
        elif choice == 7 :
            print("Thank you for using our Bank Account Management System.")
            break
        else:
            print("WRONG INPUT! Please, Enter a number between 1 and 7")
            
    except Exception as ex : 
        print(str(ex))