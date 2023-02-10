class BankAccount():
    """A bank account for a customer."""

    def __init__(self, customer_id):
        """Initialise the bank account for a particular customer."""
        self.customer_id = customer_id
        self._balance = 0
        self._history = []

    @property
    def balance(self):
        """Return the current account balance."""
        return self._balance

    @property
    def history(self):
        """Return the history of the account."""
        return self._history

    def withdraw(self, amount):
        """Accept a withdrawal from the account."""
        self._balance -= amount

    def deposit(self, amount):
        """Accept a payment into the account."""
        self._balance += amount

    def request_advance(self, amount):
        """Allow an advance if the balance is more than R500 and the amount is positive."""
        return False if self._balance < 500 and amount else True


class InvalidAmountException(Exception):
    """Error raised when an invalid amount is used in a transaction."""

    pass


class AccountOverdrawnException(Exception):
    """Error raised if the account ever reaches a state of negative balance."""

    pass
