class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if(nums[i]==target):
                return i
                break
        for i in range(len(nums)):
            if target<nums[0]:
                return 0
            if i==len(nums)-1:
                return len(nums)
            elif nums[i]<target and nums[i+1]>target:
                return i+1
                
            
