def binary_search(n, m, comp):
    """
    Here I avoided using recurrsion for performance reasons.
    :type n: int
    :type comp: a -> { -1, 0, 1 }
    """
    i = n
    j = m + 1
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
        n = len(nums1)
        m = len(nums2)

        if n < m:
            n, m = m, n
            nums1, nums2 = nums2, nums1

        if n == 0:
            raise ValueError

        if m == 0:
            med1 = nums1[n // 2 - 1]
            med2 = nums1[n // 2]
        else:
            e1 = (n - m) // 2
            e2 = (n + m) // 2

            def comp(i):
                if nums1[e1 + i - 1] > nums2[m - i]:
                    return -1
                elif nums1[e1 + i] < nums2[m - i - 1]:
                    return 1
                else:
                    return 0

            if nums1[e1] >= nums2[m - 1]:
                med2 = nums1[e1]
                if e1 > 0:
                    med1 = max(nums1[e1 - 1], nums2[m - 1])
                else:
                    med1 = nums2[m - 1]
            elif nums1[e2 - 1] <= nums2[0]:
                med1 = nums1[e2 - 1]
                if e2 < n:
                    med2 = min(nums1[e2], nums2[0])
                else:
                    med2 = nums2[0]
            else:
                cut = binary_search(1, m - 1, comp)
                med1 = max(nums1[e1 + cut - 1], nums2[m - cut - 1])
                med2 = min(nums1[e1 + cut], nums2[m - cut])

        if (n - m) % 2 == 0:
            return (med1 + med2) / float(2)
        else:
            return med2
