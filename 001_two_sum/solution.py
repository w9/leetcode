class Solution(object):
    def twoSum(self, nums, target):
        looking_for = {}
        for i in range(len(nums)):
            j = looking_for.get(nums[i])
            if j is not None:
                return [j, i]
            else:
                looking_for[target - nums[i]] = i
