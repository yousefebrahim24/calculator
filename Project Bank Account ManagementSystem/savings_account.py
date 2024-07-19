from account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, owner, balance)
        self._interest_rate = interest_rate

    def add_interest(self):
        self._balance += self._balance * self._interest_rate

    def get_details(self):
        details = super().get_details()
        details.update({
            "type": "savings",
            "interest_rate": self._interest_rate
        })
        return details

    def modify_account(self, owner=None, balance=None, interest_rate=None):
        super().modify_account(owner, balance)
        if interest_rate is not None:
            self._interest_rate = interest_rate

    def __str__(self):
        return f"Savings Account {self._account_number}: Owner - {self._owner}, Balance - {self._balance}, Interest Rate - {self._interest_rate}"