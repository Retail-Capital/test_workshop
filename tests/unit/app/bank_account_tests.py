import pytest

from app.bank_account import AccountOverdrawnException, BankAccount, InvalidAmountException


def test_withdrawal_with_positive_amount():
    """withdrawal: balance is adjusted when a positive amount is withdrawn."""
    account = BankAccount(1)

    # Set the balance so that a withdrawal doesn't exceed its limit
    account._balance = 200
    account.withdraw(100)

    assert account.balance == 100


def test_withdrawal_with_positive_amount_raises_error_if_overdrawn():
    """withdrawal: error is raised if withdrawal amount is overdraws account."""
    account = BankAccount(1)

    with pytest.raises(AccountOverdrawnException):
        account.withdraw(100)


def test_withdrawal_with_invalid_amount_raises_error():
    """withdrawal: error is raised if invalid amount is withdrawn."""
    account = BankAccount(1)

    with pytest.raises(InvalidAmountException):
        account.withdraw('R100')


def test_withdrawal_with_negative_amount_raises_error():
    """withdrawal: error is raised if negative amount is withdrawn."""
    account = BankAccount(1)

    with pytest.raises(InvalidAmountException):
        account.withdraw(-100)
