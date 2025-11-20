

class Wallet(object):
    def __init__(self, initial_amount=0):
        self.amount = initial_amount

    def spend_cash(self, amount):
        if amount > self.amount:
            raise InsufficientAmount(
                'Not enough available to spend {}'.format(amount))
        self.amount -= amount

    def add_cash(self, amount):
        self.amount += amount


class InsufficientAmount(Exception):
    pass
