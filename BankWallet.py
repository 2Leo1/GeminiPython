class InsufficientFundsError(Exception):
    pass

class Wallet:
    def __init__(self, name: str, currency: str):
        self._name = name
        self._currency = currency
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount >= 0:
            self._balance += amount
        else:
            print("Ошибка")
            raise ValueError

    def withdraw(self, amount: float) -> None:
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Ошибка")
            raise InsufficientFundsError

    def __str__(self) -> str:
        return 'Wallet of ' + self._name + ': ' + str(self._balance) + ' ' + self._currency


if __name__ == "__main__":
    wallet = Wallet("Alex", "USD")
    wallet.deposit(100.0)
    print(wallet)

    try:
        wallet.withdraw(150.0)
    except InsufficientFundsError:
        print("Caught expected error: Not enough money")

    try:
        wallet.deposit(-50)
    except ValueError:
        print("Caught expected error: Negative amount")

    print(f"Final balance: {wallet.balance}")