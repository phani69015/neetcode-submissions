class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #approach 1 - dic 
        # d = {}
        # for i in nums:
        #     if i in d:
        #         return i 
        #     d[i]=nums.index(i)
        # return 0
        
        #approach 2 - sort and find 
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==nums[i-1]:
                return nums[i]


