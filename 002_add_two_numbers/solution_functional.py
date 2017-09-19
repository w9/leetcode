"""
I personally think functional programming is awkward in Python. And it's
considerably harder to debug. Not to mention the performance (esp. memory-wise)
is poor.
"""

from list_node import ListNode
from itertools import izip_longest


def carry(l, base=10):
    c = 0
    for x in l:
        x += c
        if x >= base:
            c = x // base
            x = x % base
        else:
            c = 0
        yield x
    if c > 0:
        yield c


def iter_to_ll(l):
    last = None
    for x in reversed(list(l)):
        node = ListNode(x)
        node.next = last
        last = node
    return node


def ll_to_iter(l):
    while l is not None:
        yield l.val
        l = l.next


class Solution(object):
    def addTwoNumbersFunctional(self, l1, l2):
        return iter_to_ll(
            carry([
                x + y
                for x, y in izip_longest(
                    ll_to_iter(l1), ll_to_iter(l2), fillvalue=0)
            ]))
