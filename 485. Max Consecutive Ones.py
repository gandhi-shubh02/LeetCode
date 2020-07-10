class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                maxcount=max(count,maxcount)
                count=0
            
        return max(count,maxcount)
