def binary_search(n, comp):
    """
    Here I avoided using recurrsion for performance reasons.
    :type n: int
    :type comp: a -> { -1, 0, 1 }
    """
    i = 0
    j = len(n)
    while i < j:
        k = (i + j) // 2
        c = comp(k)
        if c < 0:
            j = k
        elif c > 0:
            i = k + 1
        else:
            return k

    return -1


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 > l2:
            m = l2
            xs = nums1
            ys = nums2
        else:
            m = l1
            xs = nums2
            ys = nums1

        def comp_xy(i):
            x = xs[i]
            y = ys[m - 1 - i]
            if x > y:
                return -1
            elif x < y:
                return 1
            else:
                return 0

        binary_search(m + 1, comp_xy)
