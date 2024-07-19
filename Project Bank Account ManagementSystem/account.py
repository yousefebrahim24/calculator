class Account:
    def __init__(self, account_number, owner, balance=0.0):
        self._account_number = account_number
        self._owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def get_details(self):
        return {
            "account_number": self._account_number,
            "owner": self._owner,
            "balance": self._balance,
            "type": "account"
        }

    def modify_account(self, owner=None, balance=None):
        if owner:
            self._owner = owner
        if balance is not None:
            self._balance = balance

    def __str__(self):
        return f"Account {self._account_number}: Owner - {self._owner}, Balance - {self._balance}"

    def __add__(self, other):
        return self._balance + other._balance

    def __sub__(self, other):
        return self._balance - other._balance