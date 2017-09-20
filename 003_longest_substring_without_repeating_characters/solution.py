class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best = 0

        last_appeared = dict()
        last_repeated = -1

        for i, c in enumerate(s):
            j = last_appeared.get(c, -1)
            last_repeated = max(j, last_repeated)
            best = max(best, i - last_repeated)
            last_appeared[c] = i

        return best
