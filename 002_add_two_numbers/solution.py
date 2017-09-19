from list_node import ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        This is a manually optimized verion. It exploits in-place operations
        and greedily use existing chains.
        """
        carry = 0
        head = l1
        last = None

        while l1 is not None and l2 is not None:
            l1.val += l2.val + carry

            if l1.val > 9:
                carry = 1
                l1.val -= 10
            else:
                carry = 0

            last = l1

            l1 = l1.next
            l2 = l2.next

        l = l1 if l2 is None else l2
        last.next = l
        while carry:
            if l is None:
                last.next = ListNode(1)
                break
            l.val += carry
            if l.val > 9:
                carry = 1
                l.val -= 10
            else:
                carry = 0
            last = l
            l = l.next

        return head

    # If you really want to functional (TM), do the following

    def addTwoNumbersFunctional(self, l1, l2):
        return iter_to_ll(
            carry([
                x + y
                for x, y in izip_longest(
                    ll_to_iter(l1), ll_to_iter(l2), fillvalue=0)
            ]))
