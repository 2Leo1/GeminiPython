import pytest
from BankWallet import Wallet, InsufficientFundsError

def test_wallet_initial_balance():
    wallet = Wallet("Test User", "USD")
    assert wallet.balance == 0.0

def test_deposit():
    wallet = Wallet("Test User", "USD")
    wallet.deposit(100)
    assert wallet.balance == 100.0

def test_deposit_error():
    wallet = Wallet("Test User", "USD")
    with pytest.raises(ValueError):
        wallet.deposit(-100)

def test_withdraw():
    wallet = Wallet("Test User", "USD")
    wallet.deposit(100)
    wallet.withdraw(20)
    assert wallet.balance == 80.0

def test_withdraw_error():
    wallet = Wallet("Test User", "USD")
    with pytest.raises(InsufficientFundsError):
        wallet.withdraw(10)