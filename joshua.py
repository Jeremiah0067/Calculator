class CreditClass:

    def __init__(self, customer, bank, acnt, limit, balance = 0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance


    def get_customers(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit()

    def get_balance(self):
        return self._balance()

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if amount > 0:
           self._balance -= amount

        if amount < 0:
            raise ValueError


if __name__ == "__main__":
    wallet = []
    wallet.append(CreditClass('John Bowman', 'California Savings',
                              '56 5391 0375 9387 5309', 2500))
    wallet.append(CreditClass("John Bowman", "California Federal",
                              '58 3485 0399 3395 1954', 3500))
    wallet.append(CreditClass('John Bowman', 'California Finance',
                              '60 5391 0375 9387 5309', 5000))

for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2 * val)
    wallet[2].charge(3 * val)

for w in range(3):
    print('customer=', wallet[w].get_customers())
    print('Bank =', wallet[w].get_bank())
    print('Account=', wallet[w].get_account())
    print("limit=", wallet[w].get_limit)
    print("balance=", wallet[w].get_balance)

while wallet[w].get_balance() > 100:
    wallet[w].make_payment(100)
    print("new balance=", wallet[w].get_balance)
    print()


class PredatoryCreditClass(CreditClass):
    OVERLIMIT_FEE = 5

    def __init__(self, customer, bank, acnt, limit, apr):
        
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += PredatoryCreditClass.OVERLIMIT_FEE
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor





