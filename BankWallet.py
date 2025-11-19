class InsufficientFundsError(Exception):
    pass

class Wallet:
    def __init__(self, name: str, currency: str):
        self._name = name
        self._currency = currency
        self._balance = 0.0

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise InsufficientFundsError("Not enough funds")
        self._balance -= amount

    def __str__(self) -> str:
        return f'Wallet of {self._name}: {self._balance} {self._currency}'