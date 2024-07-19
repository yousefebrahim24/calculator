import json
from account import Account
from savings_account import SavingsAccount
from checking_account import CheckingAccount

class Bank:
    def __init__(self, data_file='data.json'):
        self._data_file = data_file
        self._accounts = self._load_data()

    def _load_data(self):
        try:
            with open(self._data_file, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
                accounts = []
                for acc in data:
                    if acc['type'] == 'savings':
                        accounts.append(SavingsAccount(
                            acc['account_number'], acc['owner'], acc['balance'], acc['interest_rate']))
                    elif acc['type'] == 'checking':
                        accounts.append(CheckingAccount(
                            acc['account_number'], acc['owner'], acc['balance'], acc['overdraft_limit']))
                    else:
                        accounts.append(Account(
                            acc['account_number'], acc['owner'], acc['balance']))
                return accounts
        except FileNotFoundError:
            return []

    def _save_data(self):
        with open(self._data_file, 'w') as file:
            json.dump([acc.get_details() for acc in self._accounts], file, indent=4)

    def add_account(self, account):
        if self.account_exists(account._account_number):
            print(f"Account number {account._account_number} already exists. Please choose a different account number.")
            return False
        self._accounts.append(account)
        self._save_data()
        return True

    def account_exists(self, account_number):
        return any(account._account_number == account_number for account in self._accounts)

    def get_account(self, account_number):
        for account in self._accounts:
            if account._account_number == account_number:
                return account
        return None

    def delete_account(self, account_number):
        account = self.get_account(account_number)
        if account:
            self._accounts.remove(account)
            self._save_data()

    def modify_account(self, account_number, **kwargs):
        account = self.get_account(account_number)
        if account:
            if isinstance(account, SavingsAccount):
                account.modify_account(**kwargs)
            elif isinstance(account, CheckingAccount):
                account.modify_account(**kwargs)
            else:
                account.modify_account(kwargs.get('owner'), kwargs.get('balance'))
            self._save_data()

    def get_all_accounts(self):
        return [acc.get_details() for acc in self._accounts]

    def __str__(self):
        return f"Bank with {len(self._accounts)} accounts."