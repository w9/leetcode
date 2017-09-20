from solution import Solution


def test(s):
    print('{} -> {}'.format(s, Solution().lengthOfLongestSubstring(s)))


test('asdffff')
test('ffffasd')
test('zbzbzbzbzbbbbb')
test('')
test('aaaa')
test('1234567890')
