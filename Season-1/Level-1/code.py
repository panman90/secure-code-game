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

MAX_ITEM_AMOUNT = Decimal('100000')
MAX_QUANTITY = 100
MAX_TOTAL = Decimal('1000000')

def validorder(order: Order):
    net = Decimal('0')  # net = payments - products; should be 0 at end

    for item in order.items:
        if item.type == 'payment':
            try:
                amount = Decimal(str(item.amount))
            except InvalidOperation:
                continue
            # Clamp out-of-range payments to zero (treat as invalid/ignored)
            if -MAX_ITEM_AMOUNT <= amount <= MAX_ITEM_AMOUNT:
                net += amount
        elif item.type == 'product':
            if (type(item.quantity) is not int
                    or not (0 < item.quantity <= MAX_QUANTITY)):
                continue
            try:
                amount = Decimal(str(item.amount))
            except InvalidOperation:
                continue
            if not (0 < amount <= MAX_ITEM_AMOUNT):
                continue
            net -= amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type

        if abs(net) > MAX_TOTAL:
            return "Total amount payable for an order exceeded"

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
