from solution import Solution
from list_node import ListNode


def linked_list_to_int(l):
    s = ''
    while l:
        s += str(l.val)
        l = l.next
    s = s[::-1]

    return int(s)


def int_to_linked_list(n):
    s = str(n)

    last = None
    for d in s:
        this = ListNode(int(d))
        this.next = last
        last = this

    return this


def test(a, b):
    l1 = int_to_linked_list(a)
    l2 = int_to_linked_list(b)
    l3 = Solution().addTwoNumbersFunctional(l1, l2)
    print('{} + {} = {}'.format(a, b, linked_list_to_int(l3)))


test(0, 0)

test(1000, 0)

test(14, 17)

test(5, 5)

test(99999, 1)

test(12345, 12345)
