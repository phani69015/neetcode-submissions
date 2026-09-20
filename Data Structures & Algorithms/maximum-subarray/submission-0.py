class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        maxs = nums[0]

        for i in range(1,len(nums)):
            if curr+nums[i] < nums[i]:
                curr = nums[i]
            else:
                curr+=nums[i]
            maxs = max(maxs,curr)
        return maxs


        