from account import Account

class CheckingAccount(Account):
    def __init__(self, account_number, owner, balance=0.0, overdraft_limit=0.0):
        super().__init__(account_number, owner, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self._balance + self._overdraft_limit:
            self._balance -= amount

    def get_details(self):
        details = super().get_details()
        details.update({
            "type": "checking",
            "overdraft_limit": self._overdraft_limit
        })
        return details

    def modify_account(self, owner=None, balance=None, overdraft_limit=None):
        super().modify_account(owner, balance)
        if overdraft_limit is not None:
            self._overdraft_limit = overdraft_limit

    def __str__(self):
        return f"Checking Account {self._account_number}: Owner - {self._owner}, Balance - {self._balance}, Overdraft Limit - {self._overdraft_limit}"