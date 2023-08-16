import uuid
from decimal import Decimal
import datetime


class BankAccount:
    def __init__(self, account_name, initial_balance=0):
        self.account_name = account_name
        self.account_id = uuid.uuid4() #використання uuid допомагає відрізнити різні рахунки один від одного
        self.balance = Decimal(initial_balance) #встановлює початковий баланс рахунку
        self.transactions = []

    def perform_transaction(self, amount, transaction_type):
        if amount <= 0:
            print('Invalid amount.')
            return False

        if transaction_type == 'withdrawal' and amount > self.balance:
            print('Insufficient funds.')
            return False

        commission = amount * Decimal('0.01')
        if transaction_type == 'withdrawal':
            self.balance -= amount + commission
        else:
            self.balance += amount - commission

        self.transactions.append((amount, transaction_type, datetime.datetime.now()))
        return True

    def deposit(self, amount):
        if self.perform_transaction(amount, 'deposit'):
            print(f'Deposit of {amount} successful.')

    def withdraw(self, amount):
        if self.perform_transaction(amount, 'withdrawal'):
            print(f'Withdrawal of {amount} successful.')

    def print_transactions(self):
        print("Transactions:")
        for amount, transaction_type, transaction_date in self.transactions:
            print(f'{transaction_date}: {transaction_type.capitalize()} of {amount}')

    def get_balance(self):
        return self.balance


#приклад використання класу
account = BankAccount('John Smith', 1000)
account.deposit(500)
account.withdraw(200)
account.print_transactions()
print(f'Current balance: {account.get_balance()}')657