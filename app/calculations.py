
class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, balance=0, interest_rate=0.10):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Not enough balance")
        self.balance -= amount

    def collect_interest(self):
        self.balance += self.balance * self.interest_rate



def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
