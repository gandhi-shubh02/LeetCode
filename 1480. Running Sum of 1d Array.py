class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(0,len(nums)):
            l.append(sum(nums[:i+1]))
        return l
