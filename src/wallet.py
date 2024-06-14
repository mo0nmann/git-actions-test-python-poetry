class InsufficientAmount(Exception):
    """Exception raised for errors in the input amount.

    Attributes:
        message -- explanation of the error
    """

    pass


class Wallet(object):
    """A simple wallet class to manage cash balance.

    Args:
        initial_amount (int, optional): Initial amount of cash in the wallet.
            Defaults to 0.

    Attributes:
        balance (int): The current balance of the wallet.
    """

    def __init__(self, initial_amount=0):
        """Initializes the wallet with an initial amount.

        Args:
            initial_amount (int, optional): Initial amount of cash in the
            wallet.
                Defaults to 0.
        """
        self.balance = initial_amount

    def spend_cash(self, amount):
        """Spend a specified amount of cash from the wallet.

        Args:
            amount (int): The amount of cash to spend.

        Raises:
            InsufficientAmount: If the amount to spend is greater than
                the current balance.
        """
        if self.balance < amount:
            raise InsufficientAmount("Not enough available to spend {}".format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        """Add a specified amount of cash to the wallet.

        Args:
            amount (int): The amount of cash to add.
        """
        self.balance += amount


def main():
    """Main function to demonstrate wallet operations."""
    wallet = Wallet(100)
    wallet.add_cash(90)
    wallet.spend_cash(10)
    print(f"{wallet.balance}")


if __name__ == "__main__":
    main()
