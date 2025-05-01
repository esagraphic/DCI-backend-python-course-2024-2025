class WithdrawalError(ValueError):
    def __init__(self, amount, balance) -> None:
        # parent
        super().__init__(f'Withdrawal of amount {amount} failed')
        self.amount = amount 
        self.balance = balance 

    def overage(self):
        return self.balance - self.amount
        


def withdraw_money(amount):
    balance = 500
    if balance < amount:
        # raise an exception
        # We want an exception that is going to
        # inform the client by how much his amount is 
        # is more than the balance.
        # raise ValueError(f'Your amount is more than the balance by {balance - amount}')
        raise WithdrawalError(balance, amount)
    else:
        balance -= amount 
        return amount
    

amount = int(input('Enter the amount to withdraw: '))

try:
    amount_to_withdraw = withdraw_money(amount)
except WithdrawalError as ex:
    print(f'Your amount is more than your balance by {ex.overage()}')
else:
    print(amount_to_withdraw)
finally:
    print('Thank you for using our services!')