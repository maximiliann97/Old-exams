import abc


class BankAccount(metaclass=abc.ABCMeta):
    def __init__(self, statement):
        self.statement = statement

    @abc.abstractmethod
    def available_amount(self):
        pass

    @abc.abstractmethod
    def withdraw(self, amount):
        pass

    @abc.abstractmethod
    def deposit(self, amount):
        pass

    def __repr__(self):
        return f'Account({self.statement})'


class SavingsAccount(BankAccount):
    def __init__(self, statement):
        super().__init__(statement)

    def available_amount(self):
        return self.statement

    def withdraw(self, amount):
        if self.statement-amount < 0:
            raise OverdraftException("There's not enough money to withdraw")
        self.statement -= amount

    def deposit(self, amount):
        self.statement += amount


class SpendingAccount(BankAccount):
    def __init__(self, statement):
        super().__init__(statement)

    def available_amount(self):
        return self.statement

    def withdraw(self, amount):
        if self.statement - amount < -5000:
            raise OverdraftException('You cannot exceed a overdraft of -5000')
        self.statement -= amount

        if self.statement < 0:
            self.apply_overdraft_fee()

    def deposit(self, amount):
        self.statement += amount

    def apply_overdraft_fee(self):
        if self.statement * 0.1 < -500:
            fee = -500
        else:
            fee = self.statement * 0.1
        self.statement += fee


class OverdraftException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        return self.msg