'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal, InvalidOperation

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ABS_AMOUNT = Decimal('100000')
MAX_TOTAL = Decimal('1000000')

def to_decimal(value):
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError):
        return None

def validorder(order: Order):
    net = Decimal('0')

    for item in order.items:
        amount = to_decimal(item.amount)
        if amount is None:
            return "Invalid amount"

        if item.type == 'payment':
            if abs(amount) > MAX_ABS_AMOUNT:
                return "Total amount payable for an order exceeded"
            net += amount

        elif item.type == 'product':
            if type(item.quantity) is not int or item.quantity <= 0:
                continue
            if amount <= 0 or amount > MAX_ABS_AMOUNT:
                continue

            line_total = amount * item.quantity
            net -= line_total

        else:
            return "Invalid item type: %s" % item.type

        if abs(net) > MAX_TOTAL:
            return "Total amount payable for an order exceeded"

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
