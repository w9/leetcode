from __future__ import division
from solution import Solution


def median(zs):
    n = len(zs)

    if n == 0:
        return -1

    if n % 2 == 0:
        return (zs[n // 2 - 1] + zs[n // 2]) / 2
    else:
        return zs[n // 2]


def test(xs, ys):
    print('xs: {}'.format(xs))
    print('ys: {}'.format(ys))
    zs = sorted(xs + ys)
    print('combined: {}'.format(zs))
    print('median: {}'.format(median(zs)))
    print('result: {}'.format(Solution().findMedianSortedArrays(xs, ys)))
    print('')


test([1, 2, 3, 4], [2, 3, 4, 5])
test([1, 2, 3, 4], [4, 5, 6, 7])
test([1, 2, 3, 4], [14, 15, 16, 17])
test([4, 5, 6, 7], [1, 2, 3, 4])
test([1, 2, 3, 4, 5, 6, 7, 8, 9], [5])
test([1, 2, 3, 4, 5, 6, 7, 8, 9], [7, 8, 9])

print('---------------')
print('')

test([1, 2, 3, 4, 4], [2, 3, 4, 5])
test([1, 2, 3, 4, 5], [4, 5, 6, 7])
test([1, 2, 3, 4], [14, 15, 16, 17, 18])
test([4, 5, 6, 7, 8], [1, 2, 3, 4])
test([1, 2, 3, 4, 5, 6, 7, 8], [5])
test([1, 2, 3, 4, 5, 6, 7, 8], [7, 8, 9])

print('---------------')
print('')

test([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3])
test([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [1])
test([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3])
test([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [1])
test([], [1])
test([1], [])

print('---------------')
print('')

test([1, 4, 5], [2, 3, 6])
